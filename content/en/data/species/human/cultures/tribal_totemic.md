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

## Overview

- Configures: `species/human/cultures` 데이터 도메인 설정 값. Configuration values for the `species/human/cultures` data domain.
- Read by systems/modules: species_manager
- Related documentation: [`species_manager`](../../../../core/species_manager.md)

## Interpreted Parameters

### Thresholds & Bounds

| Parameter | Value | Type | What it controls |
|----------------------|-----------|------------|-----------------------------|
| `naming_culture` | tribal_totemic | string | Activation boundary used by game logic. (작동 임계값) |

### Stress & Emotion

| Parameter | Value | Type | What it controls |
|----------------------|-----------|------------|-----------------------------|
| `emotion_modifiers.disgust` | 1.1 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotion_modifiers.fear` | 0.8 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotion_modifiers.trust` | 1.3 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |

### Identifiers & Labels

| Parameter | Value | Type | What it controls |
|----------------------|-----------|------------|-----------------------------|
| `culture_id` | tribal_totemic | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `culture_name` | 부족 토템 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |

### Other Parameters

| Parameter | Value | Type | What it controls |
|----------------------|-----------|------------|-----------------------------|
| `personality_shift.A` | 0.2 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `personality_shift.C` | 0.2 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `personality_shift.E` | 0 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `personality_shift.H` | 0.2 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `personality_shift.O` | -0.2 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `personality_shift.X` | 0 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |

## References

- [`species_manager`](../../../../core/species_manager.md) - references data under `data/species/`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
