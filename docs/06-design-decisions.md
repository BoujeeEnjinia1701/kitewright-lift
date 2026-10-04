---
doc_id: KWL-DEC-001
title: Kitewright Lift design decisions register
project: Kitewright Lift
doc_type: Design decisions register
version: "0.4"
status: Draft
date: '2026-10-04'
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
  change: Open decisions 1 and 2 decided by Amish (34A and 35A, KWL-DDR-003) and moved to Decisions made; new open decision 3 on R1 and R2
- version: "0.3"
  date: '2026-10-04'
  author: Amish Chadha
  change: Round-3 decisions 8A, 9A and 10A (KWL-DDR-004) recorded in Decisions made; open decision 3 closed by 8A; new open decision 4 on R4's wording
- version: "0.4"
  date: '2026-10-04'
  author: Amish Chadha
  change: Open decision 4 closed as a consequence of round-3 decision 8A (KWL-DDR-005); R4 restated to the rated payload
---

# Kitewright Lift design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in `docs/REVIEW.md`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several decisions below set Lift's safety case: the arms fold down against a fixed stop, every hinge is proof-loaded before flight, the tether runs from an isolated and monitored 400 V supply with a breakaway, the float's line is never tied to the aircraft and drops are made from 10 m or higher. Each took the conservative option; the evidence that would relax it is in KWL-DDR-001, Table 1.

## Open decisions

None. Open decision 3 (R1 and R2) was overtaken by Amish's round-3 decision 8A of 2026-10-04 (KWL-DDR-004), and open decision 4 (R4's wording at sea level) was closed on 2026-10-04 as a consequence of 8A, option A (KWL-DDR-005). Nothing in carrying them out needs Amish.

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | The motors' full-throttle thrust with a 30 x 10 propeller at 51 V (about 10 kg), their mass (about 450 g) and their base hole pattern (35 mm circle assumed) | Sets the thrust margins (R3, R5) and the clamp's tapped holes | KWL-CAL-001, D; KWL-DWG-107 |
| 2 | The lithium-ion 21700 cells' continuous current rating (45 A assumed), capacity (4.5 Ah) and mass (70 g), and the pack's energy at -20 °C with its heater running (85 % assumed) | Hover draws about 11 A per cell and a climb 16 A; R4 has 0.1 min of margin at sea level | KWL-CAL-001, C; KWL-DDR-003 |
| 3 | The controllers run on the 14S lithium-ion bus (58.8 V full) with margin and report telemetry to the Core | Bus voltage and failure detection for R5 | KWL-CAL-001, D |
| 4 | The propellers' hub height and blade fold: both blades turn back along the arm when folded | Folded size (R9) and blade clearance to the gear (14 mm) | KWL-CAL-001, I |
| 5 | The ball-lock pins' grip length fits the 46 mm hinge block, and the shoulder bolts' shoulder is 8.00 mm | A pin too short will not lock; a loose pivot lets the arm rattle | KWL-DWG-104 |
| 6 | The DC-DC converter's input range covers 400 V less the 23 V tether drop, its output is adjustable to the bus float voltage, and it is rated at 4 kW at +45 °C | R7 for two hours in heat | KWL-CAL-001, G |
| 7 | The breakaway connector's pull-release force (about 200 N) and voltage rating (600 V) | It must part before the tether pulls the aircraft over | KWL-DDR-001, item 5 |
| 8 | The release unit stays closed when unpowered and on a failed signal | A release that opens on a fault drops the float unasked | KWL-DDR-001, item 7 |
| 9 | The Core stack fits 150 x 100 x 40 mm on four 10 mm dampers and the payload rails are 112 mm apart with 8 mm slots | Lift's plates are drilled for these (Cross-repo actions) | KWL-DDR-001, item 8 |
| 10 | Each lithium-ion ColdCell pack fits 126 x 232 x 85 mm and weighs about 3.56 kg | Deck, guides and straps are sized for this; every 0.1 kg counts against R1 | KWL-DDR-003 |
| 11 | The frame-to-Core leads: 8 AWG wire and AS150 halves weigh about 0.12 kg in all and fit the Core's pads, strain-relief bar and grommets | Mass against R1; the Core no longer carries the leads (Core decision 33B) | KWL-DDR-003 |

## Value engineering

