"""Convert supplied LandXML horizontal alignments into sampled XY chainage JSON."""

from __future__ import annotations

import json
import math
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    "GO110": ("data/source/alignments/GO110.xml", "easting_northing"),
    "GO236": ("data/source/alignments/GO236.xml", "northing_easting"),
}
SAMPLE_SPACING_M = 5.0


def children(element: ET.Element, name: str) -> list[ET.Element]:
    return [child for child in list(element) if child.tag.rsplit("}", 1)[-1] == name]


def point(element: ET.Element, order: str) -> tuple[float, float]:
    first, second = map(float, (element.text or "").split()[:2])
    return (first, second) if order == "easting_northing" else (second, first)


def sample_alignment(road: str, relative_path: str, order: str) -> dict:
    tree = ET.parse(ROOT / relative_path)
    alignment = next(node for node in tree.iter() if node.tag.rsplit("}", 1)[-1] == "Alignment")
    coord_geom = next(node for node in list(alignment) if node.tag.rsplit("}", 1)[-1] == "CoordGeom")
    output: list[dict[str, float]] = []
    chainage = 0.0

    for segment in list(coord_geom):
        kind = segment.tag.rsplit("}", 1)[-1]
        if kind not in {"Line", "Curve", "Spiral"}:
            continue
        start_el = next((node for node in list(segment) if node.tag.rsplit("}", 1)[-1] == "Start"), None)
        end_el = next((node for node in list(segment) if node.tag.rsplit("}", 1)[-1] == "End"), None)
        if start_el is None or end_el is None:
            continue
        start, end = point(start_el, order), point(end_el, order)
        length = float(segment.attrib.get("length", math.dist(start, end)))
        count = max(1, math.ceil(length / SAMPLE_SPACING_M))
        center_el = next((node for node in list(segment) if node.tag.rsplit("}", 1)[-1] == "Center"), None)

        if kind == "Curve" and center_el is not None:
            center = point(center_el, order)
            radius = math.dist(start, center)
            a0 = math.atan2(start[1] - center[1], start[0] - center[0])
            a1 = math.atan2(end[1] - center[1], end[0] - center[0])
            if segment.attrib.get("rot", "ccw").lower() == "cw":
                sweep = -((a0 - a1) % (2 * math.pi))
            else:
                sweep = (a1 - a0) % (2 * math.pi)

            def at(fraction: float) -> tuple[float, float]:
                angle = a0 + sweep * fraction
                return center[0] + radius * math.cos(angle), center[1] + radius * math.sin(angle)

        else:
            # Spirals are linearly sampled between their exported endpoints. The GPS
            # uncertainty is much larger than this approximation for the supplied axis.
            def at(fraction: float) -> tuple[float, float]:
                return start[0] + (end[0] - start[0]) * fraction, start[1] + (end[1] - start[1]) * fraction

        if not output:
            output.append({"x": start[0], "y": start[1], "m": chainage})
        for index in range(1, count + 1):
            fraction = index / count
            x, y = at(fraction)
            output.append({"x": x, "y": y, "m": chainage + length * fraction})
        chainage += length

    equations = []
    for equation in children(alignment, "StaEquation"):
        equations.append({key: float(value) for key, value in equation.attrib.items() if key in {"staAhead", "staBack", "staInternal"}})

    return {
        "road": road,
        "alignmentName": alignment.attrib.get("name", road),
        "stationStart": float(alignment.attrib.get("staStart", "0")),
        "stationIntervalMeters": 20.0,
        "coordinateOrder": "easting_northing",
        "sourceCoordinateOrder": order,
        "sourceLengthMeters": float(alignment.attrib.get("length", chainage)),
        "sampleLengthMeters": chainage,
        "stationEquations": equations,
        "points": output,
    }


for road, (source, order) in INPUTS.items():
    data = sample_alignment(road, source, order)
    destination = ROOT / "data/processed/alignments" / f"{road}-centerline.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"{road}: {len(data['points'])} points, {data['sampleLengthMeters']:.3f} m -> {destination.relative_to(ROOT)}")

