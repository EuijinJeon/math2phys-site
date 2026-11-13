#!/usr/bin/env python3
"""증명 지도(섹션 지도 + 섹션별 지도)를 미리 SVG 로 그린다. export_artifact.py 가 이것을 쓴다.

build.py 의 all_maps() 가 만든 Mermaid 텍스트를 build/artifact/maps/<이름>.mmd 로 쓰고,
헤드리스 Chromium(Playwright, 노드)으로 <이름>.svg 를 그린다.

사용: python3 tools/render_maps.py [--root DIR] [--out DIR] [--mermaid mermaid.min.js]
  --out  지도 파일(.mmd, .svg)을 쓸 디렉터리 (기본: <root>/build/artifact/maps)
  Mermaid 는 이 순서로 찾는다: --mermaid, 환경변수 M2P_MERMAID, <root>/build/artifact/vendor/mermaid.min.js,
  없으면 npm 레지스트리에서 mermaid@10.9.3 을 받아 임시 디렉터리에 푼다(CDN 이 막힌 환경에서도 npm 은 열려 있을 수 있다).
  Chromium: 환경변수 CHROME, 없으면 /opt/pw-browsers 아래의 headless_shell 이나 chrome.
  node 의 playwright: NODE_PATH 가 없으면 전역 node_modules 를 찾아 넣는다. `playwright install` 은 하지 않는다.
"""
import argparse, glob, importlib.util, os, shutil, subprocess, sys, tarfile, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REAL_ROOT = os.path.dirname(HERE)


def load_build():
    spec = importlib.util.spec_from_file_location("build", os.path.join(HERE, "build.py"))
    B = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("build_mod", B)
    spec.loader.exec_module(B)
    return B


def find_mermaid(arg, root):
    for p in (arg, os.environ.get("M2P_MERMAID"), os.path.join(root, "build", "artifact", "vendor", "mermaid.min.js")):
        if p and os.path.isfile(p):
            return os.path.abspath(p)
    tmp = tempfile.mkdtemp(prefix="m2p-mermaid-")
    r = subprocess.run(["npm", "pack", "mermaid@10.9.3", "--silent"], cwd=tmp, capture_output=True, text=True)
    tgz = glob.glob(os.path.join(tmp, "mermaid-*.tgz"))
    if r.returncode or not tgz:
        sys.exit("Mermaid 를 찾지 못했고 npm 에서도 받지 못했다. --mermaid 로 mermaid.min.js 를 알려 준다.\n" + r.stderr[-300:])
    with tarfile.open(tgz[0]) as t:
        t.extractall(tmp)
    return os.path.join(tmp, "package", "dist", "mermaid.min.js")


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for pat in ("/opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell",
                "/opt/pw-browsers/chromium-*/chrome-linux64/chrome"):
        m = sorted(glob.glob(pat))
        if m:
            return m[-1]
    return None


def node_path():
    if os.environ.get("NODE_PATH"):
        return os.environ["NODE_PATH"]
    r = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True)
    return r.stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--mermaid", default=None)
    args = ap.parse_args()
    root = os.path.abspath(args.root or os.environ.get("M2P_ROOT") or REAL_ROOT)
    B = load_build()
    C = B.C
    cards = C.load_cards(root)
    S = B.Struct(cards, C.load_graph())
    maps = B.all_maps(S)
    out = os.path.abspath(args.out) if args.out else os.path.join(root, "build", "artifact", "maps")
    os.makedirs(out, exist_ok=True)
    for f in glob.glob(os.path.join(out, "*.mmd")) + glob.glob(os.path.join(out, "*.svg")):
        os.remove(f)
    for name, text in maps.items():
        with open(os.path.join(out, name + ".mmd"), "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
    mer = find_mermaid(args.mermaid, root)
    env = dict(os.environ, NODE_PATH=node_path())
    chrome = find_chrome()
    if chrome:
        env["CHROME"] = chrome
    print(f"지도 {len(maps)}개, mermaid={mer}, chrome={chrome}")
    r = subprocess.run(["node", os.path.join(HERE, "render_maps.js"), mer, out, *maps], env=env)
    if r.returncode:
        sys.exit(f"일부 지도를 그리지 못했다 (종료 코드 {r.returncode})")
    old = os.path.join(root, "build", "artifact", "map.svg")
    if not args.out and os.path.isfile(old):
        os.remove(old)   # 옛 단일 지도(§7 시범 때의 것)
        print("옛 build/artifact/map.svg 삭제")


if __name__ == "__main__":
    main()
