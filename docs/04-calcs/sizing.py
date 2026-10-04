"""Kitewright Lift sizing calculations (KWL-CAL-001).

Run from the repo root:  python docs/04-calcs/sizing.py
Prints every section of docs/04-calcs/01-sizing.md and writes docs/04-calcs/results.csv.
Made-part masses and the folded envelope come from the build123d model (cad/src/model.py);
bought-part masses and costs come from the assumptions below and bom/bom.csv.
All results are first-order estimates for TRL 3; nothing here has been measured.
"""
from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "cad" / "src")]

G = 9.81
R_AIR = 287.05

# ---------------------------------------------------------------- assumptions
A = {
    "n_rotor": 8,                 # coaxial X8: 4 arms, a motor above and below each
    "prop_d": 0.762,              # m, 30 inch
    "k_coax": 1.28,               # induced power factor of a coaxial pair against two isolated rotors (Leishman)
    "fm": 0.65,                   # figure of merit of a 30 inch hobby-grade propeller (isolated)
    "eta_drive": 0.80,            # motor x controller efficiency at hover
    "p_avionics": 35.0,           # W, Kitewright Core stack
    "p_payload": 15.0,            # W, release servo or converter control
    "t_max_sl": 10.0,             # kg, maker's class figure: static thrust of one motor at full throttle, sea level
    "k_lower": 0.80,              # lower rotor at full throttle in the upper rotor's wake
    "usable": 0.80,               # fraction of nominal pack energy used (20 % kept to land)
    "cold_factor": 0.85,          # ColdCell R1: energy delivered at -20 C, heater energy included
    "cd_a": 0.30,                 # m2, drag area of the aircraft with a payload, side on (estimate)
    "mtow_limit": 25.0,           # kg, R1
    # Packs. Since KWL-DDR-003 (decision 2 option A) Lift flies two ColdCell lithium-ion 14S3P packs; their
    # mass is ColdCell's estimate (CCL-CAL-001 K: 3,844 g, of which 42 cells 2,940 g). The LiFePO4 16S2P pack of
    # KWL-CAL-001 v0.1 and the 0.62 kg allowance Lift assumed for decision 2 are kept for comparison only.
    "cell_lfp": dict(v=3.2, ah=3.0, kg=0.085, amps=30.0, name="LiFePO4 26650, 3.0 Ah, 10C"),
    "cell_li": dict(v=3.6, ah=4.5, kg=0.070, amps=45.0, name="Li-ion 21700, 4.5 Ah, 45 A"),
    "pack_lfp": dict(s=16, p=2, extra_kg=0.62),   # heater film, insulation, BMS, shell, connector
    "pack_li": dict(s=14, p=3, extra_kg=0.904),   # ColdCell CCL-CAL-001 K: 3.844 kg less 2.940 kg of cells
    "pack_li_assumed": dict(s=14, p=3, extra_kg=0.62),   # what Lift assumed when decision 2 was posed
    "preheat_wh_pack": 35.6,      # ColdCell CCL-CAL-001 K: pre-heat energy of one variant pack from -20 C
    "n_packs": 2,
    # tether
    "v_tether": 400.0,            # V DC at the ground supply, fixed
    "tether_len": 60.0,           # m
    "tether_mm2": 0.75,           # each conductor
    "rho_cu": 0.0175,             # ohm mm2 / m at 20 C
    "tether_kg_m": 0.025,
    "hover_height": 50.0,         # m, highest tethered hover
    "eta_dcdc": 0.95,
    "conv_kw": 4.0,
    # float drop
    "drop_h": 10.0,
    "float_kg": 0.85, "float_area": 0.12 * 0.42, "float_cd": 0.9,
    "wind": 10.0, "aim_residual": 0.3,
    "hold_err": 2.0,
}

