---
doc_id: KWL-DDR-002
title: Kitewright Lift design for construction
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
  change: Constructability review and the changes that make the design buildable, decided under Amish's pre-approvals of 2026-10-03
---

# 0002: Design for construction

- **Date:** 2026-10-03
- **Status:** accepted

## Context

STANDARDS section 18 asks for every part to be makeable by its stated process and to fit and fasten to its neighbours (Amish, 2026-09-30: "fix the design assumptions to match and be physically feasible"). The TRL 2 concept (KWL-PRC-001, KWL-DDR-001) named the parts but not how they are made or joined: "folding carbon arms", "a central body", "a battery bay", "wide gear". Each was worked out in `cad/src/model.py`, part by part, and checked with build123d in three states: flying with the float release, flying with the tether module, and folded for transport. The checks report no overlapping parts and no part out of contact with what holds it; the only contacts allowed are pins and bolts passing through the holes made for them, and the pack straps passing through their deck slots. Amish pre-approved every recommendation on 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds". No change alters what Kitewright Lift does or its pitch; the safety-related changes all take the conservative side.

## Options considered

For each problem the simplest physically sound fix was chosen; the alternatives are noted in Table 1.

## Decision

*Table 1. Changes made for construction.*

| # | Part | The concept had | The constructable design has | Why |
| --- | --- | --- | --- | --- |
| 1 | Arm fold | "Folding carbon arms", no joint | A machined aluminium hinge block at each hub corner: a 32 mm clevis slot with 7 mm cheeks, an 8 mm shoulder-bolt pivot 14 mm above the block's bottom, an 8 mm ball-lock pin, and a 10 x 10 mm stop bridge across the cheek tops 30 mm outboard of the pivot | The thrust of an arm (up to 177 N, 78 N m about the pivot) is carried by the bridge in bearing (2.6 kN, bridge bending 41 MPa); the pin only resists droop (about 610 N in a 3 g landing) |
| 2 | Arm root | Tube straight into the body | A one-piece aluminium root fitting: a 30 mm tongue in the clevis and a 48 mm collar round the tube, with a 22 x 24 mm window to save weight | Gives the pivot and lock holes a solid seat; the collar takes the tube by bonding plus two M5 cross bolts |
| 3 | Fold clearance | Not checked | Pivot 180 mm from the centre; plate corners cut at 162 mm; tongue starts 15 mm inboard of the pivot | With the pivot nearer the centre the folded root fitting cut into the bottom plate (960 mm3 overlap in the check); now 6 mm clear, and the tongue's swing stays 6 mm clear of the block's solid end |
| 4 | Central body | "A central body" | Two 3 mm carbon plates 280 mm square, 60 mm apart on the four hinge blocks and four 60 mm spacers; the Core stack between them on four rubber dampers | A light, stiff box with the avionics protected and every hole defined |
| 5 | Battery bay | "Holds two heated packs" | A 3 mm carbon deck 330 x 290 mm on four 25 mm standoffs above the top plate, two aluminium angle guides and four cam straps through deck slots | Packs sit clear of the hinge pins and outside the upper rotor discs in plan (58 mm); the straps were first placed over a standoff (overlap in the check) and were moved |
| 6 | Coaxial motor mount | Not defined | A split aluminium clamp 50 x 60 x 52 mm on the arm tip, four M4 bolts, one M5 cross bolt through the tube; a motor on its top face and one inverted on its bottom face | A solid block thick enough above the tube for the motor screws (the first block left 2 mm); coaxial gap 170 mm (0.22 propeller diameters) |
| 7 | Motor controllers | Not placed | Two controllers strapped to each arm tube near the tip | They fold with the arm; only the two power leads per arm cross the hinge, in a slack loop |
| 8 | Hub height and gear | "Wide gear" | Hub underside 500 mm up; four 20 mm carbon struts bonded into machined top and skid blocks; skids 340 mm long, 450 mm apart | The folded motors stay 32 mm above the ground and 17 mm clear of the skids; the lower rotor discs stay 99 mm clear of the struts in flight |
| 9 | Payload bay | "Clear space under the body" | The Core payload mount on the bottom plate (two slotted rails, ball-lock pin, DS-014 socket); a standard 240 x 124 x 6 mm payload plate with a lock lug and plug pad | One plate design carries every payload; the pin passes through both rails and the lug, so it cannot be half-fitted |
| 10 | Line-and-float release | "Drops a flotation device" | Payload plate, two printed saddles, a fail-closed servo pin release and a webbing sling round a 120 x 420 mm foam float with a 30 m line in a bag | Makes the drop mechanism real with bought parts; the float sits 48 mm clear of the lower rotor discs |
| 11 | Tether module | "Ground supply, reel and onboard converter" | Payload plate with a 4 kW isolated converter (200 x 110 x 65 mm), a breakaway connector under its rear, and a lead to the Core bus tether input | Fits the same rails; the breakaway parts the tether at the aircraft if it snags |
| 12 | GNSS mast | Not placed | A 16 mm carbon mast on the deck centre between the packs, 230 mm tall | Keeps the receiver clear of the power wiring and above the packs |
| 13 | Spacer and standoff positions | Not placed | On the X and Y axes, 130 mm from the centre | Clear of the hinge blocks, the Core stack and the pack straps |
| 14 | Fittings' mass | Solid blocks | Lightening pocket in each hinge block and a window in each root fitting | The first solid blocks weighed 0.62 kg (hinge) and 0.55 kg (mount) each; now 0.29 and 0.24 kg. Deeper pockets are a saving worth trying (value engineering) |

## Consequences

- `cad/src/model.py` is the constructable design; STEP and STL are regenerated; the general arrangement is KWL-DWG-001 Rev P2 and the folded arrangement KWL-DWG-002 Rev P1.
- `bom/bom.csv` gains the hinge pivot bolts, lock pins, spacers, gear blocks, pack guides and straps, the payload plates, saddles and sling.
- KWL-CAL-001 uses the model's masses; the made parts weigh 6.15 kg.
- `project.yaml` records `design_state: constructable`.
- The build plan KWL-BLD-001 describes this design; its pictures come from `cad/src/build_plan_media.py`.
