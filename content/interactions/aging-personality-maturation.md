---
title: "aging ↔ personality_maturation Interaction"
description: "Cross-system interaction analysis"
generated: true
source_files:
  - "scripts/systems/age_system.gd"
  - "scripts/systems/personality_maturation.gd"
nav_order: 10
---

# aging ↔ personality_maturation

## Interaction Summary
`aging` and `personality_maturation` interact through 2 connection types: shared dependencies, direct calls.

## Shared Entity Fields
| Field | aging Access | personality_maturation Access |
|-------|----------------|----------------|
| (none) | - | - |

## Signal Flow
- None

## Shared Dependencies
- Both import `scripts/systems/personality_maturation.gd`

## Direct Calls
- `aging` directly calls `personality_maturation.new()`

## Data Flow Diagram
```mermaid
graph LR
  A[aging]
  B[personality_maturation]
  E[(Entity)]
  A -->|calls new()| B
```

## Source References
- 📄 source: `scripts/systems/age_system.gd:L7`
- 📄 source: `scripts/systems/age_system.gd:L22`
- 📄 source: `scripts/systems/personality_maturation.gd:L6`

## Manual Notes
<!-- MANUAL:START -->
<!-- MANUAL:END -->