# bought or sibling parts: (BOM line, kg each, qty) for the flying aircraft
# Power wiring: 0.650 kg as before plus 0.124 kg for the two pack input and two frame output leads, 8 AWG with
# AS150 plugs, that moved from the Kitewright Core to this harness (KWC-DDR-003). The Core stays at 1.0 kg (0.996 kg).
BOUGHT = {
    "Hub spacers and standoffs": (3, 0.005, 8), "Arm lock pins": (9, 0.030, 4), "Motors": (10, 0.450, 8),
    "Motor controllers": (11, 0.110, 8), "Propellers": (12, 0.110, 8), "Pack straps": (19, 0.030, 4),
    "GNSS mast": (20, 0.060, 1), "Kitewright Core with payload mount": (21, 1.000, 1),
    "Power wiring": (24, 0.774, 1), "Fasteners, epoxy, dampers": (25, 0.250, 1), "Skid end caps": (16, 0.010, 4),
}
PAYLOAD_BOUGHT = {"float": {"Release unit": 0.08, "Float sling": 0.03, "Rescue float and line bag": 0.85},
                  "tether": {"DC-DC converter": 1.40, "Breakaway connector": 0.15}}

ISA = {0: (101325.0, 288.15), 5000: (54020.0, 255.65)}


def rho(p, T):
    return p / (R_AIR * T)


def pack(cell, cfg):
    n = cfg["s"] * cfg["p"]
    kg = n * cell["kg"] + cfg["extra_kg"]
    wh = n * cell["v"] * cell["ah"]
    return dict(cells=n, kg=kg, wh=wh, v=cfg["s"] * cell["v"], amps_max=cfg["p"] * cell["amps"], wh_kg=wh / kg)


def hover_power(m, r):
    """Electrical hover power (W) of the coaxial X8 at mass m (kg) and air density r (kg/m3)."""
    T = m * G
    area = A["n_rotor"] * math.pi * (A["prop_d"] / 2) ** 2
    p_ideal = A["k_coax"] * T ** 1.5 / math.sqrt(2 * r * area)
    return p_ideal / (A["fm"] * A["eta_drive"])


def cad_values():
    import model
    m = model.masses()
    c = model.clearances()
    D = model.derived()
    return m, c, D


