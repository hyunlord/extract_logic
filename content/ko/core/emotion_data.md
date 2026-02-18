---
title: "Emotion Data"
description: "Plutchik 8 basic emotions with 3-layer temporal dynamics."
generated: true
source_files:
  - "scripts/core/emotion_data.gd"
nav_order: 5
---

# Emotion Data

> Plutchik 8 basic emotions with 3-layer temporal dynamics. Fast (episodic) + Slow (mood/baseline, OU process) + Memory trace (long-term scars). Valence-Arousal derived each tick. 24 Dyads computed on-the-fly. References: Plutchik (1980, 2001) — 8 emotions, intensity levels, Dyad system Russell (1980) — Circumplex Model of Affect (Valence-Arousal)

📄 source: `scripts/core/emotion_data.gd` | 365 lines | extends: RefCounted

## 개요 (Overview)
Plutchik 8 basic emotions with 3-layer temporal dynamics.

## 공개 API (Public API)

### Functions
| Function | Parameters | Returns | Line |
|----------|------------|---------|------|
| - | - | - | - |

### Signals
| Signal | Parameters |
|--------|------------|
| - | - |

## 의존성 (Dependencies)
- Imports: [`emotion_data.gd`](emotion_data.md)
- Used by: [`emotion_data.gd`](emotion_data.md), [`entity_data.gd`](entity_data.md), [`save_manager.gd`](save_manager.md), [`emotion_system.gd`](../systems/emotions.md)
