---
title: "mental_breaks Data"
description: "data data file documentation"
generated: true
source_files:
  - "data/mental_breaks.json"
nav_order: 10
---

# mental_breaks

📄 source (출처): `data/mental_breaks.json` | Category (분류): data | Type (유형): object

## 개요 (Overview)

- Configures (설정 내용): `data` 데이터 도메인 설정 값. Configuration values for the `data` data domain.
- Read by systems/modules (읽는 시스템/모듈): mental_break
- Related documentation (관련 문서): [`mental_break`](../../systems/mental_break.md)

## 해석된 파라미터 (Interpreted Parameters)

### Timing & Decay (시간/감쇠)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `compulsive_ritual.duration_base_ticks` | 1 multiplier | int | 기본 지속 시간 (틱) — mental break 지속 틱 수 기준값. Base duration in ticks for this mental break type. |
| `compulsive_ritual.duration_variance_ticks` | 3 multiplier | int | 지속 시간 분산 (틱) — 기준값에 더해지는 무작위 분산 범위. Random variance range added to base duration. |
| `fugue.duration_base_ticks` | 24 multiplier | int | 기본 지속 시간 (틱) — mental break 지속 틱 수 기준값. Base duration in ticks for this mental break type. |
| `fugue.duration_variance_ticks` | 60 multiplier | int | 지속 시간 분산 (틱) — 기준값에 더해지는 무작위 분산 범위. Random variance range added to base duration. |
| `grief_withdrawal.duration_base_ticks` | 24 multiplier | int | 기본 지속 시간 (틱) — mental break 지속 틱 수 기준값. Base duration in ticks for this mental break type. |
| `grief_withdrawal.duration_variance_ticks` | 36 multiplier | int | 지속 시간 분산 (틱) — 기준값에 더해지는 무작위 분산 범위. Random variance range added to base duration. |
| `hysterical_bonding.duration_base_ticks` | 3 multiplier | int | 기본 지속 시간 (틱) — mental break 지속 틱 수 기준값. Base duration in ticks for this mental break type. |
| `hysterical_bonding.duration_variance_ticks` | 9 multiplier | int | 지속 시간 분산 (틱) — 기준값에 더해지는 무작위 분산 범위. Random variance range added to base duration. |
| `outrage_violence.duration_base_ticks` | 5 multiplier | int | 기본 지속 시간 (틱) — mental break 지속 틱 수 기준값. Base duration in ticks for this mental break type. |
| `outrage_violence.duration_variance_ticks` | 7 multiplier | int | 지속 시간 분산 (틱) — 기준값에 더해지는 무작위 분산 범위. Random variance range added to base duration. |
| `panic.duration_base_ticks` | 2 multiplier | int | 기본 지속 시간 (틱) — mental break 지속 틱 수 기준값. Base duration in ticks for this mental break type. |
| `panic.duration_variance_ticks` | 2 multiplier | int | 지속 시간 분산 (틱) — 기준값에 더해지는 무작위 분산 범위. Random variance range added to base duration. |
| `paranoia.duration_base_ticks` | 48 multiplier | int | 기본 지속 시간 (틱) — mental break 지속 틱 수 기준값. Base duration in ticks for this mental break type. |
| `paranoia.duration_variance_ticks` | 120 multiplier | int | 지속 시간 분산 (틱) — 기준값에 더해지는 무작위 분산 범위. Random variance range added to base duration. |
| `purge.duration_base_ticks` | 3 multiplier | int | 기본 지속 시간 (틱) — mental break 지속 틱 수 기준값. Base duration in ticks for this mental break type. |
| `purge.duration_variance_ticks` | 5 multiplier | int | 지속 시간 분산 (틱) — 기준값에 더해지는 무작위 분산 범위. Random variance range added to base duration. |
| `rage.duration_base_ticks` | 3 multiplier | int | 기본 지속 시간 (틱) — mental break 지속 틱 수 기준값. Base duration in ticks for this mental break type. |
| `rage.duration_variance_ticks` | 3 multiplier | int | 지속 시간 분산 (틱) — 기준값에 더해지는 무작위 분산 범위. Random variance range added to base duration. |

