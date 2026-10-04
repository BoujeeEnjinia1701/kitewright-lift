---
doc_id: KWL-DDR-005
title: Kitewright Lift R4 restated to the rated payload (open decision 4 closed)
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
  change: Open decision 4 closed as a consequence of Amish's round-3 decision 8A
---

# 0005: R4 restated to the rated payload

- **Date:** 2026-10-04
- **Status:** accepted. Decided by Amish Chadha on 2026-10-04: "For round 3, I agree with all your proposed recommendations". Open decision 4 follows from round-3 decision 8A (the payload rated at what fits inside the 25 kg take-off limit) and is closed with its recommended option A.

## Context

R4 asked for at least 20 min of hover "with 5 kg at sea level". Under decision 8A (KWL-DDR-004) Lift keeps its 25 kg take-off limit (R1) with two ColdCell packs of 4.46 kg and rates its payload at what fits, about 3.3 kg (R2, 3.2 kg on paper). A 5 kg payload no longer fits inside R1, so the sea-level case was being read at the rated payload.

## Decision

R4 restated in KWL-REQ-001 v0.5: "At least 20 min with the rated payload (R2) at sea level and 10 min with 2 kg at 5,000 m and -20 °C (targets)". The altitude case is unchanged.

## Results (KWL-CAL-001 v0.3, unchanged)

20.4 min at sea level with the rated 3.2 kg (25.0 kg take-off) and 14.5 min at 5,000 m and -20 °C with 2 kg. **R4 met on paper.**

## Consequences

- Records only: no change to the model, calculations, BOM, drawings or pictures.
- A heavier sea-level payload would need a lighter airframe or packs in a later prototype; that is not a requirement of this one.

> **Safety:** The rated payload is the most Lift may carry; flying above it breaks R1's 25 kg limit and the class rules that rest on it.
