"""Kitewright Lift parametric model (build123d), TRL 3, constructable design (KWL-DDR-002).

Run from the repo root:
    python cad/src/model.py            print derived sizes, run the constructability checks, export STEP and STL
    python cad/src/model.py --check    checks only, no export

The aircraft is a coaxial X8: four folding carbon arms on a two-plate carbon hub, a motor on top of and
a motor under each arm tip, 30 inch folding propellers. Each arm hinges on a machined aluminium clevis
block at a hub corner and folds DOWN for transport; in flight the thrust presses the arm up against a
stop bridge on the clevis, and a ball-lock pin only stops the arm drooping. The Kitewright Core stack
sits between the hub plates, two ColdCell packs sit on a deck above them, and payloads slide onto the
Core payload rails under the hub. Two payload modules are modelled: the line-and-float release and the
tether power module.

Axes: X forward, Y left, Z up from the ground (the skids stand on Z = 0). The arms lie on the diagonals
at 45, 135, 225 and 315 degrees. Each arm group is built in a local frame (radial = +X, tangential = +Y)
and turned into place. Units mm. Parts marked (Core) and (ColdCell) are made to the sibling designs;
their sizes here are interface assumptions listed in docs/REVIEW.md, Cross-repo actions.
CONCEPT, NOT FOR FABRICATION.
"""
from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

from build123d import (Axis, Box, Compound, Cylinder, Polyline, Pos, Rot, Solid, Vector, export_step,
                       export_stl, extrude, make_face)

ROOT = Path(__file__).resolve().parents[2]

PARAMS = {
    # hub
    "hub_half": 140.0,        # half side of the square hub plates
    "chamfer_r": 162.0,       # corner cut, measured along the diagonal from the centre
    "plate_t": 3.0,           # carbon plate thickness
    "z_bot": 500.0,           # underside of the bottom hub plate above the ground
    "gap": 60.0,              # clear height between the plates (hinge block height)
    # hinge (local radial r, heights relative to z_bot)
    "blk_r": (125.0, 215.0),  # hinge block, radial extent
    "blk_w": 46.0,            # hinge block width (tangential)
    "slot_r0": 150.0,         # inner end of the clevis slot
    "slot_w": 32.0,           # clevis slot width
    "bridge_r": (205.0, 215.0),   # stop bridge across the top of the cheeks
    "bridge_h": 10.0,
    "pivot": (180.0, 17.0),   # pivot bolt (r, height above z_bot)
    "lock": (193.0, 40.0),    # lock pin (r, height above z_bot)
    "pin_d": 8.0,
    "tongue_r": (165.0, 230.0),
    "tongue_w": 30.0,
    "tongue_z": (5.0, 53.0),  # heights above z_bot
    # arm
    "collar_r": (230.0, 280.0),
    "collar_d": 48.0,
    "tube": (40.0, 36.0),     # carbon arm tube OD, ID
    "tube_r": (235.0, 645.0),
    "motor_r": 620.0,         # motor axis radius from the aircraft centre
    "mount": (50.0, 60.0, 52.0),  # motor mount split clamp: radial, tangential, height
    "motor": (90.0, 50.0),    # motor diameter, height
    "hub_d": (40.0, 18.0),    # propeller hub diameter, height
    "prop_d": 762.0,          # 30 inch
    "blade": (50.0, 24.0, 6.0),   # root chord, tip chord, thickness
    "esc": (70.0, 30.0, 18.0),
    "esc_r0": 470.0,
    # deck and packs
    "standoff": (8.0, 25.0),
    "post_xy": 130.0,
    "deck": (290.0, 430.0, 3.0),      # sized for the long lithium-ion packs (KWL-DDR-003; was 330 x 290)
    "deck_chamfer": 35.0,
    "pack": (90.4, 378.0, 85.8),      # ColdCell lithium-ion 14S3P variant: X, Y, Z (CCL-DDR-003, CCL-DWG-002)
    "pack_gap": 30.0,
    "guide": (20.0, 2.0),
    "strap_w": 25.0,
    "mast": (16.0, 230.0),
    "puck": (70.0, 18.0),
    # Core stack (interface assumption)
    "core": (150.0, 100.0, 40.0),
    "damper": (10.0, 6.0),
    # landing gear
    "gear_x": 60.0,
    "strut_top": (112.0, -5.0),       # (y, height relative to z_bot)
    "strut_bot": (222.0, 33.0),       # (y, z)
    "strut_d": (20.0, 17.0),
    "skid_y": 225.0,
    "skid_z": 17.0,
    "skid_half": 170.0,
    "gtop": (30.0, 40.0, 25.0),
    "gskid": (30.0, 30.0, 50.0),
    # payload mount (Core, interface assumption)
    "rail": (260.0, 20.0, 22.0),      # length, width, height
    "rail_in": 56.0,                  # inner face of each rail from the centre line
    "slot": (8.0, 8.0),               # slot depth into the rail, slot height
    "pplate": (240.0, 124.0, 6.0),    # payload plate
    "pplate_x0": -128.0,
    "plug_x": -132.0,                 # front face of the DS-014 socket block
    "lockpin_x": 105.0,
    # float release payload
    "float": (120.0, 420.0),          # diameter, length
    "bag": (90.0, 90.0),
    "saddle_x": 90.0,
    # tether module payload
    "conv": (200.0, 110.0, 65.0),
    # deeper pockets in the machined fittings (KWL-DDR-003, decision 1 option A): side pockets that
    # leave walls and webs of at least 4.5 mm round every hole, boss and face
    "pockets": True, "web": 4.5,
}
ARM_ANGLES = (45.0, 135.0, 225.0, 315.0)
COLLAR_BOLTS = (245.0, 267.0)
GUIDE_X = (-95.0, 0.0, 95.0)


