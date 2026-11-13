#!/usr/bin/env python3
"""Regression tests against real source/graph, with isolated minimal cards."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHECK = Path(__file__).resolve().parents[1] / 'check.py'

def card(cid, kind, uses, children, file, lines):
    return f'''---
id: {cid}
kind: {kind}
title: Fixture
uses: [{', '.join(uses)}]
children: [{', '.join(children)}]
source:
  - {{file: {file}, lines: [{lines[0]}, {lines[1]}]}}
status: proposed
---
'''

class DependencyTest(unittest.TestCase):
    def test_section_descendant_and_ancestor_uses(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root / 'cards').mkdir()
            def write(name, text): (root / 'cards' / (name + '.md')).write_text(text)
            write('section', card('model:section', 'section', [], ['model:functional'], 'model.tex', (1, 1)))
            write('child', card('model:functional', 'definition', [], [], 'model.tex', (80, 80)))
            write('parent', card('x:fixture-parent', 'device', ['model:functional'], ['comp:bounded-lower'], 'comparison.tex', (1, 1)))
            def run():
                out = root / 'report.md'
                subprocess.run([sys.executable, str(CHECK), '--root', tmp, '--out', str(out)], capture_output=True, check=False)
                report = out.read_text()
                return [line for line in report.splitlines() if 'comparison.tex:227' in line and '`comp:bounded-lower`' in line]
            write('consumer', card('comp:bounded-lower', 'corollary', ['model:functional'], [], 'comparison.tex', (227, 227)))
            self.assertEqual(run(), [])  # direct descendant
            write('consumer', card('comp:bounded-lower', 'corollary', [], [], 'comparison.tex', (227, 227)))
            self.assertEqual(run(), [])  # ancestor's uses
            write('parent', card('x:fixture-parent', 'device', [], ['comp:bounded-lower'], 'comparison.tex', (1, 1)))
            self.assertEqual(len(run()), 1)  # no relevant uses must warn
            write('consumer', card('comp:bounded-lower', 'corollary', ['model:section'], [], 'comparison.tex', (227, 227)))
            self.assertEqual(run(), [])  # explicit section

if __name__ == '__main__': unittest.main()
