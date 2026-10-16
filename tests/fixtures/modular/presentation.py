"""Synthetic calibration fixture, not a benchmark submission."""

import xml.etree.ElementTree as ET
import engine


def run_batch(jobs):
    """Return ordered results; invalid job structure raises ValueError before work."""
    if not isinstance(jobs, list) or len(jobs) > 100:
        raise ValueError('invalid jobs')
    for job in jobs:
        if (not isinstance(job, dict) or set(job)-{'expression', 'variables'}
                or 'expression' not in job or not isinstance(job['expression'], str)):
            raise ValueError('invalid job')
        engine.variables_checked(job.get('variables'))
    results = []
    for job in jobs:
        try:
            results.append({'ok': True, 'value': engine.evaluate(job['expression'], job.get('variables'))})
        except ValueError as error:
            results.append({'ok': False, 'error': str(error)})
    return results


def write_svg(points, output_path, title=''):
    """Write SVG from points and text title; filesystem errors propagate as OSError."""
    root = ET.Element('svg', xmlns='http://www.w3.org/2000/svg', width='640', height='480', viewBox='0 0 640 480')
    ET.SubElement(root, 'title').text = title
    valid = [(x, y) for x, y in points if y is not None]
    if valid:
        xs, ys = zip(*valid)
        lowx, highx, lowy, highy = min(xs), max(xs), min(ys), max(ys)
        segments, segment = [], []
        for x, y in points:
            if y is None:
                segments.append(segment)
                segment = []
            else:
                segment.append((20+600*(x-lowx)/(highx-lowx or 1), 460-440*(y-lowy)/(highy-lowy or 1)))
        segments.append(segment)
        for segment in segments:
            if len(segment) >= 2:
                ET.SubElement(root, 'polyline', {'data-series': 'curve', 'fill': 'none', 'stroke': 'blue',
                                               'points': ' '.join(f'{x},{y}' for x, y in segment)})
    ET.ElementTree(root).write(output_path, encoding='utf-8', xml_declaration=True)
