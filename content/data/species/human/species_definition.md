---
title: "species_definition Data"
description: "species/human data file documentation"
generated: true
source_files:
  - "data/species/human/species_definition.json"
nav_order: 10
---

# species_definition

📄 source (출처): `data/species/human/species_definition.json` | Category (분류): species/human | Type (유형): object

## 개요 (Overview)

- Configures (설정 내용): `species/human` 데이터 도메인 설정 값. Configuration values for the `species/human` data domain.
- Read by systems/modules (읽는 시스템/모듈): species_manager
- Related documentation (관련 문서): [`species_manager`](../../../core/species_manager.md)

## 해석된 파라미터 (Interpreted Parameters)

### Thresholds & Bounds (임계/경계)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `base_stats.max_age` | 120 | int | Activation boundary used by game logic. (작동 임계값) |

### Stress & Emotion (스트레스/감정)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `emotion_model` | plutchik | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotion_path` | res://data/species/human/emotions/ | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |

### Identifiers & Labels (식별자/라벨)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `species_id` | human | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `species_name` | Human | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `species_name_kr` | 인간 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |

### Other Parameters (기타)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `available_cultures` | 3 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `available_cultures.sample` | proto_nature | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `base_stats.fertility_range` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `base_stats.fertility_range.sample` | 15 | int | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `base_stats.gestation_days` | 270 days | int | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `base_stats.maturity_age` | 15 | int | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `mortality_model` | siler | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `mortality_path` | res://data/species/human/mortality/ | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `needs_model` | maslow_erg | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `needs_path` | res://data/species/human/needs/ | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `personality_model` | hexaco | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `personality_path` | res://data/species/human/personality/ | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |

## 참조하는 시스템 (Referenced By)

- [`species_manager`](../../../core/species_manager.md) - references data under `data/species/`

## 수동 노트 (Manual Notes)

<!-- MANUAL:START -->
<!-- MANUAL:END -->
