"""Offline protocol guards; no processes or model calls in these unit tests."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from preflight_parallel_pilot import hashes, snapshot


class ParallelGuards(unittest.TestCase):
    def test_exact_deliverables_and_hashes(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'engine.py').write_text('fixture')
            files = snapshot(root, {'engine.py'})
            self.assertEqual(files, {'engine.py': b'fixture'})
            self.assertEqual(len(hashes(files)['engine.py']), 64)

    def test_missing_and_extra_files_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            with self.assertRaises(ValueError):
                snapshot(root, {'engine.py'})
            (root/'engine.py').write_text('fixture')
            (root/'other.py').write_text('outside assignment')
            with self.assertRaises(ValueError):
                snapshot(root, {'engine.py'})

    def test_symlink_and_directory_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'file').write_text('fixture')
            (root/'engine.py').symlink_to(root/'file')
            with self.assertRaises(ValueError):
                snapshot(root, {'engine.py', 'file'})
            (root/'engine.py').unlink()
            (root/'engine.py').mkdir()
            with self.assertRaises(ValueError):
                snapshot(root, {'engine.py', 'file'})

    def test_no_live_mode_or_implicit_launch(self):
        script = Path(__file__).resolve().parents[1]/'scripts/preflight_parallel_pilot.py'
        for arguments in ([], ['--live'], ['--simulate', '--live']):
            result = subprocess.run([sys.executable, '-B', str(script), *arguments],
                                    capture_output=True, text=True, timeout=5)
            self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main()
