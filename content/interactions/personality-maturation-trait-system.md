---
title: "personality_maturation ↔ trait_system Interaction"
description: "Cross-system interaction analysis"
generated: true
source_files:
  - "scripts/systems/personality_maturation.gd"
  - "scripts/systems/trait_system.gd"
nav_order: 12
---

# personality_maturation ↔ trait_system

## Interaction Summary
`personality_maturation` and `trait_system` interact through 2 connection types: shared dependencies, direct calls.

## Shared Entity Fields
| Field | personality_maturation Access | trait_system Access |
|-------|----------------|----------------|
| (none) | - | - |

## Signal Flow
- None

## Shared Dependencies
- Both import `scripts/systems/trait_system.gd`

## Direct Calls
- `personality_maturation` directly calls `trait_system.check_traits()`

## Data Flow Diagram
```mermaid
graph LR
  A[personality_maturation]
  B[trait_system]
  E[(Entity)]
  A -->|calls check_traits()| B
```

## Source References
- 📄 source: `scripts/systems/personality_maturation.gd:L9`
- 📄 source: `scripts/systems/personality_maturation.gd:L57`
- 📄 source: `scripts/systems/trait_system.gd:L4`

## Manual Notes
<!-- MANUAL:START -->
<!-- MANUAL:END -->
