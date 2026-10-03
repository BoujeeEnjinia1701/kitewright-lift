# Review note: Kitewright Lift

## Session 2026-10-03: TRL 3 (kit 1.7.0, /to-trl3 under Amish's pre-approvals)

Amish, 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and, for this second batch, "Proceed with the remaining 15 scaffolds". Every design recommendation in this session is therefore recorded as decided, dated 2026-10-03, in `docs/06-design-decisions.md`. Requirements not met or at risk are not decided; they are posed below under "Decisions for Amish" (Amish, 2026-10-03: "A simple statement doesn't add value - ensure you are identifying a state and posing it as a clear recommendation for me to decide on."). Kit 1.7.0 was installed from the kit source; `.kit/PHASE.yaml` kept as installed. Kitewright Core and Kitewright Range were worked on in parallel by other sessions; their repositories were not touched, and the interface sizes Lift assumes are listed under "Cross-repo actions".

### TRL 2

**What was done.**

- `docs/01-problem.md` (KWL-PRB-001 v0.2): first co-design candidate with a checklist, answers to the TRL 1 open questions, safety section; the budget restated as a value-engineering target.
- `docs/03-requirements.md` (KWL-REQ-001 v0.2): status of every requirement; targets unchanged.
- `docs/02-concept.md` (KWL-PRC-001 v0.2): how it works, components, key design choices, first-order numbers, safety.
- `docs/decisions/0001-trl2-review-decisions.md` (KWL-DDR-001): fourteen TRL 2 review items decided.

**Results.** A coaxial X8 with 30 inch propellers on 1,240 mm motor spacing lifts the R2 and R3 payloads with ample thrust and keeps flying after the loss of any one motor. The open questions were the arm fold (which way, and what holds the arm in flight), the pack chemistry's effect on hover time, and the tether voltage.

**Requirements not met.** None decided at TRL 2; R4 (hover time) was already doubtful with the ColdCell LiFePO4 chemistry.

**Decisions made under the pre-approvals.** KWL-DDR-001, items 1 to 14: coaxial X8; arms fold down against a stop bridge, lock pin against droop only; 30 inch propellers, 100 KV class motors, controllers on the arms; two ColdCell LiFePO4 16S2P packs as the baseline; fixed 400 V tether with a monitored isolated supply and a breakaway; no winch until screened; fail-closed float release with the line never tied to the aircraft and drops from 10 m or higher; the Core payload mount and one payload plate; fixed skid gear; 15 m keep-out; the Himalayan Rescue Association as first co-design candidate and Khumbu, Nepal as first high-altitude region (neither agreed); AltiRig and CalRig as first proof rigs; budget kept.

**Safety concerns.** Propeller strike; an arm folding in flight; pack fire after a crash or cold charge; the 400 V tether; downwash on people in water or on snow.

### TRL 3

**What was done.**

- `docs/04-calcs/01-sizing.md`, `docs/04-calcs/sizing.py` and `docs/04-calcs/results.csv` (KWL-CAL-001 v0.1): mass, hover power and time, thrust margin and motor out, wind, structure, tether, float drop, transport, temperature, cost.
- `cad/src/model.py`: parametric build123d model with constructability checks in three states (flying with the float release, flying with the tether module, folded): no overlaps, nothing floating. STEP in `cad/step` (assembly, folded, tether module and eleven made parts) and STL in `cad/stl`.
- `cad/src/sheets.py`: KWL-DWG-001 general arrangement (Rev P2) and KWL-DWG-002 folded arrangement (Rev P1).
- `bom/bom.csv`: 38 lines, all priced, with suppliers by type; lines 1 to 25 are the aircraft, 26 to 38 the payloads and tether ground set.
- `cad/src/concept_media.py`: `media/hero.png`, `cutaway.png`, `exploded.png`, `flow.png`, `concept-blueprint.png` and `.pdf` (KWL-DWG-010), `model.glb` (about 3 MB, coarse tessellation) and `viewer.html`.
- `docs/decisions/0002-design-for-construction.md` (KWL-DDR-002); `design_state: constructable`.
- `cad/src/build_plan_media.py`: overview, fourteen making sketches (KWL-DWG-101 to 114), eleven joint close-ups and sixteen step pictures; `docs/05-build-plan.md` (KWL-BLD-001) and `docs/06-design-decisions.md` (KWL-DEC-001).
- `cad/src/product_model.py` (`product_parts()`, `TITLE`, `RENDER_VIEWS` hero, exploded, detail); scenes exported to `/home/claude/renders/kitewright-lift` (three .npz and .json, `kitewright-lift__jobs.json`). Photoreal renders, captions and cards are made on Amish's Mac; the README already leads with `media/render-hero.png`.
- `README.md`, `project.yaml` (trl 3, trl_target 3).

