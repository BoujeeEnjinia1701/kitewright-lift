---
doc_id: KWL-REQ-001
title: Kitewright Lift requirements
project: Kitewright Lift
doc_type: Requirements
version: "0.3"
status: Draft
date: '2026-10-03'
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
  change: Status after the round 2 decisions (KWL-DDR-003) against KWL-CAL-001 v0.2; targets unchanged
---

# Kitewright Lift requirements

Requirements for the first prototype, with the status of each against the TRL 3 calculations (KWL-CAL-001 v0.2) for the constructable design (KWL-DDR-002) as changed by Amish's round 2 decisions (KWL-DDR-003). Targets are as set at TRL 1; none has been changed. "Met on paper" means the calculation shows the target is reachable; every requirement is verified by test at TRL 4 or later. Requirements not met or at risk are posed to Amish in `docs/REVIEW.md` and listed in the design decisions register (`docs/06-design-decisions.md`).

Table 1. Requirements

| ID | Requirement | Target | Verification (TRL 3 or later) | Status at TRL 3 (KWL-CAL-001) |
| --- | --- | --- | --- | --- |
| R1 | Maximum take-off mass | 25 kg or less including payload | Weigh the fully loaded aircraft | Not met with a 5 kg payload: 26.3 kg (was 25.5 kg). Ready to fly 21.3 kg. New open decision 3 |
| R2 | Payload at sea level | 5 kg on the core mount (target) | Hover test with calibrated mass | At risk: thrust is ample (thrust to weight 2.74) but R1 leaves 3.7 kg. New open decision 3 |
| R3 | Payload at altitude | 2 kg at air density equivalent to 5,000 m (target) | AltiRig thrust data, then flight at a high site | Met on paper: thrust to weight 1.87 at 5,000 m and -20 C with 2 kg |
| R4 | Hover time | At least 20 min with 5 kg at sea level and 10 min with 2 kg at 5,000 m and -20 °C (targets) | Timed hover flights with logged energy use | With the lithium-ion ColdCell packs: met at 5,000 m (15.0 min); not met at sea level with 5 kg, 18.9 min (was 8.9 and 7.1 min). New open decision 3 |
| R5 | Motor-out tolerance | Controlled descent and landing after one motor failure at rated payload | Deliberate motor cut test over a safe area | Met on paper: thrust to weight with one motor out 2.13 at sea level, 1.46 at 5,000 m; yaw control to be shown in the motor-cut test |
| R6 | Wind | Holds position within 2 m in 10 m/s steady wind (target) | Logged position hold on a windy test day | Met on paper for thrust: 18 N drag, 4.1 deg tilt; position hold depends on tuning and is shown in flight |
| R7 | Tethered endurance | At least 2 h continuous hover on fixed-voltage tether power (target) | Tethered endurance run with logged voltages and temperatures | Met on paper: 3.1 kW hover on a 4 kW converter (margin 1.28); converter and motor temperatures over 2 h to be measured |
| R8 | Float and line drop | Places a float within 3 m of a target from 10 m height (target) | Drop trials over water | Met on paper: expected miss 2.2 m in 10 m/s wind when the drift is aimed off |
| R9 | Transport | Folds to fit a case of 1.2 m by 0.6 m by 0.5 m or smaller; set up in 10 min or less (target) | Pack and timed set-up trials | Met on paper: folded 0.84 x 0.48 x 0.45 m with the gear on; set-up about 9 min |
| R10 | Operating temperature | Flies from -20 to +45 °C with ColdCell packs (target) | Cold soak then hover test | At risk: cold side met on paper (pre-heat about 71 Wh); the lithium-ion packs stay under 50 °C in a 20 min hover only up to 25 °C ambient with their jackets on (ColdCell open decision 6; new open decision 4) |
| R11 | Prototype cost | USD 5,000 or less excluding payloads | Bill of materials and receipts | Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 6,418 (USD 1,418 over the target) |

## Assumptions

- Air at 5,000 m and -20 °C: 54.0 kPa and 0.743 kg/m3 (71 % of the pressure and 61 % of the density at sea level).
- Motor and propeller performance from makers' figures for the 30 inch, 100 KV class, until AltiRig measures it at 5,000 m density.
- ColdCell delivers 85 % of its rated energy at -20 °C with its heater running (ColdCell R1). The packs are ColdCell's lithium-ion 14S3P variant, 3.84 kg and 680 Wh each (CCL-DDR-003).
- The Kitewright Core stack with its payload mount weighs 1.0 kg or less (Core R9, estimate 0.996 kg); its four power leads and AS150 plugs are in Lift's harness (KWC-DDR-003).
- Local rules at the test sites allow external loads and tethered flight with permission.

## Safety

> **Safety:** The requirements describe a 25 kg class aircraft with large propellers, two 680 Wh lithium-ion packs, a 400 V tether and suspended loads. R5 (motor out) and R7 (tether) are tested only over cleared ground with the keep-out and isolation set out in the build plan's safety stops (KWL-BLD-001, section 6).
