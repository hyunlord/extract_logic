---
title: "Save Manager"
description: "Binary save/load system (version 2)."
generated: true
source_files:
  - "scripts/core/save_manager.gd"
nav_order: 19
---

# Save Manager

> Binary save/load system (version 2). Structure: user://saves/quicksave/ directory with: meta.json, entities.bin, buildings.bin, relationships.bin, settlements.bin, world.bin, stats.json Minimum loadable save version (v3 loads with defaults for new fields) Track loaded version for conditional field reading

📄 source: `scripts/core/save_manager.gd` | 592 lines | extends: RefCounted

## 개요
Binary save/load system (version 2).

## 공개 API

### Functions
| Function | Parameters | Returns | Line |
|----------|------------|---------|------|
| - | - | - | - |

### Signals
| Signal | Parameters |
|--------|------------|
| `game_loaded` | `-` |
| `game_saved` | `-` |

## 의존성
- Imports: [`building_data.gd`](building_data.md), [`emotion_data.gd`](emotion_data.md), [`entity_data.gd`](entity_data.md), [`game_calendar.gd`](game_calendar.md), [`personality_data.gd`](personality_data.md), [`relationship_data.gd`](relationship_data.md), [`settlement_data.gd`](settlement_data.md)
- Used by: -
