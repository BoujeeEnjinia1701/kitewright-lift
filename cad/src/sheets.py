"""Kitewright Lift drawing sheets, Rev P2 (TRL 3, constructable design KWL-DDR-002).

Run from the repo root:  python cad/src/sheets.py [ga|folded]
    KWL-DWG-001  general arrangement, flying with the float release payload
    KWL-DWG-002  folded for transport (arms down, propeller blades turned back, payload off)
Written to cad/drawings/ as SVG, PDF and a 300 dpi PNG with .kit/drawing.py. Sizes come from
cad/src/model.py (PARAMS and derived()), so they follow any parameter change. The concept
blueprint in media/ is KWL-DWG-010.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from drawing import Sheet  # noqa: E402
from model import PARAMS as P, assembly, derived  # noqa: E402

DATE_P1 = "2026-10-03"


def safe_project_views(part, workdir, line_weight=0.3):
    """As drawing.project_views, edge by edge, so a degenerate edge from the hidden-line projection
    is skipped instead of stopping the export."""
    from build123d import ExportSVG, LineType, Unit
    workdir = Path(workdir)
    workdir.mkdir(parents=True, exist_ok=True)
    bb = part.bounding_box()
    c = bb.center()
    d = max(bb.size.X, bb.size.Y, bb.size.Z) * 10
    setups = {"front": ((c.X, c.Y - d, c.Z), (0, 0, 1)), "top": ((c.X, c.Y, c.Z + d), (0, 1, 0)),
              "right": ((c.X + d, c.Y, c.Z), (0, 0, 1)), "iso": ((c.X + d, c.Y - d, c.Z + d * 0.8), (0, 0, 1))}
    out, skipped = {}, 0
    for name, (origin, up) in setups.items():
        visible, hidden = part.project_to_viewport(origin, up, (c.X, c.Y, c.Z))
        ex = ExportSVG(unit=Unit.MM, line_weight=line_weight)
        ex.add_layer("Visible", line_color=0x111827)
        ex.add_layer("Hidden", line_color=0x9CA3AF, line_type=LineType.ISO_DASH, line_weight=line_weight / 2)
        for layer, edges in (("Visible", visible), ("Hidden", hidden if name in ("front", "right") else [])):
            for e in edges:
                try:
                    ex.add_shape(e, layer=layer)
                except (AssertionError, ValueError, ZeroDivisionError):
                    skipped += 1
        p = workdir / f"{name}.svg"
        ex.write(str(p))
        out[name] = p
    print(f"projected views; skipped {skipped} degenerate edges")
    return out


def ga():
    D = derived(P)
    work = ROOT / "cad" / "drawings" / "_ga_views"
    views = safe_project_views(assembly(P, "float"), work)
    s = Sheet(project="Kitewright Lift", title="Coaxial X8 rescue multirotor: general arrangement", dwg_no="KWL-DWG-001",
              rev="P2", author="Amish Chadha", date=DATE_P1, scale=None,
              material="Carbon plates and tubes, 6061-T6 fittings; bought parts per bom/bom.csv. PRELIMINARY, NOT FOR FABRICATION",
              revisions=[("P1", "Preliminary GA from the TRL 3 model", DATE_P1, "AC"),
                         ("P2", "KWL-DDR-002: design for construction", DATE_P1, "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 32, 140, 90, label="Isometric view", sublabel="Not to scale; float release payload fitted")
    s.add_notes("Main dimensions and interfaces (mm)", [
        f"Motor axes {P['motor_r']:.0f} from the centre on the diagonals; {D['wheelbase']:,.0f} motor to motor",
        f"Propellers 30 inch ({P['prop_d']:.0f}); tip gap {D['tip_gap']:.0f}; coaxial gap {D['coax_gap']:.0f}",
        f"Hub plates 3 carbon, {2 * P['hub_half']:.0f} square, {P['gap']:.0f} apart; underside {P['z_bot']:.0f} up",
        f"Arm tube carbon {P['tube'][0]:.0f} x {P['tube'][1]:.0f}; hinge pivot {P['pivot'][0]:.0f} from centre",
        f"Arm stop bridge {D['stop_lever']:.0f} outboard of the pivot; 8 lock pin",
        f"Upper rotor plane {D['z_upper_prop']:.0f} up; lower rotor plane {D['z_lower_prop']:.0f} up",
        f"Deck {P['deck'][0]:.0f} x {P['deck'][1]:.0f}, top {D['z_deck_top']:.0f} up; packs {P['pack'][0]:.0f} x {P['pack'][1]:.0f} x {P['pack'][2]:.0f}",
        f"Skids {2 * P['skid_half']:.0f} long, {2 * P['skid_y']:.0f} apart; struts 20 carbon",
        f"Payload rails 260 long, 112 apart (Core); payload plate {P['pplate'][1]:.0f} wide",
        f"GNSS puck top {D['z_mast_top']:.0f} above the ground",
        "Arms fold down about the pivot: see KWL-DWG-002",
        "Third-angle; front view from -Y; X forward; arms on the diagonals",
    ], x=276, y=134, width=146)
    out = s.save(ROOT / "cad" / "drawings" / "KWL-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote", out)


def folded():
    work = ROOT / "cad" / "drawings" / "_fold_views"
    asm = assembly(P, None, folded=True)
    bb = asm.bounding_box()
    views = safe_project_views(asm, work)
    s = Sheet(project="Kitewright Lift", title="Coaxial X8 rescue multirotor: folded for transport", dwg_no="KWL-DWG-002",
              rev="P1", author="Amish Chadha", date=DATE_P1, scale=None,
              material="As KWL-DWG-001. PRELIMINARY, NOT FOR FABRICATION",
              revisions=[("P1", "Folded arrangement from the constructable model", DATE_P1, "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 32, 140, 90, label="Isometric view", sublabel="Not to scale; payload removed")
    s.add_notes("Folding (mm)", [
        f"Envelope {bb.size.X:.0f} x {bb.size.Y:.0f} x {bb.size.Z:.0f} (X x Y x Z) with the gear on",
        "Fits a case 1,200 x 600 x 500 standing on its skids or on its side",
        "Pull each lock pin, swing the arm down 90 deg about its pivot",
        "Turn both blades of each propeller back along its arm",
        "Payload off before folding; packs may stay on the deck",
        f"Lowest folded part {P['z_bot'] + P['pivot'][1] - (P['motor_r'] - P['pivot'][0]) - 45:.0f} above the ground",
        "Unfold in reverse; every lock pin in and flagged before arming",
    ], x=276, y=134, width=146)
    out = s.save(ROOT / "cad" / "drawings" / "KWL-DWG-002")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote", out)


if __name__ == "__main__":
    for w in sys.argv[1:] or ["ga", "folded"]:
        globals()[w]()
