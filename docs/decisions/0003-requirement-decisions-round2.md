---
doc_id: KWL-DDR-003
title: Kitewright Lift requirement decisions, round 2
project: Kitewright Lift
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Decisions 1 and 2 (R1 and R2, R4) decided by Amish as recommended, option A each, and Kitewright Core decision O1 option B carried into Lift's harness
---

# 0003: Requirement decisions, round 2

- **Date:** 2026-10-03
- **Status:** Decided. Decided by Amish Chadha on 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." Each decision below is the recommended option, exactly as worded, including its conditions.

## Context

The TRL 3 calculations (KWL-CAL-001 v0.1) left R1 not met and R2 at risk (25.5 kg with a 5 kg payload) and R4 not met (8.9 min at sea level, 7.1 min at 5,000 m). Both were posed to Amish in `docs/REVIEW.md` and in the design decisions register (KWL-DEC-001). In the same round Amish decided Kitewright Core's O1 option B (KWC-DDR-003), which moves the Core's pack and frame leads and their AS150 plugs into each frame's harness. This record states what was chosen, what it changed when carried into the model, and the conditions.

## Options considered

*Table 1. Decisions as posed (global numbers 18 and 19).*

| # | Requirement | Option A | Option B | Option C |
| --- | --- | --- | --- | --- |
| 1 (18) | R1 and R2, take-off mass with 5 kg | Pocket the hinge blocks, root fittings and motor clamps deeper: 24.4 kg with 5 kg, both met, hover +0.6 min, about USD 120, 1.04 kg less | Rate the sea-level payload at 4.5 kg: R1 met, R2 not met by 0.5 kg | |
| 2 (19) | R4, hover time | A lithium-ion ColdCell variant, 14S3P of 21700 high-power cells, with decision 1 A: 20.5 and 16.5 min, met, 24.9 kg, about USD 416 more, 0.44 kg more than LiFePO4 (net 0.6 kg less with 1 A) | LiFePO4 16S3P: 13.8 min with only 1.7 kg payload, 9.0 min at 5,000 m, not met, USD 130, 2.9 kg more | Keep LiFePO4 16S2P and use the tether: not met |

## Decision

*Table 2. Decisions, effect and conditions.*

| # | Requirement | Option chosen | Effect, as carried into the model | Condition |
| --- | --- | --- | --- | --- |
| 1 (18) | R1 and R2 | **A**: pocket the hinge blocks, root fittings and motor clamps deeper (side pockets leaving 4 to 5 mm walls and webs round the holes) | Pockets drawn with 4.5 mm walls and webs round every hole, boss and face; the bridge, pivot and lock-pin bosses untouched. Saving **0.41 kg** (hinge blocks 0.20, root fittings 0.13, clamps 0.08), not the 1.04 kg estimated: the fittings do not hold that much removable metal under the stated wall rule. USD 120 more machining (lines 4, 5, 7) | "Stresses stay under a third of yield": the load-carrying sections (bridge, pivot and lock bosses, cheeks at the pins) are unchanged, so the stresses of KWL-CAL-001 F stand; the 4.5 mm cheek walls beside the pockets are covered by the hinge proof load at TRL 4 |
| 2 (19) | R4 | **A**: the lithium-ion ColdCell variant, 14S3P of 21700 high-power cells, with decision 1 A | ColdCell now carries the variant (CCL-DDR-003): 680 Wh, 3.84 kg, 378 x 90 x 86 mm, USD 662 a pack. Hover 18.9 min at sea level with 5 kg and 15.0 min at 5,000 m with 2 kg (was 8.9 and 7.1). The deck grows to 290 x 430 mm and the guides shorten to 210 mm for the long packs | The decision's condition "it needs ColdCell to accept a lithium-ion variant": accepted in ColdCell (CCL-DDR-003) with its full protections. Motors, controllers and the Core bus stay unchanged (14S, 42 to 58.8 V, inside the Core's 18 to 60 V) |
| Core O1 (17) | Kitewright Core R9 | Kitewright Core's **B**: the pack and frame leads and AS150 plugs move to each frame's harness | Lift's harness (line 24) gains 2 m of 8 AWG wire and four AS150 halves, two pack inputs and two frame outputs, soldered to the Core's board pads and tied to its strain-relief bar: USD 60, 0.12 kg. The Core allowance stays 1.0 kg (Core estimate 0.996 kg without leads) | "The lead lengths were frame-specific anyway": Lift's leads are cut to its deck and hub |

**Outcome against the requirements.** Taken together, the decisions do not deliver the 24.9 kg they were posed with: the aircraft is estimated at **26.3 kg with a 5 kg payload**, so R1 is still not met and R2 is at risk (3.7 kg of payload inside 25 kg). R4 is met at 5,000 m (15.0 min) but missed by 1.1 min at sea level with 5 kg (18.9 min). The causes are set out in KWL-CAL-001 v0.2, Table 5: the smaller pocket saving (0.63 kg), ColdCell's heavier pack (0.57 kg for two), the larger deck (0.12 kg) and the Core leads (0.12 kg). The decisions are carried out as approved; the shortfall is posed to Amish as a new question (KWL-DEC-001, open decision 3), not decided here.

## Consequences

- `cad/src/model.py`: pocket geometry in the hinge blocks, root fittings and motor clamps (`pockets`, `web` parameters); pack envelope 90.4 x 378 x 85.8 mm; deck 290 x 430 mm; guides at X -95, 0 and 95 mm. Constructability checks pass in all three states.
- KWL-CAL-001 v0.2; `bom/bom.csv` lines 4, 5, 7, 17, 18, 21, 23 and 24; KWL-DWG-001 Rev P3 and KWL-DWG-002 Rev P2; making sketches, joints and steps regenerated; build plan KWL-BLD-001 v0.2.
- New questions (KWL-DEC-001, proposed, awaiting Amish): 3, take-off mass after round 2; 4, hot-weather operation with the lithium-ion packs (with ColdCell open decision 6).

> **Safety:** Lift now carries two 680 Wh lithium-ion packs, 1.36 kWh in all, about twice the energy of the LiFePO4 packs, in cells whose failure can vent flammable gas and spread from cell to cell. A crash, a puncture or a cold charge is more dangerous than before: after any hard landing the packs come out and are watched outside for 24 hours (build plan safety stop 7), they are charged and stored in a fire-resistant container, never unattended, and they cannot travel with air passengers. ColdCell's charge lockout, heater cut-offs and new 60 C discharge cut-out apply in full. The deeper pockets do not touch the stop bridge or the pin bosses that carry the arm's lift; every hinge is still proof-loaded at 1.5 times its full-thrust moment before first flight.
