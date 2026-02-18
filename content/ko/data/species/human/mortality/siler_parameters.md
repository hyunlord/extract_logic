---
title: "siler_parameters Data"
description: "species/human/mortality data file documentation"
generated: true
source_files:
  - "data/species/human/mortality/siler_parameters.json"
nav_order: 10
---

# siler_parameters

📄 소스: `data/species/human/mortality/siler_parameters.json` | 분류: species/human/mortality | 유형: object

## 개요

- 설정 내용: 종족 사망률 위험도와 생존 보정값. Species mortality hazards and survival modifiers.
- 읽는 시스템/모듈: species_manager
- 관련 문서: [`mortality`](../../../../systems/mortality.md)

## 사망 모델 해석

This file defines parameters for the Siler competing-risk hazard model used by the mortality system. (사망 시스템이 사용하는 Siler 경쟁위험도 모델 파라미터)

Siler hazard (Siler 사망 위험도):

$$\mu(x) = a_1 e^{-b_1 x} + a_2 + a_3 e^{b_3 x}$$

- `a1,b1`: infant/early-life hazard that decays with age. (영아/초기 위험도, 연령 증가로 감소)
- `a2`: background hazard floor. (연령 무관 기본 위험도)
- `a3,b3`: senescent hazard that grows with age. (노년기 위험도, 연령 증가로 증가)

### 기본 파라미터

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `a1` | 0.6 | float | Infant mortality amplitude in the Siler hazard term. (영아 사망 위험도 진폭) |
| `a2` | 0.01 | float | Age-independent background mortality floor. (연령 무관 기본 사망률) |
| `a3` | 0.0001 | float | Late-life mortality growth amplitude. (노년기 위험도 진폭) |
| `b1` | 1.3 | float | Rate at which infant mortality hazard declines with age. (연령에 따른 영아 위험도 감소율) |
| `b3` | 0.09 | float | Exponential growth rate of senescent mortality. (노년기 위험도 증가율) |

### 기술 보정

Higher technology typically reduces mortality via these coefficients; lower hazard ⇒ higher survival. (기술 수준이 높을수록 위험도↓ → 생존율↑)

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `tech_modifiers.k1` | 0.3 | float | Tech-driven reduction for infant hazard; lower hazard ⇒ higher survival. (기술로 영아 위험도 감소 → 생존율 증가) |
| `tech_modifiers.k2` | 0.2 | float | Tech-driven reduction for background hazard; lower hazard ⇒ higher survival. (기술로 기본 위험도 감소 → 생존율 증가) |
| `tech_modifiers.k3` | 0.05 | float | Tech-driven reduction for senescent hazard; lower hazard ⇒ higher survival. (기술로 노년 위험도 감소 → 생존율 증가) |

### 영아 보호

These parameters model caregiver buffering for infant survival during vulnerable periods. (보호자 돌봄에 따른 생존 완충)

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `care_protection.hunger_min` | 0.3 threshold | float | Minimum hunger condition where infant care protection remains active. (보호 유지 최소 배고픔) |
| `care_protection.protection_factor` | 0.6 multiplier | float | Fraction of infant mortality risk reduced by effective care. (보호로 줄어드는 위험 비율) |

### 계절 환경 영향

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `season_modifiers.summer.infant` | 0.9 | float | Seasonal multiplier for infant mortality during summer. (summer 영아 사망률 계절 배수) |
| `season_modifiers.winter.background` | 1.2 | float | Seasonal multiplier for background mortality during winter. (winter 기본 사망률 계절 배수) |
| `season_modifiers.winter.infant` | 1.3 | float | Seasonal multiplier for infant mortality during winter. (winter 영아 사망률 계절 배수) |

## 참고 문헌

- Siler (1979) Competing-Risk Model

## 레퍼런스

- [`species_manager`](../../../../core/species_manager.md) - references data under `data/species/`

## 수동 노트

<!-- MANUAL:START -->
<!-- MANUAL:END -->