# ---------------------------------------------------------------- helpers
def bx(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(abs(x1 - x0), abs(y1 - y0), abs(z1 - z0))


def zcyl(x, y, r, z0, z1):
    return Pos(x, y, (z0 + z1) / 2) * Cylinder(r, abs(z1 - z0))


def xcyl(y, z, r, x0, x1):
    return Pos((x0 + x1) / 2, y, z) * Rot(0, 90, 0) * Cylinder(r, abs(x1 - x0))


def ycyl(x, z, r, y0, y1):
    return Pos(x, (y0 + y1) / 2, z) * Rot(90, 0, 0) * Cylinder(r, abs(y1 - y0))


def rod(a, b, r):
    a, b = Vector(*a), Vector(*b)
    d = b - a
    L = d.length
    c = Cylinder(r, L)
    z = Vector(0, 0, 1)
    ax = z.cross(d)
    ang = math.degrees(math.acos(max(-1.0, min(1.0, z.dot(d) / L))))
    if ax.length > 1e-9:
        c = c.rotate(Axis((0, 0, 0), (ax.X, ax.Y, ax.Z)), ang)
    return Pos(*((a + b) * 0.5)) * c


def prism_xy(points, z0, z1):
    face = make_face(Polyline(*[(x, y, z0) for x, y in points], close=True))
    return extrude(face, z1 - z0)


def fuse(shapes):
    out = shapes[0]
    for s in shapes[1:]:
        out = out + s
    return out


def turn(shape, deg):
    return Rot(0, 0, deg) * shape


def fold_about(shape, P, deg=90.0):
    """Swing an arm-group shape (local frame) tip-down about the hinge pivot."""
    r, h = P["pivot"]
    z = P["z_bot"] + h
    return Pos(r, 0, z) * Rot(0, deg, 0) * Pos(-r, 0, -z) * shape


# ---------------------------------------------------------------- derived sizes
def derived(P=PARAMS):
    zb, t = P["z_bot"], P["plate_t"]
    z_arm = zb + sum(P["tongue_z"]) / 2
    D = {
        "z_bot_top": zb + t,
        "z_top": zb + t + P["gap"],
        "z_top_top": zb + 2 * t + P["gap"],
        "z_arm": z_arm,
        "z_pivot": zb + P["pivot"][1],
        "z_deck": zb + 2 * t + P["gap"] + P["standoff"][1],
        "z_upper_prop": z_arm + P["mount"][2] / 2 + P["motor"][1] + P["hub_d"][1] / 2,
        "z_lower_prop": z_arm - P["mount"][2] / 2 - P["motor"][1] - P["hub_d"][1] / 2,
        "wheelbase": 2 * P["motor_r"],
        "tip_gap": P["motor_r"] * math.sqrt(2) - P["prop_d"],
        "coax_gap": P["mount"][2] + 2 * P["motor"][1] + P["hub_d"][1],
        "arm_len": P["motor_r"] - P["pivot"][0],
        "stop_lever": (P["bridge_r"][0] + P["bridge_r"][1]) / 2 - P["pivot"][0],
        "lock_lever": math.hypot(P["lock"][0] - P["pivot"][0], P["lock"][1] - P["pivot"][1]),
    }
    D["z_deck_top"] = D["z_deck"] + P["deck"][2]
    D["z_pack_top"] = D["z_deck_top"] + P["pack"][2]
    D["z_mast_top"] = D["z_deck_top"] + P["mast"][1] + P["puck"][1]
    D["coax_ratio"] = (D["z_upper_prop"] - D["z_lower_prop"]) / P["prop_d"]
    D["strut_len"] = math.dist((P["gear_x"], P["strut_top"][0], zb + P["strut_top"][1]),
                               (P["gear_x"], P["strut_bot"][0], P["strut_bot"][1]))
    return D


# ---------------------------------------------------------------- hub
def plate_outline(P=PARAMS):
    h = P["hub_half"]
    c = P["chamfer_r"] * math.sqrt(2) - h   # where the chamfer meets the side
    return [(h, -c), (h, c), (c, h), (-c, h), (-h, c), (-h, -c), (-c, -h), (c, -h)]


def block_bolt_holes(P=PARAMS):
    """Four M4 holes per hinge block, in local (r, t)."""
    return [(131.0, -15.0), (131.0, 15.0), (144.0, -15.0), (144.0, 15.0)]


def hub_posts(P=PARAMS):
    a = P["post_xy"]
    return [(a, 0.0), (-a, 0.0), (0.0, a), (0.0, -a)]


def damper_xy(P=PARAMS):
    return [(sx * 65.0, sy * 40.0) for sx in (-1, 1) for sy in (-1, 1)]


def gear_bolt_xy(P=PARAMS):
    gx, yt = P["gear_x"], P["strut_top"][0]
    return [(sx * gx, sy * (yt + dy)) for sx in (-1, 1) for sy in (-1, 1) for dy in (-15.0, 15.0)]


def rail_bolt_xy(P=PARAMS):
    yc = P["rail_in"] + P["rail"][1] / 2 + P["slot"][0] / 2 + 1.0
    return [(x, sy * yc) for x in (-100.0, 0.0, 100.0) for sy in (-1, 1)]


def local_to_xy(r, t, ang):
    a = math.radians(ang)
    return r * math.cos(a) - t * math.sin(a), r * math.sin(a) + t * math.cos(a)


def hub_plate(P=PARAMS, top=False):
    zb, t = P["z_bot"], P["plate_t"]
    z0 = zb + t + P["gap"] if top else zb
    pl = prism_xy(plate_outline(P), z0, z0 + t)
    holes = []
    for ang in ARM_ANGLES:
        for r, tt in block_bolt_holes(P):
            x, y = local_to_xy(r, tt, ang)
            holes.append((x, y, 2.15))
    for x, y in hub_posts(P):
        holes.append((x, y, 1.65))
    if top:
        holes.append((0.0, 0.0, 15.0))                       # cable pass to the deck and mast
    else:
        holes += [(x, y, 1.65) for x, y in damper_xy(P)]
        holes += [(x, y, 2.15) for x, y in gear_bolt_xy(P)]
        holes += [(x, y, 2.15) for x, y in rail_bolt_xy(P)]
        holes += [(-142.0, 0.0, 2.15), (-142.0, 20.0, 2.15), (-142.0, -20.0, 2.15)]  # DS-014 socket block
        holes.append((40.0, 0.0, 12.0))                       # payload cable pass
    for x, y, r in holes:
        pl = pl - zcyl(x, y, r, z0 - 1, z0 + t + 1)
    return pl


def hinge_block_local(P=PARAMS):
    zb = P["z_bot"]
    z0, z1 = zb + P["plate_t"], zb + P["plate_t"] + P["gap"]
    r0, r1 = P["blk_r"]
    w, sw = P["blk_w"] / 2, P["slot_w"] / 2
    b = bx(r0, r1, -w, w, z0, z1)
    b = b - bx(P["slot_r0"], r1 + 1, -sw, sw, z0 - 1, z1 - P["bridge_h"])           # slot, open below
    b = b - bx(P["slot_r0"], P["bridge_r"][0], -sw, sw, z1 - P["bridge_h"] - 1, z1 + 1)  # slot, open above inboard of the bridge
    b = b - bx(128.0, 147.0, -8.0, 8.0, z0 - 1, z1 + 1)                              # lightening pocket
    pr, ph = P["pivot"]
    lr, lh = P["lock"]
    if P.get("pockets"):
        wb = P["web"]
        # side pockets in the bolting end, between the top and bottom bolt bosses, 4.5 mm from the centre pocket
        for s in (-1, 1):
            b = b - bx(r0 + wb, P["slot_r0"] - 2.0, s * (8.0 + wb), s * (w + 1), z0 + 12 + wb, z1 - 12 - wb)
        # outer-face pockets in the cheeks, 2.5 mm deep (4.5 mm of cheek left), clear of the pin bosses and the bridge
        zp, zl = zb + ph, zb + lh
        bp, bl_ = P["pin_d"] / 2 + wb, P["pin_d"] / 2 + wb
        rects = [(P["slot_r0"] + 2.0, pr - bp - 0.5, z0 + wb, z1 - wb),
                 (pr - bp + 0.5 + 0.0, lr - bl_ - 0.5, zp + bp + 1.0, z1 - wb),
                 (pr + bp + 0.5, P["bridge_r"][0] - 3.0, z0 + wb, zl - bl_ - 0.5)]
        for ra, rb, za, zb_ in rects:
            if rb - ra > 4 and zb_ - za > 4:
                for s in (-1, 1):
                    b = b - bx(ra, rb, s * (sw + wb), s * (w + 1), za, zb_)
    b = b - ycyl(pr, zb + ph, P["pin_d"] / 2 + 0.05, -w - 1, w + 1)
    b = b - ycyl(lr, zb + lh, P["pin_d"] / 2 + 0.1, -w - 1, w + 1)
    for r, tt in block_bolt_holes(P):
        b = b - zcyl(r, tt, 1.65, z0 - 1, z0 + 12) - zcyl(r, tt, 1.65, z1 - 12, z1 + 1)
    return b


def tongue_local(P=PARAMS):
    """Arm root fitting: tongue in the clevis and a collar round the arm tube (one machined part)."""
    zb = P["z_bot"]
    za0, za1 = zb + P["tongue_z"][0], zb + P["tongue_z"][1]
    z_arm = (za0 + za1) / 2
    w = P["tongue_w"] / 2
    t = bx(P["tongue_r"][0], P["tongue_r"][1], -w, w, za0, za1)
    c0, c1 = P["collar_r"]
    t = t + xcyl(0, z_arm, P["collar_d"] / 2, c0, c1)
    t = t - xcyl(0, z_arm, P["tube"][0] / 2 + 0.1, P["tube_r"][0] - 1, c1 + 1)
    pr, ph = P["pivot"]
    lr, lh = P["lock"]
    t = t - ycyl(pr, zb + ph, P["pin_d"] / 2 + 0.05, -w - 1, w + 1)
    t = t - ycyl(lr, zb + lh, P["pin_d"] / 2 + 0.1, -w - 1, w + 1)
    t = t - bx(206.0, 228.0, -w - 1, w + 1, z_arm - 12, z_arm + 12)                   # lightening window
    if P.get("pockets"):
        wb = P["web"]
        web_half = 5.0                                                               # 10 mm centre web
        bp = P["pin_d"] / 2 + wb
        rects = [(P["tongue_r"][0] + wb, lr - bp - 0.5, zb + ph + bp + 0.5, za1 - wb),
                 (pr + bp + 0.5, 206.0 - wb, za0 + wb, zb + lh - bp - 0.5)]
        for ra, rb, za, zb_ in rects:
            if rb - ra > 4 and zb_ - za > 4:
                for s in (-1, 1):
                    t = t - bx(ra, rb, s * web_half, s * (w + 1), za, zb_)
    for r in COLLAR_BOLTS:
        t = t - ycyl(r, z_arm, 2.65, -30, 30)
    return t


def tube_local(P=PARAMS):
    z_arm = derived(P)["z_arm"]
    o, i = P["tube"]
    r0, r1 = P["tube_r"]
    tb = xcyl(0, z_arm, o / 2, r0, r1) - xcyl(0, z_arm, i / 2, r0 - 1, r1 + 1)
    for r in COLLAR_BOLTS + (P["motor_r"],):
        tb = tb - ycyl(r, z_arm, 2.65, -40, 40)
    return tb


def clamp_bolts(P=PARAMS):
    rc = P["motor_r"]
    mr, mt, _ = P["mount"]
    return [(rc + dr, s * (mt / 2 - 4.5)) for dr in (-mr / 2 + 8, mr / 2 - 8) for s in (-1, 1)]


def motor_holes(P=PARAMS):
    rc = P["motor_r"]
    return [(rc + 17.5 * math.cos(math.radians(45 + 90 * k)), 17.5 * math.sin(math.radians(45 + 90 * k))) for k in range(4)]


def mount_local(P=PARAMS):
    """Motor mount: a split clamp round the arm tip, two halves joined by four M4 bolts; each half
    carries one motor on its outer face."""
    z_arm = derived(P)["z_arm"]
    mr, mt, mh = P["mount"]
    rc = P["motor_r"]
    halves = []
    for s in (1, -1):
        z0, z1 = (z_arm + 0.0, z_arm + mh / 2) if s > 0 else (z_arm - mh / 2, z_arm - 0.0)
        h = bx(rc - mr / 2, rc + mr / 2, -mt / 2, mt / 2, z0, z1)
        h = h - xcyl(0, z_arm, P["tube"][0] / 2 + 0.1, rc - mr / 2 - 1, rc + mr / 2 + 1)
        for x, y in clamp_bolts(P):
            h = h - zcyl(x, y, 2.15, z_arm - mh, z_arm + mh)
        for x, y in motor_holes(P):
            zf = z_arm + s * mh / 2
            h = h - zcyl(x, y, 1.65, min(zf, zf - s * 9), max(zf, zf - s * 9))
        h = h - ycyl(rc, z_arm, 2.65, -mt, mt)
        if P.get("pockets"):
            wb = P["web"]
            dr = 17.0 - 2.15 - wb                                                     # clear of the clamp bolts
            zi0, zi1 = (z_arm + wb, z_arm + mh / 2 - wb) if s > 0 else (z_arm - mh / 2 + wb, z_arm - wb)
            for sy in (-1, 1):
                h = h - bx(rc - dr, rc + dr, sy * (P["tube"][0] / 2 + 0.1 + wb), sy * (mt / 2 + 1), zi0, zi1)
        halves.append(h)
    return Compound(halves)


def blade(P, z, direction, flip=False):
    """One propeller blade in the rotor plane at height z, pointing at `direction` degrees about the
    motor axis (0 = radially outward)."""
    rc = P["motor_r"]
    c0, c1, th = P["blade"]
    R = P["prop_d"] / 2
    r0 = P["hub_d"][0] / 2 - 2
    pts = [(r0, -c0 / 2), (R, -c1 / 2), (R, c1 / 2), (r0, c0 / 2)]
    b = prism_xy(pts, -th / 2, th / 2)
    return Pos(rc, 0, z) * Rot(0, 0, direction) * b


def rotor_local(P=PARAMS, upper=True, folded_blades=False):
    """Motor, propeller hub and two blades for the upper or lower rotor of an arm (local frame)."""
    D = derived(P)
    z_arm = D["z_arm"]
    mh = P["mount"][2] / 2
    md, mhgt = P["motor"]
    hd, hh = P["hub_d"]
    rc = P["motor_r"]
    s = 1 if upper else -1
    zm0 = z_arm + s * mh
    motor = zcyl(rc, 0, md / 2, min(zm0, zm0 + s * mhgt), max(zm0, zm0 + s * mhgt))
    zh0 = zm0 + s * mhgt
    hub = zcyl(rc, 0, hd / 2, min(zh0, zh0 + s * hh), max(zh0, zh0 + s * hh))
    zp = zh0 + s * hh / 2
    if folded_blades:   # both blades swung back along the arm, side by side, for transport
        blades = [Pos(0, dy, 0) * blade(P, zp, 180.0) for dy in (-14.0, 14.0)]
        blades = [b - zcyl(rc, 0, hd / 2 + 0.5, zp - 10, zp + 10) for b in blades]
    else:
        blades = [blade(P, zp, a) for a in (90.0, 270.0)]
    return motor, hub + fuse(blades)


def esc_local(P=PARAMS):
    z_arm = derived(P)["z_arm"]
    L, W, H = P["esc"]
    r0 = P["esc_r0"]
    ro = P["tube"][0] / 2
    return [bx(r0, r0 + L, s * ro, s * (ro + W), z_arm - H / 2, z_arm + H / 2) for s in (-1, 1)]


def pivot_pin_local(P=PARAMS):
    w = P["blk_w"] / 2
    pr, ph = P["pivot"]
    z = P["z_bot"] + ph
    shank = ycyl(pr, z, P["pin_d"] / 2, -w - 2, w + 2)
    head = ycyl(pr, z, 7.0, w + 2, w + 7)
    nut = ycyl(pr, z, 7.0, -w - 8, -w - 2)
    return shank + head + nut


def lock_pin_local(P=PARAMS):
    w = P["blk_w"] / 2
    lr, lh = P["lock"]
    z = P["z_bot"] + lh
    shank = ycyl(lr, z, P["pin_d"] / 2, -w - 4, w + 1)
    head = ycyl(lr, z, 9.0, w + 1, w + 9)
    return shank + head


def arm_group_local(P=PARAMS, folded_blades=False):
    """Every part that swings with the arm (local frame), by key."""
    um, ur = rotor_local(P, True, folded_blades)
    lm, lr = rotor_local(P, False, folded_blades)
    return {"arm_roots": tongue_local(P), "arm_tubes": tube_local(P), "motor_mounts": mount_local(P),
            "motors": um + lm, "props": ur + lr, "escs": fuse(esc_local(P))}


def hub_spacers(P=PARAMS):
    zb, t = P["z_bot"], P["plate_t"]
    d, h = P["standoff"]
    out = [zcyl(x, y, d / 2, zb + t, zb + t + P["gap"]) for x, y in hub_posts(P)]
    zt = zb + 2 * t + P["gap"]
    out += [zcyl(x, y, d / 2, zt, zt + h) for x, y in hub_posts(P)]
    return [s - zcyl(*xy, 1.6, 0, 2000) for s, xy in zip(out, hub_posts(P) * 2)]


# ---------------------------------------------------------------- deck, packs, mast
def pack_centres(P=PARAMS):
    px = P["pack"][0] / 2 + P["pack_gap"] / 2
    return [(-px, 0.0), (px, 0.0)]


def strap_x(P=PARAMS):
    return [cx + s * 30.0 for cx, _ in pack_centres(P) for s in (-1, 1)]


def deck(P=PARAMS):
    D = derived(P)
    L, W, t = P["deck"]
    c = P["deck_chamfer"]
    hx, hy = L / 2, W / 2
    pts = [(hx - c, -hy), (hx, -hy + c), (hx, hy - c), (hx - c, hy), (-hx + c, hy), (-hx, hy - c), (-hx, -hy + c), (-hx + c, -hy)]
    z0 = D["z_deck"]
    d = prism_xy(pts, z0, z0 + t)
    for x, y in hub_posts(P):
        d = d - zcyl(x, y, 1.65, z0 - 1, z0 + t + 1)
    py = P["pack"][1] / 2
    for x in strap_x(P):
        for s in (-1, 1):
            d = d - bx(x - 15, x + 15, s * (py + 0.5), s * (py + 4.5), z0 - 1, z0 + t + 1)
    gy = py + 5.0 + P["guide"][0] / 2
    for x in GUIDE_X:
        for s in (-1, 1):
            d = d - zcyl(x, s * gy, 2.15, z0 - 1, z0 + t + 1)
    d = d - zcyl(0, 0, 8.5, z0 - 1, z0 + t + 1)   # mast foot and pack leads
    return d


def guides(P=PARAMS):
    D = derived(P)
    a, t = P["guide"]
    z0 = D["z_deck_top"]
    py = P["pack"][1] / 2 + 5.0
    L = P["deck"][0] - 2 * P["deck_chamfer"] - 10
    out = []
    for s in (-1, 1):
        y0 = s * py
        g = bx(-L / 2, L / 2, y0, y0 + s * a, z0, z0 + t) + bx(-L / 2, L / 2, y0 + s * (a - t), y0 + s * a, z0, z0 + a)
        for x in GUIDE_X:
            g = g - zcyl(x, s * (py + a / 2), 2.15, z0 - 1, z0 + t + 1)
        out.append(g)
    return out


def packs(P=PARAMS):
    D = derived(P)
    X, Y, Z = P["pack"]
    z0 = D["z_deck_top"]
    return [bx(cx - X / 2, cx + X / 2, -Y / 2, Y / 2, z0, z0 + Z) for cx, _ in pack_centres(P)]


def straps(P=PARAMS):
    D = derived(P)
    w = P["strap_w"]
    X, Y, Z = P["pack"]
    z0, zt = D["z_deck_top"], D["z_deck_top"] + Z
    zd = D["z_deck"]
    out = []
    for x in strap_x(P):
        top = bx(x - w / 2, x + w / 2, -Y / 2 - 1.5, Y / 2 + 1.5, zt, zt + 1.5)
        sides = [bx(x - w / 2, x + w / 2, s * Y / 2, s * (Y / 2 + 1.5), zd - 1.5, zt) for s in (-1, 1)]
        under = bx(x - w / 2, x + w / 2, -Y / 2 - 1.5, Y / 2 + 1.5, zd - 1.5, zd)
        out.append(fuse([top] + sides + [under]))
    return out


def mast(P=PARAMS):
    D = derived(P)
    d, h = P["mast"]
    pd, ph = P["puck"]
    z0 = D["z_deck_top"]
    foot = zcyl(0, 0, 12.0, z0, z0 + 12)
    tube = zcyl(0, 0, d / 2, z0 + 12, z0 + h)
    return foot + tube, zcyl(0, 0, pd / 2, z0 + h, z0 + h + ph)


# ---------------------------------------------------------------- Core stack and payload mount (interface assumptions)
def core_stack(P=PARAMS):
    zb, t = P["z_bot"], P["plate_t"]
    L, W, H = P["core"]
    dd, dh = P["damper"]
    z0 = zb + t + dh
    box_ = bx(-L / 2, L / 2, -W / 2, W / 2, z0, z0 + H)
    dampers = fuse([zcyl(x, y, dd / 2, zb + t, z0) for x, y in damper_xy(P)])
    return box_, dampers


def rails(P=PARAMS):
    zb = P["z_bot"]
    L, W, H = P["rail"]
    yi = P["rail_in"]
    sd, sh = P["slot"]
    zs0 = zb - H + 2
    out = []
    for s in (-1, 1):
        r = bx(-L / 2, L / 2, s * yi, s * (yi + W), zb - H, zb)
        r = r - bx(-L / 2 - 1, L / 2 + 1, s * (yi - 1), s * (yi + sd), zs0, zs0 + sh)
        for x, y in rail_bolt_xy(P):
            if y * s > 0:
                r = r - zcyl(x, y, 1.65, zb - 12, zb + 1)
        r = r - ycyl(P["lockpin_x"], zb - 8, 3.1, s * (yi - 1), s * (yi + W + 1))
        out.append(r)
    return out


def ds014_socket(P=PARAMS):
    zb = P["z_bot"]
    x1 = P["plug_x"]
    s = bx(x1 - 20, x1, -30, 30, zb - 16, zb)
    for y in (-20.0, 0.0, 20.0):
        s = s - zcyl(-142.0, y, 1.65, zb - 10, zb + 1)
    return s


def payload_lock_pin(P=PARAMS):
    zb = P["z_bot"]
    x = P["lockpin_x"]
    yo = P["rail_in"] + P["rail"][1]
    shank = ycyl(x, zb - 8, 3.0, -yo - 2, yo + 6)
    head = ycyl(x, zb - 8, 7.0, -yo - 10, -yo - 2)
    return shank + head


# ---------------------------------------------------------------- landing gear
def strut_ends(P=PARAMS, sx=1, sy=1):
    gx = P["gear_x"]
    yt, ht = P["strut_top"]
    yb, zb_ = P["strut_bot"]
    return (sx * gx, sy * yt, P["z_bot"] + ht), (sx * gx, sy * yb, zb_)


def struts(P=PARAMS):
    out = []
    o, i = P["strut_d"]
    for sx in (-1, 1):
        for sy in (-1, 1):
            a, b = strut_ends(P, sx, sy)
            out.append(rod(a, b, o / 2) - rod(a, b, i / 2))
    return out


def strut_solid(P, sx, sy, extra=0.0, grow=0.0):
    a, b = strut_ends(P, sx, sy)
    d = Vector(*b) - Vector(*a)
    u = d * (1.0 / d.length)
    a2 = Vector(*a) - u * extra
    b2 = Vector(*b) + u * extra
    return rod(tuple(a2), tuple(b2), P["strut_d"][0] / 2 + grow)


def gear_tops(P=PARAMS):
    zb = P["z_bot"]
    w, d, h = P["gtop"]
    out = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            x, y = sx * P["gear_x"], sy * P["strut_top"][0]
            b = bx(x - w / 2, x + w / 2, y - d / 2, y + d / 2, zb - h, zb)
            b = b - strut_solid(P, sx, sy, extra=40.0, grow=0.1)
            for bxy in gear_bolt_xy(P):
                if bxy[0] * sx > 0 and bxy[1] * sy > 0:
                    b = b - zcyl(bxy[0], bxy[1], 1.65, zb - 10, zb + 1)
            out.append(b)
    return out


def skids(P=PARAMS):
    o, i = P["strut_d"]
    h = P["skid_half"]
    return [xcyl(s * P["skid_y"], P["skid_z"], o / 2, -h, h) - xcyl(s * P["skid_y"], P["skid_z"], i / 2, -h - 1, h + 1)
            for s in (-1, 1)]


def skid_blocks(P=PARAMS):
    w, d, h = P["gskid"]
    out = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            x, y = sx * P["gear_x"], sy * P["skid_y"]
            b = bx(x - w / 2, x + w / 2, y - d / 2, y + d / 2, 0, h)
            b = b - xcyl(y, P["skid_z"], P["strut_d"][0] / 2 + 0.1, x - w, x + w)
            b = b - strut_solid(P, sx, sy, extra=40.0, grow=0.1)
            b = b - zcyl(x + 8, y, 2.15, -1, P["skid_z"] + 12)   # cross bolt through block and skid (vertical, beside the strut)
            out.append(b)
    return out


def end_caps(P=PARAMS):
    h = P["skid_half"]
    return [xcyl(s * P["skid_y"], P["skid_z"], 12.0, sx * h, sx * (h + 12)) for s in (-1, 1) for sx in (-1, 1)]


# ---------------------------------------------------------------- payloads
def payload_plate(P=PARAMS):
    zb = P["z_bot"]
    L, W, t = P["pplate"]
    x0 = P["pplate_x0"]
    zs0 = zb - P["rail"][2] + 2
    z0 = zs0 + 1
    pl = bx(x0, x0 + L, -W / 2, W / 2, z0, z0 + t)
    for x in (-55.0, 45.0):
        pl = pl - zcyl(x, 0, 25.0, z0 - 1, z0 + t + 1)                                  # lightening holes
    lx = P["lockpin_x"]
    lug = bx(lx - 10, lx + 10, -10, 10, z0 + t, zb - 3) - ycyl(lx, zb - 8, 3.15, -11, 11)
    plug = bx(x0, x0 + 18, -25, 25, z0 + t, zb - 3)
    return pl + lug + plug, z0


def float_release(P=PARAMS):
    zb = P["z_bot"]
    plate, z0 = payload_plate(P)
    fd, fl = P["float"]
    zf = z0 - 40.0 - fd / 2 + 12.0         # float axis
    float_ = xcyl(0, zf, fd / 2, -fl / 2, fl / 2)
    bag = xcyl(0, zf, P["bag"][0] / 2, fl / 2, fl / 2 + P["bag"][1])
    sx = P["saddle_x"]
    saddles = fuse([bx(s * sx - 10, s * sx + 10, -50, 50, z0 - 40, z0) - xcyl(0, zf, fd / 2 + 0.5, -fl, fl)
                    for s in (-1, 1)])
    unit = bx(-30, 30, -20, 20, z0 - 22, z0)
    ring = xcyl(0, zf, fd / 2 + 3.5, -12, 12) - xcyl(0, zf, fd / 2 + 0.5, -13, 13)
    tab = bx(-12, 12, -1.5, 1.5, zf + fd / 2 + 2, z0 - 22)
    return {"fr_plate": plate, "saddles": saddles, "release": unit, "sling": ring + tab, "float": float_ + bag}


def tether_module(P=PARAMS):
    plate, z0 = payload_plate(P)
    L, W, H = P["conv"]
    conv = bx(-L / 2 + 5, L / 2 + 5, -W / 2, W / 2, z0 - H, z0)
    brk = zcyl(-70.0, 0, 20.0, z0 - H - 50, z0 - H)
    cable = zcyl(-70.0, 0, 4.0, z0 - H - 450, z0 - H - 50)
    return {"tm_plate": plate, "converter": conv, "breakaway": brk, "tether": cable}


# ---------------------------------------------------------------- components
@dataclass
class Comp:
    name: str
    shape: object
    bom: int | None
    key: str


BOM = {  # key: (BOM line, plain name)
    "top_plate": (1, "Top hub plate"),
    "bot_plate": (2, "Bottom hub plate"),
    "spacers": (3, "Hub spacers and deck standoffs"),
    "hinge_blocks": (4, "Arm hinge blocks (4)"),
    "arm_roots": (5, "Arm root fittings (4)"),
    "arm_tubes": (6, "Arm tubes (4)"),
    "motor_mounts": (7, "Motor mounts (4)"),
    "pivots": (8, "Hinge pivot bolts (4)"),
    "lock_pins": (9, "Arm lock pins (4)"),
    "motors": (10, "Motors (8)"),
    "escs": (11, "Motor controllers (8)"),
    "props": (12, "Folding propellers (8)"),
    "gear_tops": (13, "Gear top blocks (4)"),
    "skid_blocks": (14, "Skid blocks (4)"),
    "struts": (15, "Gear struts (4)"),
    "skids": (16, "Skids (2) with end caps"),
    "deck": (17, "Battery deck"),
    "guides": (18, "Pack guides (2)"),
    "straps": (19, "Pack straps (4)"),
    "mast": (20, "GNSS mast"),
    "core": (21, "Kitewright Core stack (Core)"),
    "rails": (22, "Payload rails (Core)"),
    "ds014": (22, "DS-014 socket (Core)"),
    "paylock": (22, "Payload lock pin (Core)"),
    "packs": (23, "ColdCell packs (2)"),
    "fr_plate": (26, "Payload plate, float release"),
    "saddles": (27, "Float saddles (2)"),
    "release": (28, "Release unit"),
    "sling": (29, "Float sling"),
    "float": (30, "Rescue float and line bag"),
    "tm_plate": (31, "Payload plate, tether module"),
    "converter": (32, "Tether DC-DC converter"),
    "breakaway": (33, "Tether breakaway connector"),
    "tether": (34, "Tether (shown short)"),
}
MATERIAL = {  # density in g/cm3 for made parts; bought parts take their mass from bom/bom.csv
    "top_plate": 1.6, "bot_plate": 1.6, "deck": 1.6, "arm_tubes": 1.55, "struts": 1.55, "skids": 1.55,
    "hinge_blocks": 2.7, "arm_roots": 2.7, "motor_mounts": 2.7, "gear_tops": 2.7, "skid_blocks": 2.7,
    "guides": 2.7, "spacers": 2.7, "fr_plate": 2.7, "tm_plate": 2.7, "saddles": 1.27, "pivots": 7.9,
}


def build_components(P=PARAMS, payload="float", folded=False):
    """All parts in place, by key. payload: 'float', 'tether' or None. folded: arms swung down for
    transport with the propeller blades turned back along the arms (payload removed)."""
    C = {}
    loc = arm_group_local(P, folded_blades=folded)
    blk = hinge_block_local(P)
    piv, lck = pivot_pin_local(P), lock_pin_local(P)
    for key in ("arm_roots", "arm_tubes", "motor_mounts", "motors", "props", "escs"):
        s = loc[key]
        if folded:
            s = fold_about(s, P)
        C[key] = Compound([turn(s, a) for a in ARM_ANGLES])
    C["hinge_blocks"] = Compound([turn(blk, a) for a in ARM_ANGLES])
    C["pivots"] = Compound([turn(piv, a) for a in ARM_ANGLES])
    C["lock_pins"] = None if folded else Compound([turn(lck, a) for a in ARM_ANGLES])   # pulled out to fold
    C["top_plate"] = hub_plate(P, top=True)
    C["bot_plate"] = hub_plate(P, top=False)
    C["spacers"] = Compound(hub_spacers(P))
    C["deck"] = deck(P)
    C["guides"] = Compound(guides(P))
    C["packs"] = Compound(packs(P))
    C["straps"] = Compound(straps(P))
    mt, puck = mast(P)
    C["mast"] = mt + puck
    cb, dm = core_stack(P)
    C["core"] = cb + dm
    C["rails"] = Compound(rails(P))
    C["ds014"] = ds014_socket(P)
    C["paylock"] = payload_lock_pin(P) if payload else None
    C["gear_tops"] = Compound(gear_tops(P))
    C["struts"] = Compound(struts(P))
    C["skids"] = Compound(skids(P) + end_caps(P))
    C["skid_blocks"] = Compound(skid_blocks(P))
    if payload == "float":
        C.update(float_release(P))
    elif payload == "tether":
        C.update(tether_module(P))
    return {k: Comp(BOM[k][1], v, BOM[k][0], k) for k, v in C.items() if v is not None}


def assembly(P=PARAMS, payload="float", folded=False, keys=None):
    C = build_components(P, payload, folded)
    return Compound([c.shape for k, c in C.items() if keys is None or k in keys])


# ---------------------------------------------------------------- checks
HOLDS = [  # (part, what holds it): must touch or sit within 1 mm
    ("hinge_blocks", "bot_plate"), ("hinge_blocks", "top_plate"), ("spacers", "bot_plate"), ("spacers", "top_plate"),
    ("arm_roots", "pivots"), ("arm_tubes", "arm_roots"), ("motor_mounts", "arm_tubes"), ("motors", "motor_mounts"),
    ("props", "motors"), ("escs", "arm_tubes"), ("pivots", "hinge_blocks"), ("lock_pins", "hinge_blocks"),
    ("deck", "spacers"), ("guides", "deck"), ("packs", "deck"), ("straps", "packs"), ("mast", "deck"),
    ("core", "bot_plate"), ("rails", "bot_plate"), ("ds014", "bot_plate"), ("paylock", "rails"),
    ("gear_tops", "bot_plate"), ("struts", "gear_tops"), ("struts", "skid_blocks"), ("skids", "skid_blocks"),
    ("fr_plate", "rails"), ("saddles", "fr_plate"), ("release", "fr_plate"), ("float", "saddles"), ("sling", "release"),
    ("tm_plate", "rails"), ("converter", "tm_plate"), ("breakaway", "converter"),
]
ALLOWED = [  # pins and bolts pass through the holes made for them; checked by hole size instead
    {"pivots", "arm_roots"}, {"pivots", "hinge_blocks"}, {"lock_pins", "arm_roots"}, {"lock_pins", "hinge_blocks"},
    {"paylock", "rails"}, {"paylock", "fr_plate"}, {"paylock", "tm_plate"}, {"straps", "deck"},
    {"tether", "breakaway"},
]


def _dist(a, b):
    try:
        return a.distance_to(b)
    except Exception:
        return float("nan")


def _bb_apart(ba, bb_, tol=0.0):
    return (ba.min.X > bb_.max.X + tol or bb_.min.X > ba.max.X + tol or ba.min.Y > bb_.max.Y + tol
            or bb_.min.Y > ba.max.Y + tol or ba.min.Z > bb_.max.Z + tol or bb_.min.Z > ba.max.Z + tol)


def _pieces(shape):
    sols = list(shape.solids())
    return [(s, s.bounding_box()) for s in sols] if sols else [(shape, shape.bounding_box())]


def _overlap(a, b):
    """Volume shared by two shapes, solid by solid with a bounding-box pre-check (fast on compounds)."""
    v = 0.0
    pb = _pieces(b)
    for sa, ba in _pieces(a):
        for sb, bb_ in pb:
            if _bb_apart(ba, bb_):
                continue
            try:
                inter = sa & sb
                v += 0.0 if inter is None else inter.volume
            except Exception:
                return float("nan")
    return v


def checks(P=PARAMS, verbose=True):
    """Constructability checks on the flying (float payload and tether payload) and folded states:
    no two parts overlap, except a pin passing through the holes made for it; every part touches or
    sits within 1 mm of what holds it."""
    res = {}
    for label, kw in (("flying, float release", dict(payload="float")), ("flying, tether module", dict(payload="tether")),
                      ("folded for transport", dict(payload=None, folded=True))):
        C = build_components(P, **kw)
        keys = list(C)
        over, flo = [], []
        for a, b in HOLDS:
            if a in C and b in C:
                d = _dist(C[a].shape, C[b].shape)
                if not d <= 1.0:
                    flo.append((a, b, round(d, 2)))
        for i, a in enumerate(keys):
            for b in keys[i + 1:]:
                if {a, b} in ALLOWED:
                    continue
                v = _overlap(C[a].shape, C[b].shape)
                if not v < 1.0:
                    over.append((a, b, round(v, 1)))
        res[label] = (over, flo)
        if verbose:
            print(f"[{label}] overlaps (should be none): {over or 'none'}")
            print(f"[{label}] parts not touching what holds them (should be none): {flo or 'none'}")
    return res


def clearances(P=PARAMS):
    """Distances that matter in flight and in the folded state (mm)."""
    D = derived(P)
    C = build_components(P, "float")
    F = build_components(P, None, folded=True)
    out = {}
    rc = P["motor_r"] / math.sqrt(2)
    disc_lo = Pos(rc, rc, D["z_lower_prop"]) * Cylinder(P["prop_d"] / 2, 8)
    disc_up = Pos(rc, rc, D["z_upper_prop"]) * Cylinder(P["prop_d"] / 2, 8)
    out["lower disc to gear"] = _dist(disc_lo, C["struts"].shape)
    out["lower disc to float"] = _dist(disc_lo, C["float"].shape)
    out["upper disc to packs"] = _dist(disc_up, C["packs"].shape)
    out["upper disc to deck"] = _dist(disc_up, C["deck"].shape)
    out["prop tip to tip"] = D["tip_gap"]
    out["folded: motors to skids"] = _dist(F["motors"].shape, F["skids"].shape)
    out["folded: props to gear"] = min(_dist(F["props"].shape, F["struts"].shape), _dist(F["props"].shape, F["gear_tops"].shape))
    out["folded: tubes to struts"] = _dist(F["arm_tubes"].shape, F["struts"].shape)
    out["folded: lowest point above ground"] = min(F[k].shape.bounding_box().min.Z for k in ("motors", "props", "motor_mounts"))
    bb = Compound([c.shape for c in F.values()]).bounding_box()
    out["folded envelope X"], out["folded envelope Y"], out["folded envelope Z"] = bb.size.X, bb.size.Y, bb.size.Z
    bb2 = Compound([c.shape for k, c in F.items() if k not in ("skids", "skid_blocks", "struts", "gear_tops")]).bounding_box()
    out["folded envelope without gear X"], out["folded envelope without gear Y"] = bb2.size.X, bb2.size.Y
    return out


def masses(P=PARAMS):
    """Mass in kg of each made part from the model (bought parts from bom/bom.csv)."""
    C = build_components(P, "float")
    T = build_components(P, "tether")
    out = {}
    for k, rho in MATERIAL.items():
        src = C if k in C else T
        if k in src:
            out[k] = sum(x.volume for x in src[k].shape.solids()) / 1000.0 * rho / 1000.0
    return out


def export(P=PARAMS):
    step, stl = ROOT / "cad" / "step", ROOT / "cad" / "stl"
    step.mkdir(parents=True, exist_ok=True)
    stl.mkdir(parents=True, exist_ok=True)
    C = build_components(P, "float")
    export_step(assembly(P, "float"), str(step / "kitewright-lift-assembly.step"))
    export_step(assembly(P, None, folded=True), str(step / "kitewright-lift-folded.step"))
    export_step(Compound([c.shape for c in build_components(P, "tether").values()
                          if c.key in ("tm_plate", "converter", "breakaway")]), str(step / "kitewright-lift-tether-module.step"))
    loc = arm_group_local(P)
    singles = {
        "hub-plate-top": C["top_plate"].shape, "hub-plate-bottom": C["bot_plate"].shape,
        "hinge-block": hinge_block_local(P), "arm-root-fitting": loc["arm_roots"], "arm-tube": loc["arm_tubes"],
        "motor-mount": loc["motor_mounts"], "battery-deck": C["deck"].shape, "gear-top-block": gear_tops(P)[3],
        "skid-block": skid_blocks(P)[3], "float-saddle": C["saddles"].shape, "payload-plate": C["fr_plate"].shape,
    }
    for name, s in singles.items():
        export_step(s, str(step / f"kitewright-lift-{name}.step"))
        export_stl(s, str(stl / f"kitewright-lift-{name}.stl"), tolerance=0.2, angular_tolerance=0.3)
    print("exported STEP and STL to cad/step and cad/stl")


if __name__ == "__main__":
    D = derived()
    print({k: (round(v, 1) if isinstance(v, float) else v) for k, v in D.items()})
    checks()
    for k, v in clearances().items():
        print(f"{k:40s} {v:8.1f}")
    for k, v in sorted(masses().items()):
        print(f"{k:14s} {v:6.3f} kg")
    if "--check" not in sys.argv:
        export()
