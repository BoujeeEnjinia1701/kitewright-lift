"""Kitewright Core mounting envelope for the frames (Kitewright interface table, 2026-10-04).

This file is the same in Kitewright Lift, Kitewright Range and AvalancheScout. It draws the Core as the
frames see it, from the reference figures of the Core's own drawings (KWC-DWG-001 Rev P2 general
arrangement and KWC-DWG-106 payload shoe), so both frames hold one mounting envelope (Amish's
decision 10A, 2026-10-04: "For round 3, I agree with all your proposed recommendations").

Core coordinates, mm: X forward along the payload rail (the payload slides in from the rear, -X),
Y to the left, Z up, Z = 0 on the top face of the Core plate. The frame's lower deck (Lift's bottom
hub plate, Range's fuselage floor) sits on the four 8 mm corner spacers, so the deck's underside is
at Z = +8. Place the envelope in a frame with place(shape, x, y, z_plate_top).

What the frame must give the Core (the interface table):
    four M4 hard points on a 220 x 130 mm pattern; a 200 x 112 mm opening in the deck for the lid;
    lid 168 x 92 mm, its top 55 mm above the deck's underside, the GNSS mast boss to 69 mm;
    antennas and GNSS receiver at frame positions on extension cables where the frame has no 240 mm
    clear above the lid (both frames); rail, pin blocks and knobs to 47 mm below the plate top;
    payload shoe 184 x 128 x 5 mm; payload neck 88 mm wide from the shoe down to 30 mm below the lips.
CONCEPT, NOT FOR FABRICATION. The Core repository owns these parts; nothing here changes them.
"""
from __future__ import annotations

from build123d import Box, Compound, Cylinder, Pos

CORE = {
    "plate": (240.0, 150.0, 2.0),             # carbon fibre plate: X, Y, thickness
    "frame_holes": (110.0, 65.0, 4.5),        # the 220 x 130 mm M4 pattern
    "spacer": (12.0, 4.5, 8.0),               # corner spacer OD, bore, height
    "deck_opening": (200.0, 112.0),
    "slot": (70.0, 82.0, 24.0),               # pigtail slot in the plate: x from, x to, width
    "lid": (168.0, 92.0, 62.0, 1.5),          # outer X, Y, height, wall (on a 1 mm gasket)
    "flange": (180.0, 108.0, 3.0),
    "boss": (-55.0, 0.0, 22.0, 14.0),         # GNSS mast boss on the lid top: x, y, diameter, height
    "sma": (((65.0, 32.0), (65.0, -32.0), (40.0, 0.0)), 9.0, 8.0),   # SMA bulkheads: positions, diameter, height
    "switch": (-15.0, 30.0, 16.0, 8.0),       # safety switch cap: x, y, diameter, height above the lid
    "relief": (-95.0, 25.0, 5.5, 12.0, (8.0, 60.0, 2.0)),            # strain-relief standoffs and bar
    "rail_x": (-100.0, 100.0),
    "spacer_bar": (65.0, 75.0, -8.0, -2.0),   # |Y| from, to; Z from, to
    "lip": (45.0, 75.0, -11.0, -8.0),
    "front_stop": (88.0, 100.0, 45.0, 65.0),  # X from, to; |Y| from, to (between plate and lip)
    "pin_block": (-98.0, -70.0, 45.0, 75.0, -23.0, -11.0),
    "pin_xy": (-84.0, 55.0), "pin_d": 5.0, "pin_hole": 5.5, "knob": (18.0, -47.0, -33.0),
    "plug": (69.0, 83.0, 20.0, -30.0, -14.0),  # DS-014 pigtail plug: X from, to; |Y|; Z from, to
    "pigtail": (76.0, 7.0),                   # cable: x, diameter (through the plate slot and the shoe notch)
    "shoe": (-96.0, 88.0, 128.0, -7.3, -2.3),  # payload shoe: X from, to; width; Z from, to (on 0.7 mm wear tape)
    "notch": (18.0, 28.0),
    "shoe_holes": ((-70.0, 30.0), (-70.0, -30.0), (50.0, 30.0), (50.0, -30.0)),
    "neck": (88.0, -41.0),                    # payload neck: width, lowest Z of the neck zone (30 mm below the lips)
    "mass_kg": 0.99,                          # Core R9 (KWC-DDR-003): avionics, radios, GNSS, rail and pins
}


