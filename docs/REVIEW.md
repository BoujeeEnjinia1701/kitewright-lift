# Review note: Kitewright Lift

## 2026-10-04: Amish's round-3 decisions carried out

Amish Chadha (owner) on 2026-10-04: "For round 3, I agree with all your proposed recommendations". For Lift that is the Kitewright family reconciliation: 8A (ColdCell's pack as drawn is the Lift pack), 9A (ColdCell's 50 °C warning and the warm-weather limit) and 10A (AS150 everywhere, one Core mounting envelope). Kitewright Core, Kitewright Range, ColdCell, AvalancheScout and LakeWatch were brought to the same table in the same session. Recorded in `docs/decisions/0004-family-reconciliation.md` (KWL-DDR-004) and the register (`docs/06-design-decisions.md` v0.3). Nothing was committed or pushed.

### Changes made

- **8A, battery deck re-sized for two ColdCell packs of 410 x 94 x 94 mm and 4.46 kg** (`cad/src/model.py`): packs side by side in Y with a 30 mm gap for the GNSS mast; deck 430 x 280 x 2 mm carbon (was 330 x 290 x 3) with four 120 x 60 mm windows; on 60 mm standoffs (were 25) so its underside is 9 mm above the upper blades, with the deck's corner cuts 12.7 mm and the pack corners 22.7 mm outside the upper discs in plan; guides 15 x 15 x 1.5 angle, 340 mm; four 900 mm straps round both packs. Deck check added: 19 MPa at mid-span and 27 MPa through the windows at a 3 g landing.
- **8A, R1 and R2 restated** (`docs/03-requirements.md` v0.4, Amish quoted): 25 kg take-off limit kept (US 55 lb class); payload rated at what fits; both designed payloads must fit.
- **9A:** ColdCell's 50 °C warning kept; warm-weather limit (about 27 °C ambient for a full hover flight; at 45 °C the warning after about 6 min) in the build plan's operating note (section 3.17) and in R10.
- **10A, the Core to the family envelope** (new `cad/src/core_envelope.py`, the same file as Range's): the Core plate hangs under the bottom hub plate on its 8 mm spacers (M4 on 220 x 130 mm), its lid up through a 200 x 112 mm opening that replaces the damper, rail and socket holes; the top plate has holes over the lid's mast boss (26 mm), SMA bulkheads (12 mm) and switch (20 mm); the Core's GNSS receiver goes on Lift's deck mast and its antennas on SMA extension leads to the gear struts. Payloads hang from 184 x 128 x 5 mm payload shoes (KWC-DWG-106) inside the Core's 88 mm neck: float saddles 80 mm wide and 55 mm tall; the tether converter on four 34 mm posts, 20 mm ahead of the pin knobs. AS150 on every pack and bus lead. New model checks: payload parts outside the neck zone, the Core's parts against the hub.
- Constructability checks pass in all three states (flying with the float release, flying with the tether module, folded): no overlaps, nothing out of contact. STEP and STL regenerated.
- **BOM** (`bom/bom.csv`, 39 lines): lines 1, 2, 3, 17, 18, 19, 21, 22, 23, 24, 26, 27 and 31 changed, each with a price basis; new line 39, ColdCell's ground equipment (USD 255, not in R11).
- Documents: `docs/04-calcs/01-sizing.md` v0.3 with `sizing.py` and `results.csv`, `docs/05-build-plan.md` v0.3, `docs/02-concept.md` v0.4, `docs/03-requirements.md` v0.4, `docs/06-design-decisions.md` v0.3, `README.md`.

### New result per requirement (KWL-CAL-001 v0.3, estimates)

| ID | Before (v0.2) | Now | Target |
| --- | --- | --- | --- |
| R1 | 25.2 kg with 5 kg, not met | 24.98 kg with the rated 3.2 kg; 21.78 kg ready to fly: met on paper as restated | 25 kg or less with the rated payload |
| R2 | 4.77 kg inside R1, at risk | Rated 3.2 kg; float release 1.46 kg and tether module 3.13 kg (on payload shoes) both fit; met on paper as restated | About 3.3 kg, both payloads fit |
| R3 | Thrust to weight 1.97 | 1.84 at 5,000 m with 2 kg: met on paper | 2 kg at 5,000 m |
| R4 | 20.1 and 16.1 min | 20.4 min at sea level with the rated payload, 14.5 min at 5,000 m with 2 kg: met on paper (R4 restated to the rated payload, open decision 4 closed) | 20 and 10 min |
| R5 | 2.22 and 1.53 | 2.24 and 1.43: met on paper | Controlled descent |
| R7 | Converter margin 1.37 | 1.25 at 3.2 kW: met on paper | 2 h on the tether |
| R9 | 0.84 x 0.48 x 0.45 m | 0.88 x 0.48 x 0.45 m: met on paper | 1.2 x 0.6 x 0.5 m case |
| R10 | Part ratings | Part ratings; full hover flights to about 27 °C ambient (9A) | -20 to +45 °C |
| R11 | USD 6,335 | Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 6,627 (USD 1,627 over the target) | Reported against the target |

R6 and R8 are unchanged and met on paper. Mass: ready to fly 1.55 kg heavier (packs +1.80 kg; deck, guides and bottom plate opening -0.29 kg; standoffs and antenna leads +0.04 kg). Cost: ColdCell's packs USD 268 more (USD 762 each against USD 628 assumed), deck USD 5, straps USD 4, antenna leads USD 15. `budget_usd` unchanged.

### Kitewright interface table

The same table stands in the review notes of Kitewright Core, Kitewright Lift, Kitewright Range, ColdCell, AvalancheScout and LakeWatch (Amish's decision 10A, 2026-10-04). The Core's drawings are the reference for the mounting envelope.

| Interface | Family figure | Source |
| --- | --- | --- |
| Power connector | AS150 on every pack lead and on each frame's power harness (two pack inputs, two frame outputs, opposite genders); no XT60 or XT90 on the bus | Decision 10A; KWC-DDR-001, D3 |
| Core mounting envelope and hole pattern | Core plate 240 x 150 x 2 mm hung under the frame's lower deck on four 12 mm OD x 8 mm corner spacers; four M4 holes on a 220 x 130 mm pattern; a 200 x 112 mm opening in the deck for the lid; lid 168 x 92 mm, its top 55 mm above the deck's underside (GNSS mast boss 69 mm); where a frame has no 240 mm clear above the lid, the antennas and GNSS receiver go to frame positions on extension cables; rail, pin blocks and pin knobs to 47 mm below the plate top; payload shoe 184 x 128 x 5 mm, payload neck 88 mm wide from the shoe to 30 mm below the rail lips | KWC-DWG-001 Rev P2, KWC-DWG-106 |
| Bus voltage | 18 to 60 V at the Core's pack inputs. Lift: 14S lithium-ion, 42.0 to 58.8 V (50.4 V nominal). Range: 6S lithium-ion, 18.0 to 25.2 V (21.6 V nominal) | KWC-DDR-001, D3 |
| Pack size and mass | Lift: two ColdCell 14S3P lithium-ion packs, 410 x 94 x 94 mm, 4.46 kg and 680 Wh each (CCL-DWG-002). Range: two 6S3P lithium-ion packs of 5.0 Ah cells, 138 x 75 x 82 mm, 1.40 kg and 324 Wh each (Range's figure; ColdCell has not yet drawn this pack) | Decision 8A; CCL-CAL-001 K; KWR-CAL-001 |
| Core mass | 0.99 kg: avionics, radios, GNSS, rail and locking pins; packs, payload shoe and the frame's harness excluded | Core R9; KWC-DDR-003 |

### Pictures changed

KWL-DWG-001 general arrangement Rev P4 and KWL-DWG-002 folded Rev P3; making sketches KWL-DWG-101 (top plate), 102 (bottom plate), 103 (deck), 111 (guide), 112 (payload shoe) and 113 (saddle) to Rev P2, the others redrawn unchanged; build plan overview, all eleven joints (joint-07 now the payload shoe on the Core rail, joint-11 the Core under the hub) and all sixteen steps (step 2 the hub spacers, step 6 the Core hung under the hub, step 12 the mast and antenna leads); concept media (`media/hero.png`, `cutaway.png`, `exploded.png`, `flow.png`, `concept-blueprint.png` and `.pdf` Rev P3, `model.glb`). Looked at: the general arrangement and joint-11. `cad/src/product_model.py` takes the new parts from `model.py`; render scenes exported to `/home/claude/renders/kitewright-lift` (hero, exploded, detail). The photoreal renders, captions and cards in `media/` predate this change and need a re-run on Amish's Mac.

### Open decision 4 closed: R4 restated (consequence of 8A)

Amish Chadha, 2026-10-04: "For round 3, I agree with all your proposed recommendations". Because decision 8A rates the payload at what fits inside R1's 25 kg, R4's sea-level case no longer names 5 kg. **R4 restated** (`docs/03-requirements.md` v0.5, Amish quoted): "at least 20 min with the rated payload (R2) at sea level and 10 min with 2 kg at 5,000 m and -20 °C". Result unchanged: 20.4 min at sea level with the rated 3.2 kg and 14.5 min at 5,000 m with 2 kg, **met on paper**. Records only: no change to the model, calculations, BOM or pictures. Recorded in `docs/decisions/0005-r4-rated-payload.md` (KWL-DDR-005) and the register (`docs/06-design-decisions.md` v0.4, open decision 4 moved to Decisions made).

**Open decisions.** None. Nothing in carrying out 8A, 9A, 10A or open decision 4 needs Amish.

### Safety

- Two packs hold 1.36 kWh of lithium-ion cells: ColdCell's charge blocking below 5 °C, heater cut-outs, cell fuses and fire-resistant charging box apply in full, and the 50 °C warning lands the aircraft; on hot days flights are short.
- The deck now sits above the upper rotors and outside their discs in plan; the deck standoffs and strap buckles are checked tight before every flight.
- The tether module's margin under 25 kg is 0.07 kg: weigh it at TRL 4 before any tethered flight with it.

### Cross-repo actions

- **AvalancheScout:** the reconciled Lift puts its power harness at the Core's power board, about 12 mm above the payload shoe, and its eight motors 0.62 m out; AvalancheScout's noise check against this Lift is in its own review note. Twisting and choking Lift's pack and frame leads (its earlier option C) is now worth planning into Lift's harness at TRL 4.
- Nothing else outstanding: Core, Range, ColdCell and LakeWatch carry the same interface table.

### Recommended next step

Nothing awaits Amish. The design is ready for TRL 4 when the phase allows, as before (AltiRig thrust runs, hinge proof loads, first power-up and tethered hovers).

## 2026-10-03: Amish's requirement decisions carried out

Amish Chadha, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." For Lift that decides item 34 (open decision 1) and item 35 (open decision 2) as recommended, option A on both; Kitewright Core's decision 33B also moves the frame power leads out of the Core and into Lift. Recorded in `docs/decisions/0003-requirement-decisions.md` (KWL-DDR-003) and the register (`docs/06-design-decisions.md`, KWL-DEC-001 v0.2). Kitewright Core, Kitewright Range and ColdCell were being updated in parallel by other sessions and were not edited.

**Changes made, each with its new result.**

- **34A, lighter fittings** (`cad/src/model.py`): hinge blocks with side pockets in the bolting end, an 18 x 46 mm window through both cheeks, and the cheeks cut away below the pivot outboard and under the stop bridge to a 15 mm top rail (0.29 to 0.19 kg each); root fittings with 12.5 mm side pockets leaving a 5 mm web and 5 mm bosses round both holes, and a 22 x 28 mm window (0.29 to 0.24 kg each); motor clamps shortened from 50 to 40 mm (0.24 to 0.19 kg each), so the arm tubes are cut to 405 mm. Saving 0.78 kg against the 1.04 kg estimated when the decision was posed: the root fittings' thin collar and the full-width bosses at their two holes leave less to remove. Highest new stress 35 MPa in the top rail under the bridge (a third of yield is 80 MPa); the bridge itself, 41 MPa, is unchanged. All constructability checks pass in the three states (flying with the float release, flying with the tether module, folded): no overlaps, nothing out of contact.
- **35A, lithium-ion ColdCell packs** (BOM line 23): 14S3P of 21700 high-power cells (4.5 Ah, 45 A), 50.4 V nominal, about 680 Wh and 3.56 kg each, in the same 126 x 232 x 85 mm envelope; ColdCell's charge blocking below 5 °C, heater cut-outs, cell-level fuse and fire-resistant charging box apply in full. USD 628 each (USD 208 more). **R4 met on paper: 20.1 min at sea level with 5 kg (target 20) and 16.1 min at 5,000 m and -20 °C with 2 kg (target 10).** About 11 A per cell in hover against 45 A.
- **Frame-to-Core power leads** (Core decision 33B; BOM line 24, build plan section 3.17a): 8 AWG wire and four AS150 halves, about 0.12 kg and USD 60; the Core is taken at 0.99 kg.

**Results against the requirements (KWL-CAL-001 v0.2).**

| Requirement | Before | Now | Status |
| --- | --- | --- | --- |
| R1, take-off mass with 5 kg (25 kg or less) | 25.5 kg | 25.2 kg; 20.2 kg ready to fly | Not met, by about 0.2 kg (decision 3 below) |
| R2, 5 kg at sea level | 4.5 kg inside R1 | 4.77 kg inside R1; thrust to weight 2.85 | At risk (decision 3 below) |
| R3, 2 kg at 5,000 m | Thrust to weight 1.94 | 1.97 | Met on paper |
| R4, hover time (20 and 10 min) | 8.9 and 7.1 min | 20.1 and 16.1 min | Met on paper |
| R5, motor out | 2.20 and 1.51 | 2.22 and 1.53 | Met on paper |
| R7, tethered endurance | Converter margin 1.35 | 1.37 | Met on paper |
| R10, temperature | 53 Wh pre-heat | 58 Wh pre-heat | Met on paper |
| R11, cost | USD 5,739 | Value-engineering target: USD 5,000. Estimated cost of the constructable design: USD 6,335 (USD 1,335 over the target) | Reported against the target |

R6, R8 and R9 are unchanged and met on paper. `budget_usd` is unchanged.

**Pictures changed.** KWL-DWG-001 general arrangement Rev P3 and KWL-DWG-002 folded Rev P2; making sketches KWL-DWG-104 (hinge block), 105 (root fitting), 106 (arm tube) and 107 (motor mount) Rev P2; the build plan overview, joints and steps redrawn from the model (step 13 now plugs the packs into the frame leads); concept media (`media/hero.png`, `cutaway.png`, `exploded.png`, `flow.png`, `concept-blueprint.png` and `.pdf` Rev P2, `model.glb`). `docs/05-build-plan.md` v0.2 (sections 2, 3.2, 3.5, 3.9, 3.10, 3.11, 3.17, new 3.17a, step 13, safety stop 2), `docs/04-calcs/01-sizing.md` v0.2, `docs/03-requirements.md` v0.3, `docs/02-concept.md` and `README.md` figures. Appearance model (`cad/src/product_model.py`) takes the lightened parts from `model.py`; scenes re-exported to `/home/claude/renders/kitewright-lift` (hero, exploded, detail). The photoreal renders on Amish's Mac predate this change and should be re-rendered.

**Decision for Amish.**

*Decision 3: R1 and R2, take-off mass with a 5 kg payload, after decisions 34A and 35A.* State: the aircraft weighs 25.2 kg with a 5 kg payload, about 0.23 kg over R1; inside R1 it carries 4.77 kg. Cause: the lightened fittings saved 0.78 kg rather than the estimated 1.04 kg, the lithium-ion packs add 0.44 kg and the frame-to-Core leads 0.12 kg. R1 sits at the 25 kg line that matters for permissions (the US Part 107 class is under 55 lb, 24.9 kg), so restating R1 upward has a cost beyond the number.

| Option | Effect on R1 and R2 | Cost | Mass |
| --- | --- | --- | --- |
| A: rate the sea-level payload at 4.7 kg (restate R2 as "4.7 kg on the core mount at sea level"); the TRL 4 weigh-in sets the final rating | R1 met at 24.9 kg; R2 met as restated; R4 20.3 min. The float release (1.6 kg) and tether module (3.3 kg) both fit | None | None |
| B: lightening windows in the battery deck (two 80 x 160 mm under the packs) and the top hub plate (four 60 x 50 mm), and rate the payload at 4.9 kg | R1 met at 24.95 kg with 4.9 kg; deck and plate stiffness to be checked | About USD 15 more routing (estimate) | About 0.18 kg less |
| C: restate R1 to 25.5 kg and keep the 5 kg payload | Both met as restated | None | None, but above the 24.9 kg (55 lb) line, so more permission paperwork at test sites |

**Recommendation: A.** It costs nothing, every payload designed so far is well under 4.7 kg, it keeps Lift inside the 25 kg class, and the real mass from the TRL 4 weigh-in (bought masses are class estimates) decides whether the full 5 kg can be restored. Listed in the register as open decision 3, "Proposed, awaiting Amish".

**Cross-repo actions** (not edited here):

- **ColdCell:** add and confirm the lithium-ion variant for Lift (decision 35A): 14S3P of 21700 high-power cells, 4.5 Ah and 45 A, about 680 Wh and 3.56 kg, in the 126 x 232 x 85 mm envelope, 85 % of rated energy at -20 °C with the heater running; charge blocking below 5 °C, heater cut-outs, cell-level fuse and fire-resistant charging box. Lift's R4 margin at sea level is 0.1 min, so a lower energy figure from ColdCell would put R4 at risk again.
- **Kitewright Core:** Lift now supplies the pack and frame leads (8 AWG, AS150) soldered to the Core's pads (decision 33B), and takes the Core at about 0.99 kg.

**Safety.** Lithium-ion packs carry more fire energy than the LiFePO4 packs first planned: the build plan's section 3.17 and safety stop 2 now require ColdCell's charge blocking below 5 °C, heater cut-outs, cell fuses and charging only in the fire-resistant box, and a polarity and insulation check of the new frame-to-Core leads before the first pack is plugged in. The lightened hinges keep every stress under a third of yield and are still proof-loaded to 117 N m before first flight.

**Recommended next step.** Amish decides decision 3; ColdCell confirms its lithium-ion variant. The design is then ready for TRL 4 when the phase allows (unchanged from the TRL 3 recommendation below).

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

## 2026-10-04: photoreal renders redone after the round-2 and round-3 decisions

Views: hero, exploded, detail; cards regenerated; image_qc passes and `render.py --check` has no FAIL.
