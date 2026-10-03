---
doc_id: KWL-PRB-001
title: Kitewright Lift problem statement
project: Kitewright Lift
doc_type: Problem statement
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 2 and 3; first co-design candidate with a checklist; open questions answered by KWL-DDR-001 and KWL-CAL-001; safety section
---

# Kitewright Lift problem statement

In the first hours after a flood, landslide or mountain accident, rescuers often know roughly where people are but cannot reach them. A drone that can hover, carry a little and stay up would help, but the ones that can are closed and expensive.

## The problem

Disasters that cut roads and bridges leave people stranded for hours or days: Pakistan's 2022 floods damaged about 3,500 km of roads and 150 bridges ([UN News, 2022](https://news.un.org/en/story/2022/08/1125752)), and the 2023 Sikkim outburst destroyed 13 bridges ([Mongabay India, 2023](http://india.mongabay.com/2023/10/no-early-warning-system-and-insufficient-dam-safety-turned-sikkim-flood-deadly/)). In the mountains the air itself works against aircraft: at 5,000 m standard air density is 0.736 kg/m3 and temperature -17.5 °C ([Engineering ToolBox](https://www.engineeringtoolbox.com/standard-atmosphere-d_604.html)), so a frame sized at sea level can run out of thrust and battery.

Commercial heavy-lift drones such as the DJI FlyCart 30 show what the task needs: tens of kilograms, a winch mode and a 6,000 m ceiling ([Wikipedia, DJI FlyCart](https://en.wikipedia.org/wiki/DJI_FlyCart)). Enterprise drones such as the Matrice 350 RTK carry under 1 kg at USD 14,814 ([Advexure](https://advexure.com/products/dji-matrice-350-rtk)). Both are closed. Open flight software exists in PX4 ([GitHub](https://github.com/PX4/PX4-Autopilot)), and an open payload bus in DS-014 ([Dronecode, 2021](https://dronecode.org/announcing-the-pixhawk-payload-bus-open-standard/)), but there is no open, documented multirotor frame tuned for altitude and cold that local teams can build and fit with their own payloads.

## Users and context

| User | Need | Context |
| --- | --- | --- |
| Flood and disaster response teams | Hover over a site, drop a float or line, and give a long overhead view | River and urban floods, landslides and road cuts |
| Mountain rescue teams | Carry search payloads and small supplies to 5,000 m in cold and wind | Himalaya and Karakoram expeditions and valley rescues |
| Hazard researchers | A stable hovering platform for short-range survey payloads | Glacial lakes and moraines |
| Payload builders and students | A proven frame to test payloads on the Kitewright mount | University labs and makerspaces |

## Operating environment

- Sea level to 5,000 m (design target), ambient -20 to +45 °C (-4 to +113 °F) (target).
- Wind up to about 10 m/s in normal operation (target), with valley gusts and rotor downwash over water, snow and dust.
- Take-off from rough ground, riverbanks, boats, rooftops and snow.
- Rain and spray during flood work; no mains power at site.
- Tethered operation from a vehicle or generator at a fixed point.

## Constraints

- Value-engineering target: USD 5,000 for the frame, motors, propellers and its share of core avionics, excluding payloads (a hypothetical control target, not a spending limit).
- Maximum take-off mass 25 kg or less including payload (FAA Part 107 and India Small class).
- Uses the Kitewright Core, ColdCell power bus and payload mount unchanged.
- All-electric; hybrid generator pack shelved.
- Tether power is a fixed-voltage ground supply with onboard DC-DC conversion.
- Winch module design waits for its own patent screen.
- Hardware under CERN-OHL-S-2.0; software under a licence compatible with PX4 (BSD 3-Clause) or ArduPilot (GPLv3).

## Out of scope

- Carrying people or lifting people on a line.
- Caged confined-space frames (deferred after the patent screen).
- Hybrid, fuel-cell or combustion power.
- Crop spraying and dispersal of chemicals.
- Aviation certification (FAA Part 107, EASA, India DGCA Drone Rules 2021) at this TRL; to be addressed if prototypes progress.
- Any weapon, targeting or military payload.

## Prior work

| Prior work | What it does | Gap for these users | Source |
| --- | --- | --- | --- |
| DJI FlyCart 30 | Closed heavy-lift delivery drone: 30 kg with two batteries, cargo crate or winch, 6,000 m service ceiling | Closed, large and costly; not adaptable by local teams | [link](https://en.wikipedia.org/wiki/DJI_FlyCart) |
| DJI FlyCart 30 Everest delivery tests | Carried 15 kg between 5,300 and 6,000 m at -15 to 5 °C in 2024 | Shows the need and conditions; a closed platform | [link](https://www.dji.com/media-center/announcements/dji-completes-world-first-drone-delivery-tests-on-mount-everest-en) |
| DJI Matrice 350 RTK | Enterprise multirotor, 960 g payload, 55 min flight, USD 14,814 | Small payload for the price; closed payload system | [link](https://advexure.com/products/dji-matrice-350-rtk) |
| PX4 Autopilot | Open flight control software with multirotor support, BSD 3-Clause | No open reference heavy-lift frame for altitude and cold | [link](https://github.com/PX4/PX4-Autopilot) |
| Pixhawk Payload Bus standard (DS-014) | Open payload power and data interface | Interface only; needs a frame and mount | [link](https://dronecode.org/announcing-the-pixhawk-payload-bus-open-standard/) |

## Co-design

A flood or mountain rescue organisation that already uses drones should set the mission profiles, try the line and float payload and review field handling. The first candidate to approach is the Himalayan Rescue Association, Nepal, which runs aid posts on the high trekking routes (KWL-DDR-001, item 11; not agreed).

Co-design checklist:

- [ ] Confirm the missions in order of need: float drop over water, search overhead, tethered lookout or radio relay, small supply drop.
- [ ] Confirm the payload masses that matter at sea level and at 5,000 m.
- [ ] Confirm the hover times a team would accept, with and without the tether.
- [ ] Review the folded size, the set-up steps and the carry weight with gloved hands.
- [ ] Agree the keep-out distances and drop heights over people.
- [ ] Agree a test site and the permissions the civil aviation authority requires.

## Answers to the TRL 1 open questions

Settled at TRL 2 and 3 (KWL-DDR-001, KWL-CAL-001):

- **Rotor layout.** A coaxial X8: four folding arms with a motor above and below each tip, 30 inch propellers. Losing one motor leaves its partner on the same arm.
- **Winch.** Not designed until its own patent screen is done; the payload bay leaves room for it.
- **Tether.** A fixed 400 V DC ground supply, a 60 m tether of two 0.75 mm2 conductors and a 4 kW onboard converter; about 3.3 kW from the ground for a tethered hover (estimate).
- **Payload at 5,000 m.** On paper the aircraft has a thrust to weight of 1.94 at 5,000 m and -20 C with 2 kg; AltiRig data will confirm it.
- **First high-altitude site.** Sea-level trials first, then the Khumbu region of Nepal with the co-design candidate, as the first candidate (not agreed), with civil aviation permission.

## Safety

> **Safety:** Kitewright Lift is a 25 kg class aircraft with eight 30 inch propellers, lithium iron phosphate packs, a 400 V tether and suspended loads. Spinning propellers can kill; packs can burn after a crash or a cold charge; the tether carries a dangerous voltage; a dropped load or a downwash blast can hurt people below. It is an open engineering reference, not certified aviation equipment, for civilian use only. Fly only where local rules allow, never over or near uninvolved people, and never carry or lift a person.
