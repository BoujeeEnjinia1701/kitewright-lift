---
doc_id: KWL-DDR-001
title: Kitewright Lift TRL 2 review decisions
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
  change: TRL 2 review items decided under Amish's pre-approvals of 2026-10-03
---

# 0001: TRL 2 review decisions

- **Date:** 2026-10-03
- **Status:** accepted

## Context

The TRL 2 review (`docs/REVIEW.md`, TRL 2 section) and the open questions in KWL-PRB-001 raised the items below. On 2026-10-03 Amish wrote: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." He then wrote: "Proceed with the remaining 15 scaffolds", under the same pre-approval, which covers Kitewright Lift. Every design recommendation below is therefore decided as recommended. Choices that touch safety take the conservative option, with the evidence that would relax them stated. Partners and regions are the first candidates to approach, not agreements. Requirements that are not met or at risk on paper (R1 and R2 on mass, R4 on hover time) are not decided here; they are posed to Amish in `docs/REVIEW.md` under "Decisions for Amish".

Kitewright Core, Lift and Range are designed in parallel. Where Lift depends on a sibling (the Core stack and payload mount, the ColdCell packs), the sizes used here are interface assumptions; they are listed in `docs/REVIEW.md` under "Cross-repo actions" for the sibling designs to confirm.

## Options considered

Table 1 lists the options for each item and the one chosen.

## Decision

*Table 1. Items decided on 2026-10-03 under Amish's pre-approvals.*

| # | Item | Options | Decision | What would relax a safety choice |
| --- | --- | --- | --- | --- |
| 1 | Rotor layout | (a) flat hexacopter; (b) flat octocopter; (c) coaxial X8 (four arms, a motor above and below each tip) | (c), conservative: losing any one motor leaves its partner on the same arm, so the aircraft can still hover (thrust to weight with one motor out 2.20 at sea level and 1.51 at 5,000 m on paper). Four arms fold into a smaller bundle than six or eight. Costs about 4 % more hover power than a flat layout of the same span | Not relaxed: motor-out tolerance is a requirement (R5) |
| 2 | Arm fold | (a) arms fold up, held by a lock pin; (b) arms fold sideways; (c) arms fold down, lift pressing each arm up against a fixed stop | (c), conservative: in flight the thrust holds the arm against a stop bridge machined into the hinge block, so a lock pin left out cannot let an arm fold under power. The ball-lock pin only stops the arm drooping on the ground or in a hard landing, and carries a red flag so a missing pin is visible | Not relaxed. A proof load on CalRig of each hinge at 1.5 times the full-thrust moment is required before first flight (item 13) |
| 3 | Propeller and motor class | 28, 30 or 32 inch propellers; integrated or separate controllers | 30 inch folding carbon propellers on 1,240 mm motor spacing (115 mm tip gap); about 100 KV motors of the 10 kg static thrust class; separate 80 A controllers strapped to the arms, so motor leads never cross the hinge | Not a safety choice |
| 4 | Power bus and packs | ColdCell as designed (LiFePO4 or sodium-ion); a lithium-ion pack | Two ColdCell LiFePO4 packs, 16S2P of 26650 power cells (51.2 V, about 307 Wh each), used unchanged as the problem statement's constraint requires. The hover time this gives is posed to Amish as decision 2 in `docs/REVIEW.md`, not decided here | Charging and cold limits stay as ColdCell sets them |
| 5 | Tether power | Low-voltage tether; fixed high-voltage tether with onboard conversion; adaptive tether voltage | Fixed 400 V DC from an isolated ground supply over a 60 m tether of two 0.75 mm2 conductors; a 4 kW isolated DC-DC converter on a payload plate; a pull-release breakaway at the aircraft. Conservative: isolated supply with an insulation monitor, residual-current protection and an emergency stop at the ground; tether hover limited to 50 m. Stays clear of adaptive tether voltage (Elistair US11059580B2) | A ground-fault and touch-current test of the complete system could allow tether hover above 50 m; the isolation and monitoring stay |
| 6 | Winch | Design a winch now; reserve space only | No winch is designed or published until its own patent screen is done. The payload bay and rails take a winch module later; nothing in this design depends on one | Not a safety choice |
| 7 | Line-and-float release | Hook release; servo pin release; drop the line attached to the aircraft | A servo pin release that fails closed holds a webbing sling round a foam float; the float's line is tied to the float only and is never attached to the aircraft. Conservative: drops from at least 10 m above the person, so downwash (about 7.5 m/s estimated at 10 m) does not push them under | Downwash measured over water at lower heights could lower the 10 m drop height |
| 8 | Payload interface | Lift-specific mount; the Core payload mount | The Kitewright Core payload mount under the bottom plate: two slotted rails, a ball-lock payload pin through both rails and the payload's lug, and the DS-014 socket at the back. Interface sizes are assumptions (Cross-repo actions) | Not relaxed: the pin must be in and flagged before arming |
| 9 | Landing gear | Folding gear; fixed skids; detachable legs | Fixed skid gear, 340 mm skids 450 mm apart, hub underside 500 mm up. Fixed gear stays on for transport (the folded aircraft still fits the R9 case) and the folded motors clear the skids by 17 mm | Not a safety choice |
| 10 | Keep-out and hover heights | Set by test later; set now | Set now, conservatively: nobody within 15 m of the aircraft when armed except over a person in water for a drop; drops from 10 m or higher; no hover over people on snow slopes or rooftops | Downwash and noise measurements in the TRL 4 trials |
| 11 | First co-design candidate | A state disaster force; a volunteer mountain rescue team; a hazard research group | The Himalayan Rescue Association, Nepal, as the first candidate to approach (not agreed): it runs aid posts on the trekking routes and works with helicopter rescue at altitude | Not a safety choice |
| 12 | First high-altitude test region | Ladakh; Sikkim; Nepal's Khumbu | Sea-level trials first, then the Khumbu region of Nepal with the co-design candidate, as the first candidate (not agreed); flights only with the civil aviation authority's permission | Not a safety choice |
| 13 | Proof before flight | Fly and see; bench proof first | AltiRig as the first candidate rig for motor and propeller thrust at 5,000 m density (R3); CalRig as the first candidate rig for proof loads: each arm hinge at 1.5 times the full-thrust moment (117 N m) and the tether breakaway pull | Not relaxed |
| 14 | Prototype budget | Raise the budget; keep it | `budget_usd` kept at USD 5,000 as a value-engineering target; the estimated cost of USD 5,739 is reported against it | Not a safety choice |

## Consequences

- KWL-PRC-001, KWL-REQ-001 and KWL-PRB-001 are updated to version 0.2 with these decisions.
- The constructable design (KWL-DDR-002) and the sizing (KWL-CAL-001) follow items 1 to 9.
- R4 (hover time) is not met with the LiFePO4 packs of item 4 and R1 is exceeded by 0.5 kg with a 5 kg payload; both are posed to Amish, with options, in `docs/REVIEW.md`.
- Items 5, 7, 8, 10 and 13 appear as safety stops in the build plan (KWL-BLD-001).
