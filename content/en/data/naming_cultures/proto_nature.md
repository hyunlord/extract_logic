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

## Overview

- Configures: `naming_cultures` 데이터 도메인 설정 값. Configuration values for the `naming_cultures` data domain.
- Read by systems/modules: name_generator
- Related documentation: [`name_generator`](../../core/name_generator.md)

## Interpreted Parameters

### Weights & Multipliers

| Parameter | Value | Type | What it controls |
|----------------------|-----------|------------|-----------------------------|
| `allow_markov_generation` | false | boolean | Strength multiplier used in gameplay calculations. (계산 강도 배수) |

### Identifiers & Labels

| Parameter | Value | Type | What it controls |
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

### Other Parameters

| Parameter | Value | Type | What it controls |
|----------------------|-----------|------------|-----------------------------|
| `description` | Names derived from nature. Early stone age. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `patronymic_rule` | none | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |

## References

- [`name_generator`](../../core/name_generator.md) - references data under `data/naming_cultures/`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
