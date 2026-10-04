# Review note: Kitewright Lift

## Session 2026-10-03: round 2 requirement decisions applied

Amish, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." For this repo that is decision 1 (global 18, R1 and R2) option A and decision 2 (global 19, R4) option A; Kitewright Core's decision O1 (global 17) option B also lands here, because the Core's pack and frame leads move into Lift's harness. Recorded in `docs/decisions/0003-requirement-decisions-round2.md` (KWL-DDR-003). ColdCell (CCL-DDR-003) and Kitewright Core (KWC-DDR-003) were edited in the same round so the three repos agree. Work stayed inside the TRL 3 cap: no test articles, test plans, firmware, PCB layouts, build-log entries or purchasing lists.

### What was done

- `cad/src/model.py`: side pockets in the hinge blocks (bolting end and cheeks), the root fittings (tongue) and the motor clamps, each leaving at least 4.5 mm round every hole, boss and face (`pockets`, `web`); pack envelope changed to ColdCell's lithium-ion variant, 90.4 x 378 x 85.8 mm; deck 290 x 430 mm (was 330 x 290); guides 210 mm at X -95, 0 and 95 mm. Constructability checks pass in the flying (float and tether) and folded states: no overlaps, nothing loose.
- `docs/04-calcs/sizing.py`, `results.csv` and `01-sizing.md` (KWL-CAL-001 v0.2): packs at ColdCell's estimate (3.84 kg, 680 Wh); pocket saving and deck growth taken from the model; wiring 0.77 kg with the Core leads; pre-heat from ColdCell; R10 now flags the packs' warm-weather limit; Table 5 compares the design before, between and after the decisions with the estimate they were posed on.
- `bom/bom.csv`: lines 4, 5 and 7 (pockets, USD 120 in all), 17 (deck), 18 (guides), 21 (Core note), 23 (lithium-ion packs, USD 662 each) and 24 (wiring with the Core leads, USD 150).
- Regenerated: STEP and STL; `cad/drawings/KWL-DWG-001` Rev P3 and `KWL-DWG-002` Rev P2; making sketches KWL-DWG-101 to 114, joints and steps; concept media (`media/hero.png`, `cutaway.png`, `exploded.png`, `flow.png`, `concept-blueprint.png` and `.pdf`, `model.glb` at 1.0 mm linear and 0.35 rad angular deflection).
- `docs/05-build-plan.md` (KWL-BLD-001 v0.2), `docs/03-requirements.md` (KWL-REQ-001 v0.3), `docs/02-concept.md` (KWL-PRC-001 v0.3), `docs/06-design-decisions.md` (KWL-DEC-001 v0.2), `README.md`, `cad/src/sheets.py`, `cad/src/build_plan_media.py`, `cad/src/concept_media.py`, `project.yaml` (trl_evidence). `budget_usd` stays 5,000: it is a value-engineering target, not a limit (STANDARDS section 18).

### Requirement status

| ID | Before | After |
| --- | --- | --- |
| R1 | Not met, 25.5 kg with 5 kg | **Not met, 26.3 kg with 5 kg** (21.3 kg ready to fly) |
| R2 | At risk, 4.5 kg inside R1 | **At risk, 3.7 kg inside R1** |
| R3 | Met on paper, thrust to weight 1.94 | Met on paper, 1.87 |
| R4 | Not met, 8.9 and 7.1 min | **Met at 5,000 m (15.0 min); not met at sea level with 5 kg (18.9 min, 1.1 min short)** |
| R5 | Met on paper, 2.20 and 1.51 | Met on paper, 2.13 and 1.46 |
| R7 | Met on paper, margin 1.35 | Met on paper, margin 1.28 |
| R10 | Met on paper (part ratings) | **At risk**: packs under 50 °C only to 25 °C ambient with jackets on |
| R11 | USD 739 over the target | USD 1,418 over the target |
| R6, R8, R9 | Met on paper | Unchanged |

Why the decisions did not deliver the 24.9 kg they were posed with (KWL-CAL-001 v0.2, Table 5): the pockets, drawn to the option's own rule of 4 to 5 mm walls and webs, save 0.41 kg rather than 1.04 kg (0.63 kg short); ColdCell's design of the variant weighs 3.84 kg a pack rather than the 3.56 kg assumed (0.57 kg for two); the long packs need a larger deck and guides (0.12 kg); and the Core's leads (0.12 kg) now ride in Lift's harness while the Core allowance stays 1.0 kg.

### Cost

Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 6,418 (USD 1,418 over the target); before: USD 5,739. Changes: packs USD 484, pockets USD 120, Core leads USD 60, deck USD 15. Payloads and ground set unchanged at USD 3,716.

