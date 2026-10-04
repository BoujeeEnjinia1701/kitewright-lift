---
doc_id: KWL-DEC-001
title: Kitewright Lift design decisions register
project: Kitewright Lift
doc_type: Design decisions register
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened; design decisions made under Amish's pre-approvals of 2026-10-03; two requirement decisions proposed
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Decisions 1 and 2 decided by Amish (option A each, KWL-DDR-003) and moved to Decisions made; Core leads in the harness; new open decisions 3 and 4; items to confirm and value engineering updated
---

# Kitewright Lift design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in `docs/REVIEW.md`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several decisions below set Lift's safety case: the arms fold down against a fixed stop, every hinge is proof-loaded before flight, the tether runs from an isolated and monitored 400 V supply with a breakaway, the float's line is never tied to the aircraft and drops are made from 10 m or higher. Each took the conservative option; the evidence that would relax it is in KWL-DDR-001, Table 1.

## Open decisions

Proposed, awaiting Amish. Decisions 1 and 2 were decided on 2026-10-03 and are under Decisions made. Decisions 3 and 4 were raised while carrying them into the model (KWL-CAL-001 v0.2); figures are estimates.

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| 3 | R1, R2 and R4 after round 2. State: 26.3 kg with a 5 kg payload (R1 not met by 1.3 kg; 3.7 kg of payload fits inside 25 kg, so R2 is at risk); hover 18.9 min at sea level with 5 kg (R4 missed by 1.1 min) and 15.0 min at 5,000 m (met). Causes: the pockets save 0.41 kg, not 1.04 kg, under the 4.5 mm wall rule; ColdCell's variant weighs 3.84 kg, not 3.56 kg; the larger deck adds 0.12 kg; the Core leads add 0.12 kg | A: rate the sea-level payload at 3.5 kg for the first prototype (R2 restated): 24.8 kg, R1 met; about 20.5 min at sea level with 3.5 kg (estimate). B: a second lightening round: 2 mm carbon hub plates and deck (estimate 0.42 kg, after a stiffness check), ColdCell open decision 4 A (estimate 0.16 to 0.20 kg for two packs) and stress-sized pockets below the 4.5 mm webs after a structural check: about 25.6 kg before that check, so still not met. C: raise R1 to 26.5 kg; 25 kg is a common threshold in drone rules, so this changes the aircraft's regulatory class | **A for the first prototype, with B pursued as value engineering** and revisited when the fittings and packs are weighed at TRL 4. A is the only option that meets R1 now; C changes the pitch. Proposed, awaiting Amish | Rated payload in KWL-REQ-001 (R2, R4); deck and hub plate thickness under B | KWL-CAL-001 v0.2, A and C; `docs/REVIEW.md`, Session 2026-10-03 round 2 |
| 4 | R10 in hot weather. State: the lithium-ion packs make 71 W each in hover; with their jackets on they stay under 50 °C for 20 minutes only up to 25 °C ambient, and at 45 °C they would pass the 60 °C discharge limit of typical cells | A: adopt ColdCell's summer configuration (top foam out, vented lid) for flights above 15 °C, as recommended in ColdCell open decision 6. B: rate Lift to 25 °C ambient with the jackets on until measured. C: shorter hovers above 25 °C, with the autopilot landing when ColdCell reports 50 °C | **A**, following ColdCell's open decision 6; until it is decided, Lift does not fly the packs above 25 °C with their jackets on. Proposed, awaiting Amish | Pack lids (ColdCell); operating limits in the build plan | ColdCell CCL-CAL-001 K; KWL-CAL-001 v0.2, J |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | The motors' full-throttle thrust with a 30 x 10 propeller at 51 V (about 10 kg), their mass (about 450 g) and their base hole pattern (35 mm circle assumed) | Sets the thrust margins (R3, R5) and the clamp's tapped holes | KWL-CAL-001, D; KWL-DWG-107 |
| 2 | The lithium-ion cells' continuous current rating (45 A assumed), capacity (4.5 Ah at 70 g) and the pack mass ColdCell builds to (3.84 kg estimated) | Hover draws 11.5 A per cell and a climb 17.2 A; R1 | KWL-CAL-001, A and C; ColdCell CCL-CAL-001 K |
| 3 | The controllers run on a 14S lithium-ion bus (58.8 V full) with margin and report telemetry to the Core | Bus voltage and failure detection for R5; see also Kitewright Core open decision O2 on the 60 V power board | KWL-CAL-001, D; KWC-DEC-001 |
| 4 | The propellers' hub height and blade fold: both blades turn back along the arm when folded | Folded size (R9) and blade clearance to the gear (14 mm) | KWL-CAL-001, I |
| 5 | The ball-lock pins' grip length fits the 46 mm hinge block, and the shoulder bolts' shoulder is 8.00 mm | A pin too short will not lock; a loose pivot lets the arm rattle | KWL-DWG-104 |
| 6 | The DC-DC converter's input range covers 400 V less the 23 V tether drop, its output is adjustable to the bus float voltage, and it is rated at 4 kW at +45 °C | R7 for two hours in heat | KWL-CAL-001, G |
| 7 | The breakaway connector's pull-release force (about 200 N) and voltage rating (600 V) | It must part before the tether pulls the aircraft over | KWL-DDR-001, item 5 |
| 8 | The release unit stays closed when unpowered and on a failed signal | A release that opens on a fault drops the float unasked | KWL-DDR-001, item 7 |
| 9 | The Core stack fits 150 x 100 x 40 mm on four 10 mm dampers and the payload rails are 112 mm apart with 8 mm slots | Lift's plates are drilled for these (Cross-repo actions) | KWL-DDR-001, item 8 |
| 10 | Each ColdCell lithium-ion pack fits 378 x 90 x 86 mm (ColdCell CCL-DWG-002) and weighs about 3.84 kg | Deck, guides and straps are sized for this | KWL-DDR-003 |
| 11 | The Core's power board pads take 8 AWG leads, and the Core's strain-relief bar sits where Lift's harness can reach it | Lift's harness now carries the Core leads | KWC-DDR-003 |

