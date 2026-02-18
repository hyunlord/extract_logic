---
title: "tribal_totemic Data"
description: "species/human/cultures data file documentation"
generated: true
source_files:
  - "data/species/human/cultures/tribal_totemic.json"
nav_order: 10
---

# tribal_totemic

📄 source (출처): `data/species/human/cultures/tribal_totemic.json` | Category (분류): species/human/cultures | Type (유형): object

## 개요 (Overview)

- Configures (설정 내용): `species/human/cultures` 데이터 도메인 설정 값. Configuration values for the `species/human/cultures` data domain.
- Read by systems/modules (읽는 시스템/모듈): species_manager
- Related documentation (관련 문서): [`species_manager`](../../../../core/species_manager.md)

## 해석된 파라미터 (Interpreted Parameters)

### Thresholds & Bounds (임계/경계)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `naming_culture` | tribal_totemic | string | Activation boundary used by game logic. (작동 임계값) |

### Stress & Emotion (스트레스/감정)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `emotion_modifiers.disgust` | 1.1 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotion_modifiers.fear` | 0.8 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotion_modifiers.trust` | 1.3 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |

### Identifiers & Labels (식별자/라벨)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `culture_id` | tribal_totemic | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `culture_name` | 부족 토템 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |

### Other Parameters (기타)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `personality_shift.A` | 0.2 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `personality_shift.C` | 0.2 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `personality_shift.E` | 0 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `personality_shift.H` | 0.2 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `personality_shift.O` | -0.2 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `personality_shift.X` | 0 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |

## 참조하는 시스템 (Referenced By)

- [`species_manager`](../../../../core/species_manager.md) - references data under `data/species/`

## 수동 노트 (Manual Notes)

<!-- MANUAL:START -->
<!-- MANUAL:END -->
