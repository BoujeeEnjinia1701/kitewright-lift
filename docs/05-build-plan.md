---
doc_id: KWL-BLD-001
title: Kitewright Lift prototype build plan
project: Kitewright Lift
doc_type: Build plan
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First build plan; design made constructable (KWL-DDR-002)
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Round 2 decisions (KWL-DDR-003): deeper pockets in the hinge blocks, root fittings and motor clamps; lithium-ion ColdCell packs on a 290 x 430 mm deck; Core power leads now in Lift's harness"
---

# Kitewright Lift prototype build plan

**Plan, not yet built.** How to build the first proof-of-concept prototype, component by component. Building and testing to it is TRL 4 work. Decisions still to be made are kept in the design decisions register (`docs/06-design-decisions.md`), not here.

> **Safety:** This plan builds a 25 kg class aircraft with eight 30 inch propellers, two 680 Wh lithium-ion packs and a 400 V tether. Propellers can kill, lithium-ion packs can burn violently and spread fire from cell to cell, and the tether carries a dangerous voltage. Every safety stop in section 6 is a hard stop: work does not go on until its conditions are true. Fly only where local rules allow, never near uninvolved people, and never carry or lift a person.

## 1. What you are building

![Every component, pulled apart and numbered in build order](05-build-plan/overview.png)

*Figure 1. Every component in build order. One of the four arms is shown pulled apart; the others are the same.*

Kitewright Lift is a coaxial eight-motor aircraft: a two-plate carbon hub with the Kitewright Core stack inside, four carbon arms that fold down on machined aluminium hinges, a motor above and below each arm tip, a battery deck with two ColdCell packs on top, skid landing gear, and the Core payload rails underneath. Two payloads are built with it: a line-and-float release and a tether power module with its ground set. Of the 38 lines in the parts list, 16 are made: carbon sheet routed to shape, carbon tube cut and drilled, aluminium fittings machined, two printed saddles and a sewn sling. The rest are bought, and the Core stack and the packs are built to their own designs. The parts are estimated at USD 6,418 for the aircraft and USD 3,716 for the payloads and ground set.

## 2. What changed to make it buildable

