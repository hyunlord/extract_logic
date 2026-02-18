---
title: "tribal_totemic Data"
description: "species/human/cultures data file documentation"
generated: true
source_files:
  - "data/species/human/cultures/tribal_totemic.json"
nav_order: 10
---

# tribal_totemic

📄 source: `data/species/human/cultures/tribal_totemic.json` | Category: species/human/cultures | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `culture_id` | string | "tribal_totemic" |
| `culture_name` | string | "부족 토템" |
| `emotion_modifiers` | object | object with 4 keys |
| `emotion_modifiers.comment` | string | "Emotion sensitivity multiplier" |
| `emotion_modifiers.disgust` | float | 1.1 |
| `emotion_modifiers.fear` | float | 0.8 |
| `emotion_modifiers.trust` | float | 1.3 |
| `naming_culture` | string | "tribal_totemic" |
| `personality_shift` | object | object with 7 keys |
| `personality_shift.A` | float | 0.2 |
| `personality_shift.C` | float | 0.2 |
| `personality_shift.E` | float | 0.0 |
| `personality_shift.H` | float | 0.2 |
| `personality_shift.O` | float | -0.2 |
| `personality_shift.X` | float | 0.0 |
| `personality_shift.comment` | string | "z-score shift per axis" |

## Full Content

```json
{
  "culture_id": "tribal_totemic",
  "culture_name": "부족 토템",
  "personality_shift": {
    "comment": "z-score shift per axis",
    "H": 0.2,
    "E": 0.0,
    "X": 0.0,
    "A": 0.2,
    "C": 0.2,
    "O": -0.2
  },
  "emotion_modifiers": {
    "comment": "Emotion sensitivity multiplier",
    "trust": 1.3,
    "fear": 0.8,
    "disgust": 1.1
  },
  "naming_culture": "tribal_totemic"
}
```

## Referenced By

- [`species_manager`](../../../../core/species_manager.md) - references data under `data/species/`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
