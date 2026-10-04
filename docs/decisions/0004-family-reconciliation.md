---
doc_id: KWL-DDR-004
title: Kitewright Lift round-3 decisions, Kitewright family reconciliation
project: Kitewright Lift
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-04'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-04'
  author: Amish Chadha
  change: Amish's round-3 decisions 8A, 9A and 10A carried out for Lift
---

# 0004: Kitewright family reconciliation (round 3)

- **Date:** 2026-10-04
- **Status:** accepted. Decided by Amish Chadha on 2026-10-04: "For round 3, I agree with all your proposed recommendations".

## Context

After the round-2 decisions the six Kitewright repositories disagreed. ColdCell's lithium-ion pack for Lift, built to ColdCell's rules, came out at 410 x 94 x 94 mm and 4.46 kg against the 126 x 232 x 85 mm and 3.56 kg Lift had assumed (ColdCell open decision 3); its 50 °C warning limited full hover flights to about 27 °C ambient (ColdCell open decision 4); and Lift modelled the Core as a 150 x 100 x 40 mm stack on dampers with its own rails, not to the Core's drawing. Lift's own open decision 3 (R1 and R2 at 25.2 kg with 5 kg) was still open.

## Decision

- **8A:** ColdCell's pack as drawn is Lift's pack. Lift re-sizes its battery deck, re-runs mass, hover time and thrust margins with two of these packs, keeps the 25 kg take-off limit (US 55 lb class) and rates the payload at what fits; both designed payloads must still fit. R1 and R2 restated (KWL-REQ-001 v0.4).
- **9A:** ColdCell keeps its 50 °C firmware warning for the pack until a TRL 4 measurement supports relaxing it; the warm-weather limit (about 27 °C ambient for a full hover flight) goes into the operating notes.
- **10A:** AS150 plugs everywhere; one mounting envelope for the Core shared by Lift and Range, with the Core's drawing as the reference; the Kitewright interface table in each repository's review note.

## Carried out

| Item | Was | Now |
| --- | --- | --- |
| Packs | Two 126 x 232 x 85 mm, 3.56 kg, side by side along X | Two 410 x 94 x 94 mm, 4.46 kg, side by side in Y with a 30 mm gap for the GNSS mast |
| Battery deck | 330 x 290 x 3 mm carbon on 25 mm standoffs | 430 x 280 x 2 mm carbon with four 120 x 60 mm windows on 60 mm standoffs: its underside 9 mm above the upper blades, its corner cuts 12.7 mm and the pack corners 22.7 mm outside the upper discs in plan |
| Pack guides and straps | 20 x 20 x 2 angle, 250 mm; a strap round each pack | 15 x 15 x 1.5 angle, 340 mm; four 900 mm straps round both packs |
| Kitewright Core | 150 x 100 x 40 mm stack on dampers between the hub plates; Lift's own rails, pin and socket | The Core to KWC-DWG-001: hung under the bottom plate on its 8 mm spacers (M4, 220 x 130 mm), lid up through a 200 x 112 mm opening; top plate drilled over the mast boss, SMA bulkheads and switch; GNSS on the deck mast, antennas on extension leads to the gear |
| Payload interface | 240 x 124 x 6 mm payload plate with a lock lug | 184 x 128 x 5 mm payload shoe to KWC-DWG-106; saddles 80 mm wide inside the 88 mm neck; the tether converter on four 34 mm posts below the neck, 20 mm ahead of the pin knobs |
| Connectors | AS150 and XT60 | AS150 on every pack and bus lead |

## Results (KWL-CAL-001 v0.3)

- Ready to fly 21.78 kg; rated payload 3.2 kg at 24.98 kg take-off (R1, R2 met as restated); float release 1.46 kg and tether module 3.13 kg both fit.
- Hover 20.4 min at sea level with the rated payload and 14.5 min at 5,000 m with 2 kg (R4); thrust to weight 1.84 at 5,000 m (R3); with one motor out 2.24 and 1.43 (R5); tether converter margin 1.25 (R7).
- Full hover flights to about 27 °C ambient under ColdCell's 50 °C warning (R10).
- Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 6,627 (USD 1,627 over the target).

## Consequences

- R4's target still names 5 kg at sea level, which no longer fits inside R1; posed to Amish as open decision 4.
- The tether module's margin under 25 kg is 0.07 kg: the TRL 4 weigh-in decides it.

> **Safety:** Two packs hold 1.36 kWh of lithium-ion cells. ColdCell's charge blocking below 5 °C, heater cut-outs, cell fuses, fire-resistant charging box and 50 °C warning apply in full; above about 27 °C ambient, flights are cut short when the warning comes.
