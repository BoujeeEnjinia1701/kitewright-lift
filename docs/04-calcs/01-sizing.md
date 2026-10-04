---
doc_id: KWL-CAL-001
title: Kitewright Lift sizing calculations
project: Kitewright Lift
doc_type: Calculation
version: "0.3"
status: Draft
date: '2026-10-04'
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
  change: Amish's decisions 34A and 35A (KWL-DDR-003); lightened fittings from the model, lithium-ion ColdCell packs, frame-to-Core power leads and a 0.99 kg Core (Core decision 33B); new results for R1, R2, R3, R4, R5, R7, R10 and R11
- version: "0.3"
  date: '2026-10-04'
  author: Amish Chadha
  change: Amish's round-3 decisions 8A, 9A and 10A (KWL-DDR-004); ColdCell's packs as drawn (4.46 kg, 410 x 94 x 94 mm) on a re-sized, raised deck; the Kitewright Core to the family envelope with payload shoes; rated payload and R1, R2 as restated; deck check added; every section re-run
---

# Kitewright Lift sizing calculations

This version carries out Amish's round-3 decisions of 2026-10-04 (KWL-DDR-004): "For round 3, I agree with all your proposed recommendations". ColdCell's lithium-ion pack as drawn (410 x 94 x 94 mm, 4.46 kg, 680 Wh) is Lift's pack (8A); the aircraft keeps the 25 kg take-off limit (the US 55 lb class) and is rated for the payload that fits; ColdCell's 50 °C warning sets a warm-weather limit (9A); and the Kitewright Core hangs under the hub to the family envelope with AS150 plugs everywhere (10A). With two of these packs on a re-sized, raised 2 mm deck the aircraft weighs 21.8 kg ready to fly, so the rated payload is **3.2 kg** at 25.0 kg take-off mass; the float release (1.46 kg) and the tether module (3.13 kg) both fit. Every requirement is met on paper as restated; R11 is reported against its value-engineering target.

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
| Pack | ColdCell 14S3P lithium-ion pack as drawn: 21700 high-power cells, 4.5 Ah, 3.6 V, 45 A; 680 Wh, 410 x 94 x 94 mm, 4.46 kg with heater, insulation, BMS, shell and AS150 lead (v0.2 assumed 3.56 kg in 126 x 232 x 85 mm; the LiFePO4 16S2P pack of v0.1 kept for comparison: 26650 cells, 3.0 Ah, 85 g, 30 A) | Decision 8A; CCL-DWG-002 and CCL-CAL-001 K |
| Take-off limit and rated payload | 25 kg (the US 55 lb class); the rated payload is the largest 0.1 kg step that fits | R1 and R2 as restated (KWL-REQ-001 v0.4) |
| Energy used per flight | 80 % of nominal; 85 % of that at -20 °C | 20 % kept to land; ColdCell R1, assumed to hold for the lithium-ion variant with its heater running |
| Drag area, side on | 0.30 m2 | Hub, packs, gear and payload (estimate) |
| Bought masses | Motors 450 g, controllers 110 g, propellers 110 g, Core 0.99 kg with its rail and pins, wiring 0.65 kg plus 0.12 kg of frame-to-Core leads and 0.03 kg of antenna extension leads, fasteners and epoxy 0.25 kg | Class figures; Core R9, Core decision 33B; Kitewright interface table |
| Tether | 400 V DC fixed, 60 m, 2 x 0.75 mm2 copper, 25 g/m, 50 m highest hover; converter 95 %, 4 kW | KWL-DDR-001, item 5 |
| Float | 0.85 kg, 0.12 x 0.42 m, drag coefficient 0.9 | Foam float with line bag |

## A. Mass

