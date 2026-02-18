---
title: "trait_definitions_fixed Data"
description: "personality data file documentation"
generated: true
source_files:
  - "data/personality/trait_definitions_fixed.json"
nav_order: 10
---

# trait_definitions_fixed

📄 소스: `data/personality/trait_definitions_fixed.json` | 분류: personality | 유형: array

## 개요

- 설정 내용: `personality` 데이터 도메인 설정 값. Configuration values for the `personality` data domain.
- 읽는 시스템/모듈: references.json에서 추론되지 않음
- 관련 문서: 없음

## 해석된 파라미터

### 임계 & 경계

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `item.condition.threshold` | 0.92 threshold | float | Activation boundary used by game logic. (작동 임계값) |
| `item.effects.stress_modifiers.break_threshold_mult` | 0.98 threshold | float | Activation boundary used by game logic. (작동 임계값) |

### 가중치 & 배수

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `item.effects.behavior_weights.betray` | 0.75 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.behavior_weights.leadership` | 1.05 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.behavior_weights.social` | 1.1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.behavior_weights.steal` | 0.7 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.combat_modifiers.aggression_mult` | 0.95 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.combat_modifiers.morale_mult` | 1.02 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.combat_modifiers.war_crime_propensity_mult` | 0.6 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.relationship_modifiers.betrayal_propensity_mult` | 0.6 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.relationship_modifiers.trust_gain_mult` | 1.25 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.relationship_modifiers.trust_loss_mult` | 0.85 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.stress_modifiers.stress_gain_mult` | 1.05 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.stress_modifiers.stress_recovery_mult` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.work_modifiers.error_rate_mult` | 0.95 rate | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.work_modifiers.quality_mult` | 1.05 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `item.effects.work_modifiers.speed_mult` | 0.98 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |

### 스트레스 & 감정

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `item.effects.emotion_modifiers.anger_sensitivity` | 0.95 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `item.effects.emotion_modifiers.guilt_sensitivity` | 1.2 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `item.effects.emotion_modifiers.shame_sensitivity` | 1.1 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `item.effects.stress_modifiers.violation_stress.deceive` | 12 | int | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `item.effects.stress_modifiers.violation_stress.lie` | 14 | int | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `item.effects.stress_modifiers.violation_stress.take_bribe` | 18 | int | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |

### 식별자 & 라벨

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `item.id` | f_sincere | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `item.name_en` | Sincere | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `item.name_kr` | 진실한 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `item.type` | personality | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |

### 기타 파라미터

| 매개변수 | 값 | 유형 | 게임 영향 |
|----------------------|-----------|------------|-----------------------------|
| `items` | 187 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `item.anti_synergies` | 3 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `item.anti_synergies.sample` | f_deceptive | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `item.condition.direction` | high | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `item.condition.facet` | H_sincerity | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `item.description_en` | Prefers telling the truth as-is and feels strong aversion to deception or backroom deals. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `item.description_kr` | 사실을 왜곡하기보다 있는 그대로 말하려 하며, 속임수나 뒷거래에 강한 거부감을 느낀다. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `item.opposite_actions` | 3 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `item.opposite_actions.sample` | lie | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `item.synergies` | 3 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `item.synergies.sample` | f_fair_minded | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `item.valence` | positive | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |

## 레퍼런스

- 참조 없음

## 수동 노트

<!-- MANUAL:START -->
<!-- MANUAL:END -->
