---
doc_id: KWL-CAL-001
title: Kitewright Lift sizing calculations
project: Kitewright Lift
doc_type: Calculation
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First sizing of the constructable design (KWL-DDR-002) against every requirement
---

# Kitewright Lift sizing calculations

The constructable design lifts its payloads with ample thrust at sea level and at 5,000 m, survives the loss of any one motor on paper, folds into the R9 case and carries its loads with large margins in the arms and hinges. Two results fall short: with a 5 kg payload the aircraft weighs 25.5 kg (R1 and R2), and the LiFePO4 ColdCell packs give 8.9 min of hover at sea level and 7.1 min at 5,000 m (R4). Both are posed to Amish in `docs/REVIEW.md`.

Every number comes from `docs/04-calcs/sizing.py`, which reads made-part masses and the folded envelope from the build123d model (`cad/src/model.py`) and prices from `bom/bom.csv`, and writes `docs/04-calcs/results.csv`. All results are first-order estimates; nothing has been measured.

## Assumptions

*Table 1. Assumptions.*

| Quantity | Value | Basis |
| --- | --- | --- |
| Air at sea level; at 5,000 m and -20 °C; at sea level and +45 °C | 1.225; 0.743; 1.109 kg/m3 | ISA pressure (101.3 and 54.0 kPa), ideal gas |
| Rotors | 8 x 30 inch (0.762 m), coaxial pairs on four arms | KWL-DDR-001, item 1 |
| Coaxial induced power factor | 1.28 against two isolated rotors | Leishman, momentum theory with the lower rotor in the upper's slipstream |
| Figure of merit; motor and controller efficiency | 0.65; 0.80 | Typical for 30 inch carbon propellers and 100 KV motors in hover |
| Full-throttle thrust per motor at sea level | 10 kg; lower rotor 80 % of that in a pair | Maker's class figure; to be measured on AltiRig |
| Avionics and payload power | 35 W and 15 W | Core stack; release servo or converter control |
| Pack | 16S2P LiFePO4 26650 power cells, 3.0 Ah, 85 g, 30 A; plus 0.62 kg heater, insulation, BMS, shell | ColdCell design as assumed for Lift |
| Energy used per flight | 80 % of nominal; 85 % of that at -20 °C | 20 % kept to land; ColdCell R1 |
| Drag area, side on | 0.30 m2 | Hub, packs, gear and payload (estimate) |
| Bought masses | Motors 450 g, controllers 110 g, propellers 110 g, Core 1.0 kg, wiring 0.65 kg, fasteners and epoxy 0.25 kg | Class figures; Core R9 |
| Tether | 400 V DC fixed, 60 m, 2 x 0.75 mm2 copper, 25 g/m, 50 m highest hover; converter 95 %, 4 kW | KWL-DDR-001, item 5 |
| Float | 0.85 kg, 0.12 x 0.42 m, drag coefficient 0.9 | Foam float with line bag |

## A. Mass

Made parts from the model weigh 6.15 kg: hinge blocks 1.15, root fittings 1.15, motor clamps 0.96, arm tubes 0.61, hub plates 0.69, deck 0.44, gear 0.88, pivot bolts 0.13, guides 0.10, spacers 0.04. Bought parts weigh 7.64 kg, so the aircraft weighs 13.8 kg empty. Each ColdCell pack (32 cells) weighs 3.34 kg and holds 307 Wh (92 Wh/kg); two weigh 6.68 kg and hold 614 Wh.

*Table 2. Take-off mass.*

| Case | Mass |
| --- | --- |
| Ready to fly, no payload | 20.5 kg |
| With 5 kg | 25.5 kg |
| With 2 kg | 22.5 kg |
| With the tether module (1.25 kg of tether hanging at 50 m) | 23.7 kg |
| Float release payload as fitted | 1.58 kg |
| Payload allowed inside 25 kg | 4.5 kg |

## B. Hover power

Hover power is the momentum-theory power for the total thrust over the eight rotor discs, raised by the coaxial factor and divided by the figure of merit and drive efficiency:

P = 1.28 x T^1.5 / sqrt(2 ρ A) / (0.65 x 0.80) + avionics and payload