## Value engineering

Value-engineering target: USD 5,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 6,418 (USD 1,418 over the target), excluding the payloads and ground set (USD 3,716). Before the round 2 decisions it was USD 5,739; the lithium-ion packs added USD 484, the deeper pockets USD 120, the Core leads USD 60 and the larger deck USD 15. Main cost drivers and savings worth trying:

- Motors (USD 1,480), the two ColdCell lithium-ion packs (USD 1,324), the Core stack and payload mount (USD 1,050), the controllers (USD 680) and the propellers (USD 440) are 77 % of the aircraft.
- The machined fittings (USD 776 for 20 parts) are the largest made cost.
- Savings worth trying: integrated motor-and-controller units of the agricultural-drone class bought as a set of eight; one batch order of all machined parts from one CNC service; carbon plates nested on one sheet; motors and propellers bought as a matched set; the variant cells bought in a 100-cell lot.
- The tether ground set (USD 2,390) is the largest payload cost; a shared ground supply across the Kitewright family would spread it.

## Decisions made

The pre-approvals: Amish, 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and, for this batch, "Proceed with the remaining 15 scaffolds".

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | Coaxial X8 layout: four arms, a motor above and below each tip | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 1 |
| 2026-10-03 | Arms fold down; lift held by a stop bridge; lock pin against droop only | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 2 |
| 2026-10-03 | 30 inch folding propellers, 100 KV class motors, controllers on the arms | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 3 |
| 2026-10-03 | Two ColdCell LiFePO4 16S2P packs as the baseline (hover time posed as open decision 2; superseded by decision 2 option A, KWL-DDR-003) | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 4 |
| 2026-10-03 | Fixed 400 V DC tether, 60 m, 4 kW onboard converter, breakaway, monitored isolated ground supply, 50 m highest hover | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 5 |
| 2026-10-03 | No winch designed until its patent screen | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 6 |
| 2026-10-03 | Fail-closed servo pin release; float line never tied to the aircraft; drops from 10 m or higher | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 7 |
| 2026-10-03 | Core payload mount under the bottom plate; one standard payload plate | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 8 |
| 2026-10-03 | Fixed skid gear, 450 mm apart, hub 500 mm up | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 9 |
| 2026-10-03 | Keep-out 15 m when armed; no hover over people on snow slopes or roofs | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 10 |
| 2026-10-03 | First co-design candidate to approach: the Himalayan Rescue Association, Nepal (not agreed) | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 11 |
| 2026-10-03 | First high-altitude test region to approach: Khumbu, Nepal, after sea-level trials (not agreed) | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 12 |
| 2026-10-03 | AltiRig for thrust at 5,000 m density; CalRig for hinge proof loads at 1.5 times full thrust and the breakaway pull | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 13 |
| 2026-10-03 | `budget_usd` kept at 5,000 as a value-engineering target | Amish: "I also accept any cost overruns or variations from the assumed scope cost." | KWL-DDR-001, item 14 |
| 2026-10-03 | Design for construction: the fourteen changes of KWL-DDR-002 | Amish, under both pre-approvals quoted above | KWL-DDR-002 |
| 2026-10-03 | Appearance model additions for renders: mannequin beside the aircraft; one arm hinge with short pieces of the hub plates for the detail view | Amish, under both pre-approvals quoted above | `docs/REVIEW.md`, TRL 3 |
| 2026-10-03 | Decision 1 (R1, R2), option A: pocket the hinge blocks, root fittings and motor clamps deeper, leaving 4 to 5 mm walls and webs round the holes (as modelled: 0.41 kg less, USD 120) | Amish, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." | KWL-DDR-003 |
| 2026-10-03 | Decision 2 (R4), option A: a lithium-ion ColdCell variant, 14S3P of 21700 high-power cells, with decision 1 A (ColdCell accepted it, CCL-DDR-003) | Amish, same words | KWL-DDR-003 |
| 2026-10-03 | Kitewright Core decision O1 option B: the pack and frame leads and AS150 plugs move into Lift's harness | Amish, same words (Kitewright Core decision) | KWL-DDR-003; KWC-DDR-003 |

Change log: 2026-10-03, decisions 1 and 2 moved from Open decisions to Decisions made (option A each); the Core leads added to the harness; open decisions 3 and 4 and items 10 and 11 to confirm added; item 2, 3 and 10 rewritten for the lithium-ion packs.