def results(verbose=False):
    m_cad, clr, D = cad_values()
    R = {}
    # ---- A. mass
    frame_made = {k: v for k, v in m_cad.items() if k not in ("fr_plate", "tm_plate", "saddles")}
    R["made_kg"] = sum(frame_made.values())
    R["bought_kg"] = sum(kg * q for _, kg, q in BOUGHT.values())
    R["empty_kg"] = R["made_kg"] + R["bought_kg"]
    P_lfp = pack(A["cell_lfp"], A["pack_lfp"])
    P_li = pack(A["cell_li"], A["pack_li"])
    R["pack_lfp"], R["pack_li"] = P_lfp, P_li
    R["packs_kg"] = A["n_packs"] * P_li["kg"]
    R["packs_wh"] = A["n_packs"] * P_li["wh"]
    R["ready_kg"] = R["empty_kg"] + R["packs_kg"]
    R["float_module_kg"] = m_cad["fr_plate"] + m_cad["saddles"] + sum(PAYLOAD_BOUGHT["float"].values())
    hanging = A["tether_kg_m"] * A["hover_height"]
    R["tether_module_kg"] = m_cad["tm_plate"] + sum(PAYLOAD_BOUGHT["tether"].values()) + hanging
    R["tether_hanging_kg"] = hanging
    R["mtow_5"] = R["ready_kg"] + 5.0
    R["mtow_2"] = R["ready_kg"] + 2.0
    R["max_payload_sl"] = A["mtow_limit"] - R["ready_kg"]
    R["mtow_tether"] = R["ready_kg"] + R["tether_module_kg"]
    # ---- B. air and hover power
    r_sl = rho(*ISA[0])
    r_alt = rho(ISA[5000][0], 253.15)          # 5,000 m at -20 C
    r_hot = rho(101325.0, 318.15)               # sea level at +45 C
    R["rho_sl"], R["rho_alt"], R["rho_hot"] = r_sl, r_alt, r_hot
    R["sigma_alt"] = r_alt / r_sl
    base = A["p_avionics"] + A["p_payload"]
    R["p_sl_5"] = hover_power(R["mtow_5"], r_sl) + base
    R["p_sl_0"] = hover_power(R["ready_kg"], r_sl) + A["p_avionics"]
    R["p_alt_2"] = hover_power(R["mtow_2"], r_alt) + base
    R["p_hot_5"] = hover_power(R["mtow_5"], r_hot) + base
    R["p_tether"] = hover_power(R["mtow_tether"], r_sl) + base
    area = A["n_rotor"] * math.pi * (A["prop_d"] / 2) ** 2
    R["disc_loading"] = R["mtow_5"] * G / (area / 2)       # N/m2 on the projected (4 disc) area
    R["v_induced"] = math.sqrt(R["mtow_5"] * G / (2 * r_sl * area / 2))
    # ---- C. endurance (R4)
    def minutes(wh, p, cold=False):
        e = wh * A["usable"] * (A["cold_factor"] if cold else 1.0)
        return 60.0 * e / p
    R["t_sl_5"] = minutes(R["packs_wh"], R["p_sl_5"])
    R["t_sl_0"] = minutes(R["packs_wh"], R["p_sl_0"])
    R["t_alt_2"] = minutes(R["packs_wh"], R["p_alt_2"], cold=True)
    R["t_hot_5"] = minutes(R["packs_wh"], R["p_hot_5"])
    # pack current
    R["i_hover"] = R["p_sl_5"] / P_li["v"]
    R["i_cell_hover"] = R["i_hover"] / (A["n_packs"] * A["pack_li"]["p"])
    R["i_cell_climb"] = 1.5 * R["i_cell_hover"]
    # comparison: the design of KWL-CAL-001 v0.1 (LiFePO4 16S2P, fittings unpocketed, 330 x 290 deck, Core leads in the Core)
    import model as _m
    before_P = dict(_m.PARAMS, pockets=False, deck=(330.0, 290.0, 3.0), pack=(126.0, 232.0, 85.0))
    m_before = _m.masses(before_P)
    made_before = sum(v for k, v in m_before.items() if k not in ("fr_plate", "tm_plate", "saddles"))
    empty_before = made_before + R["bought_kg"] - 0.124
    lfp_kg, lfp_wh = A["n_packs"] * P_lfp["kg"], A["n_packs"] * P_lfp["wh"]
    R["pocket_saving_model"] = sum(m_before[k] - m_cad[k] for k in ("hinge_blocks", "arm_roots", "motor_mounts"))
    R["deck_growth"] = (m_cad["deck"] + m_cad["guides"]) - (m_before["deck"] + m_before["guides"])
    P_as = pack(A["cell_li"], A["pack_li_assumed"])
    CMP = {}

    def case(name, empty, pk_kg, pk_wh):
        m5, m2 = empty + pk_kg + 5.0, empty + pk_kg + 2.0
        CMP[name] = dict(mtow_5=m5, payload=A["mtow_limit"] - (empty + pk_kg),
                         t_sl=minutes(pk_wh, hover_power(m5, r_sl) + base), t_alt=minutes(pk_wh, hover_power(m2, r_alt) + base, cold=True))
    case("KWL-CAL-001 v0.1: LiFePO4, fittings as first drawn", empty_before, lfp_kg, lfp_wh)
    case("Decision 1 A only (pockets as modelled), LiFePO4", empty_before - R["pocket_saving_model"], lfp_kg, lfp_wh)
    case("Both decisions with the 3.56 kg pack Lift assumed", R["empty_kg"], A["n_packs"] * P_as["kg"], A["n_packs"] * P_as["wh"])
    case("Both decisions as now designed (ColdCell 3.84 kg packs)", R["empty_kg"], R["packs_kg"], R["packs_wh"])
    R["CMP"] = CMP
    R["t_sl_45"] = minutes(R["packs_wh"], hover_power(A["mtow_limit"], r_sl) + base)
    # ---- D. thrust margin and motor out (R3, R5)
    pair_max = A["t_max_sl"] * (1 + A["k_lower"])
    for tag, sig, m in (("sl", 1.0, R["mtow_5"]), ("alt", R["sigma_alt"], R["mtow_2"])):
        R[f"tw_{tag}"] = 4 * pair_max * sig / m
        R[f"tw_out_{tag}"] = (2 * A["t_max_sl"] + 2 * pair_max) * sig / m
        R[f"arm_share_{tag}"] = m / 4.0
        R[f"single_max_{tag}"] = A["t_max_sl"] * sig
    R["motor_p_max"] = hover_power(A["t_max_sl"] * A["n_rotor"], r_sl) / A["n_rotor"] * A["k_coax"] ** -1 * 1.0
    R["motor_i_max"] = R["motor_p_max"] / (A["pack_li"]["s"] * 3.3)
    # ---- E. wind (R6)
    drag = 0.5 * r_sl * A["wind"] ** 2 * A["cd_a"]
    R["drag_10"] = drag
    R["tilt_10"] = math.degrees(math.atan(drag / (R["mtow_5"] * G)))
    R["thrust_10"] = math.hypot(drag, R["mtow_5"] * G) / (R["mtow_5"] * G)
    R["gust_tilt"] = math.degrees(math.atan(0.5 * r_sl * 15.0 ** 2 * A["cd_a"] / (R["mtow_5"] * G)))
    # ---- F. arm, hinge and fixings at full thrust (structure)
    F_arm = pair_max * G                              # N, both motors of one arm at full throttle
    L_arm = D["arm_len"] / 1000.0
    M_hinge = F_arm * L_arm
    R["arm_force"], R["hinge_moment"] = F_arm, M_hinge
    R["stop_force"] = M_hinge / (D["stop_lever"] / 1000.0)
    R["pivot_force"] = R["stop_force"] + F_arm
    R["pivot_shear"] = R["pivot_force"] / (2 * math.pi * 4.0 ** 2)
    R["bridge_stress"] = (R["stop_force"] * 32.0 / 12.0) / (10.0 * 10.0 ** 2 / 6.0)
    R["bridge_bearing"] = R["stop_force"] / (10.0 * 30.0)
    R["cheek_bearing"] = R["pivot_force"] / (2 * 7.0 * 8.0)
    do, di = 40.0, 36.0
    I = math.pi / 64 * (do ** 4 - di ** 4)
    L_tube = (620.0 - 280.0)
    R["tube_stress"] = F_arm * L_tube / (I / (do / 2))
    R["tube_defl_max"] = F_arm * L_tube ** 3 / (3 * 70000.0 * I)
    R["tube_defl_hover"] = R["tube_defl_max"] * (R["mtow_5"] / 4.0) / pair_max
    R["droop_moment"] = 2.2 * G * 0.25 * 3.0          # arm group about 2.2 kg, centroid 0.25 m out, 3 g landing
    R["lock_force"] = R["droop_moment"] / (D["lock_lever"] / 1000.0)
    R["lock_shear"] = R["lock_force"] / (2 * math.pi * 4.0 ** 2)
    R["hover_stop_force"] = (R["mtow_5"] / 4 * G) * L_arm / (D["stop_lever"] / 1000.0)
    # landing gear: 2 m/s touchdown on one skid, all four struts in compression (estimate)
    R["gear_load"] = R["mtow_5"] * G * 3.0 / 2.0
    th = math.radians(13.4)
    R["strut_force"] = R["gear_load"] / 2 / math.cos(th)
    R["strut_stress"] = R["strut_force"] / (math.pi / 4 * (20.0 ** 2 - 17.0 ** 2))
    R["tip_angle_x"] = math.degrees(math.atan(170.0 / (D["z_deck"] + 30.0)))
    # ---- G. tether (R7)
    Rl = 2 * A["tether_len"] * A["rho_cu"] / A["tether_mm2"]
    P_in = R["p_tether"] / A["eta_dcdc"]
    I = P_in / A["v_tether"]
    for _ in range(5):                                 # voltage drop raises the current a little
        I = P_in / (A["v_tether"] - I * Rl)
    R["tether_ohm"], R["tether_i"], R["tether_drop"] = Rl, I, I * Rl
    R["tether_loss"] = I ** 2 * Rl
    R["tether_ground_kw"] = (P_in + R["tether_loss"]) / 1000.0
    R["conv_margin"] = A["conv_kw"] * 1000.0 / R["p_tether"]
    R["tether_wind_kw"] = (hover_power(R["mtow_tether"], r_sl) * R["thrust_10"] ** 1.5 + base) / 1000.0
    R["tether_2h_kwh"] = R["tether_ground_kw"] * 2.0
    # ---- H. float drop (R8)
    t_fall = math.sqrt(2 * A["drop_h"] / G)
    a_d = 0.5 * r_sl * A["wind"] ** 2 * A["float_cd"] * A["float_area"] / A["float_kg"]
    drift = min(0.5 * a_d * t_fall ** 2, A["wind"] * t_fall)
    R["t_fall"], R["drift_10"] = t_fall, drift
    R["drop_err"] = math.hypot(A["hold_err"], drift * A["aim_residual"])
    R["v_impact"] = G * t_fall
    R["downwash_10m"] = 2 * R["v_induced"] * 0.5        # far wake halved by 10 m of mixing (estimate)
    # ---- I. transport (R9)
    R["fold_x"], R["fold_y"], R["fold_z"] = clr["folded envelope X"], clr["folded envelope Y"], clr["folded envelope Z"]
    R["setup_min"] = 4 * 0.75 + 8 * 0.15 + 2 * 0.5 + 1.0 + 1.5 + 1.0
    R["clearances"] = clr
    # ---- J. temperature (R10)
    R["heater_wh"] = A["n_packs"] * A["preheat_wh_pack"]      # ColdCell CCL-CAL-001 K, from -20 C
    # ---- K. cost (R11)
    rows = list(csv.DictReader((ROOT / "bom" / "bom.csv").open()))
    frame = payload = 0.0
    for r_ in rows:
        n = int(r_["item"].split(" ")[0])
        c = float(r_["qty"]) * float(r_["unit_cost_usd"])
        if n <= 25:
            frame += c
        else:
            payload += c
    R["cost_frame"], R["cost_payload"] = frame, payload
    R["D"] = D
    return R


