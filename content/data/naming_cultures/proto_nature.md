---
title: "proto_nature Data"
description: "naming_cultures data file documentation"
generated: true
source_files:
  - "data/naming_cultures/proto_nature.json"
nav_order: 10
---

# proto_nature

📄 source: `data/naming_cultures/proto_nature.json` | Category: naming_cultures | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `allow_markov_generation` | boolean | false |
| `culture_id` | string | "proto_nature" |
| `description` | string | "Names derived from nature. Early stone age." |
| `display_name` | string | "Nature Names (Primitive)" |
| `given_names` | object | object with 3 keys |
| `given_names.female` | array | array (65 items, string entries) |
| `given_names.male` | array | array (64 items, string entries) |
| `given_names.neutral` | array | array (16 items, string entries) |
| `name_structure` | string | "given" |
| `patronymic_rule` | string | "none" |
| `surname_rule` | string | "none" |

## Full Content

```json
{
  "culture_id": "proto_nature",
  "display_name": "Nature Names (Primitive)",
  "description": "Names derived from nature. Early stone age.",
  "name_structure": "given",
  "given_names": {
    "male": [
      "Ash",
      "Birch",
      "Brook",
      "Cedar",
      "Clay",
      "Dusk",
      "Elm",
      "Fern",
      "Flint",
      "Glen",
      "Heath",
      "Ivy",
      "Kael",
      "Lark",
      "Moss",
      "Nix",
      "Oak",
      "Pike",
      "Quinn",
      "Reed",
      "Sage",
      "Stone",
      "Thorn",
      "Vale",
      "Wolf",
      "Yew",
      "Blaze",
      "Cliff",
      "Crag",
      "Dale",
      "Dune",
      "Ember",
      "Frost",
      "Gale",
      "Hawk",
      "Lake",
      "Marsh",
      "Peak",
      "Ridge",
      "Shade",
      "Sky",
      "Storm",
      "Swift",
      "Tide",
      "Wren",
      "Briar",
      "Coral",
      "Delta",
      "Echo",
      "Fox",
      "Grove",
      "Haven",
      "Jet",
      "Leaf",
      "Mist",
      "North",
      "Onyx",
      "Pine",
      "Raven",
      "Rush",
      "Slate",
      "Spark",
      "Trail",
      "Vine"
    ],
    "female": [
      "Alba",
      "Amber",
      "Aspen",
      "Autumn",
      "Berry",
      "Bloom",
      "Breeze",
      "Clover",
      "Coral",
      "Dahlia",
      "Dawn",
      "Dew",
      "Dove",
      "Ember",
      "Fawn",
      "Flora",
      "Gem",
      "Hazel",
      "Heron",
      "Holly",
      "Iris",
      "Jade",
      "Jasmine",
      "Lily",
      "Luna",
      "Maple",
      "Marigold",
      "Meadow",
      "Myrtle",
      "Opal",
      "Pearl",
      "Petal",
      "Poppy",
      "Rain",
      "River",
      "Rose",
      "Rowan",
      "Ruby",
      "Sable",
      "Sage",
      "Sierra",
      "Snow",
      "Sparrow",
      "Spring",
      "Star",
      "Summer",
      "Sunny",
      "Terra",
      "Violet",
      "Willow",
      "Wren",
      "Zinnia",
      "Aurora",
      "Brook",
      "Crystal",
      "Fern",
      "Ginger",
      "Ivy",
      "Juniper",
      "Lark",
      "Moss",
      "Olive",
      "Raven",
      "Shell",
      "Teal"
    ],
    "neutral": [
      "Ash",
      "Brook",
      "Cedar",
      "Dawn",
      "Echo",
      "Fern",
      "Glen",
      "Haven",
      "Ivy",
      "Lark",
      "Moss",
      "Quinn",
      "Reed",
      "Sage",
      "Sky",
      "Wren"
    ]
  },
  "allow_markov_generation": false,
  "patronymic_rule": "none",
  "surname_rule": "none"
}
```

## Referenced By

- [`name_generator`](../../core/name_generator.md) - references data under `data/naming_cultures/`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
