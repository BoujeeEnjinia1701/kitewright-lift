"""Kitewright Lift prototype build plan pictures (KWL-BLD-001, STANDARDS section 18).

Run from the repo root:  python cad/src/build_plan_media.py [overview|sheets|joints|steps ...]
With no argument it draws everything (one picture group per process is kinder to a small machine).
Every picture is drawn from cad/src/model.py, so the pictures and the model never disagree:
    docs/05-build-plan/overview.png       every component pulled apart, numbered in build order
    cad/drawings/KWL-DWG-101 to 114       making sketches for the made components
    docs/05-build-plan/joint-NN.png       close-ups of the joints that need explaining
    docs/05-build-plan/step-NN.png        one picture per assembly step
Uses .kit/build_views.py. Single-arm pictures are drawn in the arm's own frame (arm along +X).
BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
"""
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
from build123d import Compound, Pos  # noqa: E402
import model as M  # noqa: E402
from model import PARAMS as P, bx, turn, fold_about, derived  # noqa: E402

OUT = ROOT / "docs" / "05-build-plan"
DWG = ROOT / "cad" / "drawings"
DATE = "2026-10-03"
D = derived(P)
ARM = 315.0                                    # the front-right arm, nearest the usual camera
U = (math.cos(math.radians(ARM)), math.sin(math.radians(ARM)))

COL = {"top_plate": "#374151", "bot_plate": "#374151", "spacers": "#9CA3AF", "hinge_blocks": "#0F766E",
       "arm_roots": "#14B8A6", "arm_tubes": "#1F2937", "motor_mounts": "#0E7490", "pivots": "#6B7280",
       "lock_pins": "#DC2626", "motors": "#6B7280", "escs": "#475569", "props": "#334155",
       "gear_tops": "#0F766E", "skid_blocks": "#0F766E", "struts": "#1F2937", "skids": "#1F2937",
       "deck": "#4B5563", "guides": "#9CA3AF", "straps": "#F59E0B", "mast": "#94A3B8", "core": "#7C3AED",
       "rails": "#A855F7", "ds014": "#A855F7", "paylock": "#DC2626", "packs": "#2563EB",
       "fr_plate": "#94A3B8", "saddles": "#CBD5E1", "release": "#1D4ED8", "sling": "#FACC15", "float": "#F97316",
       "tm_plate": "#94A3B8", "converter": "#16A34A", "breakaway": "#FACC15", "tether": "#F59E0B"}

_C = {}


def C(key, payload="float"):
    k = (key, payload)
    if k not in _C:
        comps = M.build_components(P, payload)
        for kk, c in comps.items():
            _C[(kk, payload)] = c.shape
    return _C[k]


def part(key, shape=None, explode=(0, 0, 0), name=None, payload="float"):
    return Part(name or M.BOM[key][1], C(key, payload) if shape is None else shape, COL[key], None, tuple(explode))


def ghost(name, shape):
    return Part(name, shape, "#D1D5DB")


RIGHT = (0.797, 0.498)                         # screen-right for the default camera (20 deg, -58 deg)


def side(k, dz):
    """Offset that moves a part to the right of the hub stack in the overview, then up by dz."""
    return (RIGHT[0] * k, RIGHT[1] * k, dz)


def out(vec_r, dz=0.0):
    """Explode vector along the front-right arm (outward by vec_r) plus dz."""
    return (U[0] * vec_r, U[1] * vec_r, dz)


# single arm, placed (world frame) and local (arm along +X)
LOC = M.arm_group_local(P)
LOC_HB = M.hinge_block_local(P)
LOC_PIV = M.pivot_pin_local(P)
LOC_LCK = M.lock_pin_local(P)


def arm1(key):
    src = {"hinge_blocks": LOC_HB, "pivots": LOC_PIV, "lock_pins": LOC_LCK}
    return turn(src.get(key, LOC.get(key)), ARM)


def crop(shape, *b):
    return shape & bx(*b)


