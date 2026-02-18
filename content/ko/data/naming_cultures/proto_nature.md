---
title: "proto_nature Data"
description: "naming_cultures data file documentation"
generated: true
source_files:
  - "data/naming_cultures/proto_nature.json"
nav_order: 10
---

# proto_nature

📄 source (출처): `data/naming_cultures/proto_nature.json` | Category (분류): naming_cultures | Type (유형): object

## 개요 (Overview)

- Configures (설정 내용): `naming_cultures` 데이터 도메인 설정 값. Configuration values for the `naming_cultures` data domain.
- Read by systems/modules (읽는 시스템/모듈): name_generator
- Related documentation (관련 문서): [`name_generator`](../../core/name_generator.md)

## 해석된 파라미터 (Interpreted Parameters)

### Weights & Multipliers (가중/배수)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `allow_markov_generation` | false | boolean | Strength multiplier used in gameplay calculations. (계산 강도 배수) |

### Identifiers & Labels (식별자/라벨)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `culture_id` | proto_nature | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `display_name` | Nature Names (Primitive) | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `given_names.female` | 65 items | array | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `given_names.female.sample` | Alba | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `given_names.male` | 64 items | array | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `given_names.male.sample` | Ash | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `given_names.neutral` | 16 items | array | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `given_names.neutral.sample` | Ash | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `name_structure` | given | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `surname_rule` | none | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |

### Other Parameters (기타)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `description` | Names derived from nature. Early stone age. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `patronymic_rule` | none | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |

## 참조하는 시스템 (Referenced By)

- [`name_generator`](../../core/name_generator.md) - references data under `data/naming_cultures/`

## 수동 노트 (Manual Notes)

<!-- MANUAL:START -->
<!-- MANUAL:END -->