REQ = [  # id, requirement, result function, status function
    ("R1", "Maximum take-off mass", lambda R: f"{R['mtow_5']:.1f} kg with a 5 kg payload; {R['ready_kg']:.1f} kg ready to fly with no payload",
     lambda R: "Met on paper" if R["mtow_5"] <= 25.0 else "Not met"),
    ("R2", "Payload at sea level", lambda R: f"Payload allowance inside R1: {R['max_payload_sl']:.1f} kg; full-throttle thrust to weight {R['tw_sl']:.2f}",
     lambda R: "Met on paper" if R["max_payload_sl"] >= 5.0 else "At risk"),
    ("R3", "Payload at altitude", lambda R: f"Thrust to weight {R['tw_alt']:.2f} at 5,000 m and -20 C with 2 kg ({R['mtow_2']:.1f} kg)",
     lambda R: "Met on paper" if R["tw_alt"] >= 1.6 else "At risk"),
    ("R4", "Hover time", lambda R: f"{R['t_sl_5']:.1f} min with 5 kg at sea level ({R['mtow_5']:.1f} kg); {R['t_alt_2']:.1f} min with 2 kg at 5,000 m and -20 C",
     lambda R: "Not met" if (R["t_sl_5"] < 20 or R["t_alt_2"] < 10) else "Met on paper"),
    ("R5", "Motor-out tolerance", lambda R: f"Thrust to weight with one motor out {R['tw_out_sl']:.2f} at sea level, {R['tw_out_alt']:.2f} at 5,000 m",
     lambda R: "Met on paper" if R["tw_out_alt"] >= 1.15 else "At risk"),
    ("R6", "Wind", lambda R: f"{R['drag_10']:.0f} N drag at 10 m/s; tilt {R['tilt_10']:.1f} deg; position hold set by tuning",
     lambda R: "Met on paper (thrust); hold to be shown in flight"),
    ("R7", "Tethered endurance", lambda R: f"{R['p_tether'] / 1000:.2f} kW hover on the tether; converter margin {R['conv_margin']:.2f}; tether drop {R['tether_drop']:.0f} V",
     lambda R: "Met on paper" if R["conv_margin"] >= 1.2 else "At risk"),
    ("R8", "Float and line drop", lambda R: f"Expected miss {R['drop_err']:.1f} m from 10 m (2 m hold, wind drift {R['drift_10']:.1f} m aimed off)",
     lambda R: "Met on paper" if R["drop_err"] <= 3.0 else "At risk"),
    ("R9", "Transport", lambda R: f"Folded {R['fold_z'] / 1000:.2f} x {R['fold_y'] / 1000:.2f} x {R['fold_x'] / 1000:.2f} m; set-up about {R['setup_min']:.0f} min",
     lambda R: "Met on paper" if (R["fold_z"] <= 1200 and R["fold_y"] <= 600 and R["fold_x"] <= 500) or (R["fold_x"] <= 600 and R["fold_y"] <= 500) else "Not met"),
    ("R10", "Operating temperature", lambda R: f"ColdCell heating about {R['heater_wh']:.0f} Wh from the ground supply before take-off; parts rated -20 to +45 C",
     lambda R: "At risk: the lithium-ion packs stay under 50 C in a 20 min hover only up to 25 C ambient with their jacket on (ColdCell CCL-CAL-001 K, open decision 6)"),
    ("R11", "Prototype cost", lambda R: f"USD {R['cost_frame']:,.0f} for the aircraft excluding payloads",
     lambda R: f"Over the value-engineering target by USD {R['cost_frame'] - 5000:,.0f}" if R["cost_frame"] > 5000 else "Within the value-engineering target"),
]