# ----------------------------------------------------------------- overview
def overview():
    zb = P["z_bot"]
    hub = [
        ("Bottom hub plate", C("bot_plate"), "bot_plate", (0, 0, 0)),
        ("Arm hinge blocks (4), one shown", arm1("hinge_blocks"), "hinge_blocks", side(250, 60)),
        ("Hub spacers and deck standoffs (8)", C("spacers"), "spacers", (0, 0, 250)),
        ("Kitewright Core stack (Core)", C("core"), "core", (0, 0, 120)),
        ("Top hub plate", C("top_plate"), "top_plate", (0, 0, 330)),
        ("Gear top blocks (4)", C("gear_tops"), "gear_tops", (0, 0, -220)),
        ("Gear struts (4)", C("struts"), "struts", (0, 0, -330)),
        ("Skid blocks (4)", C("skid_blocks"), "skid_blocks", (0, 0, -440)),
        ("Skids (2)", C("skids"), "skids", (0, 0, -500)),
        ("Core payload mount: rails, pin, DS-014 socket", C("rails") + C("ds014") + C("paylock"), "rails", (0, 0, -120)),
        ("Arm tubes (4), one shown", arm1("arm_tubes"), "arm_tubes", side(650, 330)),
        ("Arm root fittings (4), one shown", arm1("arm_roots"), "arm_roots", side(500, 330)),
        ("Motor mounts (4), one shown", arm1("motor_mounts"), "motor_mounts", side(800, 330)),
        ("Motors (8), two shown", arm1("motors"), "motors", side(950, 330)),
        ("Motor controllers (8), two shown", arm1("escs"), "escs", side(650, 520)),
        ("Pivot bolt and lock pin (4 each), one shown", arm1("pivots") + arm1("lock_pins"), "lock_pins", side(350, 200)),
        ("Folding propellers (8), two shown", arm1("props"), "props", side(1100, 600)),
        ("Battery deck", C("deck"), "deck", (0, 0, 440)),
        ("Pack guides (2)", C("guides"), "guides", (0, 0, 540)),
        ("GNSS mast", C("mast"), "mast", (0, 0, 800)),
        ("ColdCell packs (2) and straps (4)", C("packs") + C("straps"), "packs", (0, 0, 640)),
        ("Float release payload", C("fr_plate") + C("saddles") + C("release") + C("sling") + C("float"), "float", (-300, -800, -450)),
        ("Tether module payload", Pos(-900, 650, 0) * (C("tm_plate", "tether") + C("converter", "tether") + C("breakaway", "tether")),
         "converter", (0, 0, -300)),
    ]
    parts = [Part(n, s, COL[k], None, tuple(e)) for n, s, k, e in hub]
    bv.overview(parts, OUT / "overview.png", "Kitewright Lift prototype: every component in build order",
                subtitle="Hub stack, gear and payload mount first, then the arms (one of four shown), deck, packs and payloads",
                key=True, size=(12, 8.5), elev=20)