### Cross-repo consistency

- **ColdCell**: Lift's packs, deck, BOM line 23 and calculations use ColdCell's variant figures (CCL-DDR-003, CCL-DWG-002): 14S3P, 50.4 V, 680 Wh, 3.84 kg, 378 x 90 x 86 mm, USD 662, AS150 pigtail. The earlier interface assumption (126 x 232 x 85 mm, 3.3 kg LiFePO4) is withdrawn.
- **Kitewright Core**: Lift's harness carries the Core's two pack input and two frame output leads (8 AWG, AS150), soldered to the Core's board pads and tied to its strain-relief bar (KWC-DDR-003); the Core allowance stays 1.0 kg (Core estimate 0.996 kg). Core open decision O2 (60 V power board against the 58.8 V full 14S pack) bears on Lift; the controllers are rated 16S (67 V).

### New questions (Proposed, awaiting Amish)

**3. R1, R2 and R4 after round 2.**
- State: 26.3 kg with a 5 kg payload; 3.7 kg of payload fits inside 25 kg; hover 18.9 min at sea level with 5 kg and 15.0 min at 5,000 m with 2 kg.
- Option A: rate the sea-level payload at 3.5 kg for the first prototype (R2 restated): 24.8 kg, R1 met; about 20.5 min at sea level with 3.5 kg (estimate).
- Option B: a second lightening round: 2 mm carbon hub plates and deck (estimate 0.42 kg, after a stiffness check), ColdCell open decision 4 A (estimate 0.16 to 0.20 kg for two packs) and stress-sized pockets below 4.5 mm webs after a structural check; about 25.6 kg before that check, so still not met.
- Option C: raise R1 to 26.5 kg; 25 kg is a common threshold in drone rules (India's Small class, for one), so this changes the aircraft's regulatory class and the pitch.
- **Recommendation: A for the first prototype, with B pursued as value engineering** and revisited when the fittings and packs are weighed at TRL 4.

**4. R10 in hot weather.**
- State: the lithium-ion packs make 71 W each in hover; with their jackets on they stay under 50 °C for 20 minutes only up to 25 °C ambient; at 45 °C they would pass the typical 60 °C discharge limit.
- Option A: adopt ColdCell's summer configuration (top foam out, vented lid) above 15 °C (ColdCell open decision 6). Option B: rate Lift to 25 °C until measured. Option C: shorter hovers above 25 °C, landing when ColdCell reports 50 °C.
- **Recommendation: A**, following ColdCell open decision 6.

### Safety notes

- **Lithium-ion fire energy.** Lift now carries 1.36 kWh in two lithium-ion packs, about twice the LiFePO4 packs' energy, in cells that vent flammable gas and can drive their neighbours into thermal runaway. After a crash or hard landing the packs come out and are watched outside for 24 hours (safety stop 7); they are charged, pre-heated and stored in a fire-resistant container on a non-flammable surface, never unattended; ColdCell's 5 C charge lockout, heater cut-offs and new 60 C discharge cut-out apply in full; they cannot travel with air passengers and ship only as dangerous goods. Until question 4 is settled they are not flown above 25 °C ambient with their jackets on (added to safety stop 2).
- **Hinges.** The deeper pockets leave the stop bridge, the pivot and lock-pin bosses and the cheek at the pivot untouched, so the full-thrust stresses of KWL-CAL-001 F are unchanged; the 4.5 mm cheek walls beside the pockets are first-order only and the 1.5 times proof load of every hinge before first flight stays a hard stop.
- **Harness.** The Core leads are now soldered into the Core when Lift's harness is fitted; polarity and the opposite-gender keying are checked at a hold point (build plan step 2).
- **Rotor clearance.** The longer packs and larger deck bring the upper rotor discs to 35 mm from the packs and 19 mm from the deck in plan (was 58 and 47 mm); still clear on paper, with less margin than before.

### Re-render

Yes. The hero geometry changed visibly: the two packs are now long and narrow (90 x 378 mm, running side to side) on a deck 140 mm wider, and the fittings carry pockets. `media/render-hero.png`, the exploded and detail renders and the cards should be re-rendered on Amish's Mac.

### Checks

- `python cad/src/model.py --check`: no overlaps and nothing loose in all three states.
- `python .kit/render.py --check`: see this session's report; the only failure left is the missing `media/render-hero.png` storefront image of this working copy.

### Recommended next step

Amish decides open decisions 3 and 4 (and, in ColdCell, decisions 3 to 6 on the variant pack). The design is then ready for TRL 4 when the phase allows: AltiRig thrust runs, hinge proof loads on CalRig, first power-up and tethered hovers.

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
