---
title: "proto_syllabic Data"
description: "species/human/cultures data file documentation"
generated: true
source_files:
  - "data/species/human/cultures/proto_syllabic.json"
nav_order: 10
---

# proto_syllabic

📄 source: `data/species/human/cultures/proto_syllabic.json` | Category: species/human/cultures | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `culture_id` | string | "proto_syllabic" |
| `culture_name` | string | "음절 원시" |
| `emotion_modifiers` | object | object with 4 keys |
| `emotion_modifiers.anger` | float | 0.9 |
| `emotion_modifiers.comment` | string | "Emotion sensitivity multiplier" |
| `emotion_modifiers.joy` | float | 1.1 |
| `emotion_modifiers.trust` | float | 1.1 |
| `naming_culture` | string | "proto_syllabic" |
| `personality_shift` | object | object with 7 keys |
| `personality_shift.A` | float | 0.0 |
| `personality_shift.C` | float | 0.1 |
| `personality_shift.E` | float | -0.1 |
| `personality_shift.H` | float | 0.1 |
| `personality_shift.O` | float | -0.1 |
| `personality_shift.X` | float | 0.2 |
| `personality_shift.comment` | string | "z-score shift per axis" |

## Full Content

```json
{
  "culture_id": "proto_syllabic",
  "culture_name": "음절 원시",
  "personality_shift": {
    "comment": "z-score shift per axis",
    "H": 0.1,
    "E": -0.1,
    "X": 0.2,
    "A": 0.0,
    "C": 0.1,
    "O": -0.1
  },
  "emotion_modifiers": {
    "comment": "Emotion sensitivity multiplier",
    "joy": 1.1,
    "anger": 0.9,
    "trust": 1.1
  },
  "naming_culture": "proto_syllabic"
}
```

## Referenced By

- [`species_manager`](../../../../core/species_manager.md) - references data under `data/species/`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