# ----------------------------------------------------------------- making sketches
def sheets():
    zb = P["z_bot"]
    hb_n = [ghost("plate", crop(C("bot_plate"), 0, 200, -200, 0, 0, 2000)), ghost("root", arm1("arm_roots"))]
    S = [
        ("KWL-DWG-101", "Top hub plate: making sketch", part("top_plate"),
         [ghost("blocks", C("hinge_blocks")), ghost("spacers", C("spacers"))], None,
         "3 mm carbon fibre sheet (woven, 0/90)",
         [f"Square {2 * P['hub_half']:.0f} x {2 * P['hub_half']:.0f}; cut each corner square to the arm: 72 long face",
          f"Corner faces lie {P['chamfer_r']:.0f} from the centre, measured along the diagonal",
          "Per corner four 4.3 holes for the hinge block: on the diagonal, 131 and 144 out, 15 either side",
          f"Four 3.3 holes for the spacers, {P['post_xy']:.0f} from the centre on the X and Y axes",
          "30 hole at the centre for the pack leads and mast cable",
          "Route with a diamond or carbide cutter; wear a dust mask; seal the edges with thin epoxy",
          "Check: lies flat on the bottom plate with every hole in line"]),
        ("KWL-DWG-102", "Bottom hub plate: making sketch", part("bot_plate"),
         [ghost("blocks", C("hinge_blocks")), ghost("core", C("core")), ghost("gear", C("gear_tops")), ghost("rails", C("rails"))], None,
         "3 mm carbon fibre sheet (woven, 0/90)",
         ["Same outline and hinge-block and spacer holes as the top plate",
          "Four 3.3 holes for the Core dampers at 130 x 80 centres",
          f"Eight 4.3 holes for the gear blocks at X {P['gear_x']:.0f} either side, Y 97 and 127 either side",
          "Six 4.3 holes for the payload rails at X -100, 0, 100 and Y 71 either side",
          "Three 4.3 holes for the DS-014 socket block 142 behind the centre",
          "24 hole 40 ahead of the centre for the payload cable",
          "Check: the Core damper and gear holes match their parts before bonding anything"]),
        ("KWL-DWG-103", "Battery deck: making sketch", part("deck"),
         [ghost("packs", C("packs")), ghost("guides", C("guides")), ghost("spacers", C("spacers"))], None,
         "3 mm carbon fibre sheet",
         [f"{P['deck'][0]:.0f} x {P['deck'][1]:.0f}; corners cut 35 x 35",
          f"Four 3.3 holes for the standoffs, {P['post_xy']:.0f} from the centre on the axes",
          "Eight strap slots 30 x 4, two beside each long side of each pack",
          "Slot centres at X -90, -30, 30, 90; inner edge 189.5 from the centre line",
          "Six 4.3 guide holes at X -95, 0, 95, Y 204 either side",
          "17 hole at the centre for the mast foot and the pack leads",
          "Sized for the 378 long lithium-ion ColdCell packs (was 330 x 290)",
          "Check: each strap threads through its pair of slots without twisting"]),
        ("KWL-DWG-104", "Arm hinge block: making sketch", Part("Arm hinge block", arm1("hinge_blocks"), COL["hinge_blocks"]),
         hb_n, LOC_HB, "6061-T6 aluminium bar 50 x 50, machined",
         ["Block 90 long x 46 wide x 60 high; inner end 125 from the hub centre",
          "Clevis slot 32 wide, from 25 in from the inner end to the outer end",
          "Slot open below and above, except the stop bridge 10 x 10 across the top at the outer end",
          "Pivot hole 8.05 reamed, 14 up from the bottom, 55 from the inner end",
          "Lock-pin hole 8.1, 37 up, 68 from the inner end",
          "Four M4 x 10 deep tapped holes top and bottom, 6 and 19 from the inner end, 15 either side",
          "Pocket 19 x 16 through between the bolt holes to save weight",
          "Side pockets 18.5 x 27 from each side, 4.5 from the centre pocket,",
          "  clear of the bolt holes by 4.5; cheek pockets 2.5 deep beside the pins",
          "Deburr; the stop bridge underside must be flat: it carries the arm's lift",
          "Check: an 8 mm pin slides through both pivot holes and both lock holes"]),
        ("KWL-DWG-105", "Arm root fitting: making sketch", Part("Arm root fitting", arm1("arm_roots"), COL["arm_roots"]),
         [ghost("block", arm1("hinge_blocks")), ghost("tube", arm1("arm_tubes"))],
         LOC["arm_roots"], "6061-T6 aluminium, machined in one piece",
         ["Tongue 65 long x 30 wide x 48 high; collar 48 OD x 50 long on its outer end",
          "Collar bore 40.2, 45 deep, on the tongue's centre height",
          "Pivot hole 8.05 reamed, 12 up from the tongue's bottom, 15 from its inner end",
          "Lock-pin hole 8.1, 35 up, 28 from the inner end",
          "Window 22 x 24 through the tongue, 41 to 63 from its inner end",
          "Side pockets 10 deep each side (10 centre web), 4.5 clear of both pin holes",
          "Two 5.2 cross holes through the collar, 15 and 37 from its inner end",
          "Top face of the tongue's outer end flat: it bears on the stop bridge",
          "Check: the tongue swings freely in the hinge block slot with 1 mm each side"]),
        ("KWL-DWG-106", "Arm tube: making sketch", Part("Arm tube", arm1("arm_tubes"), COL["arm_tubes"]),
         [ghost("root", arm1("arm_roots")), ghost("mount", arm1("motor_mounts"))], LOC["arm_tubes"],
         "Roll-wrapped carbon tube 40 OD x 36 ID",
         [f"Cut to {P['tube_r'][1] - P['tube_r'][0]:.0f} with a fine abrasive disc; square the ends",
          "Three 5.2 holes square through both walls on one line: 10, 32 and 385 from the inner end",
          "Drill through a wooden V block with a sharp brad-point bit; tape first",
          "Lightly sand 45 at the inner end and 40 at the outer end for bonding",
          "Make four; check all four are the same length within 0.5"]),
        ("KWL-DWG-107", "Motor mount: making sketch", Part("Motor mount", arm1("motor_mounts"), COL["motor_mounts"]),
         [ghost("tube", arm1("arm_tubes")), ghost("motors", arm1("motors"))], LOC["motor_mounts"],
         "6061-T6 aluminium, two halves machined together",
         ["Block 50 x 60 x 52, bored 40.2 through on the split line, then sawn in two",
          "Four 4.3 holes 8 in from the ends and 4.5 in from the sides, through both halves",
          "Each outer face: four M4 x 9 deep on a 35 circle at 45 deg, for the motor bought",
          "5.2 cross hole through both halves and the tube at the motor axis",
          "Face both halves flat so they close on the tube with 0.5 to 1 gap",
          "Side pockets 20.7 long between the bolts, 4.5 walls to the bore and faces",
          "Check: the motor axis is square to the tube within 1 deg"]),
        ("KWL-DWG-108", "Gear top block: making sketch", Part("Gear top block", C("gear_tops"), COL["gear_tops"]),
         [ghost("plate", crop(C("bot_plate"), -200, 200, 0, 200, 0, 2000)), ghost("strut", C("struts"))],
         M.gear_tops(P)[3], "6061 aluminium bar 30 x 40",
         ["Block 30 x 40 x 25",
          "20.1 socket 20 deep from the bottom, leaning out 13.4 deg from vertical",
          "Socket centre on the block centre line 5 below the top face",
          "Two M4 x 10 deep tapped holes in the top face, 30 apart along the long side",
          "Make four: two left-hand, two right-hand (socket leans outward)",
          "Check: a strut offcut sits fully home in the socket"]),
        ("KWL-DWG-109", "Skid block: making sketch", Part("Skid block", C("skid_blocks"), COL["skid_blocks"]),
         [ghost("skid", C("skids")), ghost("strut", C("struts"))], M.skid_blocks(P)[3], "6061 aluminium bar 30 x 30",
         ["Block 30 x 30 x 50",
          f"20.1 cross bore for the skid, centre {P['skid_z']:.0f} up from the bottom",
          "20.1 socket from the top face leaning in 13.4 deg; stops 6 above the skid bore",
          "4.3 hole up through the bottom face, 8 to the side of centre, through the skid bore",
          "Make four",
          "Check: the skid slides through the bore; a strut offcut sits home in the socket"]),
        ("KWL-DWG-110", "Gear struts and skids: making sketch", Part("Gear strut and skid", C("struts") + C("skids"), COL["struts"]),
         [ghost("blocks", C("gear_tops") + C("skid_blocks"))], None, "Carbon tube 20 OD x 17 ID",
         [f"Struts: four, {D['strut_len']:.0f} long; ends cut square",
          f"Skids: two, {2 * P['skid_half']:.0f} long; 4.3 holes 118 and 238 from one end",
          "Sand 20 at each strut end and the skid at the blocks for bonding",
          "Rubber end caps pushed on the skid ends",
          "Check: struts the same length within 1"]),
        ("KWL-DWG-111", "Pack guide: making sketch", Part("Pack guide", C("guides"), COL["guides"]),
         [ghost("deck", C("deck")), ghost("packs", C("packs"))], M.guides(P)[1], "Aluminium angle 20 x 20 x 2",
         ["Cut to 210 long; round the ends",
          "Three 4.3 holes on the flat leg's centre line, 10, 105 and 200 along",
          "Upright leg outboard, so the pack slides along its inside face",
          "Make two; check they sit flat on the deck"]),
        ("KWL-DWG-112", "Payload plate: making sketch", part("fr_plate", name="Payload plate"),
         [ghost("rails", C("rails")), ghost("socket", C("ds014"))], None, "6061-T6 plate 6 mm",
         [f"{P['pplate'][0]:.0f} x {P['pplate'][1]:.0f} x 6; two 50 lightening holes 100 apart",
          "Lock lug 20 x 20 x 10 screwed and bonded on top, its centre 7 from the front edge",
          "6.3 cross hole through the lug 5 up from the plate, across the plate",
          "DS-014 plug pad 18 x 50 on top at the rear edge",
          "Edges smooth and straight: they slide in the rail slots",
          "Float release: tap M4 for the saddles and release unit",
          "Tether module: tap M5 for the converter corners",
          "Check: slides the full length of the rails without binding"]),
        ("KWL-DWG-113", "Float saddle: making sketch", part("saddles", name="Float saddles (2)"),
         [ghost("plate", C("fr_plate")), ghost("float", C("float"))], None, "PETG, 3D printed, 40 % infill",
         ["Block 20 x 100 x 40 with a 121 round seat for the 120 float",
          "Two M4 heat-set inserts in the top face, 60 apart",
          "Print seat up, four walls; no supports needed",
          "Make two; check the float sits in both without rocking"]),
        ("KWL-DWG-114", "Float sling: making sketch", part("sling", name="Float sling"),
         [ghost("float", C("float")), ghost("release", C("release"))], None, "25 mm polyester webbing; bar-tack stitching",
         ["Loop round the float: 380 circumference, sewn into a ring with a bar tack",
          "Release tab: 80 of webbing folded and sewn to the ring, with a 15 loop at its end",
          "The release unit's pin passes through the tab loop",
          "The float's line is tied to the float only, never to the sling or the aircraft",
          "Check: with the pin pulled the sling drops clear under the float's weight"]),
    ]
    for no, title, p, neigh, vs, mat, notes in S:
        bv.component_sheet(p, neigh, "Kitewright Lift", no, title, mat, notes, DATE, view_shape=vs)
        print("sheet", no)