| Component | The concept had | The buildable design has | Why |
| --- | --- | --- | --- |
| Arm fold | Folding arms, no joint drawn | A machined hinge block at each hub corner: a slot for the arm's tongue, an 8 mm pivot bolt near the bottom, an 8 mm lock pin, and a stop bridge across the top | Lift presses the arm up against the bridge, so the arm cannot fold under power; the pin only stops it drooping |
| Arm root | Tube into the body | A one-piece aluminium fitting: a tongue in the hinge and a collar round the tube | A solid seat for the pivot and lock holes; the tube is bonded and bolted in |
| Hinge position | Not set | Pivot 180 mm from the centre and the plate corners cut at 162 mm | The folded arm otherwise cut into the bottom plate; now 6 mm clear |
| Central body | A body | Two 3 mm carbon plates 60 mm apart on the hinge blocks and four spacers, the Core stack inside on dampers | A light, stiff box with the avionics protected |
| Battery bay | Two heated packs | A carbon deck on four standoffs above the top plate, two guides and four cam straps | Packs clear of the hinge pins and of the rotors |
| Motor mount | Not drawn | A split clamp on the arm tip with a motor on its top face and one under it | Thick enough above the tube for the motor screws |
| Motor controllers | Not placed | Strapped to the arm near the tip | They fold with the arm; only two power leads cross the hinge |
| Landing gear | Wide gear | Four carbon struts in machined blocks, skids 450 mm apart, hub 500 mm up | Folded motors clear the skids and the ground |
| Payload bay | Clear space | The Core's slotted rails, payload pin and DS-014 socket; one standard payload plate | Every payload fits the same way and is pinned through both rails |
| Float release | A release | Plate, printed saddles, a servo pin release and a sewn sling round a foam float | Bought release, simple made parts |
| Tether module | Converter and reel | Plate, 4 kW converter, breakaway connector; ground supply, reel and safety set | Fits the same rails; parts if the tether snags |
| Fittings | Solid blocks | A pocket in each hinge block and a window in each root fitting | Halves their weight |
| Deeper pockets | Fittings with one pocket or window | Side pockets in the hinge blocks, root fittings and motor clamps, leaving at least 4.5 mm round every hole, boss and face | 0.41 kg lighter in all (Amish's decision 1, KWL-DDR-003) |
| Packs and deck | Two LiFePO4 packs 126 x 232 x 85 mm on a 330 x 290 mm deck | Two lithium-ion ColdCell packs 90 x 378 x 86 mm on a 290 x 430 mm deck, guides 210 mm long | Hover time (Amish's decision 2, KWL-DDR-003) |
| Core power leads | Four 8 AWG leads with AS150 plugs inside the Kitewright Core | Part of Lift's harness, soldered to the Core's board pads and tied to its strain-relief bar | The Core's mass (Kitewright Core decision O1, KWC-DDR-003) |

## 3. Making the components

Sizes are in millimetres unless stated. Carbon sheet and tube: cut with a diamond or carbide tool, wear a dust mask and gloves, and seal cut edges with thin epoxy. Aluminium fittings are 6061-T6, machined by a machine shop or an online CNC service from the making sketches; deburr every edge.

### 3.1 Bottom hub plate

![Making sketch: bottom hub plate](../cad/drawings/KWL-DWG-102.png)

**What it is and what it is made from.** The floor of the hub: 3 mm woven carbon sheet, 280 mm square with each corner cut square to its arm.

**How to make it.**

1. Route the outline: 280 x 280 with each corner cut off by a 72 mm face, 162 mm from the centre measured along the diagonal.
2. Drill four 4.3 mm holes per corner for the hinge block: on the diagonal, 131 and 144 mm out from the centre, 15 mm either side.
3. Drill four 3.3 mm spacer holes 130 mm from the centre on the forward, back, left and right lines.
4. Drill four 3.3 mm holes for the Core dampers on a 130 x 80 mm rectangle round the centre.
5. Drill eight 4.3 mm holes for the gear top blocks: 60 mm either side of the centre line fore and aft, 97 and 127 mm out to each side.
6. Drill six 4.3 mm holes for the payload rails at 100 mm ahead, at the centre and 100 mm behind, 71 mm either side; three 4.3 mm holes for the DS-014 socket block 142 mm behind the centre; a 24 mm cable hole 40 mm ahead of the centre.
7. Seal the edges.

**How it fits the parts next to it.** The hinge blocks, spacers and Core dampers sit on its top face; the gear top blocks, payload rails and socket block hang under it. Every fixing is a screw through the plate into a tapped hole in the part.

**Check before moving on.** Lay the top plate on it: every shared hole lines up.

### 3.2 Arm hinge blocks (four)

![Making sketch: arm hinge block](../cad/drawings/KWL-DWG-104.png)

**What it is and what it is made from.** The joint between hub and arm, and the spacer between the hub plates at each corner: 6061-T6 aluminium from 50 x 50 bar, 90 x 46 x 60 mm.

**How to make it.**

1. Square the block to 90 long, 46 wide, 60 high.
2. Mill the 32 mm slot from 25 mm in from the inner end to the outer end, open at the bottom, and open at the top except for a 10 x 10 mm bridge across the outer end.
3. Ream the 8.05 mm pivot hole through both cheeks, 14 mm up from the bottom and 55 mm from the inner end.
4. Drill the 8.1 mm lock-pin hole, 37 mm up and 68 mm from the inner end.
5. Tap four M4 holes 10 deep in the top face and four in the bottom face, 6 and 19 mm from the inner end, 15 mm either side.
6. Mill the 19 x 16 mm lightening pocket through between the tapped holes.
7. Mill a side pocket into each side face of the bolting end: 4.5 to 23 mm from the inner end, 16.5 to 43.5 mm up from the bottom, 10.5 mm deep, so 4.5 mm stays between it and the through pocket and 4.5 mm round the tapped holes above and below.
8. Mill 2.5 mm deep pockets into the outside face of each cheek, leaving 4.5 mm of cheek: one from the slot's start to 8.5 mm short of the pivot hole, one above the pivot hole up to 8.5 mm short of the lock-pin hole, and one beyond the pivot hole below the lock-pin hole, each ending 4.5 mm from the top and bottom faces and clear of the bridge (KWL-DWG-104).
9. Deburr. The underside of the bridge must be flat and smooth: it carries the arm's lift.

**How it fits the parts next to it.**

![Close-up: arm hinge, cut open](05-build-plan/joint-01.png)

*Figure 2. The arm hinge cut open on the arm's centre line. In flight the tongue's top presses up on the bridge; the pivot bolt is near the bottom; the lock pin stops the arm drooping.*

The block sits between the hub plates with its slot facing out along the diagonal. The arm's tongue fits the slot with 1 mm each side, turns on the pivot bolt, and in flight bears up against the bridge. The lock pin passes through both cheeks and the tongue.

**Check before moving on.** An 8 mm pin slides through both pivot holes and both lock holes in one line.

### 3.3 Top hub plate

![Making sketch: top hub plate](../cad/drawings/KWL-DWG-101.png)

**What it is and what it is made from.** The roof of the hub, 3 mm carbon sheet, the same outline as the bottom plate.

**How to make it.**

1. Route the same outline as the bottom plate.
2. Drill the same hinge-block and spacer holes.
3. Drill a 30 mm hole at the centre for the pack leads and the mast cable.
4. Seal the edges.

**How it fits the parts next to it.**

![Close-up: hinge block between the hub plates](05-build-plan/joint-02.png)

*Figure 3. Each hinge block is held by four M4 screws up through the bottom plate and four down through the top plate.*

**Check before moving on.** It lies flat on all four hinge blocks and spacers with no rocking.

### 3.4 Hub spacers and deck standoffs (bought)

Buy four 60 mm and four 25 mm aluminium round standoffs, 8 mm across, M3 inside both ends. The 60 mm spacers hold the hub plates apart beside the Core; the 25 mm standoffs carry the battery deck. One long M3 screw through the deck, a standoff, the top plate and a spacer ties each stack.

### 3.5 Kitewright Core stack and payload mount (built to the Core design)

Build the Core stack, its power bus with the tether input, and its payload mount (two slotted rails, the payload pin and the DS-014 socket block) to the Kitewright Core build plan. Lift needs the stack to fit a 150 x 100 x 40 mm space on four 10 mm rubber dampers, and the rails to be 260 mm long, 112 mm apart on their inner faces, with 8 mm slots.

![Close-up: Core stack between the hub plates, cut open](05-build-plan/joint-11.png)

*Figure 4. The Core on its four dampers between the hub plates, with the spacers and hinge blocks holding the plates apart.*

### 3.6 Gear top blocks (four)

![Making sketch: gear top block](../cad/drawings/KWL-DWG-108.png)

**What it is and what it is made from.** The fixing that holds each gear strut under the hub: 6061 aluminium, 30 x 40 x 25 mm.

**How to make it.**

1. Square the block.
2. Bore a 20.1 mm socket 20 mm deep from the bottom, leaning outward 13.4 degrees from vertical, its centre on the block's centre line 5 mm below the top face.
3. Tap two M4 holes 10 mm deep in the top face, 30 mm apart.
4. Make two left-hand and two right-hand, so each socket leans outward.

**How it fits the parts next to it.**

![Close-up: gear top block](05-build-plan/joint-05.png)

*Figure 5. Two M4 screws down through the bottom plate hold the block; the strut is bonded into its socket.*

**Check before moving on.** A strut offcut sits fully home in the socket.

### 3.7 Skid blocks (four)

![Making sketch: skid block](../cad/drawings/KWL-DWG-109.png)

**What it is and what it is made from.** The foot of each strut, where it meets the skid: 6061 aluminium, 30 x 30 x 50 mm.

**How to make it.**

1. Square the block.
2. Bore the 20.1 mm cross bore for the skid, its centre 17 mm up from the bottom.
3. Bore the 20.1 mm strut socket down from the top face, leaning inward 13.4 degrees, stopping 6 mm above the skid bore.
4. Drill a 4.3 mm hole up through the bottom face, 8 mm to the side of centre, through the skid bore.

**How it fits the parts next to it.**

![Close-up: skid block, strut and skid](05-build-plan/joint-06.png)

*Figure 6. The skid passes through the cross bore and is held by an M4 bolt; the strut is bonded into the socket above it.*

**Check before moving on.** The skid slides through the bore and a strut offcut sits home in the socket.

### 3.8 Gear struts and skids

![Making sketch: gear struts and skids](../cad/drawings/KWL-DWG-110.png)

**What it is and what it is made from.** Carbon tube 20 mm across, 17 mm inside.

**How to make it.**

1. Cut four struts 475 mm long and two skids 340 mm long; square the ends.
2. Drill each skid with two 4.3 mm holes, 118 and 238 mm from the same end.
3. Sand the bonding areas: 20 mm at each strut end, and the skid where it passes through each block.
4. Push a rubber cap on each skid end.

**Check before moving on.** The four struts are the same length within 1 mm.

### 3.9 Arm tubes (four)

![Making sketch: arm tube](../cad/drawings/KWL-DWG-106.png)

**What it is and what it is made from.** Roll-wrapped carbon tube 40 mm across, 36 mm inside, 410 mm long.

**How to make it.**

1. Wrap the cut line with tape and cut with a fine abrasive disc; square the ends.
2. In a wooden V block, drill three 5.2 mm holes square through both walls on one line: 10, 32 and 385 mm from the inner end.
3. Sand 45 mm at the inner end and 40 mm at the outer end for bonding.

**Check before moving on.** The four tubes are the same length within 0.5 mm.

### 3.10 Arm root fittings (four)

![Making sketch: arm root fitting](../cad/drawings/KWL-DWG-105.png)

**What it is and what it is made from.** One machined 6061-T6 piece: a 65 x 30 x 48 mm tongue with a 48 mm collar on its outer end.

**How to make it.**

1. Turn the collar to 48 mm and bore it 40.2 mm, 45 mm deep, on the tongue's centre height.
2. Mill the tongue to 30 mm wide and 48 mm high.
3. Ream the pivot hole 8.05 mm, 12 mm up from the tongue's bottom and 15 mm from its inner end; drill the lock-pin hole 8.1 mm, 35 mm up and 28 mm from the inner end.
4. Mill the 22 x 24 mm window through the tongue, 41 to 63 mm from its inner end.
5. Drill two 5.2 mm cross holes through the collar, 15 and 37 mm from its inner end.
6. Mill two side pockets 10 mm deep into each face of the tongue, leaving a 10 mm web on its centre line and 4.5 mm round both pin holes and the window: one above the pivot hole inboard of the lock-pin hole, one below the lock-pin hole beyond the pivot hole (KWL-DWG-105).
7. Keep the top face of the tongue's outer end flat: it bears on the bridge.

**How it fits the parts next to it.**

![Close-up: arm tube in the root collar, cut open](05-build-plan/joint-03.png)

*Figure 7. The tube goes 45 mm into the collar, bonded with structural epoxy and held by two M5 bolts through collar and tube.*

**Check before moving on.** The tongue swings freely in a hinge block's slot with about 1 mm each side.

### 3.11 Motor mounts (four)

![Making sketch: motor mount](../cad/drawings/KWL-DWG-107.png)

**What it is and what it is made from.** A split clamp on the arm tip, 50 x 60 x 52 mm, two halves of 6061-T6 machined together.

**How to make it.**

1. Square the block, bore it 40.2 mm on the split line, then saw it in two and face both halves so they close on the tube with a 0.5 to 1 mm gap.
2. Drill four 4.3 mm clamp holes through both halves, 8 mm in from the ends and 4.5 mm in from the sides.
3. Tap four M4 holes 9 mm deep in each outer face to suit the motors bought (a 35 mm circle on most motors of this class).
4. Drill a 5.2 mm cross hole through both halves at the motor axis.
5. Mill a pocket 20.7 mm long, centred on the motor axis between the clamp holes, into each side face of each half: 5.4 mm deep (4.5 mm left to the bore) and from 4.5 mm off the split face to 4.5 mm short of the motor face.

**How it fits the parts next to it.**

![Close-up: motor clamp at the arm tip, cut open](05-build-plan/joint-04.png)

*Figure 8. The clamp halves close on the tube with four M4 bolts and one M5 cross bolt through tube and clamp; the upper motor sits on the top face and the lower motor, upside down, on the bottom face.*

**Check before moving on.** The motor axis is square to the tube within 1 degree.

### 3.12 Motors, controllers and propellers (bought)

Buy eight brushless motors for 30 inch propellers, about 100 KV, rated 12S to 16S, about 450 g, with a maker's figure of about 10 kg static thrust on a 30 x 10 propeller at 51 V; eight controllers rated 16S and 80 A continuous with telemetry; and eight 30 x 10 carbon folding propellers, four turning each way. Upper and lower rotors on each arm turn opposite ways. Balance each propeller before fitting.

### 3.13 Pivot bolts and lock pins (bought)

Buy four stainless M8 shoulder bolts with an 8 mm shoulder 50 mm long, nyloc nuts and washers, and four 8 mm ball-lock pins with a grip of about 55 mm, a ring handle, a lanyard and a red flag. Tie each pin's lanyard to its hinge block so it cannot be lost.

### 3.14 Battery deck

![Making sketch: battery deck](../cad/drawings/KWL-DWG-103.png)

**What it is and what it is made from.** The shelf the packs sit on: 3 mm carbon sheet, 290 x 430 mm (290 mm across the aircraft's front-to-back line, 430 mm side to side) with 35 mm corner cuts, sized for the 378 mm long lithium-ion packs.

**How to make it.**

1. Route the outline.
2. Drill four 3.3 mm standoff holes 130 mm from the centre on the forward, back, left and right lines, and a 17 mm hole at the centre.
3. Cut eight 30 x 4 mm strap slots beside the ends of the packs, centred 30 and 90 mm either side of the centre, their inner edges 189.5 mm from the centre line.
4. Drill six 4.3 mm guide holes at the centre and 95 mm either side, 204 mm out on each side.

**How it fits the parts next to it.**

![Close-up: deck, pack guide, pack and strap](05-build-plan/joint-08.png)

*Figure 9. Each pack sits between its guide and the centre gap; a cam strap goes over it and through two deck slots.*

**Check before moving on.** Each strap threads through its pair of slots without twisting.

### 3.15 Pack guides (two)

![Making sketch: pack guide](../cad/drawings/KWL-DWG-111.png)

Cut two pieces of 20 x 20 x 2 mm aluminium angle 210 mm long, round the ends, and drill three 4.3 mm holes on the flat leg's centre line, 10, 105 and 200 mm along. Fit with the upright leg outboard. Check they sit flat on the deck.

### 3.16 Pack straps and GNSS mast (bought)

Buy four 25 mm cam-buckle straps 600 mm long with rubber backing, and a 16 mm carbon GNSS mast 230 mm long with a foot clamp.

### 3.17 ColdCell packs (built to the ColdCell design)

Two ColdCell lithium-ion packs to the ColdCell variant design (CCL-DWG-002): 14 cells in series, three in parallel, 21700 high-power cells of about 4.5 Ah, with the external film heaters, insulation, 14S BMS with charge lockout and 60 C discharge cut-out, and shell; 50.4 V, 680 Wh, about 3.84 kg, 378 x 90 x 86 mm, with an 8 AWG pigtail ending in an AS150 half. ColdCell has not yet issued a build plan for this variant (how its cells are joined is still open there), so the packs are the last item to be made.

### 3.18 Payload plates (two)

![Making sketch: payload plate](../cad/drawings/KWL-DWG-112.png)

**What it is and what it is made from.** The standard plate every payload is built on: 6061-T6, 240 x 124 x 6 mm.

**How to make it.**

1. Cut the plate square with straight, smooth long edges: they slide in the rail slots.
2. Cut two 50 mm lightening holes 100 mm apart on the centre line.
3. Screw and bond a 20 x 20 x 10 mm lock lug on top, its centre 7 mm from the front edge; drill a 6.3 mm hole across it, 5 mm above the plate.
4. Fit the DS-014 plug pad, 18 x 50 mm, on top at the rear edge.
5. Float release plate: tap M4 for the saddles and the release unit. Tether module plate: tap M5 for the converter's four corners.

**How it fits the parts next to it.**

![Close-up: payload plate in the Core rails, locked](05-build-plan/joint-07.png)

*Figure 10. The plate's edges slide in the rail slots; the payload pin passes through both rails and the lug.*

**Check before moving on.** The plate slides the full length of the rails without binding, and the pin goes through rails and lug together.

### 3.19 Float saddles (two)

![Making sketch: float saddle](../cad/drawings/KWL-DWG-113.png)

Print two saddles in PETG, 20 x 100 x 40 mm with a 121 mm round seat, seat up, four walls and 40 % infill; set two M4 heat-set inserts in each top face 60 mm apart. Check the float sits in both without rocking.

### 3.20 Float sling

![Making sketch: float sling](../cad/drawings/KWL-DWG-114.png)

Sew a ring of 25 mm polyester webbing 380 mm round to fit the float, with a bar tack. Sew an 80 mm tab to it with a 15 mm loop at its end for the release pin. The float's line is tied to the float only, never to the sling or the aircraft. Check that with the pin pulled the sling drops clear under the float's weight.

![Close-up: float release, cut open](05-build-plan/joint-09.png)

*Figure 11. The release unit's pin holds the sling's tab; the float sits in the two saddles.*

### 3.21 Release unit, float and line (bought)

Buy a servo-driven pin release rated 10 kg that stays closed when unpowered, a closed-cell foam rescue float about 120 x 420 mm (about 0.6 kg), and 30 m of 6 mm floating line in a throw bag that clips to the float's end.

### 3.22 Tether module and ground set (bought)

Buy an isolated DC-DC converter (380 to 420 V in, 51 V out, 4 kW, conduction cooled, about 200 x 110 x 65 mm), a two-pole 600 V breakaway connector that pulls apart at about 200 N, 60 m of tether with two 0.75 mm2 conductors and an aramid strength member, a 400 V DC isolated ground supply of 4.5 kW, a hand reel with a 600 V slip ring, and a ground safety set: insulation monitor, emergency stop, residual-current protection and an earth spike.

![Close-up: tether module](05-build-plan/joint-10.png)

*Figure 12. The converter on four M5 screws under the plate; the breakaway connector under its rear end.*

## 4. Putting it together

Use medium threadlocker on every metal-to-metal screw. Bonded joints use structural epoxy on sanded, cleaned surfaces and cure for 24 h before load.

### Step 1: Bolt the hinge blocks to the bottom plate

![Step 1](05-build-plan/step-01.png)

Four M4 x 10 screws up through the plate into each block, slot facing out along the diagonal.

### Step 2: Fit the Core stack and the hub spacers

![Step 2](05-build-plan/step-02.png)

Core stack on its four dampers; the four 60 mm spacers on M3 screws from below. Route the eight controller leads and the payload cable to the Core before the roof goes on. Lift's harness now carries the Core's four power leads (8 AWG, two pack inputs and two frame outputs with opposite-gender AS150 plugs): with the Core lid off, pass them in through its rear grommets, solder each to its marked pad on the Core's power board, refit the lid and tie them to the Core's strain-relief bar. **Hold point:** check the polarity of every lead at its plug with a meter.

### Step 3: Fit the top hub plate

![Step 3](05-build-plan/step-03.png)

Sixteen M4 screws down into the hinge blocks; the four 25 mm deck standoffs screwed through the plate into the spacers.

### Step 4: Build the landing gear

![Step 4](05-build-plan/step-04.png)

On a flat board, bond the struts into the top and skid blocks with the skids through their bores, and bolt each skid with its M4 bolt. Cure 24 h.

### Step 5: Bolt the gear under the hub

![Step 5](05-build-plan/step-05.png)

Two M4 screws down through the bottom plate into each top block.

### Step 6: Fit the Core payload mount

![Step 6](05-build-plan/step-06.png)

Rails on six M4 screws with their slots facing in; the DS-014 socket block at the back on three M4 screws.

### Step 7: Make up each arm

![Step 7](05-build-plan/step-07.png)

Bond the tube 45 mm into the root fitting's collar and 40 mm into the motor clamp, with the clamp's top face square to the tongue's top. Fit the two M5 bolts through collar and tube and the M5 bolt through clamp and tube; close the clamp's four M4 bolts. Cure 24 h. Make four.

### Step 8: Fit the motors and controllers

![Step 8](05-build-plan/step-08.png)

Upper motor on the clamp's top face and lower motor, upside down, on its bottom face, four M4 screws each. Strap a controller to each side of the tube near the tip and solder or plug the motor leads. Leave a 60 mm slack loop in the two power leads where they will cross the hinge.

### Step 9: Hang each arm in its hinge block

![Step 9](05-build-plan/step-09.png)

Slide the tongue into the slot, push the pivot bolt through block and tongue, and snug the nyloc nut so the arm swings without play. Swing the arm up until its tongue meets the stop bridge and push the lock pin home. **Hold point:** each hinge is proof-loaded before first flight (section 6).

### Step 10: Fit the propellers

![Step 10](05-build-plan/step-10.png)

Check the direction arrow on each hub against the motor's direction: upper and lower rotors on an arm turn opposite ways. **Hold point:** propellers stay off until the first power-up in section 5 is complete.

### Step 11: Fit the battery deck and pack guides

![Step 11](05-build-plan/step-11.png)

Deck on the four standoffs with M3 screws; guides on M4 screws, upright legs outboard; thread the four straps through their slots.

### Step 12: Fit the GNSS mast

![Step 12](05-build-plan/step-12.png)

Mast foot on the deck centre; lead the cable down through the deck and top plate to the Core.

### Step 13: Fit the ColdCell packs

![Step 13](05-build-plan/step-13.png)

Slide each pack between its guides, close its two straps, and plug its AS150 pigtail into a pack input lead of the harness. **Hold point:** packs go on only after the safety stop for first power (section 6).

### Step 14: Slide in the float release payload

![Step 14](05-build-plan/step-14.png)

From the front, slide the plate into the rail slots until its plug seats in the DS-014 socket; push the payload pin through both rails and the lug until its balls lock.

### Step 15: Or slide in the tether module

![Step 15](05-build-plan/step-15.png)

The same rails and pin. Plug the converter's output lead into the Core bus tether input and lead the tether through the breakaway connector.

### Step 16: Fold for transport

![Step 16](05-build-plan/step-16.png)

Take the payload off. For each arm, pull the lock pin, swing the arm down 90 degrees about its pivot, and turn both blades of each propeller back along the arm. Unfold in reverse; every lock pin goes back in and flagged before arming.

## 5. First checks

| Check | Requirement | How | Pass when |
| --- | --- | --- | --- |
| Weigh ready to fly, then with each payload | R1, R2 | Hanging scale | Mass recorded against R1 with the payload fitted (estimate 21.3 kg ready to fly) |
| Fold and pack | R9 | Fold, place in a 1.2 x 0.6 x 0.5 m case, unfold and time the set-up | Fits the case; set-up in 10 min or less |
| Hinge proof load | R5 (safety) | Each arm on CalRig at 117 N m (1.5 times full thrust) for 1 min | No movement at the stop, no crack, no yield |
| First power-up, propellers off | R10 | Core on the bench supply, then the packs; every motor turns the right way at low throttle | Each motor turns the right way; no fault on any controller |
| Motor and propeller thrust | R3 | AltiRig at sea-level and 5,000 m density | Full-throttle thrust per motor about 10 kg at sea level |
| Tethered hover on the ground set | R7 | Ground supply, insulation monitor, tether at 10 m height first | Bus steady at 51 V; no insulation alarm |
| Motor-cut test | R5 | One motor cut by the autopilot at 10 m over cleared ground | Controlled descent and landing |
| Hover time | R4 | Timed hover with 5 kg, logged energy | Time recorded against R4 |
| Float drop | R8 | Ten drops from 10 m onto a marked target on water | Float lands within the R8 distance |
| Wind hold | R6 | Logged position hold on a windy day | Position held within the R6 distance |

## 6. Safety stops

1. **Before any machining or cutting of carbon.** Dust extraction or a wet cut and a dust mask; carbon dust is an irritant and conducts electricity, so keep it away from the electronics.
2. **Before the first power-up.** Propellers off. The Core is powered from a current-limited bench supply first. Packs are charged and handled to ColdCell's rules: never charged below their lockout temperature, charged on a non-flammable surface with a lithium-rated extinguisher or sand to hand. The lithium-ion packs hold 680 Wh each: charge, pre-heat and store them in a fire-resistant container, never unattended, and never fly them above 25 C ambient with their jackets on until ColdCell's warm-weather question is settled.
3. **Before the first flight.** Every hinge proof-loaded on CalRig (section 5) and inspected; every lock pin in and flagged; propellers balanced and checked for cracks; failsafes for loss of link and low battery set and tested; nobody within 15 m; a written arming and keep-out procedure followed.
4. **Before energising the tether.** Ground supply earthed, insulation monitor and residual-current protection working, emergency stop tested, the tether laid clear of people, roads, water currents and power lines, and the breakaway fitted at the aircraft. Nobody touches the tether or the module while the supply is on. First tethered hovers at 10 m; never above 50 m.
5. **Before any payload drop.** Nobody under the aircraft except the person the float is for, who is approached from at least 10 m up; the float's line is tied to the float only. The release is tested on the ground first, with the aircraft unpowered.
6. **Before the motor-cut test.** Done over cleared ground at 10 m with a pilot ready to take over, and only after every other first check passes.
7. **After any hard landing.** Packs removed and watched outside for 24 h; hinges, bridges, pivots and arm tubes inspected before the next flight.

## 7. Tools, skills and workspace

- **Tools:** drill press and a wooden V block; hand drill; fine abrasive cut-off disc or a tube cutter for carbon; files and deburring tool; M3, M4, M5 and M8 hex keys and nut drivers; torque screwdriver; 3D printer (or a printing service); sewing machine for webbing (or a sail or upholstery shop); soldering station for the motor leads; hanging scale to 50 kg; multimeter; insulation tester for the tether set.
- **Bought machining:** the hinge blocks, root fittings, motor clamps and gear blocks are best made by a machine shop or an online CNC service from the making sketches; the carbon plates by a CNC routing service.
- **Skills:** careful drilling and bonding of carbon; multirotor assembly and autopilot setup (PX4 or ArduPilot); handling lithium packs; for the tether set, an electrician who works with DC above 120 V.
- **Workspace:** a clean bench with dust extraction for carbon work; a non-flammable area for pack charging; a clear outdoor flight area with permission, at least 30 m across, for the first flights.

## 8. Where the numbers come from

- `cad/src/model.py`: the parametric model and its constructability checks; STEP and STL in `cad/step` and `cad/stl`.
- `cad/drawings/KWL-DWG-001` (general arrangement), `KWL-DWG-002` (folded) and `KWL-DWG-101` to `KWL-DWG-114` (making sketches).
- `docs/04-calcs/01-sizing.md` and `docs/04-calcs/sizing.py` (KWL-CAL-001).
- `bom/bom.csv` (parts, specifications and indicative prices).
- `docs/decisions/0001-trl2-review-decisions.md`, `docs/decisions/0002-design-for-construction.md` and `docs/decisions/0003-requirement-decisions-round2.md`.
- `cad/src/build_plan_media.py` (every picture in this plan).
