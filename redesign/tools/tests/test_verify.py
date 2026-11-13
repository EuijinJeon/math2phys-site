"""verify_site 시험: 일부러 깨뜨린 작은 사이트에서 수식 오류, 깨진 링크, 가로 넘침, 콘솔 오류를 모두 센다.
Chromium·노드 playwright·npm 이 없으면 건너뛴다. (MathJax 는 npm 에서 받아 캐시한다.)
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent

GOOD = """<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<script>window.MathJax={tex:{inlineMath:[['$','$']]}};</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script></head>
<body><p>$x^2$ <a href="bad.html">bad</a></p><a id="here" href="#here">ok</a> <a href="sub/p.html#a1">ok2</a></body></html>"""
BAD = """<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<script>window.MathJax={tex:{inlineMath:[['$','$']]}};</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script>console.error('boom')</script></head>
<body><p>$\\undefinedmacro{x}$</p><a href="nope.html">x</a> <a href="index.html#missing">y</a>
<div style="width:900px;height:10px;background:#ccc"></div></body></html>"""
SUB = """<!doctype html><html><body><h1 id="a1">t</h1></body></html>"""


class TestVerify(unittest.TestCase):
    def test_detects_problems(self):
        if not shutil.which("node") or not shutil.which("npm"):
            self.skipTest("node/npm 없음")
        site = Path(tempfile.mkdtemp(prefix="m2p-vsite-"))
        self.addCleanup(shutil.rmtree, site, True)
        (site / "sub").mkdir()
        (site / "index.html").write_text(GOOD.replace('href="bad.html"', 'href="bad.html"'), encoding="utf-8")
        (site / "bad.html").write_text(BAD, encoding="utf-8")
        (site / "sub" / "p.html").write_text(SUB, encoding="utf-8")
        out = site / "out.json"
        r = subprocess.run([sys.executable, str(TOOLS / "verify_site.py"), "--site", str(site), "--json", str(out)],
                           capture_output=True, text=True, timeout=300)
        if not out.is_file():
            self.skipTest("Chromium 을 띄우지 못했다: " + (r.stdout + r.stderr)[-300:])
        s = json.loads(out.read_text())["summary"]
        self.assertEqual(r.returncode, 1)
        self.assertEqual(s["pages"], 3)
        self.assertGreaterEqual(s["pages_with_merror"], 1)
        self.assertEqual(s["broken_links"], 2)          # nope.html, index.html#missing (bad.html 는 있다)
        self.assertEqual(s["pages_overflow"], 1)
        self.assertGreaterEqual(s["pages_with_console_errors"], 1)


if __name__ == "__main__":
    unittest.main()