with T the weight in newtons and A the area of all eight discs (3.65 m2).

*Table 3. Hover power.*

| Case | Power |
| --- | --- |
| Sea level, 5 kg | 3.30 kW |
| Sea level, no payload | 2.38 kW |
| 5,000 m and -20 °C, 2 kg | 3.51 kW |
| Sea level and +45 °C, 5 kg | 3.47 kW |
| Tethered at sea level | 2.97 kW |

Disc loading is 137 N/m2 on the four projected discs and the induced velocity 7.5 m/s.

## C. Hover time (R4)

*Table 4. Hover time with two LiFePO4 packs (614 Wh).*

| Case | Hover time |
| --- | --- |
| Sea level, 5 kg | 8.9 min |
| Sea level, no payload | 12.4 min |
| 5,000 m and -20 °C, 2 kg | 7.1 min |
| Sea level and +45 °C, 5 kg | 8.5 min |

**R4 is not met.** The packs hold 92 Wh/kg once the heater, BMS and shell are added, and a 25 kg aircraft needs about 3.3 kW to hover. Pack current in hover is 64 A, 16 A per cell (24 A in a climb), inside the 30 A cell rating.

*Table 5. Options examined for R4 and R1 (posed to Amish in `docs/REVIEW.md`).*

| Option | Take-off mass with 5 kg | Sea level, 5 kg | 5,000 m, 2 kg |
| --- | --- | --- | --- |
| As designed | 25.5 kg | 8.9 min | 7.1 min |
| Deeper pockets in the hinge blocks, root fittings and clamps (1.04 kg off) | 24.4 kg | 9.5 min | 7.7 min |
| Lithium-ion ColdCell variant, 14S3P 21700 high-power cells (2 x 680 Wh, 7.1 kg) | 25.9 kg | 19.3 min | 15.4 min |
| Lithium-ion variant and deeper pockets | 24.9 kg | 20.5 min | 16.5 min |
| LiFePO4 16S3P (9.6 kg): payload inside 25 kg falls to 1.7 kg | 28.4 kg | 13.8 min (1.7 kg) | 9.0 min |

The lithium-ion variant keeps the same 51 V class bus (14 cells in series), so motors, controllers and the Core are unchanged; each cell carries 11 A in hover against a 45 A rating.

## D. Thrust margin and motor out (R3, R5)

A coaxial pair gives 18 kg at full throttle at sea level (10 kg plus 80 % of 10 kg), and 61 % of that at 5,000 m and -20 °C.

- Thrust to weight: 2.83 at sea level with 5 kg; **1.94 at 5,000 m with 2 kg (R3 met on paper)**.
- One motor out: the failed arm keeps its partner (10 kg at sea level, 6.1 kg at 5,000 m). Because opposite arms must pull equally, the failed arm and the arm opposite it can each give the single-motor figure and the other two the pair figure. Thrust to weight with one motor out is **2.20 at sea level and 1.51 at 5,000 m (R5 met on paper)**. Yaw control after a motor loss is shown in the motor-cut test.
- One motor at full throttle draws about 1.8 kW, 38 A: inside the 80 A controller rating.

## E. Wind (R6)

At 10 m/s the drag is 18 N, so the aircraft leans 4.2 degrees and needs 0.3 % more thrust; a 15 m/s gust needs 9.4 degrees. Thrust is not the limit; holding position within 2 m depends on the autopilot tuning and is shown in flight.

## F. Arms, hinges and gear

At full throttle one arm lifts 177 N, 440 mm outboard of its pivot: 78 N m about the pivot.

*Table 6. Structure at full thrust (hover in brackets).*

| Item | Load | Stress or factor |
| --- | --- | --- |
| Stop bridge, 30 mm outboard of the pivot | 2.59 kN (0.92 kN) | Bending 41 MPa in 6061-T6 (yield 240 MPa); bearing 8.6 MPa |
| Pivot bolt, 8 mm, double shear | 2.77 kN | 27.5 MPa |
| Hinge cheeks, 7 mm, at the pivot | 2.77 kN | Bearing 24.7 MPa |
| Arm tube, 40 x 36 carbon, at the collar | 177 N at 340 mm | Bending 28 MPa; tip deflection 0.76 mm (0.27 mm) |
| Lock pin, 3 g landing, arm about 2.2 kg | 16.2 N m, 613 N | Shear 6.1 MPa |
| Gear strut, 3 g touchdown on one skid | 193 N | 2.2 MPa |

