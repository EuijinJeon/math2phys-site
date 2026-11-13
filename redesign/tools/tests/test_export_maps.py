#!/usr/bin/env python3
"""An export must reject missing or stale diagrams in an independent root."""
import shutil
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
REDESIGN = TOOLS.parent

class ExportMapsTest(unittest.TestCase):
    def test_missing_and_stale(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(REDESIGN / 'cards', root / 'cards')
            spec = importlib.util.spec_from_file_location('test_build', TOOLS / 'build.py')
            build = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(build)
            maps = build.all_maps(build.Struct(build.C.load_cards(root), build.C.load_graph()))
            mapsdir = root / 'build' / 'artifact' / 'maps'; mapsdir.mkdir(parents=True)
            for name, text in maps.items():
                (mapsdir / (name + '.mmd')).write_text(text + '\n')
                (mapsdir / (name + '.svg')).write_text('<svg/>')
            site = root / 'site'; site.mkdir()
            (site / 'index.html').write_text('<html><body><div class="wrap">test</div></body></html>')
            def run():
                return subprocess.run([sys.executable, str(TOOLS / 'export_artifact.py'), '--root', tmp], capture_output=True, text=True)
            valid = run()
            self.assertEqual(valid.returncode, 0, valid.stderr)
            mmd = root / 'build' / 'artifact' / 'maps' / 'sections.mmd'
            mmd.write_text(mmd.read_text() + '% stale\n')
            stale = run()
            self.assertNotEqual(stale.returncode, 0)
            self.assertIn('현재 카드와 다르다', stale.stderr)
            mmd.unlink()
            missing = run()
            self.assertNotEqual(missing.returncode, 0)
            self.assertIn('없다', missing.stderr)

if __name__ == '__main__': unittest.main()
