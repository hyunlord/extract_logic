---
title: "System Interaction Index"
description: "Master dependency graph of cross-system interactions"
generated: true
source_files:
  - "extracted/references.json"
  - "extracted/systems.json"
nav_order: 1
---

# System Interaction Index

Generated 7 interaction link(s) total, with 3 significant pair page(s) (2+ types).

## Master Dependency Graph
```mermaid
graph LR
  S1[aging]
  S2[chronicle_system]
  S3[family]
  S4[mortality]
  S5[personality_generator]
  S6[personality_maturation]
  S7[trait_system]
  S1 ---|shared_dependencies, direct_calls| S6
  S5 ---|shared_dependencies, direct_calls| S7
  S6 ---|shared_dependencies, direct_calls| S7
  S2 ---|shared_dependencies| S3
  S2 ---|shared_dependencies| S4
  S3 ---|shared_dependencies| S4
  S5 ---|shared_dependencies| S6
```

## Interaction Strength Table
| Pair | Strength | Types |
|------|----------|-------|
| `aging ↔ personality_maturation` | 2 | shared_dependencies, direct_calls |
| `personality_generator ↔ trait_system` | 2 | shared_dependencies, direct_calls |
| `personality_maturation ↔ trait_system` | 2 | shared_dependencies, direct_calls |
| `chronicle_system ↔ family` | 1 | shared_dependencies |
| `chronicle_system ↔ mortality` | 1 | shared_dependencies |
| `family ↔ mortality` | 1 | shared_dependencies |
| `personality_generator ↔ personality_maturation` | 1 | shared_dependencies |

## Manual Notes
<!-- MANUAL:START -->
<!-- MANUAL:END -->