# ----------------------------------------------------------------- joints
def joints():
    zb = P["z_bot"]
    za = D["z_arm"]
    r = lambda k: Part(M.BOM[k][1].split(" (")[0], LOC.get(k) if k in LOC else {"hinge_blocks": LOC_HB, "pivots": LOC_PIV, "lock_pins": LOC_LCK}[k], COL[k])  # noqa: E731
    plates = Part("Hub plates (cut)", (M.hub_plate(P, False) + M.hub_plate(P, True)).rotate(M.Axis.Z, -45) & bx(100, 200, -60, 60, 0, 2000), COL["top_plate"])
    J = [
        ("joint-01.png", "Arm hinge, cut open on the arm's centre line",
         "Lift presses the tongue up against the stop bridge; the lock pin only stops the arm drooping",
         [r("hinge_blocks"), Part("Arm root fitting", LOC["arm_roots"] & bx(150, 300, -60, 60, 0, 2000), COL["arm_roots"]),
          r("pivots"), r("lock_pins"), plates,
          Part("Arm tube", LOC["arm_tubes"] & bx(200, 320, -60, 60, 0, 2000), COL["arm_tubes"])], "+Y", 18, -90),
        ("joint-02.png", "Hinge block between the hub plates",
         "Four M4 screws up through the bottom plate and four down through the top plate into each block",
         [r("hinge_blocks"), plates, r("pivots"), r("lock_pins")], None, 24, -58),
        ("joint-03.png", "Arm tube in the root collar, cut open",
         "Tube bonded 45 mm into the collar with structural epoxy and held by two M5 cross bolts",
         [Part("Arm root fitting", LOC["arm_roots"] & bx(200, 300, -60, 60, 0, 2000), COL["arm_roots"]),
          Part("Arm tube", LOC["arm_tubes"] & bx(220, 330, -60, 60, 0, 2000), COL["arm_tubes"])], "+Y", 20, -70),
        ("joint-04.png", "Motor clamp at the arm tip, cut open",
         "Two clamp halves on four M4 bolts; one M5 cross bolt through tube and clamp; a motor on each face",
         [Part("Motor mount", LOC["motor_mounts"], COL["motor_mounts"]), Part("Motors (upper and lower)", LOC["motors"], COL["motors"]),
          Part("Arm tube", LOC["arm_tubes"] & bx(540, 700, -60, 60, 0, 2000), COL["arm_tubes"]),
          Part("Propeller hubs", LOC["props"] & bx(560, 680, -60, 60, 0, 2000), COL["props"])], "+Y", 15, -70),
        ("joint-05.png", "Gear top block under the bottom plate, cut open",
         "Two M4 screws down through the plate; strut bonded 20 mm into the angled socket",
         [Part("Gear top block", M.gear_tops(P)[3], COL["gear_tops"]),
          Part("Bottom plate (part)", C("bot_plate") & bx(20, 100, 60, 160, 0, 2000), COL["bot_plate"]),
          Part("Gear strut", C("struts") & bx(20, 100, 60, 180, 380, 520), COL["struts"])], None, 20, -30),
        ("joint-06.png", "Skid block, strut and skid",
         "Skid through the cross bore with an M4 bolt; strut bonded into the socket above it",
         [Part("Skid block", M.skid_blocks(P)[3], COL["skid_blocks"]),
          Part("Skid", C("skids") & bx(-10, 140, 180, 270, -10, 60), COL["skids"]),
          Part("Gear strut", C("struts") & bx(20, 100, 150, 260, 0, 180), COL["struts"])], None, 22, -40),
        ("joint-07.png", "Payload plate in the Core rails, locked",
         "Plate edges slide in the rail slots; the payload pin passes through both rails and the plate's lug",
         [Part("Payload rails (Core)", C("rails") & bx(40, 140, -200, 200, 0, 2000), COL["rails"]),
          Part("Payload plate", C("fr_plate") & bx(40, 140, -200, 200, zb - 30, 2000), COL["fr_plate"]),
          Part("Payload pin (Core)", C("paylock"), COL["paylock"])], None, 24, -58),
        ("joint-08.png", "Deck, pack guide, pack and strap",
         "Pack between the guides on the deck; cam strap over the top and through two deck slots",
         [Part("Battery deck (part)", C("deck") & bx(-20, 165, 0, 160, 0, 2000), COL["deck"]),
          Part("Pack guide", C("guides") & bx(-20, 165, 0, 160, 0, 2000), COL["guides"]),
          Part("ColdCell pack", C("packs") & bx(-20, 165, 0, 160, 0, 2000), COL["packs"]),
          Part("Pack strap", C("straps") & bx(80, 140, -10, 160, 0, 2000), COL["straps"]),
          Part("Deck standoff", C("spacers") & bx(110, 150, -20, 20, D["z_top_top"] - 1, 2000), COL["spacers"])], None, 24, -58),
        ("joint-09.png", "Float release, cut open",
         "The release unit's pin holds the sling's tab; the float sits in two printed saddles",
         [Part("Payload plate", C("fr_plate"), COL["fr_plate"]), Part("Release unit", C("release"), COL["release"]),
          Part("Float sling", C("sling"), COL["sling"]), Part("Float saddles", C("saddles"), COL["saddles"]),
          Part("Rescue float", C("float"), COL["float"])], "+Y", 15, -80),
        ("joint-10.png", "Tether module",
         "Converter on four M5 screws under the plate; breakaway connector under the converter's rear",
         [Part("Payload plate", C("tm_plate", "tether"), COL["tm_plate"]), Part("DC-DC converter", C("converter", "tether"), COL["converter"]),
          Part("Breakaway connector", C("breakaway", "tether"), COL["breakaway"]),
          Part("Tether (short)", C("tether", "tether") & bx(-200, 200, -50, 50, zb - 300, zb), COL["tether"])], None, 22, -58),
        ("joint-11.png", "Core stack between the hub plates, cut open",
         "Core on four rubber dampers on the bottom plate; spacers and hinge blocks hold the plates apart",
         [Part("Hub plates", C("bot_plate") + C("top_plate"), COL["bot_plate"]), Part("Kitewright Core stack", C("core"), COL["core"]),
          Part("Hub spacers", C("spacers") & bx(-200, 200, -200, 200, 0, D["z_top_top"]), COL["spacers"]),
          Part("Hinge blocks", C("hinge_blocks"), COL["hinge_blocks"])], "+Y", 18, -70),
    ]
    for fn, title, sub, parts, cut, el, az in J:
        bv.joint(parts, OUT / fn, title, sub, cut=cut, elev=el, azim=az)
        print("joint", fn)