def main():
    R = results()
    D = R["D"]
    P = R["pack_li"]
    print("A. Mass (kg)")
    print(f"  made parts from the model {R['made_kg']:.2f}; bought {R['bought_kg']:.2f}; empty {R['empty_kg']:.2f}")
    print(f"  ColdCell lithium-ion pack 14S3P: {P['cells']} cells, {P['kg']:.2f} kg, {P['wh']:.0f} Wh, {P['v']:.1f} V, {P['wh_kg']:.0f} Wh/kg; two packs {R['packs_kg']:.2f} kg, {R['packs_wh']:.0f} Wh")
    print(f"  pockets as modelled save {R['pocket_saving_model']:.3f} kg; deck and guides grew {R['deck_growth']:.3f} kg for the long packs")
    print(f"  ready to fly {R['ready_kg']:.2f}; float module {R['float_module_kg']:.2f}; tether module {R['tether_module_kg']:.2f} (hanging tether {R['tether_hanging_kg']:.2f})")
    print(f"  MTOW with 5 kg {R['mtow_5']:.2f}; with 2 kg {R['mtow_2']:.2f}; tethered {R['mtow_tether']:.2f}; payload allowance {R['max_payload_sl']:.2f}")
    print("B. Air and hover power")
    print(f"  density SL {R['rho_sl']:.3f}, 5,000 m -20 C {R['rho_alt']:.3f} (sigma {R['sigma_alt']:.3f}), SL +45 C {R['rho_hot']:.3f}")
    print(f"  hover W: SL 5 kg {R['p_sl_5']:.0f}; SL empty {R['p_sl_0']:.0f}; 5,000 m 2 kg {R['p_alt_2']:.0f}; +45 C 5 kg {R['p_hot_5']:.0f}; tethered {R['p_tether']:.0f}")
    print(f"  disc loading {R['disc_loading']:.0f} N/m2; induced velocity {R['v_induced']:.1f} m/s")
    print("C. Endurance (min)")
    print(f"  SL 5 kg {R['t_sl_5']:.1f}; SL empty {R['t_sl_0']:.1f}; 5,000 m 2 kg -20 C {R['t_alt_2']:.1f}; +45 C 5 kg {R['t_hot_5']:.1f}")
    print(f"  pack current at hover {R['i_hover']:.0f} A; per cell {R['i_cell_hover']:.1f} A hover, {R['i_cell_climb']:.1f} A climb (cell rating {A['cell_li']['amps']:.0f} A)")
    for k, v in R["CMP"].items():
        print(f"  compare: {k}: MTOW with 5 kg {v['mtow_5']:.2f}; payload inside 25 kg {v['payload']:.2f}; {v['t_sl']:.1f} min SL 5 kg, {v['t_alt']:.1f} min 5,000 m 2 kg")
    print(f"  at the {R['max_payload_sl']:.2f} kg payload allowed by R1: {R['t_sl_45']:.1f} min")
    print("D. Thrust margin and motor out")
    print(f"  T/W SL {R['tw_sl']:.2f}, 5,000 m {R['tw_alt']:.2f}; one motor out SL {R['tw_out_sl']:.2f}, 5,000 m {R['tw_out_alt']:.2f}")
    print(f"  arm share SL {R['arm_share_sl']:.2f} kg vs single motor {R['single_max_sl']:.1f}; 5,000 m {R['arm_share_alt']:.2f} vs {R['single_max_alt']:.2f}")
    print(f"  one motor at full thrust about {R['motor_p_max']:.0f} W, {R['motor_i_max']:.0f} A")
    print("E. Wind")
    print(f"  drag {R['drag_10']:.1f} N at 10 m/s; tilt {R['tilt_10']:.1f} deg; thrust needed {R['thrust_10']:.3f} x weight; 15 m/s gust tilt {R['gust_tilt']:.1f} deg")
    print("F. Structure at full thrust")
    print(f"  arm force {R['arm_force']:.0f} N; hinge moment {R['hinge_moment']:.1f} N m; stop {R['stop_force']:.0f} N (hover {R['hover_stop_force']:.0f} N); pivot {R['pivot_force']:.0f} N")
    print(f"  pivot shear {R['pivot_shear']:.1f} MPa; bridge bending {R['bridge_stress']:.0f} MPa, bearing {R['bridge_bearing']:.1f} MPa; cheek bearing {R['cheek_bearing']:.1f} MPa")
    print(f"  tube bending {R['tube_stress']:.0f} MPa; tip deflection {R['tube_defl_max']:.2f} mm full, {R['tube_defl_hover']:.2f} mm hover")
    print(f"  droop moment {R['droop_moment']:.1f} N m; lock pin {R['lock_force']:.0f} N, shear {R['lock_shear']:.1f} MPa")
    print(f"  gear load {R['gear_load']:.0f} N; strut {R['strut_force']:.0f} N, {R['strut_stress']:.1f} MPa; tip-over angle {R['tip_angle_x']:.1f} deg")
    print("G. Tether")
    print(f"  loop {R['tether_ohm']:.2f} ohm; {R['tether_i']:.2f} A; drop {R['tether_drop']:.1f} V; loss {R['tether_loss']:.0f} W; ground {R['tether_ground_kw']:.2f} kW; "
          f"converter margin {R['conv_margin']:.2f}; in 10 m/s wind {R['tether_wind_kw']:.2f} kW; 2 h {R['tether_2h_kwh']:.1f} kWh")
    print("H. Float drop")
    print(f"  fall {R['t_fall']:.2f} s; drift at 10 m/s {R['drift_10']:.2f} m; expected miss {R['drop_err']:.2f} m; impact {R['v_impact']:.1f} m/s; downwash at 10 m about {R['downwash_10m']:.1f} m/s")
    print("I. Transport")
    print(f"  folded {R['fold_x']:.0f} x {R['fold_y']:.0f} x {R['fold_z']:.0f} mm; set-up {R['setup_min']:.1f} min")
    for k, v in R["clearances"].items():
        print(f"    {k}: {v:.1f}")
    print("J. Temperature")
    print(f"  pre-heat energy {R['heater_wh']:.0f} Wh")
    print("K. Cost")
    print(f"  aircraft USD {R['cost_frame']:,.0f}; payloads and ground equipment USD {R['cost_payload']:,.0f}")
    print("Results against requirements")
    out = ROOT / "docs" / "04-calcs" / "results.csv"
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "requirement", "result", "status"])
        for rid, name, res, st in REQ:
            w.writerow([rid, name, res(R), st(R)])
            print(f"  {rid:4s} {name:24s} {res(R)} | {st(R)}")
        # numbers the media scripts use
        for k in ("mtow_5", "ready_kg", "packs_wh", "p_sl_5", "p_alt_2", "t_sl_5", "t_alt_2", "tw_alt", "tw_out_alt",
                  "tether_ground_kw", "tether_loss", "p_tether", "cost_frame", "fold_x", "fold_y", "fold_z"):
            w.writerow(["value", k, f"{R[k]:.4f}", ""])
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
