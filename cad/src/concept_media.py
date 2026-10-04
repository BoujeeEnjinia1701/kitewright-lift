"""Kitewright Lift concept media from the TRL 3 parametric model (constructable design, KWL-DDR-002,
with decisions 34A and 35A of 2026-10-03, KWL-DDR-003).

Run from the repo root:  python cad/src/concept_media.py [hero|cutaway|exploded|flow|web|blueprint ...]
With no argument it draws everything. On a small machine run one picture per process.
Geometry comes from cad/src/model.py; figures come from docs/04-calcs/results.csv (KWL-CAL-001,
run docs/04-calcs/sizing.py first). Every coloured part carries its bom/bom.csv line number.
The aircraft is shown flying-ready with the line-and-float release payload. CONCEPT, NOT FOR FABRICATION.

Axes: X forward, Y left, Z up from the ground.
"""
import csv
import math
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import concept as K  # noqa: E402
from concept import Part  # noqa: E402
from model import build_components  # noqa: E402

PROJECT, TITLE, DWG, DATE = "Kitewright Lift", "Coaxial X8 rescue multirotor with folding arms", "KWL-DWG-010", "2026-10-03"
MD = ROOT / "media"

COLOR = {
    "top_plate": "#374151", "bot_plate": "#374151", "spacers": "#9CA3AF", "hinge_blocks": "#0F766E",
    "arm_roots": "#14B8A6", "arm_tubes": "#1F2937", "motor_mounts": "#0E7490", "pivots": "#9CA3AF",
    "lock_pins": "#DC2626", "motors": "#6B7280", "escs": "#475569", "props": "#334155",
    "gear_tops": "#0F766E", "skid_blocks": "#0F766E", "struts": "#1F2937", "skids": "#1F2937",
    "deck": "#4B5563", "guides": "#9CA3AF", "straps": "#F59E0B", "mast": "#E5E7EB",
    "core": "#7C3AED", "rails": "#A855F7", "ds014": "#A855F7", "paylock": "#DC2626",
    "packs": "#2563EB", "fr_plate": "#94A3B8", "saddles": "#E5E7EB", "release": "#1D4ED8",
    "sling": "#FACC15", "float": "#F97316", "tm_plate": "#94A3B8", "converter": "#16A34A",
    "breakaway": "#FACC15", "tether": "#F59E0B",
}
EXPLODE = {  # exploded-view offsets (mm)
    "packs": (0, 0, 520), "straps": (0, 0, 640), "mast": (0, 0, 760), "guides": (0, 0, 380), "deck": (0, 0, 300),
    "spacers": (0, 0, 120), "top_plate": (0, 0, 200), "core": (0, 0, -120), "bot_plate": (0, 0, -60),
    "rails": (0, 0, -170), "ds014": (0, 0, -170), "paylock": (0, -150, -170),
    "fr_plate": (0, 0, -330), "release": (0, 0, -400), "saddles": (0, 0, -400), "sling": (0, 0, -480), "float": (0, 0, -560),
    "gear_tops": (0, 0, -220), "struts": (0, 0, -300), "skid_blocks": (0, 0, -360), "skids": (0, 0, -420),
    "lock_pins": (0, 0, 160), "pivots": (0, 0, 0),
}


def values():
    out = {}
    with (ROOT / "docs" / "04-calcs" / "results.csv").open() as f:
        for r in csv.DictReader(f):
            if r["id"] == "value":
                out[r["requirement"]] = float(r["result"])
    return out


def parts(payload="float", explode=False):
    C = build_components(payload=payload)
    return [Part(c.name, c.shape, COLOR[k], c.bom, EXPLODE.get(k, (0, 0, 0)) if explode else (0, 0, 0))
            for k, c in C.items()]


def person():
    # beside the aircraft, to the left of it as the hero camera sees it and no nearer the camera
    return K.human_figure(1750.0, x=-1150.0, y=-720.0, z=0.0)


def hero():
    ps = parts() + [person()]
    return K._render(ps, MD / "hero.png", title=PROJECT, elev=22, azim=-58,
                     note="Seen from the front right and above, 22 deg elevation. Grey figure: 1.75 m person for scale, "
                          "standing beside the aircraft. Line-and-float release payload fitted under the hub")


