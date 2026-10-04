---
doc_id: KWL-CAL-001
title: Kitewright Lift sizing calculations
project: Kitewright Lift
doc_type: Calculation
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First sizing of the constructable design (KWL-DDR-002) against every requirement
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Round 2 decisions applied (KWL-DDR-003): pocketed fittings as modelled, ColdCell lithium-ion 14S3P packs at ColdCell's mass and size, larger deck, Core power leads in the harness; every section recalculated"
---

# Kitewright Lift sizing calculations

The constructable design, with Amish's round 2 decisions applied (KWL-DDR-003), lifts its payloads with ample thrust at sea level and at 5,000 m, survives the loss of any one motor on paper, folds into the R9 case and carries its loads with large margins. The ColdCell lithium-ion packs more than double the hover time: 18.9 min at sea level with 5 kg and 15.0 min at 5,000 m with 2 kg (was 8.9 and 7.1 min). The take-off mass, however, does not come down to the 24.9 kg the decisions were posed with: it is 26.3 kg with a 5 kg payload. The deeper pockets, modelled with the 4.5 mm walls the option set, save 0.41 kg, not the 1.04 kg estimated; ColdCell's own design of the variant weighs 3.84 kg a pack, not the 3.56 kg assumed; the longer packs need a larger deck (0.12 kg); and the Core's power leads (0.12 kg) now count here. R1 is not met, R2 is at risk (3.7 kg of payload inside 25 kg), R4 is met at altitude but 1.1 min short at sea level, and R10 is at risk in hot weather. These are posed to Amish as new questions in the design decisions register.

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
| Pack | ColdCell lithium-ion variant, 14S3P of 21700 cells (4.5 Ah, 70 g, 45 A); 3.84 kg and 680 Wh a pack; 378 x 90 x 86 mm | ColdCell CCL-CAL-001 section K and CCL-DWG-002 (CCL-DDR-003) |
| Energy used per flight | 80 % of nominal; 85 % of that at -20 °C | 20 % kept to land; ColdCell R1 |
| Drag area, side on | 0.30 m2 | Hub, packs, gear and payload (estimate) |
| Bought masses | Motors 450 g, controllers 110 g, propellers 110 g, Core 1.0 kg, wiring 0.77 kg (0.65 kg plus the Core's four 8 AWG leads with AS150 plugs, 0.12 kg), fasteners and epoxy 0.25 kg | Class figures; Core R9 and KWC-DDR-003 |
| Tether | 400 V DC fixed, 60 m, 2 x 0.75 mm2 copper, 25 g/m, 50 m highest hover; converter 95 %, 4 kW | KWL-DDR-001, item 5 |
| Float | 0.85 kg, 0.12 x 0.42 m, drag coefficient 0.9 | Foam float with line bag |

## A. Mass

Made parts from the model weigh 5.86 kg: root fittings 1.02, hinge blocks 0.95, motor clamps 0.87, arm tubes 0.61, hub plates 0.69, deck 0.58, gear 0.88, pivot bolts 0.13, guides 0.09, spacers 0.04. The deeper pockets of decision 1 take 0.41 kg off the fittings (hinge blocks 0.20, root fittings 0.13, clamps 0.08 kg); the deck and guides for the long packs add 0.12 kg. Bought parts weigh 7.76 kg, so the aircraft weighs 13.6 kg empty. Each ColdCell lithium-ion pack (42 cells) weighs 3.84 kg and holds 680 Wh (177 Wh/kg); two weigh 7.69 kg and hold 1,361 Wh.

*Table 2. Take-off mass.*

| Case | Mass |
| --- | --- |
| Ready to fly, no payload | 21.3 kg |
| With 5 kg | 26.3 kg |
| With 2 kg | 23.3 kg |
| Payload allowed inside 25 kg | 3.7 kg |

## B. Hover power

Hover power is the momentum-theory power for the total thrust over the eight rotor discs, raised by the coaxial factor and divided by the figure of merit and drive efficiency:

P = 1.28 x T^1.5 / sqrt(2 ρ A) / (0.65 x 0.80) + avionics and payload

with T the weight in newtons and A the area of all eight discs (3.65 m2).

*Table 3. Hover power.*

| Case | Power |
| --- | --- |
| Sea level, 5 kg | 3.46 kW |
| Sea level, no payload | 2.52 kW |
| 5,000 m and -20 °C, 2 kg | 3.70 kW |
| Sea level and +45 °C, 5 kg | 3.64 kW |
| Tethered at sea level | 3.13 kW |

Disc loading is 141 N/m2 on the four projected discs and the induced velocity 7.6 m/s.

## C. Hover time (R4)

*Table 4. Hover time with two ColdCell lithium-ion packs (1,361 Wh).*

| Case | Hover time |
| --- | --- |
| Sea level, 5 kg | 18.9 min |
| Sea level, no payload | 25.9 min |
| 5,000 m and -20 °C, 2 kg | 15.0 min |
| Sea level and +45 °C, 5 kg | 18.0 min |
| Sea level at the 3.7 kg payload R1 allows | 20.3 min |

**R4 is met at 5,000 m (15.0 min against 10 min) and missed by 1.1 min at sea level with 5 kg.** Pack current in hover is 69 A, 11.5 A per cell (17.2 A in a climb), against the 45 A cell rating.

*Table 5. What the round 2 decisions did, as modelled (KWL-DDR-003).*

| Design | Take-off mass with 5 kg | Payload inside 25 kg | Sea level, 5 kg | 5,000 m, 2 kg |
| --- | --- | --- | --- | --- |
| KWL-CAL-001 v0.1: LiFePO4 packs, fittings as first drawn | 25.5 kg | 4.5 kg | 8.9 min | 7.1 min |
| Decision 1 A only, pockets as modelled (0.41 kg off), LiFePO4 | 25.1 kg | 5.0 kg | 9.2 min | 7.3 min |
| Both decisions, with the 3.56 kg pack Lift assumed | 25.7 kg | 4.3 kg | 19.5 min | 15.5 min |
| Both decisions as now designed (ColdCell 3.84 kg packs) | 26.3 kg | 3.7 kg | 18.9 min | 15.0 min |
| As posed to Amish (pockets 1.04 kg off, 3.56 kg packs, Core leads in the Core) | 24.9 kg | 5.1 kg | 20.5 min | 16.5 min |

The last row is the estimate the decisions were taken on. The difference is 1.4 kg: 0.63 kg because the pockets, drawn with 4.5 mm walls and webs, save 0.41 kg rather than 1.04 kg; 0.57 kg from ColdCell's heavier pack; 0.12 kg for the larger deck and guides; and 0.12 kg of Core leads now carried in Lift's harness (the Core allowance stays 1.0 kg). The 14S bus is unchanged in class, so motors and controllers stay as specified.

## D. Thrust margin and motor out (R3, R5)

A coaxial pair gives 18 kg at full throttle at sea level (10 kg plus 80 % of 10 kg), and 61 % of that at 5,000 m and -20 °C.

- Thrust to weight: 2.74 at sea level with 5 kg; **1.87 at 5,000 m with 2 kg (R3 met on paper)**.
- One motor out: the failed arm keeps its partner (10 kg at sea level, 6.1 kg at 5,000 m). Because opposite arms must pull equally, the failed arm and the arm opposite it can each give the single-motor figure and the other two the pair figure. Thrust to weight with one motor out is **2.13 at sea level and 1.46 at 5,000 m (R5 met on paper)**. Yaw control after a motor loss is shown in the motor-cut test.
- One motor at full throttle draws about 1.8 kW, 38 A at a sagging 14S pack: inside the 80 A controller rating.

## E. Wind (R6)

At 10 m/s the drag is 18 N, so the aircraft leans 4.1 degrees and needs 0.3 % more thrust; a 15 m/s gust needs 9.1 degrees. Thrust is not the limit; holding position within 2 m depends on the autopilot tuning and is shown in flight.

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
| Gear strut, 3 g touchdown on one skid | 199 N | 2.3 MPa |

Every item is far inside its material's strength; the hinge proof load before first flight is 1.5 times the full-thrust moment, 117 N m. The deeper pockets leave the stop bridge, the pivot and lock-pin bosses and the 7 mm cheek at the pivot untouched (4.5 mm of metal kept round each), so the figures above are unchanged; the thinner cheek beside the pockets (4.5 mm) and the pocketed tongue are first-order only and are covered by the hinge proof load at TRL 4. The aircraft tips over on a slope of 15 degrees along its short gear axis, with packs fitted.

## G. Tethered hover (R7)

The tether loop is 2.80 ohm. With 3.29 kW into the converter, 8.8 A flows, the tether drops 25 V and loses 215 W, and the ground supply gives 3.51 kW. The 4 kW converter runs at 78 % of its rating (margin 1.28), and the extra power for 10 m/s of wind is small. Two hours of tethered hover take 7.0 kWh from the ground supply. **R7 is met on paper**; the converter's and motors' temperatures over two hours are measured at TRL 4.

## H. Float drop (R8)

A float dropped from 10 m falls for 1.43 s and hits the water at 14 m/s. In 10 m/s wind it drifts about 3.3 m; aiming off for the drift leaves about 30 % of it. With the 2 m position hold of R6, the expected miss is **2.2 m (R8 met on paper)**. The downwash about 10 m below the aircraft is about 7.6 m/s (estimate), which sets the 10 m minimum drop height.

## I. Transport (R9)

The folded model measures 451 x 480 x 842 mm with the gear on, so it stands in a 1.2 x 0.6 x 0.5 m case on its skids. Folded, the motors are 32 mm above the ground and 17 mm clear of the skids, and the turned-back blades are 14 mm clear of the gear. Set-up takes about 9 min: four arms at 45 s, eight propellers at 9 s, two packs at 30 s, the payload 1 min, power-up 1.5 min and checks 1 min. **R9 is met on paper.**

In flight the rotor discs are clear of everything: lower discs 99 mm from the gear struts and 48 mm from the float, upper discs 35 mm from the longer packs and 19 mm from the larger deck (was 58 and 47 mm); tip to tip 115 mm.

## J. Temperature (R10)

Pre-heating both lithium-ion packs from -20 °C takes about 71 Wh from the ground supply before take-off (ColdCell CCL-CAL-001 K, 35.6 Wh a pack on two 100 W films; a 24 V 20 A supply heats both at once). The motors, controllers, carbon and aluminium parts are rated from -20 to +45 °C; at +45 °C the hover power rises to 3.64 kW and the hover time falls to 18.0 min. **R10 is at risk in hot weather:** ColdCell finds that its lithium-ion pack, jacket on, makes 71 W of heat in a Lift hover and stays under 50 °C for 20 minutes only up to 25 °C ambient; at 45 °C the cells would pass the 60 °C discharge limit of typical high-power cells (ColdCell open decision 6).

## K. Cost (R11)

Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 6,418 (USD 1,418 over the target); before the round 2 decisions USD 5,739. The change is USD 679: the two lithium-ion packs USD 484 (USD 662 each against USD 420 for LiFePO4), the deeper pockets USD 120, the Core's leads and plugs USD 60 (moved from the Kitewright Core) and the larger deck USD 15. The payloads and the tether ground set add USD 3,716, unchanged.

## Results against requirements

*Table 7. Results.*

| ID | Requirement | Result | Status |
| --- | --- | --- | --- |
| R1 | Maximum take-off mass | 26.3 kg with a 5 kg payload; 21.3 kg ready to fly | **Not met** (new question) |
| R2 | Payload at sea level | 3.7 kg inside R1; thrust to weight 2.74 | **At risk** |
| R3 | Payload at altitude | Thrust to weight 1.87 at 5,000 m and -20 °C with 2 kg | Met on paper |
| R4 | Hover time | 18.9 min at sea level with 5 kg; 15.0 min at 5,000 m with 2 kg | **Not met** at sea level by 1.1 min; met at altitude |
| R5 | Motor-out tolerance | Thrust to weight with one motor out 2.13 and 1.46 | Met on paper |
| R6 | Wind | 18 N drag, 4.1 deg tilt at 10 m/s | Met on paper (thrust) |
| R7 | Tethered endurance | 3.1 kW hover; converter margin 1.28 | Met on paper |
| R8 | Float and line drop | Expected miss 2.2 m | Met on paper |
| R9 | Transport | 0.84 x 0.48 x 0.45 m; about 9 min set-up | Met on paper |
| R10 | Operating temperature | 71 Wh pre-heat; packs stay under 50 °C only to 25 °C ambient | **At risk** (ColdCell open decision 6) |
| R11 | Prototype cost | USD 6,418 | USD 1,418 over the value-engineering target |

> **Safety:** These figures size a 25 kg class aircraft with 30 inch propellers, two 680 Wh lithium-ion packs and a 400 V tether. They are estimates; the proof loads, bench thrust runs and tethered runs listed in the build plan (KWL-BLD-001) come before any flight.