def bx(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(abs(x1 - x0), abs(y1 - y0), abs(z1 - z0))


def zc(x, y, d, z0, z1):
    return Pos(x, y, (z0 + z1) / 2) * Cylinder(d / 2, abs(z1 - z0))


def _fuse(shapes):
    out = shapes[0]
    for s in shapes[1:]:
        out = out + s
    return out


def frame_points(C=CORE):
    fx, fy, _ = C["frame_holes"]
    return [(sx * fx, sy * fy) for sx in (1, -1) for sy in (1, -1)]


def core_body(C=CORE, lid_top_items=True):
    """Plate, corner spacers, gasket and lid with its boss, SMA bulkheads and switch, strain-relief bar."""
    L, W, t = C["plate"]
    plate = bx(-L / 2, L / 2, -W / 2, W / 2, -t, 0)
    for x, y in frame_points(C):
        plate = plate - zc(x, y, C["frame_holes"][2], -t - 1, 1)
    sx0, sx1, sw = C["slot"]
    plate = plate - bx(sx0, sx1, -sw / 2, sw / 2, -t - 1, 1)
    od, bore, h = C["spacer"]
    spacers = [zc(x, y, od, 0, h) - zc(x, y, bore, -1, h + 1) for x, y in frame_points(C)]
    lL, lW, lH, wall = C["lid"]
    fL, fW, fT = C["flange"]
    lid = bx(-lL / 2, lL / 2, -lW / 2, lW / 2, 1, 1 + lH) - bx(-lL / 2 + wall, lL / 2 - wall, -lW / 2 + wall, lW / 2 - wall, 0, 1 + lH - wall)
    lid = lid + (bx(-fL / 2, fL / 2, -fW / 2, fW / 2, 0, 1 + fT) - bx(-lL / 2 + wall, lL / 2 - wall, -lW / 2 + wall, lW / 2 - wall, -1, 5))
    top = 1 + lH
    if lid_top_items:
        bxx, byy, bd, bh = C["boss"]
        lid = lid + zc(bxx, byy, bd, top, top + bh)
        (pts, sd, sh) = C["sma"]
        for x, y in pts:
            lid = lid + zc(x, y, sd, top, top + sh)
        swx, swy, swd, swh = C["switch"]
        lid = lid + zc(swx, swy, swd, top, top + swh)
    rx, ry, rsd, rsh, (rbl, rbw, rbt) = C["relief"]
    relief = _fuse([zc(rx, s * ry, rsd, 0, rsh) for s in (1, -1)]) + bx(rx - rbl / 2, rx + rbl / 2, -rbw / 2, rbw / 2, rsh, rsh + rbt)
    return _fuse([plate] + spacers + [lid, relief])


def core_rail(C=CORE):
    """Spacer bars, lips, front stops and pin blocks (the Core's plain rail, under the plate)."""
    x0, x1 = C["rail_x"]
    parts = []
    for s in (1, -1):
        a, b, z0, z1 = C["spacer_bar"]
        parts.append(bx(x0, x1, s * a, s * b, z0, z1))
        a, b, z0, z1 = C["lip"]
        lip = bx(x0, x1, s * a, s * b, z0, z1) - zc(C["pin_xy"][0], s * C["pin_xy"][1], C["pin_hole"], z0 - 1, z1 + 1)
        parts.append(lip)
        fx0, fx1, fa, fb = C["front_stop"]
        parts.append(bx(fx0, fx1, s * fa, s * fb, C["lip"][3], C["spacer_bar"][3]))
        px0, px1, pa, pb, pz0, pz1 = C["pin_block"]
        parts.append(bx(px0, px1, s * pa, s * pb, pz0, pz1) - zc(C["pin_xy"][0], s * C["pin_xy"][1], 10.0, pz0 - 1, pz1 + 1))
    return _fuse(parts)


def core_pins(C=CORE):
    """The two locking pins (indexing plungers) with jam nuts and knobs, engaged in the shoe."""
    px, py = C["pin_xy"]
    kd, kz0, kz1 = C["knob"]
    pz0, pz1 = C["pin_block"][4], C["pin_block"][5]
    out = []
    for s in (1, -1):
        y = s * py
        out.append(_fuse([zc(px, y, 10.0, pz0, pz1), zc(px, y, 17.0, pz0 - 6, pz0), zc(px, y, 6.0, kz1, pz0 - 6),
                          zc(px, y, kd, kz0, kz1), zc(px, y, C["pin_d"], pz1, C["shoe"][4] - 0.5)]))
    return _fuse(out)


def core_plug(C=CORE):
    """The Core's DS-014 pigtail below the plate: cable through the slot and shoe notch, plug in front."""
    x0, x1, hy, z0, z1 = C["plug"]
    xc, cd = C["pigtail"]
    run = bx(xc - 30, xc + cd / 2, -cd / 2, cd / 2, 2, 6) + bx(xc - 34, xc - 22, -8, 8, 0, 10)   # along the plate, clipped at its end
    return bx(x0, x1, -hy, hy, z0, z1) + zc(xc, 0, cd, z1, 6) + run


def shoe(C=CORE):
    """A payload shoe to KWC-DWG-106: every payload carries its own."""
    x0, x1, w, z0, z1 = C["shoe"]
    s = bx(x0, x1, -w / 2, w / 2, z0, z1)
    nd, nw = C["notch"]
    s = s - bx(x1 - nd, x1 + 1, -nw / 2, nw / 2, z0 - 1, z1 + 1)
    px, py = C["pin_xy"]
    for sy in (1, -1):
        s = s - zc(px, sy * py, C["pin_hole"], z0 - 1, z1 + 1)
    for x, y in C["shoe_holes"]:
        s = s - zc(x, y, 4.5, z0 - 1, z1 + 1)
    return s


def neck_zone(C=CORE):
    """The space a payload may not fill wider than the neck: from the shoe down to 30 mm below the lips,
    outside |Y| = neck / 2, over the rail's length (used by the frames' checks on payloads)."""
    w, zlow = C["neck"]
    x0, x1 = C["rail_x"]
    return [bx(x0, x1, s * w / 2, s * 100.0, zlow, C["shoe"][3] - 0.01) for s in (1, -1)]


def place(shape, x=0.0, y=0.0, z=0.0):
    return Pos(x, y, z) * shape