Value-engineering target: USD 5,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 6,335 (USD 1,335 over the target), excluding the payloads and ground set (USD 3,716). Decisions 34A and 35A and Core decision 33B added USD 596 (packs USD 416, pockets USD 120, leads USD 60). Main cost drivers and savings worth trying:

- Motors (USD 1,480), the two lithium-ion ColdCell packs (USD 1,256), the Core stack and payload mount (USD 1,050), the controllers (USD 680) and the propellers (USD 440) are 77 % of the aircraft.
- The machined fittings (USD 776 for 20 parts) are the largest made cost.
- Savings worth trying: integrated motor-and-controller units of the agricultural-drone class bought as a set of eight; one batch order of all machined parts from one CNC service; carbon plates nested on one sheet; motors and propellers bought as a matched set.
- The tether ground set (USD 2,390) is the largest payload cost; a shared ground supply across the Kitewright family would spread it.

## Decisions made

The pre-approvals: Amish, 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and, for this batch, "Proceed with the remaining 15 scaffolds".

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | Coaxial X8 layout: four arms, a motor above and below each tip | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 1 |
| 2026-10-03 | Arms fold down; lift held by a stop bridge; lock pin against droop only | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 2 |
| 2026-10-03 | 30 inch folding propellers, 100 KV class motors, controllers on the arms | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 3 |
| 2026-10-03 | Two ColdCell LiFePO4 16S2P packs as the baseline (superseded by decision 35A below) | Amish, under both pre-approvals quoted above | KWL-DDR-001, item 4 |
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
| 2026-10-03 | Open decision 1, R1 and R2 (item 34A): pocket the hinge blocks, root fittings and motor clamps deeper; done in the model as side pockets, windows and cut-away corners, and a 40 mm clamp; 0.78 kg saved (1.04 kg estimated) | Amish: "i agree with all the 46 recommendations you provided. please proceed." | KWL-DDR-003 |
| 2026-10-03 | Open decision 2, R4 (item 35A): a lithium-ion ColdCell variant for Lift, 14S3P of 21700 high-power cells, about 680 Wh and 3.56 kg per pack, with ColdCell's charge blocking below 5 °C, heater cut-outs, cell fuses and charging box | Amish: "i agree with all the 46 recommendations you provided. please proceed." | KWL-DDR-003 |
| 2026-10-03 | Lift supplies its own power leads from the frame to the Core (8 AWG, four AS150 halves), following Kitewright Core decision 33B | Amish: "i agree with all the 46 recommendations you provided. please proceed." | KWL-DDR-003 |
| 2026-10-04 | Open decision 3 closed by round-3 decision 8A: ColdCell's lithium-ion pack as drawn (410 x 94 x 94 mm, 4.46 kg, 680 Wh) is Lift's pack; the battery deck re-sized (430 x 280 x 2 mm with four windows, on 60 mm standoffs so it sits above the upper rotors) and mass, hover time and thrust margins re-run; the 25 kg take-off limit (US 55 lb class) kept; R1 and R2 restated and the payload rated at what fits, 3.2 kg; the float release (1.46 kg) and tether module (3.13 kg) both fit | Amish: "For round 3, I agree with all your proposed recommendations" | KWL-DDR-004 |
| 2026-10-04 | Round-3 decision 9A (ColdCell): the 50 °C firmware warning stays for the lithium-ion pack until a TRL 4 measurement supports relaxing it; full-length hover flights to about 27 °C ambient (R10) | Amish, as above | KWL-DDR-004; CCL-DDR-004 |
| 2026-10-04 | Round-3 decision 10A: AS150 plugs everywhere; the Kitewright Core hung under the bottom hub plate to the family envelope (four M4 on 220 x 130 mm, 200 x 112 mm opening, holes in the top plate over the lid's boss, SMA bulkheads and switch; GNSS on the deck mast and antennas on extension leads); payloads on 184 x 128 x 5 mm payload shoes inside the 88 mm neck; the Kitewright interface table in `docs/REVIEW.md` | Amish, as above | KWL-DDR-004 |
| 2026-10-04 | Open decision 4 closed as a consequence of round-3 decision 8A (option A): R4's sea-level case restated to "at least 20 min with the rated payload (R2) at sea level" (was "with 5 kg"); 20.4 min with 3.2 kg, met on paper; no design change | Amish: "For round 3, I agree with all your proposed recommendations" | KWL-DDR-005 |
