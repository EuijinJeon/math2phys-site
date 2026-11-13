#!/usr/bin/env python3
"""지은 사이트를 헤드리스 Chromium(Playwright, 노드)으로 열어 검사한다.

쪽마다: (a) MathJax 렌더 오류(mjx-merror), (b) 깨진 내부 링크(파일과 #앵커), (c) 좁은 화면(기본 390px) 가로 넘침,
(d) 콘솔 오류·실패한 요청. 풀리지 않은 수식 구분자와 Mermaid 오류도 센다. 문제가 있으면 종료 코드 1.

사용:
  python3 tools/verify_site.py --build                 # build.py 로 /tmp/m2p-site 에 지어서 검사
  python3 tools/verify_site.py --site DIR              # 이미 지은 사이트 디렉터리
  python3 tools/verify_site.py --artifact FILE.html    # 한 파일 내보내기(해시 쪽마다)
  옵션: --json OUT.json  --only 정규식(쪽 이름)  --jobs 4  --width 390  --root DIR(--build 때 카드 root)
CDN: MathJax·Mermaid 는 CDN 에서 오는데, 막힌 환경(프록시가 jsdelivr 를 403 으로 막는다)을 위해 npm 레지스트리에서
mathjax@3.2.2 와 mermaid@10.9.3 을 받아 캐시(기본 /tmp/m2p-verify-vendor, 환경변수 M2P_VENDOR)에 풀고,
Chromium 의 요청을 가로채 그 파일로 응답한다. --no-local-cdn 이면 실제 CDN 을 쓴다.
Chromium: playwright 의 기본 설치를 쓴다(다시 설치하지 않는다). node 의 playwright 는 NODE_PATH 가 없으면 `npm root -g`.
"""
import argparse, glob, os, subprocess, sys, tarfile, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def npm_pack(spec, dest):
    os.makedirs(dest, exist_ok=True)
    r = subprocess.run(["npm", "pack", spec, "--silent"], cwd=dest, capture_output=True, text=True)
    tgz = sorted(glob.glob(os.path.join(dest, "*.tgz")))
    if r.returncode or not tgz:
        sys.exit(f"npm pack {spec} 실패: {r.stderr[-300:]}")
    with tarfile.open(tgz[-1]) as t:
        try:
            t.extractall(dest, filter="data")
        except TypeError:
            t.extractall(dest)
    return os.path.join(dest, "package")


def vendor():
    base = os.environ.get("M2P_VENDOR") or "/tmp/m2p-verify-vendor"
    mj = os.path.join(base, "mathjax", "package")
    if not os.path.isfile(os.path.join(mj, "es5", "tex-mml-chtml.js")):
        mj = npm_pack("mathjax@3.2.2", os.path.join(base, "mathjax"))
    me = os.path.join(base, "mermaid", "package", "dist", "mermaid.min.js")
    if not os.path.isfile(me):
        me = os.path.join(npm_pack("mermaid@10.9.3", os.path.join(base, "mermaid")), "dist", "mermaid.min.js")
    return mj, me


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site")
    ap.add_argument("--artifact")
    ap.add_argument("--build", action="store_true", help="build.py 로 --site (기본 /tmp/m2p-site)에 먼저 짓는다")
    ap.add_argument("--root", default=None)
    ap.add_argument("--json")
    ap.add_argument("--only")
    ap.add_argument("--jobs", default="4")
    ap.add_argument("--width", default="390")
    ap.add_argument("--no-local-cdn", action="store_true")
    a = ap.parse_args()
    if a.build:
        a.site = a.site or "/tmp/m2p-site"
        cmd = [sys.executable, os.path.join(HERE, "build.py"), "--out", a.site]
        if a.root:
            cmd += ["--root", a.root]
        subprocess.run(cmd, check=True)
    if not a.site and not a.artifact:
        ap.error("--site, --artifact, --build 중 하나가 필요하다")
    cmd = ["node", os.path.join(HERE, "verify_site.js"), "--jobs", a.jobs, "--width", a.width]
    cmd += ["--artifact", a.artifact] if a.artifact else ["--site", a.site]
    if a.json:
        cmd += ["--json", a.json]
    if a.only:
        cmd += ["--only", a.only]
    if not a.no_local_cdn:
        mj, me = vendor()
        cmd += ["--mathjax", mj, "--mermaid", me]
    env = dict(os.environ)
    if not env.get("NODE_PATH"):
        env["NODE_PATH"] = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    sys.exit(subprocess.run(cmd, env=env).returncode)


if __name__ == "__main__":
    main()
