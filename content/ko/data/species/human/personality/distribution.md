---
title: "distribution Data"
description: "species/human/personality data file documentation"
generated: true
source_files:
  - "data/species/human/personality/distribution.json"
nav_order: 10
---

# distribution

📄 소스: `data/species/human/personality/distribution.json` | 분류: species/human/personality | 유형: object

## 개요

- 설정 내용: `species/human/personality` 데이터 도메인 설정 값. Configuration values for the `species/human/personality` data domain.
- 읽는 시스템/모듈: species_manager
- 관련 문서: [`species_manager`](../../../../core/species_manager.md)

## 해석된 파라미터

### 가중치 & 배수

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `maturation.A.age_range` | 2 items | array | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.A.age_range.sample` | 18 multiplier | int | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.A.target_shift` | 0 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.C.age_range` | 2 items | array | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.C.age_range.sample` | 18 multiplier | int | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.C.target_shift` | 0 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.E.age_range` | 2 items | array | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.E.age_range.sample` | 18 multiplier | int | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.E.target_shift` | 0.3 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.H.age_range` | 2 items | array | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.H.age_range.sample` | 18 multiplier | int | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.H.target_shift` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.O.age_range` | 2 items | array | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.O.age_range.sample` | 18 multiplier | int | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.O.target_shift` | 0 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.X.age_range` | 2 items | array | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.X.age_range.sample` | 18 multiplier | int | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `maturation.X.target_shift` | 0.3 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |

### 기타 파라미터

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `comment_facet_spread` | Intra-axis facet variance (z-score). 0.75 allows diverse facet profiles within same axis, enabling contradictory trait combos (e.g. fearful+low empathy). Previous: 0.35 | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `comment_sd` | Academic SD=0.15, widened for gameplay. Ashton & Lee 2009 | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `correlation_matrix.axes_order` | 6 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `correlation_matrix.axes_order.sample` | H | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `correlation_matrix.matrix` | 6 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `correlation_matrix.matrix.sample` | 6 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `facet_spread` | 0.75 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `heritability.A` | 0.47 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `heritability.C` | 0.52 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `heritability.E` | 0.58 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `heritability.H` | 0.45 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `heritability.O` | 0.63 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `heritability.X` | 0.57 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `ou_parameters.sigma` | 0.03 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `ou_parameters.theta` | 0.03 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `sd` | 0.25 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `sex_difference_d.A` | 0.28 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `sex_difference_d.C` | 0 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `sex_difference_d.E` | 0.96 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `sex_difference_d.H` | 0.41 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `sex_difference_d.O` | -0.04 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `sex_difference_d.X` | 0.1 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |

## 레퍼런스

- [`species_manager`](../../../../core/species_manager.md) - references data under `data/species/`

## 수동 노트

<!-- MANUAL:START -->
<!-- MANUAL:END -->
