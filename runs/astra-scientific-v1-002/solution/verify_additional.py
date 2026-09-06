"""Contrôles complémentaires du candidat ; ne modifie pas la suite indépendante.

Lancement depuis solution/ : python3 -B verify_additional.py
"""

import math
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

from scientific_calculator import evaluate, sample_curve, write_svg


class AdditionalChecks(unittest.TestCase):
    def test_resource_limits(self):
        for expression in (
            "1" * 10001, "+".join(["1"] * 1100),
            "(" * 101 + "1" + ")" * 101, "-" * 101 + "1",
        ):
            with self.subTest(length=len(expression)):
                with self.assertRaises(ValueError):
                    evaluate(expression)
        self.assertEqual(evaluate("(" * 100 + "1" + ")" * 100), 1.0)

    def test_extreme_sampling(self):
        extreme = float.fromhex("0x1.fffffffffffffp+1023")
        for lower, upper in (
            (-extreme, extreme), (math.nextafter(extreme, 0), extreme),
            (-extreme, math.nextafter(-extreme, 0)), (-5e-324, 5e-324),
        ):
            with self.subTest(lower=lower, upper=upper):
                points = sample_curve("x", lower, upper, 201)
                self.assertEqual(points[0], (lower, lower))
                self.assertEqual(points[-1], (upper, upper))
                self.assertTrue(all(math.isfinite(x) and y == x for x, y in points))
                self.assertTrue(all(lower <= x <= upper for x, _ in points))
                self.assertTrue(all(a[0] <= b[0] for a, b in zip(points, points[1:])))

    def test_xml_and_scaling(self):
        namespace = {"s": "http://www.w3.org/2000/svg"}
        cases = [
            [(-1.7e308, -1.7e308), (0, None), (1.7e308, 1.7e308)],
            [(0, 5e-324), (5e-324, 1e-323)],
            [(1, 2)], [(1, 2), (1, 2)],
        ]
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as folder:
            for index, points in enumerate(cases):
                path = Path(folder) / f"{index}.svg"
                write_svg(points, str(path), "<script>&\x00\ud800")
                root = ET.parse(path).getroot()
                self.assertEqual(root.find("s:title", namespace).text, "<script>&\ufffd\ufffd")
                self.assertEqual(len(root.findall("s:line", namespace)), 2)
                self.assertIsNone(root.find(".//s:script", namespace))
                for element in root.iter():
                    for name, value in element.attrib.items():
                        if name in {"x", "y", "x1", "x2", "y1", "y2", "cx", "cy"}:
                            self.assertTrue(math.isfinite(float(value)))
                        if name == "points":
                            self.assertTrue(all(
                                math.isfinite(float(number))
                                for pair in value.split() for number in pair.split(",")
                            ))

    def test_invalid_parameters(self):
        for count in (True, 2.0, 1):
            with self.assertRaises(ValueError):
                sample_curve("x", 0, 1, count)
        for bound in (float("nan"), float("inf"), True):
            with self.assertRaises(ValueError):
                sample_curve("x", bound, 1)
        with self.assertRaises(ValueError):
            evaluate("x", {"x": float("inf")})
        with self.assertRaises(ValueError):
            sample_curve("unknown(x)", 0, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