**Results (KWL-CAL-001).** Empty 13.8 kg (made parts 6.15 kg from the model); two packs 6.68 kg and 614 Wh; ready to fly 20.5 kg; 25.5 kg with 5 kg. Hover power 3.30 kW at sea level with 5 kg and 3.51 kW at 5,000 m and -20 °C with 2 kg; hover time 8.9 and 7.1 min. Thrust to weight 2.83 at sea level and 1.94 at 5,000 m; with one motor out 2.20 and 1.51. Wind: 18 N and 4.2 degrees at 10 m/s. Structure at full thrust: 2.6 kN on the stop bridge (41 MPa), 2.8 kN on the 8 mm pivot (27.5 MPa), arm tube 28 MPa and 0.76 mm deflection; hinge proof load 117 N m. Tether: 3.32 kW from the ground, 23 V drop, 193 W loss, converter at 74 % of rating. Float drop: expected miss 2.2 m from 10 m in 10 m/s wind. Folded 0.84 x 0.48 x 0.45 m; set-up about 9 min. Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 5,739 (USD 739 over the target); payloads and ground set USD 3,716.

**Requirements not met or at risk.**

- **R1, not met, and R2, at risk:** 25.5 kg with a 5 kg payload; the payload that fits inside R1 is 4.5 kg.
- **R4, not met:** 8.9 min at sea level with 5 kg and 7.1 min at 5,000 m and -20 °C with 2 kg.
- R3, R5, R7, R8, R9 and R10 are met on paper; R6 is met for thrust and the position hold is shown in flight; R11 is reported against the value-engineering target (USD 739 over), not as a decision.

**Decisions for Amish.**

*Decision 1: R1 and R2, take-off mass with a 5 kg payload.* State: the aircraft weighs 25.5 kg with a 5 kg payload, 0.5 kg over the R1 limit; inside R1 it carries 4.5 kg. Cause: the machined aluminium fittings (hinge blocks, root fittings, motor clamps: 3.26 kg) are sized as simple pocketed blocks for a first prototype, and the LiFePO4 packs weigh 6.68 kg.

| Option | Effect on R1 and R2 | Cost | Mass |
| --- | --- | --- | --- |
| A: pocket the hinge blocks, root fittings and motor clamps deeper (side pockets leaving 4 to 5 mm walls and webs round the holes; stresses stay under a third of yield) | 24.4 kg with 5 kg: both met; hover time +0.6 min | About USD 120 more machining | 1.04 kg less |
| B: rate the sea-level payload at 4.5 kg | R1 met; R2 not met by 0.5 kg | None | None |

**Recommendation: A.** It meets both requirements for a small machining cost, and the saving also helps R4 under either option of decision 2.

*Decision 2: R4, hover time.* State: 8.9 min at sea level with 5 kg and 7.1 min at 5,000 m and -20 °C with 2 kg, about 45 % and 70 % of the R4 figures. Cause: the ColdCell LiFePO4 packs hold 92 Wh/kg once heater, BMS and shell are added, and a 25 kg aircraft needs 3.3 kW to hover; more LiFePO4 cells push the take-off mass past R1.

| Option | Effect on R4 | Cost | Mass |
| --- | --- | --- | --- |
| A: a lithium-ion ColdCell variant for Lift, 14S3P of 21700 high-power cells (2 x 680 Wh, same 51 V class bus), with decision 1 A | 20.5 min at sea level with 5 kg and 16.5 min at 5,000 m with 2 kg: met; take-off mass 24.9 kg | About USD 416 more | 0.44 kg more than the LiFePO4 packs (net 0.6 kg less with 1 A) |
| B: LiFePO4 with a third cell in parallel (16S3P) | 13.8 min at sea level but only 1.7 kg of payload inside R1; 9.0 min at 5,000 m: not met, and R2 worse | About USD 130 more | 2.9 kg more |
| C: keep the LiFePO4 16S2P packs for the first prototype and use the tether for long hovers | 8.9 and 7.1 min (9.5 and 7.7 with 1 A): not met | None | None |

**Recommendation: A.** It is the only option that meets R4 at both sea level and altitude while keeping R1, and it leaves motors, controllers and the Core bus unchanged. It needs ColdCell to accept a lithium-ion variant (its problem statement now limits it to LiFePO4 or sodium-ion), so it is listed under Cross-repo actions; lithium-ion cells carry more fire energy, and ColdCell's charge lockout, heater cut-off and pack enclosure rules apply in full.

**Decisions made under the pre-approvals.** KWL-DDR-002, the fourteen design-for-construction changes (listed below); the appearance model additions (below). All in `docs/06-design-decisions.md`. Open decisions: the two above, "Proposed, awaiting Amish".

**Build plan findings (design changes made for construction, KWL-DDR-002).**