### Weights & Multipliers (가중/배수)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `compulsive_ritual.behavior_override.speed_multiplier` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `compulsive_ritual.personality_weights.A` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `compulsive_ritual.personality_weights.C` | 1.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `compulsive_ritual.personality_weights.E` | 0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `compulsive_ritual.personality_weights.H` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `compulsive_ritual.personality_weights.O` | 0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `compulsive_ritual.personality_weights.X` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `compulsive_ritual.stress_catharsis_factor` | 0.85 multiplier | float | 카타르시스 회복 비율 — mental break 종료 후 스트레스 회복 계수. Stress recovery factor on break resolution. |
| `fugue.behavior_override.speed_multiplier` | 0.8 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `fugue.personality_weights.A` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `fugue.personality_weights.C` | -0.3 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `fugue.personality_weights.E` | 0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `fugue.personality_weights.H` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `fugue.personality_weights.O` | 1.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `fugue.personality_weights.X` | -0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `fugue.stress_catharsis_factor` | 0.8 multiplier | float | 카타르시스 회복 비율 — mental break 종료 후 스트레스 회복 계수. Stress recovery factor on break resolution. |
| `grief_withdrawal.behavior_override.speed_multiplier` | 0.3 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `grief_withdrawal.personality_weights.A` | 0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `grief_withdrawal.personality_weights.C` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `grief_withdrawal.personality_weights.E` | 1.3 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `grief_withdrawal.personality_weights.H` | 0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `grief_withdrawal.personality_weights.O` | -0.3 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `grief_withdrawal.personality_weights.X` | -0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `grief_withdrawal.stress_catharsis_factor` | 0.85 multiplier | float | 카타르시스 회복 비율 — mental break 종료 후 스트레스 회복 계수. Stress recovery factor on break resolution. |
| `hysterical_bonding.behavior_override.speed_multiplier` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `hysterical_bonding.personality_weights.A` | 0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `hysterical_bonding.personality_weights.C` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `hysterical_bonding.personality_weights.E` | 1 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `hysterical_bonding.personality_weights.H` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `hysterical_bonding.personality_weights.O` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `hysterical_bonding.personality_weights.X` | 1 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `hysterical_bonding.stress_catharsis_factor` | 0.8 multiplier | float | 카타르시스 회복 비율 — mental break 종료 후 스트레스 회복 계수. Stress recovery factor on break resolution. |
| `outrage_violence.behavior_override.speed_multiplier` | 1.3 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `outrage_violence.personality_weights.A` | -3 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `outrage_violence.personality_weights.C` | -1 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `outrage_violence.personality_weights.E` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `outrage_violence.personality_weights.H` | -1.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `outrage_violence.personality_weights.O` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `outrage_violence.personality_weights.X` | 0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `outrage_violence.stress_catharsis_factor` | 0.6 multiplier | float | 카타르시스 회복 비율 — mental break 종료 후 스트레스 회복 계수. Stress recovery factor on break resolution. |
| `panic.behavior_override.speed_multiplier` | 1.3 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `panic.personality_weights.A` | 0.1 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `panic.personality_weights.C` | -0.1 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `panic.personality_weights.E` | 1.7 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `panic.personality_weights.H` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `panic.personality_weights.O` | -0.1 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `panic.personality_weights.X` | -0.3 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `panic.stress_catharsis_factor` | 0.8 multiplier | float | 카타르시스 회복 비율 — mental break 종료 후 스트레스 회복 계수. Stress recovery factor on break resolution. |
| `paranoia.behavior_override.speed_multiplier` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `paranoia.personality_weights.A` | -0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `paranoia.personality_weights.C` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `paranoia.personality_weights.E` | 1.2 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `paranoia.personality_weights.H` | -0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `paranoia.personality_weights.O` | -0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `paranoia.personality_weights.X` | -1 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `paranoia.stress_catharsis_factor` | 0.95 multiplier | float | 카타르시스 회복 비율 — mental break 종료 후 스트레스 회복 계수. Stress recovery factor on break resolution. |
| `purge.behavior_override.speed_multiplier` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `purge.personality_weights.A` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `purge.personality_weights.C` | -2 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `purge.personality_weights.E` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `purge.personality_weights.H` | -0.3 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `purge.personality_weights.O` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `purge.personality_weights.X` | 0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `purge.stress_catharsis_factor` | 0.75 multiplier | float | 카타르시스 회복 비율 — mental break 종료 후 스트레스 회복 계수. Stress recovery factor on break resolution. |
| `rage.behavior_override.speed_multiplier` | 1.2 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `rage.personality_weights.A` | -2 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `rage.personality_weights.C` | -0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `rage.personality_weights.E` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `rage.personality_weights.H` | -0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `rage.personality_weights.O` | 0 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `rage.personality_weights.X` | 0.5 multiplier | float | 이 유형의 mental break 선택 가중치. Selection weight for this break type during break selection. |
| `rage.stress_catharsis_factor` | 0.65 multiplier | float | 카타르시스 회복 비율 — mental break 종료 후 스트레스 회복 계수. Stress recovery factor on break resolution. |

