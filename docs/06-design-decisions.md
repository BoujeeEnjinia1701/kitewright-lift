---
doc_id: KWL-DEC-001
title: Kitewright Lift design decisions register
project: Kitewright Lift
doc_type: Design decisions register
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened; design decisions made under Amish's pre-approvals of 2026-10-03; two requirement decisions proposed
---

# Kitewright Lift design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in `docs/REVIEW.md`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several decisions below set Lift's safety case: the arms fold down against a fixed stop, every hinge is proof-loaded before flight, the tether runs from an isolated and monitored 400 V supply with a breakaway, the float's line is never tied to the aircraft and drops are made from 10 m or higher. Each took the conservative option; the evidence that would relax it is in KWL-DDR-001, Table 1.

## Open decisions

Two results against the requirements are not decided under the pre-approval; the state, options and recommendation for each are set out in `docs/REVIEW.md`, TRL 3 section, "Decisions for Amish".

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | R1 and R2, take-off mass with a 5 kg payload: 25.5 kg | A: pocket the hinge blocks, root fittings and motor clamps deeper (1.04 kg off, about USD 120); B: rate the sea-level payload at 4.5 kg | Proposed, awaiting Amish. Recommend A | Making sketches of the hinge block, root fitting and motor mount (sections 3.2, 3.10, 3.11) | KWL-CAL-001, A and C; `docs/REVIEW.md` |
| 2 | R4, hover time: 8.9 min at sea level with 5 kg and 7.1 min at 5,000 m with 2 kg | A: a lithium-ion ColdCell variant for Lift (14S3P 21700 power cells) with 1A: 20.5 and 16.5 min; B: LiFePO4 packs with a third cell in parallel: 13.8 min but only 1.7 kg of payload; C: keep the LiFePO4 packs and use the tether for long hovers: 8.9 and 7.1 min | Proposed, awaiting Amish. Recommend A | The packs (section 3.17); ColdCell scope (Cross-repo actions in `docs/REVIEW.md`) | KWL-CAL-001, C; `docs/REVIEW.md` |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | The motors' full-throttle thrust with a 30 x 10 propeller at 51 V (about 10 kg), their mass (about 450 g) and their base hole pattern (35 mm circle assumed) | Sets the thrust margins (R3, R5) and the clamp's tapped holes | KWL-CAL-001, D; KWL-DWG-107 |
| 2 | The LiFePO4 cells' continuous current rating (30 A assumed) and capacity (3.0 Ah at 85 g) | Hover draws 16 A per cell and a climb 24 A | KWL-CAL-001, C |
| 3 | The controllers run on a 16S LiFePO4 bus (58.4 V full) with margin and report telemetry to the Core | Bus voltage and failure detection for R5 | KWL-CAL-001, D |
| 4 | The propellers' hub height and blade fold: both blades turn back along the arm when folded | Folded size (R9) and blade clearance to the gear (14 mm) | KWL-CAL-001, I |
| 5 | The ball-lock pins' grip length fits the 46 mm hinge block, and the shoulder bolts' shoulder is 8.00 mm | A pin too short will not lock; a loose pivot lets the arm rattle | KWL-DWG-104 |
| 6 | The DC-DC converter's input range covers 400 V less the 23 V tether drop, its output is adjustable to the bus float voltage, and it is rated at 4 kW at +45 °C | R7 for two hours in heat | KWL-CAL-001, G |
| 7 | The breakaway connector's pull-release force (about 200 N) and voltage rating (600 V) | It must part before the tether pulls the aircraft over | KWL-DDR-001, item 5 |
| 8 | The release unit stays closed when unpowered and on a failed signal | A release that opens on a fault drops the float unasked | KWL-DDR-001, item 7 |
| 9 | The Core stack fits 150 x 100 x 40 mm on four 10 mm dampers and the payload rails are 112 mm apart with 8 mm slots | Lift's plates are drilled for these (Cross-repo actions) | KWL-DDR-001, item 8 |
| 10 | Each ColdCell pack fits 126 x 232 x 85 mm and weighs about 3.3 kg | Deck, guides and straps are sized for this | KWL-DDR-001, item 4 |

## Value engineering

Value-engineering target: USD 5,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 5,739 (USD 739 over the target), excluding the payloads and ground set (USD 3,716). Main cost drivers and savings worth trying:

- Motors (USD 1,480), the Core stack and payload mount (USD 1,050), the two ColdCell packs (USD 840), the controllers (USD 680) and the propellers (USD 440) are 78 % of the aircraft.
- The machined fittings (USD 656 for 20 parts) are the largest made cost.
- Savings worth trying: integrated motor-and-controller units of the agricultural-drone class bought as a set of eight; one batch order of all machined parts from one CNC service; carbon plates nested on one sheet; motors and propellers bought as a matched set.
- The tether ground set (USD 2,390) is the largest payload cost; a shared ground supply across the Kitewright family would spread it.

## Decisions made

The pre-approvals: Amish, 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and, for this batch, "Proceed with the remaining 15 scaffolds".

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | Coaxial X8 layout: four arms, a motor above and below each tip | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 1 |
| 2026-10-03 | Arms fold down; lift held by a stop bridge; lock pin against droop only | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 2 |
| 2026-10-03 | 30 inch folding propellers, 100 KV class motors, controllers on the arms | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 3 |
| 2026-10-03 | Two ColdCell LiFePO4 16S2P packs as the baseline (hover time posed as open decision 2) | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 4 |
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
