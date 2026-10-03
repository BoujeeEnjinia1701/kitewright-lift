"""Kitewright Lift product appearance model (build123d), TRL 3, constructable design (KWL-DDR-002).

For photoreal renders only (.kit/export_views.py, then .kit/photoreal.py on Amish's Mac). Every
part is the model.py solid itself, flying-ready with the line-and-float release payload; colours and
material classes are added for the look. Appearance additions not in model.py, recorded in
docs/REVIEW.md: a posed 1.75 m mannequin standing beside the aircraft (never between the camera and
the aircraft), and, for the detail view, one arm hinge shown with short pieces of the hub plates.
CONCEPT, NOT FOR FABRICATION.

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Pos, Rot  # noqa: E402
import model as M  # noqa: E402
from model import PARAMS as P, build_components, bx, turn  # noqa: E402

TITLE = "Kitewright Lift: coaxial X8 rescue multirotor with folding arms"
HERO_EL, HERO_AZ = 22, -40

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "context"], "explode": False, "el": HERO_EL, "az": HERO_AZ,
     "note": "Product render from the front right and above (about 22 deg elevation): coaxial X8 on its skid gear "
             "with the line-and-float release under the hub and two ColdCell packs on the deck, and a 1.75 m person "
             "standing beside it"},
    {"name": "exploded", "groups": ["shell"], "explode": True, "el": 20, "az": -50,
     "note": "Exploded view from the front right and above (about 20 deg elevation): packs, deck, top plate and Core "
             "stack lifted; gear, payload mount and float release lowered; arms, motors and propellers in place"},
    {"name": "detail", "groups": ["internal"], "explode": False, "el": 18, "az": -60,
     "note": "Detail of one arm hinge from the front right and above (about 18 deg elevation): hinge block between "
             "the hub plates, root fitting, pivot bolt, red-flagged lock pin and the stop bridge the arm lifts against"},
]

LOOK = {  # key: (colour, material class, exploded offset)
    "top_plate": ("#2B2F36", "plastic", (0, 0, 220)), "bot_plate": ("#2B2F36", "plastic", (0, 0, -60)),
    "spacers": ("#A3A9B3", "metal", (0, 0, 120)), "hinge_blocks": ("#0F766E", "painted", (0, 0, 0)),
    "arm_roots": ("#14B8A6", "painted", (0, 0, 0)), "arm_tubes": ("#1F2328", "plastic", (0, 0, 0)),
    "motor_mounts": ("#0E7490", "painted", (0, 0, 0)), "pivots": ("#B8BEC6", "metal", (0, 0, 0)),
    "lock_pins": ("#DC2626", "painted", (0, 0, 180)), "motors": ("#3A3F47", "metal", (0, 0, 0)),
    "escs": ("#475569", "plastic", (0, 0, 0)), "props": ("#1B1E23", "plastic", (0, 0, 0)),
    "gear_tops": ("#0F766E", "painted", (0, 0, -240)), "skid_blocks": ("#0F766E", "painted", (0, 0, -420)),
    "struts": ("#1F2328", "plastic", (0, 0, -330)), "skids": ("#1F2328", "plastic", (0, 0, -480)),
    "deck": ("#33373E", "plastic", (0, 0, 320)), "guides": ("#B8BEC6", "metal", (0, 0, 400)),
    "straps": ("#F59E0B", "fabric", (0, 0, 700)), "mast": ("#E5E7EB", "plastic", (0, 0, 820)),
    "core": ("#6D28D9", "plastic", (0, 0, 100)), "rails": ("#9333EA", "painted", (0, 0, -180)),
    "ds014": ("#9333EA", "painted", (0, 0, -180)), "paylock": ("#DC2626", "painted", (0, -160, -180)),
    "packs": ("#2563EB", "plastic", (0, 0, 560)), "fr_plate": ("#A3A9B3", "metal", (0, 0, -360)),
    "saddles": ("#E5E7EB", "plastic", (0, 0, -440)), "release": ("#1D4ED8", "plastic", (0, 0, -440)),
    "sling": ("#FACC15", "fabric", (0, 0, -520)), "float": ("#F97316", "rubber", (0, 0, -600)),
}


def _detail_parts():
    """One arm hinge, in the arm's own frame (arm along +X), with short pieces of the hub plates."""
    loc = M.arm_group_local(P)
    plates = (M.hub_plate(P, False) + M.hub_plate(P, True)).rotate(M.Axis.Z, -45) & bx(90, 200, -70, 70, 0, 2000)
    tube = loc["arm_tubes"] & bx(200, 420, -40, 40, 0, 2000)
    return [("Hub plates (part)", plates, "#2B2F36", "plastic", 2),
            ("Arm hinge block", M.hinge_block_local(P), "#0F766E", "painted", 4),
            ("Arm root fitting", loc["arm_roots"], "#14B8A6", "painted", 5),
            ("Arm tube (part)", tube, "#1F2328", "plastic", 6),
            ("Hinge pivot bolt", M.pivot_pin_local(P), "#B8BEC6", "metal", 8),
            ("Arm lock pin", M.lock_pin_local(P), "#DC2626", "painted", 9)]


def product_parts(P=P):
    C = build_components(P, "float")
    out = []

    def add(name, shape, color, material, bom, group, explode):
        out.append({"name": name, "shape": shape, "color": color, "material": material,
                    "bom": bom, "group": group, "explode": tuple(float(v) for v in explode)})

    for k, c in C.items():
        color, mat, ex = LOOK[k]
        add(c.name, c.shape, color, mat, c.bom, "shell", ex)
    for name, shape, color, mat, bom in _detail_parts():
        add(name, shape, color, mat, bom, "internal", (0, 0, 0))
    from context_parts import mannequin
    a = math.radians(HERO_AZ)
    cam = (math.cos(a), math.sin(a))
    right = (-cam[1], cam[0])
    k, back = 1450.0, -200.0                          # beside the aircraft, a little behind it
    x = -right[0] * k + cam[0] * back
    y = -right[1] * k + cam[1] * back
    person = Pos(x, y, 0) * Rot(0, 0, HERO_AZ + 90 - 30) * mannequin(1750, "stand")
    add("Person, 1.75 m (scale)", person, "#D1D5DB", "clay", None, "context", (0, 0, 0))
    return out


if __name__ == "__main__":
    for p in product_parts():
        s = p["shape"]
        print(f"{p['name']:44s} {p['group']:9s} {p['material']:9s} vol={sum(x.volume for x in s.solids()) / 1000:9.1f} cm3")
