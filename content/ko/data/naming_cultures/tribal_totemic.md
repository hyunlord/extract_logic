---
title: "tribal_totemic Data"
description: "naming_cultures data file documentation"
generated: true
source_files:
  - "data/naming_cultures/tribal_totemic.json"
nav_order: 10
---

# tribal_totemic

📄 소스: `data/naming_cultures/tribal_totemic.json` | 분류: naming_cultures | 유형: object

## 개요

- 설정 내용: `naming_cultures` 데이터 도메인 설정 값. Configuration values for the `naming_cultures` data domain.
- 읽는 시스템/모듈: name_generator
- 관련 문서: [`name_generator`](../../core/name_generator.md)

## 해석된 파라미터

### 임계 & 경계

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `markov_config.max_length` | 6 | int | Activation boundary used by game logic. (작동 임계값) |
| `markov_config.min_length` | 3 | int | Activation boundary used by game logic. (작동 임계값) |
| `syllable_count.max` | 3 | int | Activation boundary used by game logic. (작동 임계값) |
| `syllable_count.min` | 1 | int | Activation boundary used by game logic. (작동 임계값) |

### 가중치 & 배수

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `allow_markov_generation` | true | boolean | Strength multiplier used in gameplay calculations. (계산 강도 배수) |

### 식별자 & 라벨

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `culture_id` | tribal_totemic | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `display_name` | Totemic Tribal | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `given_names.female` | 10 items | array | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `given_names.female.sample` | Mira | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `given_names.male` | 10 items | array | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `given_names.male.sample` | Kor | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `name_structure` | given+epithet | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `surname_rule` | none | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |

### 기타 파라미터

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `description` | Totem animal/nature + trait/deed combinations. Tribal era. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `epithet_unlock_age` | 12 | int | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `epithets.by_deed` | 4 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `epithets.by_deed.sample` | First-fire | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `epithets.by_totem` | 5 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `epithets.by_totem.sample` | of-Wolf | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `epithets.by_trait.high_agility` | 3 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `epithets.by_trait.high_agility.sample` | Swift | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `epithets.by_trait.high_intelligence` | 3 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `epithets.by_trait.high_intelligence.sample` | Wise | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `epithets.by_trait.high_openness` | 3 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `epithets.by_trait.high_openness.sample` | Seeker | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `epithets.by_trait.high_strength` | 3 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `epithets.by_trait.high_strength.sample` | Strong | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `markov_config.order` | 2 | int | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `patronymic_config.female_prefix` |  | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `patronymic_config.female_suffix` | 's daughter | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `patronymic_config.male_prefix` |  | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `patronymic_config.male_suffix` | 's son | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `patronymic_rule` | prefix | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `syllable_pools.coda` | 10 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `syllable_pools.coda.sample` | n | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `syllable_pools.coda_final` | 9 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `syllable_pools.coda_final.sample` | n | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `syllable_pools.nucleus` | 9 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `syllable_pools.nucleus.sample` | a | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `syllable_pools.onset_female` | 9 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `syllable_pools.onset_female.sample` | m | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `syllable_pools.onset_male` | 11 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `syllable_pools.onset_male.sample` | k | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |

## 레퍼런스

- [`name_generator`](../../core/name_generator.md) - references data under `data/naming_cultures/`

## 수동 노트

<!-- MANUAL:START -->
<!-- MANUAL:END -->
