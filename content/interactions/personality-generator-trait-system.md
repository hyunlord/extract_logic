---
title: "personality_generator ↔ trait_system Interaction"
description: "Cross-system interaction analysis"
generated: true
source_files:
  - "scripts/systems/personality_generator.gd"
  - "scripts/systems/trait_system.gd"
nav_order: 11
---

# personality_generator ↔ trait_system

## Interaction Summary
`personality_generator` and `trait_system` interact through 2 connection types: shared dependencies, direct calls.

## Shared Entity Fields
| Field | personality_generator Access | trait_system Access |
|-------|----------------|----------------|
| (none) | - | - |

## Signal Flow
- None

## Shared Dependencies
- Both import `scripts/systems/trait_system.gd`

## Direct Calls
- `personality_generator` directly calls `trait_system.check_traits()`

## Data Flow Diagram
```mermaid
graph LR
  A[personality_generator]
  B[trait_system]
  E[(Entity)]
  A -->|calls check_traits()| B
```

## Source References
- 📄 source: `scripts/systems/personality_generator.gd:L8`
- 📄 source: `scripts/systems/personality_generator.gd:L142`
- 📄 source: `scripts/systems/trait_system.gd:L4`

## Manual Notes
<!-- MANUAL:START -->
<!-- MANUAL:END -->
