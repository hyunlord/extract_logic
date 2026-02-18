---
title: "Mortality System — Detailed Documentation"
description: "Siler mortality model, modifiers, and per-tick death probability details"
generated: true
source_files:
  - "scripts/systems/mortality_system.gd"
  - "data/species/human/mortality/siler_parameters.json"
nav_order: 49
---

# Mortality System — Detailed Documentation

한국어 / English: 사망 시스템의 수학적 구조와 계수 결합을 설명합니다. This page explains the mortality model mathematics and modifier coupling.

📄 source: `scripts/systems/mortality_system.gd`:L130, `data/species/human/mortality/siler_parameters.json`

## The Siler Mortality Model

The mortality system implements **Siler's (1979) competing-risk model**, which produces a bathtub-shaped hazard curve:

$$
\mu(x) = a_1 \cdot e^{-b_1 \cdot x} + a_2 + a_3 \cdot e^{b_3 \cdot x}
$$

Where x = age in years, and:

| Parameter | Value | Meaning |
|:----------|------:|:--------|
| $a_1$ | 0.60 | Infant mortality amplitude - high risk at birth, rapidly declining |
| $b_1$ | 1.30 | Infant mortality decline rate - how fast infant risk drops |
| $a_2$ | 0.010 | Age-independent background mortality - constant baseline risk |
| $a_3$ | 0.00006 | Senescent mortality amplitude - exponential aging onset |
| $b_3$ | 0.090 | Senescent acceleration rate (Gompertz parameter) - how fast aging kills |

### The Three Components

| Component | Formula | Age Profile | Biological Meaning |
|:----------|:--------|:------------|:-------------------|
| Infant decline | $a_1 \cdot e^{-b_1 x}$ | Highest at birth, drops rapidly | Birth defects, immune immaturity |
| Background | $a_2$ | Constant across all ages | Accidents, infections, random events |
| Senescent | $a_3 \cdot e^{b_3 x}$ | Negligible in youth, exponential in old age | Aging, organ failure, cancer |

## Technology Modifiers

Settlement technology level reduces mortality:

$$
\mu_{\text{tech}}(x) = a_1 \cdot (1 - k_1 \cdot T) \cdot e^{-b_1 x} + a_2 \cdot (1 - k_2 \cdot T) + a_3 \cdot (1 - k_3 \cdot T) \cdot e^{b_3 x}
$$

Where T = tech_level (0.0 to 1.0):

| Modifier | Value | Effect | Interpretation |
|:---------|------:|:-------|:---------------|
| $k_1$ | 0.30 | -30% infant mortality at max tech | Better obstetric care |
| $k_2$ | 0.20 | -20% background mortality at max tech | Sanitation, medicine |
| $k_3$ | 0.05 | -5% senescent mortality at max tech | Marginal anti-aging impact |

**Design note**: Tech has the strongest effect on infant mortality (easiest wins) and weakest on aging (hard biological limit).

## Infant & Child Care Protection

Young entities receive mortality reduction when cared for:

$$
\mu_{\text{care}}(x) = \mu(x) \cdot (1 - \text{care\_factor})
$$

| Parameter | Value | Meaning |
|:----------|------:|:--------|
| care_max_age | 12.00 | Maximum age for care protection |
| care_reduction | 0.60 | Mortality reduction when cared for |
| orphan_penalty | n/a | Additional mortality risk without caregiver |

## Seasonal Mortality Modifiers

| Season | Modifier | Effect |
|:-------|:---------|:-------|
| Spring | ×1.00 | 중립 / Neutral |
| Summer | infant ×0.90 | 사망률 감소 / Reduced mortality risk |
| Autumn | ×1.00 | 중립 / Neutral |
| Winter | background ×1.20, infant ×1.30 | 사망률 증가 / Increased mortality risk |

Winter increases mortality (cold, food scarcity), while spring/summer reduce it.

## Stress → Mortality Coupling

High allostatic load from the stress system increases mortality:

$$
\mu_{\text{stress}}(x) = \mu(x) \cdot (1 + \alpha \cdot \text{allostatic\_load} / 100)
$$

This creates a feedback loop:
- Stressful events → high stress → allostatic load accumulates
- High allostatic load → increased hazard rate → earlier death
- Early death of partner/child → massive stressor → more allostatic load on survivors

## Nutrition Modifier

Malnutrition increases mortality:

$$
\mu_{\text{nutrition}}(x) = \mu(x) \cdot (1 + \beta \cdot (1 - \text{food\_satiety}))
$$

Implementation note: In code this is typically derived from `entity.hunger` / `food_satiety` (0.0 to 1.0).

## Per-Tick Death Probability

The final death probability per tick:

$$
P(\text{death}) = 1 - e^{-\mu_{\text{final}}(x) / \text{TICKS\_PER\_YEAR}}
$$

Where $\mu_{\text{final}}$ combines all modifiers:
$$
\mu_{\text{final}}(x) = \mu_{\text{tech}}(x) \cdot \text{care} \cdot \text{season} \cdot \text{stress} \cdot \text{nutrition}
$$

TICKS_PER_YEAR = **4380** (📄 source: `scripts/core/game_config.gd:L19`)

## Example Mortality Rates (Baseline, No Modifiers)

| Age | $\mu(x)$ | Annual Death Prob | Per-tick Prob | Dominant Component |
|----:|----------:|------------------:|--------------:|:-------------------|
| 0 | 0.610 | 45.7% | 0.0139% | Infant / 영아 |
| 1 | 0.174 | 15.9% | 0.0040% | Infant / 영아 |
| 5 | 0.011 | 1.09% | 0.0003% | Background / 배경 |
| 20 | 0.010 | 1.03% | 0.0002% | Background / 배경 |
| 50 | 0.015 | 1.53% | 0.0004% | Background / 배경 |
| 70 | 0.043 | 4.18% | 0.0010% | Senescent / 노화 |
| 90 | 0.208 | 18.8% | 0.0047% | Senescent / 노화 |

## Source Notes

- 📄 source: `scripts/systems/mortality_system.gd`
- 📄 source: `data/species/human/mortality/siler_parameters.json`

<!-- MANUAL:START -->

<!-- MANUAL:END -->