# ----------------------------------------------------------------- steps
def steps():
    zb = P["z_bot"]
    def g(k, payload="float"):
        return ghost(M.BOM[k][1], C(k, payload))
    hubdone = ["bot_plate", "hinge_blocks", "spacers", "core", "top_plate"]
    gear = ["gear_tops", "struts", "skid_blocks", "skids"]
    arm_keys = ["arm_roots", "arm_tubes", "motor_mounts", "motors", "escs"]
    others = [a for a in M.ARM_ANGLES if a != ARM]
    def three(k):
        src = {"hinge_blocks": LOC_HB, "pivots": LOC_PIV, "lock_pins": LOC_LCK}.get(k, LOC.get(k))
        return Compound([turn(src, a) for a in others])
    T = [
        ("Bolt the hinge blocks to the bottom plate", "Four M4 x 10 screws up through the plate into each block; slot outward",
         [g("bot_plate")], [part("hinge_blocks", explode=(0, 0, 160))], []),
        ("Fit the Core stack and the hub spacers", "Core on its four dampers; 60 mm spacers on M3 screws from below",
         [g("bot_plate"), g("hinge_blocks")], [part("core", explode=(0, 0, 160)), part("spacers", shape=M.Compound(M.hub_spacers(P)[:4]), explode=(0, 0, 220))], []),
        ("Fit the top hub plate", "Sixteen M4 screws into the blocks; M3 deck standoffs through it into the spacers",
         [g(k) for k in ["bot_plate", "hinge_blocks", "core"]] + [ghost("Hub spacers", M.Compound(M.hub_spacers(P)[:4]))],
         [part("top_plate", explode=(0, 0, 160)), part("spacers", shape=M.Compound(M.hub_spacers(P)[4:]), name="Deck standoffs (4)", explode=(0, 0, 260))], []),
        ("Build the landing gear", "Bond the struts into the top and skid blocks on a flat board; skids through the bores, M4 bolts",
         [], [part("gear_tops", explode=(0, 0, 150)), part("struts", explode=(0, 0, 60)), part("skid_blocks"), part("skids", explode=(0, 0, -60))], []),
        ("Bolt the gear under the hub", "Two M4 screws down through the bottom plate into each top block",
         [g(k) for k in hubdone], [Part("Landing gear", C("gear_tops") + C("struts") + C("skid_blocks") + C("skids"), COL["struts"], None, (0, 0, -250))], []),
        ("Fit the Core payload mount", "Rails on six M4 screws, slots facing in; DS-014 socket block at the back",
         [g(k) for k in hubdone + gear], [part("rails", explode=(0, 0, -150)), part("ds014", explode=(-120, 0, -150))], []),
        ("Make up each arm", "Bond and cross-bolt the tube into the root collar and the motor clamp; leave 24 h to cure",
         [], [Part("Arm root fitting", LOC["arm_roots"], COL["arm_roots"], None, (-120, 0, 0)),
              Part("Arm tube", LOC["arm_tubes"], COL["arm_tubes"]),
              Part("Motor mount (two halves)", LOC["motor_mounts"], COL["motor_mounts"], None, (120, 0, 0))], []),
        ("Fit the motors and controllers", "Upper motor on top, lower motor underneath, four M4 each; controllers strapped beside the tube",
         [ghost("Arm", LOC["arm_roots"] + LOC["arm_tubes"] + LOC["motor_mounts"])],
         [Part("Motors (2)", LOC["motors"], COL["motors"], None, (0, 0, 0)),
          Part("Motor controllers (2)", LOC["escs"], COL["escs"], None, (0, 0, 120))], []),
        ("Hang each arm in its hinge block", "Tongue into the slot, pivot bolt through, nut snug; swing up, push the lock pin home",
         [g(k) for k in hubdone + gear] + [ghost("Other arms", Compound([three(k) for k in arm_keys]))],
         [Part("Arm, made up", arm1("arm_roots") + arm1("arm_tubes") + arm1("motor_mounts") + arm1("motors") + arm1("escs"), COL["arm_roots"], None, out(250, -60)),
          Part("Pivot bolt", arm1("pivots"), COL["pivots"], None, out(0, -120)), Part("Lock pin", arm1("lock_pins"), COL["lock_pins"], None, out(0, 120))], []),
        ("Fit the propellers", "Upper and lower blades turn opposite ways; check the arrow on each hub",
         [g(k) for k in hubdone + gear + arm_keys], [part("props", explode=(0, 0, 160))], []),
        ("Fit the battery deck and pack guides", "Deck on the four standoffs with M3 screws; guides on M4 screws, upright legs outboard",
         [g(k) for k in hubdone + arm_keys], [part("deck", explode=(0, 0, 160)), part("guides", explode=(0, 0, 240))], []),
        ("Fit the GNSS mast", "Mast foot on the deck centre; lead down through the deck and top plate to the Core",
         [g(k) for k in hubdone + arm_keys + ["deck", "guides"]], [part("mast", explode=(0, 0, 200))], []),
        ("Fit the ColdCell packs", "Slide each pack between its guides; two cam straps each; plug its AS150 lead into the harness",
         [g(k) for k in hubdone + ["deck", "guides", "mast"]], [part("packs", explode=(0, 0, 200)), part("straps", explode=(0, 0, 320))], []),
        ("Slide in the float release payload", "From the front until the plug seats in the DS-014 socket; payload pin through rails and lug",
         [g(k) for k in hubdone + gear + ["rails", "ds014"]],
         [Part("Float release payload", C("fr_plate") + C("saddles") + C("release") + C("sling") + C("float"), COL["float"], None, (300, 0, 0)),
          part("paylock", explode=(0, -200, 0))], []),
        ("Or slide in the tether module", "Same rails and pin; converter lead to the Core bus tether input; tether through the breakaway",
         [g(k) for k in hubdone + gear + ["rails", "ds014"]],
         [Part("Tether module", C("tm_plate", "tether") + C("converter", "tether") + C("breakaway", "tether"), COL["converter"], None, (300, 0, 0)),
          part("paylock", explode=(0, -200, 0))], []),
    ]
    for i, (title, sub, dn, new, ctx) in enumerate(T, 1):
        bv.step(dn, new, OUT / f"step-{i:02d}.png", f"Step {i}: {title}", sub, context=ctx, label_done=len(dn) <= 4)
        print("step", i)
    # folding, for the transport step
    F = M.build_components(P, None, folded=True)
    fold_new = Compound([F[k].shape for k in arm_keys + ["props"]])
    bv.step([ghost(F[k].name, F[k].shape) for k in hubdone + gear + ["deck", "guides", "mast", "packs", "straps"]],
            [Part("Arms folded down, blades turned back", fold_new, COL["arm_roots"])],
            OUT / f"step-{len(T) + 1:02d}.png", f"Step {len(T) + 1}: Fold for transport",
            "Payload off; pull each lock pin, swing the arm down; turn both blades back along the arm", label_done=False)
    print("step", len(T) + 1)


if __name__ == "__main__":
    which = sys.argv[1:] or ["overview", "sheets", "joints", "steps"]
    for w in which:
        globals()[w]()
