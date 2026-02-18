---
title: "species_definition Data"
description: "species/human data file documentation"
generated: true
source_files:
  - "data/species/human/species_definition.json"
nav_order: 10
---

# species_definition

📄 source: `data/species/human/species_definition.json` | Category: species/human | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `available_cultures` | array | array (3 items, string entries) |
| `base_stats` | object | object with 4 keys |
| `base_stats.fertility_range` | array | array (2 items, int entries) |
| `base_stats.gestation_days` | int | 270 |
| `base_stats.maturity_age` | int | 15 |
| `base_stats.max_age` | int | 120 |
| `emotion_model` | string | "plutchik" |
| `emotion_path` | string | "res://data/species/human/emotions/" |
| `mortality_model` | string | "siler" |
| `mortality_path` | string | "res://data/species/human/mortality/" |
| `needs_model` | string | "maslow_erg" |
| `needs_path` | string | "res://data/species/human/needs/" |
| `personality_model` | string | "hexaco" |
| `personality_path` | string | "res://data/species/human/personality/" |
| `species_id` | string | "human" |
| `species_name` | string | "Human" |
| `species_name_kr` | string | "인간" |

## Full Content

```json
{
  "species_id": "human",
  "species_name": "Human",
  "species_name_kr": "인간",
  "personality_model": "hexaco",
  "personality_path": "res://data/species/human/personality/",
  "emotion_model": "plutchik",
  "emotion_path": "res://data/species/human/emotions/",
  "mortality_model": "siler",
  "mortality_path": "res://data/species/human/mortality/",
  "needs_model": "maslow_erg",
  "needs_path": "res://data/species/human/needs/",
  "base_stats": {
    "max_age": 120,
    "maturity_age": 15,
    "fertility_range": [
      15,
      45
    ],
    "gestation_days": 270
  },
  "available_cultures": [
    "proto_nature",
    "proto_syllabic",
    "tribal_totemic"
  ]
}
```

## Referenced By

- [`species_manager`](../../../core/species_manager.md) - references data under `data/species/`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
