---
doc_id: KWL-REQ-001
title: Kitewright Lift requirements
project: Kitewright Lift
doc_type: Requirements
version: "0.5"
status: Draft
date: '2026-10-04'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Status of each requirement against KWL-CAL-001 for the constructable design; R11 stated as a value-engineering target
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: Status after Amish's decisions 34A and 35A (KWL-DDR-003) against KWL-CAL-001 v0.2; R4 now met on paper; R1 and R2 still short and posed again; targets unchanged
- version: "0.4"
  date: '2026-10-04'
  author: Amish Chadha
  change: R1 and R2 restated under Amish's round-3 decision 8A (KWL-DDR-004); status of every requirement from KWL-CAL-001 v0.3 with ColdCell's packs as drawn, the Kitewright interface table and ColdCell's warm-weather limit (9A); open decision 3 closed
- version: "0.5"
  date: '2026-10-04'
  author: Amish Chadha
  change: R4's sea-level case restated to the rated payload, a consequence of Amish's round-3 decision 8A (KWL-DDR-005); open decision 4 closed
---

# Kitewright Lift requirements

Requirements for the first prototype, with the status of each against the TRL 3 calculations (KWL-CAL-001 v0.3). On 2026-10-04 Amish decided the Kitewright family reconciliation as recommended: "For round 3, I agree with all your proposed recommendations" (KWL-DDR-004). ColdCell's lithium-ion pack as drawn (410 x 94 x 94 mm, 4.46 kg) is Lift's pack; Lift keeps its 25 kg take-off limit (the US 55 lb class) and rates its payload at what fits, so **R1 and R2 are restated** below. The earlier decisions of 2026-10-03 (lighter fittings, lithium-ion packs; KWL-DDR-003) stand. "Met on paper" means the calculation shows the target is reachable; every requirement is verified by test at TRL 4 or later.

**R4 restated, 2026-10-04.** Amish Chadha, 2026-10-04: "For round 3, I agree with all your proposed recommendations". Because decision 8A rates the payload at what fits inside R1's 25 kg (about 3.3 kg), R4's sea-level case now reads "with the rated payload" in place of "with 5 kg" (open decision 4, option A; KWL-DDR-005). The design does not change.

Table 1. Requirements

| ID | Requirement | Target | Verification (TRL 3 or later) | Status at TRL 3 (KWL-CAL-001) |
| --- | --- | --- | --- | --- |
| R1 | Maximum take-off mass | 25 kg or less including the rated payload (the US 55 lb class); restated 2026-10-04, decision 8A | Weigh the fully loaded aircraft | Met on paper: 24.98 kg with the rated 3.2 kg; 21.78 kg ready to fly with two ColdCell packs of 4.46 kg |
| R2 | Payload at sea level | Rated at the payload that fits inside R1, about 3.3 kg (target); both designed payloads, the float release (about 1.6 kg) and the tether module (about 3.3 kg), must fit; restated 2026-10-04, decision 8A | Weigh each payload module; hover test with calibrated mass | Met on paper: rated payload 3.2 kg; float release 1.46 kg and tether module 3.13 kg on their payload shoes both fit; thrust to weight 2.88 |
| R3 | Payload at altitude | 2 kg at air density equivalent to 5,000 m (target) | AltiRig thrust data, then flight at a high site | Met on paper: thrust to weight 1.84 at 5,000 m and -20 C with 2 kg |
| R4 | Hover time | At least 20 min with the rated payload (R2) at sea level and 10 min with 2 kg at 5,000 m and -20 °C (targets); sea-level case restated 2026-10-04 as a consequence of decision 8A (was "with 5 kg") | Timed hover flights with logged energy use | Met on paper: 20.4 min at sea level with the rated 3.2 kg (25.0 kg) and 14.5 min at 5,000 m and -20 °C with 2 kg |
| R5 | Motor-out tolerance | Controlled descent and landing after one motor failure at rated payload | Deliberate motor cut test over a safe area | Met on paper: thrust to weight with one motor out 2.24 at sea level, 1.43 at 5,000 m; yaw control to be shown in the motor-cut test |
| R6 | Wind | Holds position within 2 m in 10 m/s steady wind (target) | Logged position hold on a windy test day | Met on paper for thrust: 18 N drag, 4.3 deg tilt; position hold depends on tuning and is shown in flight |
| R7 | Tethered endurance | At least 2 h continuous hover on fixed-voltage tether power (target) | Tethered endurance run with logged voltages and temperatures | Met on paper: 3.2 kW hover on a 4 kW converter (margin 1.25); converter and motor temperatures over 2 h to be measured |
| R8 | Float and line drop | Places a float within 3 m of a target from 10 m height (target) | Drop trials over water | Met on paper: expected miss 2.2 m in 10 m/s wind when the drift is aimed off |
| R9 | Transport | Folds to fit a case of 1.2 m by 0.6 m by 0.5 m or smaller; set up in 10 min or less (target) | Pack and timed set-up trials | Met on paper: folded 0.88 x 0.48 x 0.45 m with the gear on; set-up about 9 min |
| R10 | Operating temperature | Flies from -20 to +45 °C with ColdCell packs (target) | Cold soak then hover test | Met on paper by part ratings; pre-heat about 58 Wh from the ground supply; charging blocked below 5 °C. ColdCell's 50 °C warning (decision 9A) allows a full hover flight up to about 27 °C ambient; at +45 °C the warning comes after about 6 min, so hot days mean short flights |
| R11 | Prototype cost | USD 5,000 or less excluding payloads | Bill of materials and receipts | Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 6,627 (USD 1,627 over the target) |

## Assumptions

- Air at 5,000 m and -20 °C: 54.0 kPa and 0.743 kg/m3 (71 % of the pressure and 61 % of the density at sea level).
- Motor and propeller performance from makers' figures for the 30 inch, 100 KV class, until AltiRig measures it at 5,000 m density.
- ColdCell's lithium-ion pack for Lift (14S3P, 21700 high-power cells, 680 Wh, 410 x 94 x 94 mm and 4.46 kg, CCL-DWG-002) delivers 85 % of its rated energy at -20 °C with its heater running (ColdCell R1).
- The Kitewright Core weighs 0.99 kg with its rail and pins (Core R9) and hangs under the hub to the Kitewright interface table of 2026-10-04; Lift supplies the AS150 power harness between its packs, the Core and its arms.
- Amish, 2026-10-04 (decision 8A): "For round 3, I agree with all your proposed recommendations".
- Local rules at the test sites allow external loads and tethered flight with permission.

## Safety

> **Safety:** The requirements describe a 25 kg class aircraft with large propellers, lithium-ion packs, a 400 V tether and suspended loads. R5 (motor out) and R7 (tether) are tested only over cleared ground with the keep-out and isolation set out in the build plan's safety stops (KWL-BLD-001, section 6).