1. Arm hinge: clevis block with an 8 mm pivot near the bottom, a ball-lock pin, and a stop bridge 30 mm outboard of the pivot that takes the lift.
2. One-piece root fitting: tongue in the clevis and a collar round the tube, bonded and cross-bolted.
3. Pivot moved to 180 mm and plate corners cut at 162 mm, so the folded root fitting clears the bottom plate (it overlapped by 960 mm3).
4. Hub: two 3 mm carbon plates 60 mm apart on the hinge blocks and four spacers; the Core inside on dampers.
5. Battery deck on standoffs with guides and cam straps; packs clear of the hinge pins and rotors.
6. Split clamp motor mount thick enough above the tube for the motor screws.
7. Controllers on the arms; only two power leads per arm cross the hinge.
8. Hub 500 mm up and skids 450 mm apart, so the folded motors clear the ground (32 mm) and skids (17 mm).
9. Core payload rails, pin and socket under the hub; one standard payload plate.
10. Float release from a plate, printed saddles, a bought fail-closed release and a sewn sling.
11. Tether module on the same plate, with a breakaway connector.
12. GNSS mast on the deck centre.
13. Spacers and standoffs on the axes at 130 mm, clear of the pack straps (they overlapped).
14. Lightening pocket and window in the hinge blocks and root fittings (from 0.62 to 0.29 kg each).

**Appearance model.** `product_model.py` uses the `model.py` solids, flying-ready with the float release. Additions not in `model.py`: a 1.75 m mannequin (`mannequin()`, standing) beside the aircraft, to the left of it and slightly behind it as seen by the hero camera, never between the camera and the aircraft; and, for the detail view, one arm hinge in its own frame with short pieces of the hub plates and arm tube. Decided under the pre-approvals.

**Cross-repo actions** (shared-interface assumptions for the sibling sessions to confirm or correct; no sibling repository was edited):

- **Kitewright Core:** the stack fits 150 x 100 x 40 mm on four 10 mm rubber dampers at 130 x 80 mm centres, and weighs 1.0 kg with its payload mount (Core R9).
- **Kitewright Core:** payload mount as two rails 260 x 20 x 22 mm, inner faces 112 mm apart, with 8 mm x 8 mm slots; a 6 mm ball-lock payload pin through both rails 105 mm ahead of the centre and 8 mm below the mounting face; a DS-014 socket block 20 x 60 x 16 mm at the back, its face 132 mm behind the centre; M4 fixings into the frame; a standard payload plate 240 x 124 x 6 mm with a lock lug and plug pad. Range should use the same plate if its pod allows.
- **Kitewright Core:** the power bus takes two ColdCell packs at about 51 V and a tether input (51 V from an onboard isolated converter, up to 4 kW, ORed with the packs) without adaptive tether voltage.
- **ColdCell:** a 16S2P LiFePO4 pack of 26650 power cells (3.0 Ah, 30 A), 126 x 232 x 85 mm, about 3.3 kg and 307 Wh, plugging into the Core bus; the cells must be power-rated (16 A per cell in hover).
- **ColdCell:** if Amish chooses decision 2 A, a lithium-ion variant (14S3P 21700 high-power cells, about 680 Wh and 3.6 kg) in the same envelope; this widens ColdCell's chemistry constraint.
- **AltiRig:** measure a 30 x 10 propeller on a 100 KV class motor at sea level and 5,000 m density, upper and lower rotor of a coaxial pair 170 mm apart.
- **Kitewright Range:** if Range uses the same motors or packs, share the AltiRig and ColdCell results; Lift's arm hinge is not shared.

**Safety concerns.**

- An arm folding in flight would be fatal to the aircraft; the stop bridge carries the lift so the pin never does, and each hinge is proof-loaded to 1.5 times its full-thrust moment before first flight (safety stop).
- Eight 30 inch propellers: 15 m keep-out when armed; first power with propellers off.
- The 400 V tether is a dangerous voltage: isolated, monitored supply, residual-current protection, emergency stop, breakaway, no handling while live, 50 m highest hover.
- Pack fire after a crash or a cold charge; ColdCell's rules apply, and more so with a lithium-ion variant.
- Downwash (about 7.5 m/s at 10 m, estimated) can push a person in water under or knock someone over on snow; drops from 10 m or higher, and the figure is to be measured.
- The motor-out case is on paper only; yaw control after a motor loss is shown in a cut test over cleared ground.

**Recommended next step.** After Amish decides the two items above (and ColdCell confirms its pack envelope), the design is ready for TRL 4 when the phase allows: AltiRig thrust runs, hinge proof loads on CalRig, first power-up and tethered hovers, then the motor-cut and drop trials with the first co-design candidate. Suggestion not added to the repo: a snow and soft-ground foot that clips onto the skids.

## Session 2026-09-30: scaffolded

### What was done

- Repository created from kit 1.6.0 at TRL 1, target TRL 2.
- `docs/01-problem.md` (KWL-PRB-001 v0.1): problem with cited evidence, users, environment, constraints, prior work, open questions.
- `docs/02-concept.md` (KWL-PRC-001 v0.1): how it works, components, patent design-arounds, shared blocks, safety.
- `docs/03-requirements.md` (KWL-REQ-001 v0.1): 11 proposed requirements.
- `README.md` with concept rationale, burning platform, where it could be used, and what sparked the idea.

### Next

- Run `/populate` to bring the repo to a strong TRL 2 with concept media.

## 2026-10-03: photoreal renders

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.