### Probabilities (확률)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `compulsive_ritual.scar_chance_base` | 0.1 probability | float | Probability that this branch triggers during evaluation. (발생 확률) |
| `fugue.scar_chance_base` | 0.15 probability | float | Probability that this branch triggers during evaluation. (발생 확률) |
| `grief_withdrawal.scar_chance_base` | 0.22 probability | float | Probability that this branch triggers during evaluation. (발생 확률) |
| `hysterical_bonding.scar_chance_base` | 0.1 probability | float | Probability that this branch triggers during evaluation. (발생 확률) |
| `outrage_violence.scar_chance_base` | 0.25 probability | float | Probability that this branch triggers during evaluation. (발생 확률) |
| `panic.scar_chance_base` | 0.15 probability | float | Probability that this branch triggers during evaluation. (발생 확률) |
| `paranoia.scar_chance_base` | 0.28 probability | float | Probability that this branch triggers during evaluation. (발생 확률) |
| `purge.scar_chance_base` | 0.1 probability | float | Probability that this branch triggers during evaluation. (발생 확률) |
| `rage.scar_chance_base` | 0.12 probability | float | Probability that this branch triggers during evaluation. (발생 확률) |

### Stress & Emotion (스트레스/감정)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `paranoia.behavior_override.trust_override` | -0.5 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `paranoia.trait_modifiers.trusting` | 0.5 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |

