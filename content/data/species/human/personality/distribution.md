---
title: "distribution Data"
description: "species/human/personality data file documentation"
generated: true
source_files:
  - "data/species/human/personality/distribution.json"
nav_order: 10
---

# distribution

📄 source: `data/species/human/personality/distribution.json` | Category: species/human/personality | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `comment_facet_spread` | string | "Intra-axis facet variance (z-score). 0.75 allows diverse facet profiles within same axis, enabling contradictory tra... |
| `comment_sd` | string | "Academic SD=0.15, widened for gameplay. Ashton & Lee 2009" |
| `correlation_matrix` | object | object with 3 keys |
| `correlation_matrix.axes_order` | array | array (6 items, string entries) |
| `correlation_matrix.comment` | string | "HEXACO-60 student sample, Ashton & Lee 2009 Table 3" |
| `correlation_matrix.matrix` | array | array (6 items, array entries) |
| `facet_spread` | float | 0.75 |
| `heritability` | object | object with 7 keys |
| `heritability.A` | float | 0.47 |
| `heritability.C` | float | 0.52 |
| `heritability.E` | float | 0.58 |
| `heritability.H` | float | 0.45 |
| `heritability.O` | float | 0.63 |
| `heritability.X` | float | 0.57 |
| `heritability.comment` | string | "Vernon et al. 2008, extended twin-family model" |
| `maturation` | object | object with 7 keys |
| `maturation.A` | object | object with 2 keys |
| `maturation.A.age_range` | array | array (2 items, int entries) |
| `maturation.A.target_shift` | float | 0.0 |
| `maturation.C` | object | object with 2 keys |
| `maturation.C.age_range` | array | array (2 items, int entries) |
| `maturation.C.target_shift` | float | 0.0 |
| `maturation.E` | object | object with 2 keys |
| `maturation.E.age_range` | array | array (2 items, int entries) |
| `maturation.E.target_shift` | float | 0.3 |
| `maturation.H` | object | object with 2 keys |
| `maturation.H.age_range` | array | array (2 items, int entries) |
| `maturation.H.target_shift` | float | 1.0 |
| `maturation.O` | object | object with 2 keys |
| `maturation.O.age_range` | array | array (2 items, int entries) |
| `maturation.O.target_shift` | float | 0.0 |
| `maturation.X` | object | object with 2 keys |
| `maturation.X.age_range` | array | array (2 items, int entries) |
| `maturation.X.target_shift` | float | 0.3 |
| `maturation.comment` | string | "Ashton & Lee 2016, age trends. target_shift in SD, linear from age_range[0] to age_range[1]" |
| `ou_parameters` | object | object with 3 keys |
| `ou_parameters.comment` | string | "Ornstein-Uhlenbeck maturation process (annual)" |
| `ou_parameters.sigma` | float | 0.03 |
| `ou_parameters.theta` | float | 0.03 |
| `sd` | float | 0.25 |
| `sex_difference_d` | object | object with 7 keys |
| `sex_difference_d.A` | float | 0.28 |
| `sex_difference_d.C` | float | 0.0 |
| `sex_difference_d.E` | float | 0.96 |
| `sex_difference_d.H` | float | 0.41 |
| `sex_difference_d.O` | float | -0.04 |
| `sex_difference_d.X` | float | 0.1 |
| `sex_difference_d.comment` | string | "Ashton & Lee 2009, HEXACO-60 community sample, Cohen's d (positive = female higher)" |

## Full Content

```json
{
  "sd": 0.25,
  "comment_sd": "Academic SD=0.15, widened for gameplay. Ashton & Lee 2009",
  "correlation_matrix": {
    "comment": "HEXACO-60 student sample, Ashton & Lee 2009 Table 3",
    "axes_order": [
      "H",
      "E",
      "X",
      "A",
      "C",
      "O"
    ],
    "matrix": [
      [
        1.0,
        0.12,
        -0.11,
        0.26,
        0.18,
        0.21
      ],
      [
        0.12,
        1.0,
        -0.13,
        -0.08,
        0.15,
        -0.1
      ],
      [
        -0.11,
        -0.13,
        1.0,
        0.05,
        0.1,
        0.08
      ],
      [
        0.26,
        -0.08,
        0.05,
        1.0,
        0.01,
        0.03
      ],
      [
        0.18,
        0.15,
        0.1,
        0.01,
        1.0,
        0.03
      ],
      [
        0.21,
        -0.1,
        0.08,
        0.03,
        0.03,
        1.0
      ]
    ]
  },
  "heritability": {
    "comment": "Vernon et al. 2008, extended twin-family model",
    "H": 0.45,
    "E": 0.58,
    "X": 0.57,
    "A": 0.47,
    "C": 0.52,
    "O": 0.63
  },
  "sex_difference_d": {
    "comment": "Ashton & Lee 2009, HEXACO-60 community sample, Cohen's d (positive = female higher)",
    "H": 0.41,
    "E": 0.96,
    "X": 0.1,
    "A": 0.28,
    "C": 0.0,
    "O": -0.04
  },
  "maturation": {
    "comment": "Ashton & Lee 2016, age trends. target_shift in SD, linear from age_range[0] to age_range[1]",
    "H": {
      "target_shift": 1.0,
      "age_range": [
        18,
        60
      ]
    },
    "E": {
      "target_shift": 0.3,
      "age_range": [
        18,
        60
      ]
    },
    "X": {
      "target_shift": 0.3,
      "age_range": [
        18,
        60
      ]
    },
    "A": {
      "target_shift": 0.0,
      "age_range": [
        18,
        60
      ]
    },
    "C": {
      "target_shift": 0.0,
      "age_range": [
        18,
        60
      ]
    },
    "O": {
      "target_shift": 0.0,
      "age_range": [
        18,
        60
      ]
    }
  },
  "facet_spread": 0.75,
  "comment_facet_spread": "Intra-axis facet variance (z-score). 0.75 allows diverse facet profiles within same axis, enabling contradictory trait combos (e.g. fearful+low empathy). Previous: 0.35",
  "ou_parameters": {
    "comment": "Ornstein-Uhlenbeck maturation process (annual)",
    "theta": 0.03,
    "sigma": 0.03
  }
}
```

## Referenced By

- [`species_manager`](../../../../core/species_manager.md) - references data under `data/species/`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
