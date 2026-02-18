---
title: "proto_nature Data"
description: "species/human/cultures data file documentation"
generated: true
source_files:
  - "data/species/human/cultures/proto_nature.json"
nav_order: 10
---

# proto_nature

📄 source: `data/species/human/cultures/proto_nature.json` | Category: species/human/cultures | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `culture_id` | string | "proto_nature" |
| `culture_name` | string | "자연 원시" |
| `emotion_modifiers` | object | object with 4 keys |
| `emotion_modifiers.anticipation` | float | 1.1 |
| `emotion_modifiers.comment` | string | "Emotion sensitivity multiplier" |
| `emotion_modifiers.fear` | float | 1.2 |
| `emotion_modifiers.trust` | float | 0.9 |
| `naming_culture` | string | "proto_nature" |
| `personality_shift` | object | object with 7 keys |
| `personality_shift.A` | float | 0.1 |
| `personality_shift.C` | float | -0.1 |
| `personality_shift.E` | float | 0.1 |
| `personality_shift.H` | float | 0.0 |
| `personality_shift.O` | float | 0.2 |
| `personality_shift.X` | float | -0.1 |
| `personality_shift.comment` | string | "z-score shift per axis, +/- 0.1~0.3 recommended" |

## Full Content

```json
{
  "culture_id": "proto_nature",
  "culture_name": "자연 원시",
  "personality_shift": {
    "comment": "z-score shift per axis, +/- 0.1~0.3 recommended",
    "H": 0.0,
    "E": 0.1,
    "X": -0.1,
    "A": 0.1,
    "C": -0.1,
    "O": 0.2
  },
  "emotion_modifiers": {
    "comment": "Emotion sensitivity multiplier",
    "fear": 1.2,
    "anticipation": 1.1,
    "trust": 0.9
  },
  "naming_culture": "proto_nature"
}
```

## Referenced By

- [`species_manager`](../../../../core/species_manager.md) - references data under `data/species/`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
