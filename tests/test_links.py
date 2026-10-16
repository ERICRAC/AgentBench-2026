"""Meaningful link regression cases, without a browser or network."""

from pathlib import Path
import tempfile
import unittest

from scripts.check_links import anchors, inspect, targets


class LinksTests(unittest.TestCase):
    def test_reference_and_adaptive_images(self):
        text = '[Report][r]\n[r]: report.md\n<source srcset="dark.png 1x, large.png 2x">\n<img src="light.png">'
        self.assertEqual(set(targets(text)), {'report.md', 'dark.png', 'large.png', 'light.png'})

    def test_fenced_examples_are_ignored(self):
        self.assertEqual(targets('```md\n[x](missing.md)\n```\n[x](real.md)'), ['real.md'])

    def test_duplicate_unicode_headings(self):
        self.assertEqual(anchors('# Résumé\n# Résumé\n'), {'résumé', 'résumé-1'})

    def test_missing_file_anchor_and_editor_url(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            doc = root / 'README.md'
            doc.write_text('# Title\n[ok](#title)\n[bad](#absent)\n[missing](gone.md)\n[editor](https://vscode-cdn.net/file)')
            count, remote, errors = inspect([doc], root)
            self.assertEqual(count, 4)
            self.assertEqual(len(errors), 3)
            self.assertFalse(remote)


if __name__ == '__main__':
    unittest.main()
