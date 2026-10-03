---
doc_id: KWL-REQ-001
title: Kitewright Lift requirements
project: Kitewright Lift
doc_type: Requirements
version: "0.2"
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
---

# Kitewright Lift requirements

Requirements for the first prototype, with the status of each against the TRL 3 calculations (KWL-CAL-001) for the constructable design (KWL-DDR-002). Targets are as set at TRL 1; none has been changed. "Met on paper" means the calculation shows the target is reachable; every requirement is verified by test at TRL 4 or later. Requirements not met or at risk are posed to Amish in `docs/REVIEW.md` and listed in the design decisions register (`docs/06-design-decisions.md`).

Table 1. Requirements

| ID | Requirement | Target | Verification (TRL 3 or later) | Status at TRL 3 (KWL-CAL-001) |
| --- | --- | --- | --- | --- |
| R1 | Maximum take-off mass | 25 kg or less including payload | Weigh the fully loaded aircraft | Not met with a 5 kg payload: 25.5 kg. Ready to fly 20.5 kg. Open decision 1 |
| R2 | Payload at sea level | 5 kg on the core mount (target) | Hover test with calibrated mass | At risk: thrust is ample (thrust to weight 2.83) but R1 leaves 4.5 kg. Open decision 1 |
| R3 | Payload at altitude | 2 kg at air density equivalent to 5,000 m (target) | AltiRig thrust data, then flight at a high site | Met on paper: thrust to weight 1.94 at 5,000 m and -20 C with 2 kg |
| R4 | Hover time | At least 20 min with 5 kg at sea level and 10 min with 2 kg at 5,000 m and -20 °C (targets) | Timed hover flights with logged energy use | Not met: 8.9 min and 7.1 min with the LiFePO4 ColdCell packs. Open decision 2 |
| R5 | Motor-out tolerance | Controlled descent and landing after one motor failure at rated payload | Deliberate motor cut test over a safe area | Met on paper: thrust to weight with one motor out 2.20 at sea level, 1.51 at 5,000 m; yaw control to be shown in the motor-cut test |
| R6 | Wind | Holds position within 2 m in 10 m/s steady wind (target) | Logged position hold on a windy test day | Met on paper for thrust: 18 N drag, 4.2 deg tilt; position hold depends on tuning and is shown in flight |
| R7 | Tethered endurance | At least 2 h continuous hover on fixed-voltage tether power (target) | Tethered endurance run with logged voltages and temperatures | Met on paper: 3.0 kW hover on a 4 kW converter (margin 1.35); converter and motor temperatures over 2 h to be measured |
| R8 | Float and line drop | Places a float within 3 m of a target from 10 m height (target) | Drop trials over water | Met on paper: expected miss 2.2 m in 10 m/s wind when the drift is aimed off |
| R9 | Transport | Folds to fit a case of 1.2 m by 0.6 m by 0.5 m or smaller; set up in 10 min or less (target) | Pack and timed set-up trials | Met on paper: folded 0.84 x 0.48 x 0.45 m with the gear on; set-up about 9 min |
| R10 | Operating temperature | Flies from -20 to +45 °C with ColdCell packs (target) | Cold soak then hover test | Met on paper by part ratings; pre-heat about 53 Wh from the ground supply |
| R11 | Prototype cost | USD 5,000 or less excluding payloads | Bill of materials and receipts | Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 5,739 (USD 739 over the target) |

## Assumptions

- Air at 5,000 m and -20 °C: 54.0 kPa and 0.743 kg/m3 (71 % of the pressure and 61 % of the density at sea level).
- Motor and propeller performance from makers' figures for the 30 inch, 100 KV class, until AltiRig measures it at 5,000 m density.
- ColdCell delivers 85 % of its rated energy at -20 °C with its heater running (ColdCell R1).
- The Kitewright Core stack with its payload mount weighs 1.0 kg or less (Core R9).
- Local rules at the test sites allow external loads and tethered flight with permission.

## Safety

> **Safety:** The requirements describe a 25 kg class aircraft with large propellers, lithium iron phosphate packs, a 400 V tether and suspended loads. R5 (motor out) and R7 (tether) are tested only over cleared ground with the keep-out and isolation set out in the build plan's safety stops (KWL-BLD-001, section 6).
