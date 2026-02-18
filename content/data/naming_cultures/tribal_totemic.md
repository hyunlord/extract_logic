---
title: "tribal_totemic Data"
description: "naming_cultures data file documentation"
generated: true
source_files:
  - "data/naming_cultures/tribal_totemic.json"
nav_order: 10
---

# tribal_totemic

📄 source: `data/naming_cultures/tribal_totemic.json` | Category: naming_cultures | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `allow_markov_generation` | boolean | true |
| `culture_id` | string | "tribal_totemic" |
| `description` | string | "Totem animal/nature + trait/deed combinations. Tribal era." |
| `display_name` | string | "Totemic Tribal" |
| `epithet_unlock_age` | int | 12 |
| `epithets` | object | object with 3 keys |
| `epithets.by_deed` | array | array (4 items, string entries) |
| `epithets.by_totem` | array | array (5 items, string entries) |
| `epithets.by_trait` | object | object with 4 keys |
| `epithets.by_trait.high_agility` | array | array (3 items, string entries) |
| `epithets.by_trait.high_intelligence` | array | array (3 items, string entries) |
| `epithets.by_trait.high_openness` | array | array (3 items, string entries) |
| `epithets.by_trait.high_strength` | array | array (3 items, string entries) |
| `given_names` | object | object with 2 keys |
| `given_names.female` | array | array (10 items, string entries) |
| `given_names.male` | array | array (10 items, string entries) |
| `markov_config` | object | object with 3 keys |
| `markov_config.max_length` | int | 6 |
| `markov_config.min_length` | int | 3 |
| `markov_config.order` | int | 2 |
| `name_structure` | string | "given+epithet" |
| `patronymic_config` | object | object with 4 keys |
| `patronymic_config.female_prefix` | string | "" |
| `patronymic_config.female_suffix` | string | "'s daughter" |
| `patronymic_config.male_prefix` | string | "" |
| `patronymic_config.male_suffix` | string | "'s son" |
| `patronymic_rule` | string | "prefix" |
| `surname_rule` | string | "none" |
| `syllable_count` | object | object with 2 keys |
| `syllable_count.max` | int | 3 |
| `syllable_count.min` | int | 1 |
| `syllable_pools` | object | object with 5 keys |
| `syllable_pools.coda` | array | array (10 items, string entries) |
| `syllable_pools.coda_final` | array | array (9 items, string entries) |
| `syllable_pools.nucleus` | array | array (9 items, string entries) |
| `syllable_pools.onset_female` | array | array (9 items, string entries) |
| `syllable_pools.onset_male` | array | array (11 items, string entries) |

## Full Content

```json
{
  "culture_id": "tribal_totemic",
  "display_name": "Totemic Tribal",
  "description": "Totem animal/nature + trait/deed combinations. Tribal era.",
  "name_structure": "given+epithet",
  "given_names": {
    "male": [
      "Kor",
      "Bran",
      "Thane",
      "Rok",
      "Grim",
      "Tyr",
      "Arn",
      "Ulf",
      "Dag",
      "Sven"
    ],
    "female": [
      "Mira",
      "Sula",
      "Kira",
      "Lena",
      "Asha",
      "Nira",
      "Vera",
      "Tala",
      "Yara",
      "Runa"
    ]
  },
  "epithets": {
    "by_trait": {
      "high_strength": [
        "Strong",
        "Bear-arm",
        "Iron-fist"
      ],
      "high_agility": [
        "Swift",
        "Wind-foot",
        "Deer-leg"
      ],
      "high_intelligence": [
        "Wise",
        "Star-eye",
        "Deep-thought"
      ],
      "high_openness": [
        "Seeker",
        "Far-walker",
        "Sky-gazer"
      ]
    },
    "by_deed": [
      "First-fire",
      "Rain-caller",
      "Bone-setter",
      "Path-finder"
    ],
    "by_totem": [
      "of-Wolf",
      "of-Eagle",
      "of-Bear",
      "of-Elk",
      "of-Serpent"
    ]
  },
  "epithet_unlock_age": 12,
  "allow_markov_generation": true,
  "markov_config": {
    "order": 2,
    "min_length": 3,
    "max_length": 6
  },
  "syllable_pools": {
    "onset_male": [
      "k",
      "b",
      "th",
      "r",
      "g",
      "d",
      "v",
      "br",
      "gr",
      "kr",
      "sk"
    ],
    "onset_female": [
      "m",
      "s",
      "l",
      "n",
      "r",
      "t",
      "v",
      "sh",
      "al"
    ],
    "nucleus": [
      "a",
      "e",
      "i",
      "o",
      "u",
      "ai",
      "ei",
      "ar",
      "or"
    ],
    "coda": [
      "n",
      "r",
      "k",
      "m",
      "th",
      "l",
      "s",
      "rn",
      "lk",
      "nd"
    ],
    "coda_final": [
      "n",
      "r",
      "a",
      "e",
      "o",
      "k",
      "th",
      "ir",
      "ar"
    ]
  },
  "syllable_count": {
    "min": 1,
    "max": 3
  },
  "patronymic_rule": "prefix",
  "patronymic_config": {
    "male_prefix": "",
    "male_suffix": "'s son",
    "female_prefix": "",
    "female_suffix": "'s daughter"
  },
  "surname_rule": "none"
}
```

## Referenced By

- [`name_generator`](../../core/name_generator.md) - references data under `data/naming_cultures/`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
