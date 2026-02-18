---
title: "Personality Traits"
description: "HEXACO trait overview with axis grouping and synergy network."
generated: true
source_files:
  - "extracted/trait_data.json"
  - "data/species/human/personality/trait_definitions.json"
nav_order: 10
---

# Personality Traits

The WorldSim personality system uses **187 discrete traits** activated by HEXACO personality axes.
Traits modify emotion sensitivity, behavior weights, stress responses, and social interactions.

**Model basis**: Ashton & Lee (2007) HEXACO Personality Model, with extensions for dark triad traits and composite conditions.

## 개요

| HEXACO Axis | Name (EN) | Name (KR) | Traits | Positive | Negative |
| --- | --- | --- | --- | --- | --- |
| H | Honesty-Humility | 정직-겸손 | 56 | 16 | 33 |
| E | Emotionality | 감정성 | 31 | 12 | 6 |
| X | Extraversion | 외향성 | 31 | 16 | 6 |
| A | Agreeableness | 우호성 | 25 | 13 | 8 |
| C | Conscientiousness | 성실성 | 20 | 11 | 7 |
| O | Openness to Experience | 경험 개방성 | 24 | 12 | 1 |

## 특성 유형

| Type | Count | Description |
| --- | --- | --- |
| Personality | 187 | Standard facet-threshold traits |
| Dark | 0 | Dark triad/tetrad traits (composite conditions) |
| Composite | 0 | Multi-condition traits |

## 특성 작동 방식

1. **Activation**: Each entity's HEXACO personality scores are checked against trait conditions.
2. **Threshold**: A trait activates when a facet score is above (`high`) or below (`low`) the threshold.
3. **Effects**: Active traits modify behavior weights, emotion sensitivity, stress responses, and social interactions.
4. **Synergies**: Some traits amplify each other's effects; anti-synergies create internal conflict.

## 축 페이지

- [Honesty-Humility (H) - 정직-겸손](H.md)
- [Emotionality (E) - 감정성](E.md)
- [Extraversion (X) - 외향성](X.md)
- [Agreeableness (A) - 우호성](A.md)
- [Conscientiousness (C) - 성실성](C.md)
- [Openness to Experience (O) - 경험 개방성](O.md)

## 시너지 네트워크

```mermaid
graph LR
  t0["f_reckless"]
  t1["f_sincere"]
  t2["c_born_leader"]
  t3["c_caregiver"]
  t4["c_inventor"]
  t5["c_saint"]
  t6["f_corrupt"]
  t7["f_creative"]
  t8["f_deceptive"]
  t9["f_fair_minded"]
  t10["f_greedy"]
  t11["f_harsh"]
  t12["f_hot_tempered"]
  t13["f_modest"]
  t14["f_sentimental"]
  t15["c_agitator"]
  t16["c_ascetic"]
  t17["c_berserker"]
  t18["c_builder_foreman"]
  t19["c_counselor"]
  t0 -->|synergy| t12
  t0 -->|synergy| t17
  t1 -->|synergy| t9
  t1 -->|synergy| t13
  t1 -.->|conflict| t8
  t1 -.->|conflict| t6
  t3 -->|synergy| t14
  t4 -->|synergy| t7
  t5 -->|synergy| t1
  t5 -->|synergy| t9
  t6 -->|synergy| t8
  t6 -->|synergy| t10
  t6 -.->|conflict| t9
  t6 -.->|conflict| t1
  t7 -->|synergy| t4
  t8 -->|synergy| t6
  t8 -->|synergy| t10
  t8 -->|synergy| t0
  t8 -.->|conflict| t1
  t8 -.->|conflict| t9
  t9 -->|synergy| t1
  t9 -.->|conflict| t6
  t10 -->|synergy| t6
  t10 -->|synergy| t8
  t12 -->|synergy| t0
  t12 -->|synergy| t17
  t13 -->|synergy| t1
  t14 -->|synergy| t3
  t16 -.->|conflict| t10
  t17 -->|synergy| t12
  t17 -->|synergy| t0
  t18 -.->|conflict| t12
  t19 -->|synergy| t3
```

📄 source: `extracted/trait_data.json`

## 수동 노트

<!-- MANUAL:START -->
<!-- MANUAL:END -->