def cutaway():
    ps = [p for p in parts() if p.bom not in (12,)]
    return K._render(K.cutaway_parts(ps, keep="+Y"), MD / "cutaway.png", azim=-90, elev=14, title=f"{PROJECT}: cutaway",
                     note="Cut on the centre line, front half removed, propellers left out; seen from the front, 14 deg "
                          "elevation. Core under the bottom plate with its lid up in the hub, packs on the raised deck, payload shoe on the Core rail")


def exploded():
    ps = [p for p in parts(explode=True) if p.bom not in (8,)]
    return K._render(ps, MD / "exploded.png", offsets=True, labels=True, title=f"{PROJECT}: exploded view",
                     elev=20, azim=-58, size=(10, 8),
                     note="Seen from the front right and above, 20 deg elevation; numbers match bom/bom.csv. "
                          "Arms, motors and propellers stay in place; hub stack pulled up, gear and payload pulled down")


def web():
    """Coarse glTF tessellation (1 mm chord, 0.35 rad) keeps media/model.glb small for the website."""
    import functools
    import build123d as bd
    orig = bd.export_gltf
    bd.export_gltf = functools.partial(orig, linear_deflection=1.0, angular_deflection=0.35)
    try:
        return K.export_web_model(parts(), "media", title=f"{PROJECT}: {TITLE}")
    finally:
        bd.export_gltf = orig


def flow():
    v = values()
    p = v["p_sl_r"]
    base = 50.0
    drive = p - base
    shaft = drive * 0.80
    ideal = shaft * 0.65
    return K.flow_diagram(
        [("From the packs", round(p)), ("Into the motor controllers", round(drive)), ("Shaft power", round(shaft)),
         ("Lift work on the air (ideal)", round(ideal))],
        MD / "flow.png", f"{PROJECT}: power flow in hover at sea level with the rated {v['payload_rated']:.1f} kg payload (W, all values are estimates, KWL-CAL-001)", "W",
        [(0, "Core avionics and payload (est.)", round(base)), (1, "Motor and controller heat (est.)", round(drive - shaft)),
         (2, "Propeller profile, swirl and coaxial losses (est.)", round(shaft - ideal))])


def blueprint():
    from build123d import Compound
    from drawing import Sheet, project_views
    v = values()
    views = project_views(Compound([p.shape for p in parts()]), MD / "_views")
    shown = parts() + [person()]
    views["iso"] = project_views(Compound([p.shape for p in shown]), MD / "_views_fig")["iso"]
    s = Sheet(project=PROJECT, title=TITLE, dwg_no=DWG, rev="P3", author="Amish Chadha", date="2026-10-04", theme="blueprint",
              material="Massing model for concept communication",
              revisions=[("P1", "Concept sheet from the constructable model", DATE, "AC"),
                         ("P2", "KWL-DDR-003: lighter fittings, Li-ion packs", DATE, "AC"),
                         ("P3", "KWL-DDR-004: ColdCell packs, Core envelope", "2026-10-04", "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 37, 140, 113, label="Isometric view", sublabel="Not to scale; figure is a 1.75 m person")
    s.add_notes("Key figures", [
        "Coaxial X8: 8 motors, 30 inch props, 1,240 mm motor to motor",
        f"Take-off mass {v['mtow_r']:.1f} kg with the rated {v['payload_rated']:.1f} kg payload (limit 25 kg)",
        f"Two ColdCell lithium-ion packs, 4.46 kg and {v['packs_wh'] / 2:,.0f} Wh each",
        f"Hover {v['t_sl_r']:.0f} min at sea level with {v['payload_rated']:.1f} kg (est.)",
        f"Hover {v['t_alt_2']:.0f} min at 5,000 m and -20 C with 2 kg (est.)",
        f"Thrust to weight {v['tw_alt']:.2f} at 5,000 m; {v['tw_out_alt']:.2f} with a motor out",
        f"Tether: {v['p_tether'] / 1000:.1f} kW hover from a 400 V ground supply",
        f"Folds to {v['fold_z'] / 1000:.2f} x {v['fold_y'] / 1000:.2f} x {v['fold_x'] / 1000:.2f} m"], x=276, y=168, width=140)
    s.save(MD / "concept-blueprint")
    shutil.rmtree(MD / "_views", ignore_errors=True)
    shutil.rmtree(MD / "_views_fig", ignore_errors=True)
    return MD / "concept-blueprint.png"


if __name__ == "__main__":
    fns = {"hero": hero, "cutaway": cutaway, "exploded": exploded, "flow": flow, "web": web, "blueprint": blueprint}
    for w in sys.argv[1:] or list(fns):
        print(w, "->", fns[w]())