Made parts from the model weigh 5.08 kg: hinge blocks 0.77, root fittings 0.94, motor clamps 0.76, arm tubes 0.60, hub plates 0.58 (the bottom plate is 0.11 kg lighter for the Core's 200 x 112 mm opening), deck 0.28, gear 0.88, pivots 0.13, guides 0.08, spacers 0.06. Bought parts weigh 7.78 kg, so the aircraft weighs 12.9 kg empty. Each ColdCell pack holds 680 Wh in 4.46 kg (153 Wh/kg); two weigh 8.92 kg, 1.80 kg more than the 3.56 kg packs v0.2 assumed.

*Table 2. Where the mass moved (decisions 8A and 10A), against v0.2.*

| Change | Mass |
| --- | --- |
| Two ColdCell packs as drawn, 4.46 kg each (3.56 kg assumed) | +1.80 kg |
| Deck re-sized to 430 x 280 mm, made 2 mm (was 330 x 290 x 3 mm), with four 120 x 60 mm windows | -0.16 kg |
| Pack guides of 15 x 15 x 1.5 mm angle, 340 mm (were 20 x 20 x 2, 250 mm) | -0.02 kg |
| Bottom hub plate: Core opening in place of the damper, rail and socket holes | -0.11 kg |
| Deck standoffs 60 mm (were 25), antenna extension leads | +0.04 kg |
| Ready to fly | 20.23 to 21.78 kg (+1.55 kg) |

*Table 3. Take-off mass and payloads.*

| Case | Mass |
| --- | --- |
| Ready to fly, no payload | 21.78 kg |
| Payload allowance inside 25 kg | 3.22 kg |
| Rated payload (R2 as restated) | 3.2 kg, 24.98 kg take-off |
| Float release payload, on its own payload shoe | 1.46 kg (23.24 kg take-off) |
| Tether module, with 1.25 kg of tether hanging at 50 m | 3.13 kg (24.91 kg take-off) |
| With 2 kg (R3 and R4 at altitude) | 23.78 kg |
| With 5 kg (the v0.2 rating, for comparison) | 26.78 kg, over R1 |

**R1 and R2 are met on paper as restated.** The payload modules weigh less than in v0.2 (1.58 and 3.25 kg) because each now hangs from a 184 x 128 x 5 mm payload shoe to the Core's KWC-DWG-106 in place of the 240 x 124 x 6 mm plate with its lug. The tether module's margin is 0.07 kg, so the TRL 4 weigh-in decides it.

## B. Hover power

Hover power is the momentum-theory power for the total thrust over the eight rotor discs, raised by the coaxial factor and divided by the figure of merit and drive efficiency:

P = 1.28 x T^1.5 / sqrt(2 ρ A) / (0.65 x 0.80) + avionics and payload

with T the weight in newtons and A the area of all eight discs (3.65 m2).

*Table 4. Hover power.*

| Case | Power |
| --- | --- |
| Sea level, rated payload (25.0 kg) | 3.21 kW |
| Sea level, no payload | 2.61 kW |
| 5,000 m and -20 °C, 2 kg | 3.82 kW |
| Sea level and +45 °C, rated payload | 3.37 kW |
| Tethered at sea level | 3.20 kW |

Disc loading is 134 N/m2 on the four projected discs and the induced velocity 7.4 m/s.

## C. Hover time (R4)

*Table 5. Hover time with two ColdCell packs (1,361 Wh).*

| Case | Hover time |
| --- | --- |
| Sea level, rated payload (25.0 kg) | 20.4 min |
| Sea level, float release | 22.6 min |
| Sea level, no payload | 25.1 min |
| 5,000 m and -20 °C, 2 kg | 14.5 min |
| Sea level and +45 °C, rated payload | 19.4 min of energy; ColdCell's warning limits it (section J) |

**R4 is met on paper** with the rated payload: 20.4 min against 20 min at sea level, and 14.5 min against 10 min at 5,000 m with 2 kg. A 5 kg payload no longer fits inside R1, so R4's sea-level case is read at the rated payload. The pack draws 64 A in hover, 10.6 A per cell (15.9 A in a climb), well inside the 45 A cell rating.

## D. Thrust margin and motor out (R3, R5)

A coaxial pair gives 18 kg at full throttle at sea level (10 kg plus 80 % of 10 kg), and 61 % of that at 5,000 m and -20 °C.

- Thrust to weight: 2.88 at sea level with the rated payload; **1.84 at 5,000 m with 2 kg (R3 met on paper)**.
- One motor out: the failed arm keeps its partner. Thrust to weight with one motor out is **2.24 at sea level and 1.43 at 5,000 m (R5 met on paper)**. Yaw control after a motor loss is shown in the motor-cut test.
- One motor at full throttle draws about 1.8 kW, 38 A: inside the 80 A controller rating.

## E. Wind (R6)

At 10 m/s the drag is 18 N, so the aircraft leans 4.3 degrees and needs 0.3 % more thrust; a 15 m/s gust needs 9.6 degrees. Holding position within 2 m depends on the autopilot tuning and is shown in flight.

## F. Arms, hinges, deck and gear

At full throttle one arm lifts 177 N, 440 mm outboard of its pivot: 78 N m about the pivot.

*Table 6. Structure at full thrust (hover in brackets), and the deck at a 3 g landing.*

| Item | Load | Stress or factor |
| --- | --- | --- |
| Stop bridge, 30 mm outboard of the pivot | 2.59 kN (0.90 kN) | Bending 41 MPa in 6061-T6 (yield 240 MPa); bearing 8.6 MPa |
| Pivot bolt, 8 mm, double shear | 2.77 kN | 27.5 MPa |
| Hinge cheeks, 7 mm, at the pivot | 2.77 kN | Bearing 24.7 MPa |
| Arm tube, 40 x 36 carbon, at the collar | 177 N at 340 mm | Bending 28 MPa; tip deflection 0.76 mm (0.27 mm) |
| Lock pin, 3 g landing, arm about 2.2 kg | 16.2 N m, 613 N | Shear 6.1 MPa |
| Hinge block cheeks at the window | 81 N m | Bending 18 MPa |
| Hinge block top rail under the bridge | 1.30 kN per cheek | Bending 35 MPa; shear 12 MPa |
| Root fitting tongue, web and window | 39 and 71 N m | Bending 6 and 8 MPa |
| Battery deck, 2 mm carbon, both packs at 3 g on the two standoffs at X = 130 mm (decision 8A) | 3.6 N m at mid-span | 19 MPa at mid-span, 27 MPa through the windows; overhang tip 0.27 mm |
| Gear strut, 3 g touchdown on one skid | 189 N | 2.2 MPa |

Every item is far inside its material's strength; the carbon deck runs at about a tenth of a 250 MPa allowable. The hinge proof load before first flight is 1.5 times the full-thrust moment, 117 N m. With the heavier packs on the raised deck the aircraft tips over on a slope of 14.5 degrees along its short gear axis (15.3 in v0.2).

## G. Tethered hover (R7)

The tether loop is 2.80 ohm. At 24.9 kg the aircraft needs 3.20 kW; 9.0 A flows, the tether drops 25 V and loses 225 W, and the ground supply gives 3.59 kW. The 4 kW converter runs at 80 % of its rating (margin 1.25, above the 1.2 the design keeps). Two hours of tethered hover take 7.2 kWh from the ground supply. **R7 is met on paper**; the converter's and motors' temperatures over two hours are measured at TRL 4.

## H. Float drop (R8)

A float dropped from 10 m falls for 1.43 s and hits the water at 14 m/s. In 10 m/s wind it drifts about 3.3 m; aiming off for the drift leaves about 30 % of it. With the 2 m position hold of R6, the expected miss is **2.2 m (R8 met on paper)**. The downwash about 10 m below the aircraft is about 7.4 m/s (estimate).

## I. Transport and clearances (R9)

The folded model measures 451 x 480 x 876 mm with the gear on (the GNSS mast is 34 mm taller on the raised deck), so it stands in a 1.2 x 0.6 x 0.5 m case on its skids. Folded, the motors are 32 mm above the ground and 17 mm clear of the skids. Set-up takes about 9 min. **R9 is met on paper.**

The deck now stands on 60 mm standoffs so that its underside is 9 mm above the upper blades, and in plan the deck's corner cuts stay 12.7 mm and the pack corners 22.7 mm outside the upper discs, so neither reaches into the rotor path. Lower discs are 99 mm from the gear struts and 54 mm from the float; tip to tip 115 mm. The Core's lid stands up through the bottom plate into the hub; its mast boss, SMA bulkheads and switch reach holes in the top plate, and the boss top is 57 mm below the deck.

## J. Temperature (R10)

Warming the 5.9 kg of cells in both packs by 30 K takes about 58 Wh from the ground supply before take-off; ColdCell blocks charging below 5 °C. The motors, controllers, carbon and aluminium parts are rated from -20 to +45 °C. ColdCell keeps its 50 °C firmware warning for this pack until a TRL 4 measurement supports relaxing it (decision 9A): a full hover flight stays under it up to about 27 °C ambient, and at +45 °C the warning comes after about 6 min of hover (CCL-CAL-001 K). **R10 is met on paper by part ratings, with full-length hover flights limited to about 27 °C ambient;** hotter days mean shorter flights.

## K. Cost (R11)

Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 6,627 (USD 1,627 over the target). Against v0.2 (USD 6,335) ColdCell's packs cost USD 268 more (USD 762 each, against USD 628 assumed), the larger 2 mm deck USD 5, longer straps USD 4 and the antenna extension leads USD 15. The payloads and ground equipment, now with ColdCell's pre-heat supply, charger and fire-resistant charging box (USD 255), add USD 3,976.

## Results against requirements

*Table 7. Results.*

| ID | Requirement | Result | Status |
| --- | --- | --- | --- |
| R1 | Maximum take-off mass, 25 kg including the rated payload | 24.98 kg with 3.2 kg; 21.78 kg ready to fly | Met on paper as restated |
| R2 | Rated payload at sea level, 3.2 kg; both designed payloads fit | Float release 1.46 kg, tether module 3.13 kg; thrust to weight 2.88 | Met on paper as restated |
| R3 | Payload at altitude | Thrust to weight 1.84 at 5,000 m and -20 °C with 2 kg | Met on paper |
| R4 | Hover time | 20.4 min at sea level with the rated payload; 14.5 min at 5,000 m with 2 kg | Met on paper at the rated payload |
| R5 | Motor-out tolerance | Thrust to weight with one motor out 2.24 and 1.43 | Met on paper |
| R6 | Wind | 18 N drag, 4.3 deg tilt at 10 m/s | Met on paper (thrust) |
| R7 | Tethered endurance | 3.2 kW hover; converter margin 1.25 | Met on paper |
| R8 | Float and line drop | Expected miss 2.2 m | Met on paper |
| R9 | Transport | 0.88 x 0.48 x 0.45 m; about 9 min set-up | Met on paper |
| R10 | Operating temperature | Part ratings; 58 Wh pre-heat; full hover flights to about 27 °C ambient | Met on paper, warm-weather limit stated |
| R11 | Prototype cost | USD 6,627 | USD 1,627 over the value-engineering target |

> **Safety:** These figures size a 25 kg class aircraft with 30 inch propellers, 1.36 kWh of lithium-ion cells and a 400 V tether. ColdCell's charge blocking below 5 °C, heater cut-outs, cell fuses, fire-resistant charging box and 50 °C warning apply in full. They are estimates; the proof loads, bench thrust runs and tethered runs listed in the build plan (KWL-BLD-001) come before any flight.
