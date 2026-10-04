---
doc_id: KWL-DDR-003
title: Kitewright Lift requirement decisions of 2026-10-03
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
  change: Amish's decisions 34A (lighter fittings) and 35A (lithium-ion ColdCell packs) carried out, with Kitewright Core decision 33B (frame-to-Core power leads)
---

# 0003: Requirement decisions of 2026-10-03

- **Date:** 2026-10-03
- **Status:** accepted

## Context

The TRL 3 calculations (KWL-CAL-001 v0.1) left two results short of the requirements, posed to Amish as open decisions 1 and 2 in `docs/REVIEW.md`:

- R1 and R2: 25.5 kg with a 5 kg payload, 0.5 kg over the 25 kg limit; the machined fittings were simple pocketed blocks.
- R4: 8.9 min of hover at sea level with 5 kg and 7.1 min at 5,000 m and -20 °C with 2 kg on the LiFePO4 ColdCell packs.

In parallel, Kitewright Core decision 33B moves the pack and frame power leads and their AS150 plugs out of the Core and into each frame's harness, so Lift now supplies its own leads from the frame to the Core.

Amish Chadha, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed."

## Options considered

As posed in `docs/REVIEW.md` (TRL 3, "Decisions for Amish"):

- Decision 1 (item 34): A, pocket the hinge blocks, root fittings and motor clamps deeper (estimated 1.04 kg less, about USD 120); B, rate the sea-level payload at 4.5 kg.
- Decision 2 (item 35): A, a lithium-ion ColdCell variant for Lift (14S3P of 21700 high-power cells) with 1A; B, LiFePO4 with a third cell in parallel; C, keep the LiFePO4 packs and use the tether for long hovers.

## Decision

Option A on both, as recommended.

*Table 1. Changes made.*

| # | Change | Where | Result |
| --- | --- | --- | --- |
| 34A-1 | Hinge blocks: side pockets 19 x 11 mm in the bolting end, an 18 x 46 mm window through both cheeks, the cheeks cut away below the pivot outboard and under the stop bridge to a 15 mm top rail; 4 to 5 mm walls round every hole | `cad/src/model.py` (`hinge_block_local`); KWL-DWG-104 Rev P2 | 0.29 to 0.19 kg each |
| 34A-2 | Root fittings: 12.5 mm side pockets leaving a 5 mm web and 5 mm bosses round the pivot and lock holes; window 22 x 28 mm (was 22 x 24) | `tongue_local`; KWL-DWG-105 Rev P2 | 0.29 to 0.24 kg each |
| 34A-3 | Motor clamps shortened from 50 to 40 mm along the arm; arm tubes cut to 405 mm (was 410) so the tube ends flush with the clamp | `PARAMS["mount"]`, `PARAMS["tube_r"]`; KWL-DWG-106 and 107 Rev P2 | 0.24 to 0.19 kg each |
| 35A | ColdCell lithium-ion packs for Lift: 14S3P of 21700 high-power cells (4.5 Ah, 45 A), 50.4 V nominal, about 680 Wh and 3.56 kg each, in the same 126 x 232 x 85 mm envelope; ColdCell's charge blocking below 5 °C, heater cut-outs, cell-level fuse and fire-resistant charging box | BOM line 23; KWL-CAL-001; build plan section 3.17 | 1,361 Wh in two packs, against 614 Wh |
| 33B (Core) | Frame-to-Core power leads: 8 AWG silicone wire and four AS150 anti-spark halves, soldered to the Core's pads; the Core is now about 0.99 kg | BOM line 24 (and 21 mass); build plan section 3.5 and step 13 | About 0.12 kg and USD 60 added to Lift |

The highest stress in the lightened fittings at full thrust is in the 15 mm top rail under the stop bridge; every figure is under a third of the 6061-T6 yield (KWL-CAL-001, F). The stop bridge itself is unchanged.

## Consequences

*Table 2. Results against the requirements (KWL-CAL-001 v0.2).*

| Requirement | Before | After | Status |
| --- | --- | --- | --- |
| R1, take-off mass with 5 kg | 25.5 kg | 25.2 kg | Not met, by about 0.2 kg |
| R2, payload inside R1 | 4.5 kg | 4.8 kg | At risk |
| R4, hover time | 8.9 and 7.1 min | 20.1 min at sea level with 5 kg; 16.1 min at 5,000 m and -20 °C with 2 kg | Met on paper |
| R11, cost | USD 5,739 | USD 6,335 | USD 1,335 over the value-engineering target |

- The modelled fittings save 0.79 kg, not the 1.04 kg estimated when the decision was posed: the root fittings' collar is already thin-walled and their tongues need full-width bosses at both holes, so they give up about 0.05 kg each rather than 0.10. With the lithium-ion packs (0.44 kg heavier than the LiFePO4 pair) and the frame-to-Core leads (0.12 kg), the aircraft weighs 25.2 kg with a 5 kg payload. This is posed to Amish as a new open decision in `docs/REVIEW.md` and the register.
- R4 is met at both conditions with margin; hover current is about 11 A per cell against a 45 A rating.
- Lithium-ion cells carry more fire energy than LiFePO4: ColdCell's conservative rules apply in full (charge blocking below 5 °C, heater cut-outs, a cell-level fuse and the fire-resistant charging box), and the build plan's safety stops say so.
- Cross-repo: ColdCell adds and confirms the lithium-ion variant (cells, envelope, mass, energy at -20 °C); Kitewright Core's leads now come from Lift's harness.
