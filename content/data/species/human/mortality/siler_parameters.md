---
title: "siler_parameters Data"
description: "species/human/mortality data file documentation"
generated: true
source_files:
  - "data/species/human/mortality/siler_parameters.json"
nav_order: 10
---

# siler_parameters

📄 source: `data/species/human/mortality/siler_parameters.json` | Category: species/human/mortality | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `baseline` | object | object with 6 keys |
| `baseline.a1` | float | 0.6 |
| `baseline.a2` | float | 0.01 |
| `baseline.a3` | float | 6e-05 |
| `baseline.b1` | float | 1.3 |
| `baseline.b3` | float | 0.09 |
| `baseline.comment` | string | "Hunter-gatherer (tech=0), target: q0 ~ 0.40, e0 ~ 33 years" |
| `care_protection` | object | object with 3 keys |
| `care_protection.comment` | string | "Well-fed infant/toddler mortality reduction" |
| `care_protection.hunger_min` | float | 0.3 |
| `care_protection.protection_factor` | float | 0.6 |
| `comment` | string | "Siler(1979) bathtub-curve: mu(x) = a1*exp(-b1*x) + a2 + a3*exp(b3*x)" |
| `model` | string | "siler" |
| `season_modifiers` | object | object with 2 keys |
| `season_modifiers.summer` | object | object with 1 keys |
| `season_modifiers.summer.infant` | float | 0.9 |
| `season_modifiers.winter` | object | object with 2 keys |
| `season_modifiers.winter.background` | float | 1.2 |
| `season_modifiers.winter.infant` | float | 1.3 |
| `tech_modifiers` | object | object with 4 keys |
| `tech_modifiers.comment` | string | "m_i(tech) = exp(-k_i * tech), tech=0..10" |
| `tech_modifiers.k1` | float | 0.3 |
| `tech_modifiers.k2` | float | 0.2 |
| `tech_modifiers.k3` | float | 0.05 |

## Full Content

```json
{
  "model": "siler",
  "comment": "Siler(1979) bathtub-curve: mu(x) = a1*exp(-b1*x) + a2 + a3*exp(b3*x)",
  "baseline": {
    "comment": "Hunter-gatherer (tech=0), target: q0 ~ 0.40, e0 ~ 33 years",
    "a1": 0.6,
    "b1": 1.3,
    "a2": 0.01,
    "a3": 6e-05,
    "b3": 0.09
  },
  "tech_modifiers": {
    "comment": "m_i(tech) = exp(-k_i * tech), tech=0..10",
    "k1": 0.3,
    "k2": 0.2,
    "k3": 0.05
  },
  "care_protection": {
    "comment": "Well-fed infant/toddler mortality reduction",
    "hunger_min": 0.3,
    "protection_factor": 0.6
  },
  "season_modifiers": {
    "winter": {
      "infant": 1.3,
      "background": 1.2
    },
    "summer": {
      "infant": 0.9
    }
  }
}
```

## Referenced By

- [`species_manager`](../../../../core/species_manager.md) - references data under `data/species/`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