### Identifiers & Labels (식별자/라벨)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `compulsive_ritual.behavior_override.ignore_jobs` | true | boolean | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `compulsive_ritual.behavior_override.mode` | repeat_action | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `compulsive_ritual.behavior_override.target_rule` | current_location | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `compulsive_ritual.id` | compulsive_ritual | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `compulsive_ritual.name_en` | Compulsive Ritual | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `compulsive_ritual.name_kr` | 강박 의식 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `compulsive_ritual.scar_id` | hypervigilance | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `fugue.behavior_override.ignore_jobs` | true | boolean | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `fugue.behavior_override.leave_settlement` | true | boolean | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `fugue.behavior_override.mode` | wander_away | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `fugue.behavior_override.target_rule` | random_far_direction | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `fugue.id` | fugue | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `fugue.name_en` | Dissociative Fugue | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `fugue.name_kr` | 해리성 둔주 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `fugue.scar_id` | dissociative_tendency | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `grief_withdrawal.behavior_override.ignore_jobs` | true | boolean | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `grief_withdrawal.behavior_override.mode` | withdraw_to_home | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `grief_withdrawal.behavior_override.reject_social` | true | boolean | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `grief_withdrawal.behavior_override.target_rule` | home_or_corner | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `grief_withdrawal.id` | grief_withdrawal | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `grief_withdrawal.name_en` | Grief Withdrawal | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `grief_withdrawal.name_kr` | 애도 칩거 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `grief_withdrawal.scar_id` | complicated_grief | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `hysterical_bonding.behavior_override.ignore_jobs` | true | boolean | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `hysterical_bonding.behavior_override.mode` | cling_to_target | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `hysterical_bonding.behavior_override.target_rule` | closest_positive_relation | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `hysterical_bonding.id` | hysterical_bonding | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `hysterical_bonding.name_en` | Hysterical Bonding | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `hysterical_bonding.name_kr` | 불안 집착 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `hysterical_bonding.scar_id` | anxious_attachment | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `outrage_violence.behavior_override.can_use_weapons` | true | boolean | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `outrage_violence.behavior_override.ignore_jobs` | true | boolean | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `outrage_violence.behavior_override.lethal` | true | boolean | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `outrage_violence.behavior_override.mode` | seek_and_destroy | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `outrage_violence.behavior_override.target_rule` | nearest_negative_relation | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `outrage_violence.id` | outrage_violence | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `outrage_violence.name_en` | Outrage Violence | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `outrage_violence.name_kr` | 폭력 난동 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `outrage_violence.scar_id` | violence_imprint | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `panic.behavior_override.ignore_jobs` | true | boolean | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `panic.behavior_override.mode` | flee_hide | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `panic.behavior_override.target_rule` | nearest_safe_spot | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `panic.id` | panic | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `panic.name_en` | Panic | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `panic.name_kr` | 공황 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `panic.scar_id` | hypervigilance | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `paranoia.behavior_override.ignore_jobs` | false | boolean | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `paranoia.behavior_override.mode` | distrust_isolate | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `paranoia.behavior_override.target_rule` | avoid_all | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `paranoia.id` | paranoia | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `paranoia.name_en` | Paranoia | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `paranoia.name_kr` | 편집증 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `paranoia.scar_id` | chronic_paranoia | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `purge.behavior_override.ignore_jobs` | true | boolean | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `purge.behavior_override.mode` | binge_consume | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `purge.behavior_override.target_rule` | nearest_food_storage | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `purge.id` | purge | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `purge.name_en` | Purge | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `purge.name_kr` | 폭식/낭비 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `purge.scar_id` | compulsive_consumption | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `rage.behavior_override.ignore_jobs` | true | boolean | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `rage.behavior_override.mode` | attack_smash | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `rage.behavior_override.target_rule` | conflict_then_nearest | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `rage.id` | rage | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `rage.name_en` | Rage | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `rage.name_kr` | 분노 폭발 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `rage.scar_id` | anger_dysregulation | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |

### Other Parameters (기타)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `compulsive_ritual.description_en` | A brief compulsive episode in which the individual repetitively performs an action at their current location. High conscientiousness paradoxically amplifies risk; ritual provides stress relief. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `compulsive_ritual.description_kr` | 현재 위치에서 특정 행동을 반복하는 단기 강박 상태. 절제력(C축)이 높을수록 발동하기 쉬우며, 반복 행동으로 스트레스를 정화한다. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `compulsive_ritual.energy_cost` | 0.05 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `compulsive_ritual.severity` | minor | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `compulsive_ritual.trait_modifiers.impulsive` | 0.6 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `compulsive_ritual.trait_modifiers.ritualist` | 1.4 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `fugue.description_en` | A dissociative wandering episode in which the individual leaves the settlement and drifts in a random direction. Longest potential duration; high openness increases susceptibility. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `fugue.description_kr` | 정체성과 기억이 흐려지며 정착지를 벗어나 방황하는 해리 상태. 가장 긴 지속 시간을 가지며 개방성(O축)이 높을수록 발동하기 쉽다. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `fugue.energy_cost` | 0.15 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `fugue.severity` | major | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `fugue.trait_modifiers.loner` | 1.2 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `fugue.trait_modifiers.rebellious` | 1.1 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `grief_withdrawal.description_en` | A prolonged grief episode in which the individual retreats home and rejects all social contact. High emotionality prolongs the episode; may scar with complicated grief. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `grief_withdrawal.description_kr` | 집이나 구석에 칩거하며 사회적 접촉을 거부하는 장기 애도 상태. 감정이입(E축)이 높을수록 지속 시간이 길어지는 경향이 있다. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `grief_withdrawal.energy_cost` | 0.08 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `grief_withdrawal.severity` | major | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `grief_withdrawal.trait_modifiers.cold_blooded` | 0.6 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `grief_withdrawal.trait_modifiers.empathic` | 1.3 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `hysterical_bonding.description_en` | An anxious clinging episode in which the individual latches onto their closest positive relationship and refuses to separate. High sociability and dependence traits amplify risk. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `hysterical_bonding.description_kr` | 가장 친한 관계의 인물에게 달라붙어 떨어지지 않으려 하는 불안 집착 상태. 사회성(X축)이 높거나 의존적 성향이 강할수록 발생하기 쉽다. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `hysterical_bonding.energy_cost` | 0.05 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `hysterical_bonding.severity` | minor | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `hysterical_bonding.trait_modifiers.loner` | 0.4 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `hysterical_bonding.trait_modifiers.social_clinger` | 1.4 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `outrage_violence.description_en` | An extreme violent episode in which the individual seeks out negatively-regarded targets with lethal intent, potentially using weapons. The most dangerous mental break type. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `outrage_violence.description_kr` | 살상 도구까지 동원할 수 있는 극단적 폭력 상태. 부정적 관계의 대상을 찾아 공격하며, 가장 심각한 mental break 유형이다. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `outrage_violence.energy_cost` | 0.3 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `outrage_violence.severity` | extreme | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `outrage_violence.trait_modifiers.berserker` | 1.6 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `outrage_violence.trait_modifiers.peaceful` | 0.3 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `outrage_violence.trait_modifiers.ruthless` | 1.4 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `panic.description_en` | A short-lived terror episode in which the individual flees toward the nearest safe spot. Resolves quickly but may leave a hypervigilance scar. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `panic.description_kr` | 극도의 공포로 인해 가장 가까운 안전 장소로 도망치는 단기 공황 상태. 빠르게 해소되지만 과잉경계 흉터(scar)를 남길 수 있다. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `panic.energy_cost` | 0.15 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `panic.severity` | minor | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `panic.trait_modifiers.brave` | 0.6 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `panic.trait_modifiers.cowardly` | 1.6 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `paranoia.description_en` | A chronic paranoid state of intense distrust toward all others, leading to social isolation. Jobs are not abandoned but relationship trust collapses; high chronic paranoia scar risk. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `paranoia.description_kr` | 모든 타인에 대한 불신과 고립으로 이어지는 만성 편집 상태. 직업은 유지하지만 관계 신뢰도가 급락하며 만성 편집증 흉터 위험이 높다. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `paranoia.energy_cost` | 0.03 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `paranoia.severity` | major | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `paranoia.trait_modifiers.suspicious` | 1.4 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `purge.description_en` | A compulsive binge-eating or resource-wasting episode directed at the nearest food storage. Low conscientiousness amplifies the likelihood. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `purge.description_kr` | 가장 가까운 식량 저장소를 찾아 폭식하거나 자원을 낭비하는 충동 상태. 절제력(C축)이 낮을수록 발생하기 쉽다. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `purge.energy_cost` | 0.05 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `purge.severity` | minor | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `purge.trait_modifiers.ascetic` | 0.5 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `purge.trait_modifiers.greedy` | 1.3 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `rage.description_en` | An explosive burst of uncontrolled anger causing the individual to attack objects or others nearby. Highly energy-draining and may scar with anger dysregulation. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `rage.description_kr` | 통제 불능의 분노 폭발로 주변 사물이나 타인을 공격하는 상태. 에너지 소모가 크고 분노 조절 장애 흉터를 남길 수 있다. | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `rage.energy_cost` | 0.2 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `rage.severity` | major | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |

## 참조하는 시스템 (Referenced By)

- [`mental_break`](../../systems/mental_break.md) - references `data/mental_breaks.json`

## 수동 노트 (Manual Notes)

<!-- MANUAL:START -->
<!-- MANUAL:END -->