Every item is far inside its material's strength; the hinge proof load before first flight is 1.5 times the full-thrust moment, 117 N m. The aircraft tips over on a slope of 15 degrees along its short gear axis, with packs fitted.

## G. Tethered hover (R7)

The tether loop is 2.80 ohm. With 3.13 kW into the converter, 8.3 A flows, the tether drops 23 V and loses 193 W, and the ground supply gives 3.32 kW. The 4 kW converter runs at 74 % of its rating (margin 1.35), and the extra power for 10 m/s of wind is small. Two hours of tethered hover take 6.6 kWh from the ground supply. **R7 is met on paper**; the converter's and motors' temperatures over two hours are measured at TRL 4.

## H. Float drop (R8)

A float dropped from 10 m falls for 1.43 s and hits the water at 14 m/s. In 10 m/s wind it drifts about 3.3 m; aiming off for the drift leaves about 30 % of it. With the 2 m position hold of R6, the expected miss is **2.2 m (R8 met on paper)**. The downwash about 10 m below the aircraft is about 7.5 m/s (estimate), which sets the 10 m minimum drop height.

## I. Transport (R9)

The folded model measures 451 x 480 x 842 mm with the gear on, so it stands in a 1.2 x 0.6 x 0.5 m case on its skids. Folded, the motors are 32 mm above the ground and 17 mm clear of the skids, and the turned-back blades are 14 mm clear of the gear. Set-up takes about 9 min: four arms at 45 s, eight propellers at 9 s, two packs at 30 s, the payload 1 min, power-up 1.5 min and checks 1 min. **R9 is met on paper.**

In flight the rotor discs are clear of everything: lower discs 99 mm from the gear struts and 48 mm from the float, upper discs 58 mm from the packs and 47 mm from the deck in plan; tip to tip 115 mm.

## J. Temperature (R10)

Warming the cells of both packs by 30 K takes about 53 Wh from the ground supply before take-off. The motors, controllers, carbon and aluminium parts are rated from -20 to +45 °C; at +45 °C the hover power rises to 3.47 kW and the hover time falls to 8.5 min. **R10 is met on paper by part ratings.**

## K. Cost (R11)

Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 5,739 (USD 739 over the target). The payloads and the tether ground set add USD 3,716. The lithium-ion pack variant would add about USD 416.

## Results against requirements

*Table 7. Results.*

| ID | Requirement | Result | Status |
| --- | --- | --- | --- |
| R1 | Maximum take-off mass | 25.5 kg with a 5 kg payload; 20.5 kg ready to fly | **Not met** |
| R2 | Payload at sea level | 4.5 kg inside R1; thrust to weight 2.83 | **At risk** |
| R3 | Payload at altitude | Thrust to weight 1.94 at 5,000 m and -20 °C with 2 kg | Met on paper |
| R4 | Hover time | 8.9 min at sea level with 5 kg; 7.1 min at 5,000 m with 2 kg | **Not met** |
| R5 | Motor-out tolerance | Thrust to weight with one motor out 2.20 and 1.51 | Met on paper |
| R6 | Wind | 18 N drag, 4.2 deg tilt at 10 m/s | Met on paper (thrust) |
| R7 | Tethered endurance | 3.0 kW hover; converter margin 1.35 | Met on paper |
| R8 | Float and line drop | Expected miss 2.2 m | Met on paper |
| R9 | Transport | 0.84 x 0.48 x 0.45 m; about 9 min set-up | Met on paper |
| R10 | Operating temperature | Part ratings; 53 Wh pre-heat | Met on paper |
| R11 | Prototype cost | USD 5,739 | USD 739 over the value-engineering target |

> **Safety:** These figures size a 25 kg class aircraft with 30 inch propellers, lithium packs and a 400 V tether. They are estimates; the proof loads, bench thrust runs and tethered runs listed in the build plan (KWL-BLD-001) come before any flight.
