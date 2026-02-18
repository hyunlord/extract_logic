---
title: "trauma_scars Data"
description: "data data file documentation"
generated: true
source_files:
  - "data/trauma_scars.json"
nav_order: 10
---

# trauma_scars

📄 source (출처): `data/trauma_scars.json` | Category (분류): data | Type (유형): object

## 개요 (Overview)

- Configures (설정 내용): `data` 데이터 도메인 설정 값. Configuration values for the `data` data domain.
- Read by systems/modules (읽는 시스템/모듈): trauma_scar
- Related documentation (관련 문서): [`trauma_scar`](../../systems/trauma_scar.md)

## 해석된 파라미터 (Interpreted Parameters)

### Thresholds & Bounds (임계/경계)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `anger_dysregulation.break_threshold_reduction` | 15 threshold | float | Activation boundary used by game logic. (작동 임계값) |
| `anger_dysregulation.max_stacks` | 3 | int | Activation boundary used by game logic. (작동 임계값) |
| `anxious_attachment.break_threshold_reduction` | 8 threshold | float | Activation boundary used by game logic. (작동 임계값) |
| `anxious_attachment.max_stacks` | 3 | int | Activation boundary used by game logic. (작동 임계값) |
| `chronic_paranoia.break_threshold_reduction` | 15 threshold | float | Activation boundary used by game logic. (작동 임계값) |
| `chronic_paranoia.max_stacks` | 3 | int | Activation boundary used by game logic. (작동 임계값) |
| `complicated_grief.break_threshold_reduction` | 12 threshold | float | Activation boundary used by game logic. (작동 임계값) |
| `complicated_grief.max_stacks` | 4 | int | Activation boundary used by game logic. (작동 임계값) |
| `compulsive_consumption.break_threshold_reduction` | 8 threshold | float | Activation boundary used by game logic. (작동 임계값) |
| `compulsive_consumption.max_stacks` | 3 | int | Activation boundary used by game logic. (작동 임계값) |
| `dissociative_tendency.break_threshold_reduction` | 10 threshold | float | Activation boundary used by game logic. (작동 임계값) |
| `dissociative_tendency.max_stacks` | 3 | int | Activation boundary used by game logic. (작동 임계값) |
| `emotional_numbness.break_threshold_reduction` | 5 threshold | float | Activation boundary used by game logic. (작동 임계값) |
| `emotional_numbness.max_stacks` | 3 | int | Activation boundary used by game logic. (작동 임계값) |
| `hypervigilance.break_threshold_reduction` | 10 threshold | float | Activation boundary used by game logic. (작동 임계값) |
| `hypervigilance.max_stacks` | 3 | int | Activation boundary used by game logic. (작동 임계값) |
| `violence_imprint.break_threshold_reduction` | 20 threshold | float | Activation boundary used by game logic. (작동 임계값) |
| `violence_imprint.max_stacks` | 2 | int | Activation boundary used by game logic. (작동 임계값) |

### Weights & Multipliers (가중/배수)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `anger_dysregulation.stress_sensitivity_mult` | 1.2 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `anxious_attachment.stress_sensitivity_mult` | 1.1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `chronic_paranoia.stress_sensitivity_mult` | 1.2 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `complicated_grief.stress_sensitivity_mult` | 1.15 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `compulsive_consumption.stress_sensitivity_mult` | 1.1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `dissociative_tendency.stress_sensitivity_mult` | 1.12 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `emotional_numbness.stress_sensitivity_mult` | 0.9 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `hypervigilance.stress_sensitivity_mult` | 1.15 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `violence_imprint.stress_sensitivity_mult` | 1.25 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |

### Stress & Emotion (스트레스/감정)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `anger_dysregulation.description_key` | SCAR_anger_dysregulation | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `anger_dysregulation.emotion_baseline_shifts.happiness` | -0.05 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `anger_dysregulation.id` | anger_dysregulation | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `anger_dysregulation.name_en` | Anger Dysregulation | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `anger_dysregulation.name_kr` | 분노 조절 장애 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `anger_dysregulation.reactivation_triggers` | 3 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `anger_dysregulation.reactivation_triggers.sample` | conflict | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `anger_dysregulation.resilience_mod` | -0.03 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `anxious_attachment.emotion_baseline_shifts.happiness` | -0.05 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `anxious_attachment.emotion_baseline_shifts.loneliness` | 0.12 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `chronic_paranoia.emotion_baseline_shifts.happiness` | -0.1 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `chronic_paranoia.emotion_baseline_shifts.loneliness` | 0.15 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `chronic_paranoia.emotion_baseline_shifts.stress` | 0.12 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `complicated_grief.emotion_baseline_shifts.grief` | 0.15 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `complicated_grief.emotion_baseline_shifts.happiness` | -0.15 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `complicated_grief.emotion_baseline_shifts.loneliness` | 0.1 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `compulsive_consumption.emotion_baseline_shifts.happiness` | -0.05 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `dissociative_tendency.emotion_baseline_shifts.happiness` | -0.08 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `dissociative_tendency.emotion_baseline_shifts.loneliness` | 0.08 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotional_numbness.description_key` | SCAR_emotional_numbness | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotional_numbness.emotion_baseline_shifts.happiness` | -0.15 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotional_numbness.emotion_baseline_shifts.loneliness` | 0.1 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotional_numbness.emotion_baseline_shifts.love` | -0.1 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotional_numbness.id` | emotional_numbness | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotional_numbness.name_en` | Emotional Numbness | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotional_numbness.name_kr` | 감정 마비 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotional_numbness.reactivation_triggers` | 2 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotional_numbness.reactivation_triggers.sample` | loss | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotional_numbness.resilience_mod` | -0.04 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `hypervigilance.emotion_baseline_shifts.happiness` | -0.05 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `hypervigilance.emotion_baseline_shifts.stress` | 0.1 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `violence_imprint.emotion_baseline_shifts.happiness` | -0.1 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `violence_imprint.emotion_baseline_shifts.stress` | 0.08 | float | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |

### Identifiers & Labels (식별자/라벨)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `anxious_attachment.id` | anxious_attachment | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `anxious_attachment.name_en` | Anxious Attachment | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `anxious_attachment.name_kr` | 불안 애착 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `chronic_paranoia.id` | chronic_paranoia | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `chronic_paranoia.name_en` | Chronic Paranoia | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `chronic_paranoia.name_kr` | 만성 편집증 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `complicated_grief.id` | complicated_grief | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `complicated_grief.name_en` | Complicated Grief | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `complicated_grief.name_kr` | 복잡성 애도 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `compulsive_consumption.id` | compulsive_consumption | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `compulsive_consumption.name_en` | Compulsive Consumption | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `compulsive_consumption.name_kr` | 강박적 소비 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dissociative_tendency.id` | dissociative_tendency | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dissociative_tendency.name_en` | Dissociative Tendency | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dissociative_tendency.name_kr` | 해리 경향 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `hypervigilance.id` | hypervigilance | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `hypervigilance.name_en` | Hypervigilance | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `hypervigilance.name_kr` | 과각성 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `violence_imprint.id` | violence_imprint | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `violence_imprint.name_en` | Violence Imprint | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `violence_imprint.name_kr` | 폭력 각인 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |

### Other Parameters (기타)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `anxious_attachment.description_key` | SCAR_anxious_attachment | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `anxious_attachment.reactivation_triggers` | 3 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `anxious_attachment.reactivation_triggers.sample` | separation | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `anxious_attachment.resilience_mod` | -0.02 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `chronic_paranoia.description_key` | SCAR_chronic_paranoia | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `chronic_paranoia.reactivation_triggers` | 3 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `chronic_paranoia.reactivation_triggers.sample` | social_rejection | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `chronic_paranoia.resilience_mod` | -0.05 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `complicated_grief.description_key` | SCAR_complicated_grief | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `complicated_grief.reactivation_triggers` | 3 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `complicated_grief.reactivation_triggers.sample` | death | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `complicated_grief.resilience_mod` | -0.04 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `compulsive_consumption.description_key` | SCAR_compulsive_consumption | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `compulsive_consumption.reactivation_triggers` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `compulsive_consumption.reactivation_triggers.sample` | food_scarcity | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `compulsive_consumption.resilience_mod` | -0.01 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dissociative_tendency.description_key` | SCAR_dissociative_tendency | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dissociative_tendency.reactivation_triggers` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dissociative_tendency.reactivation_triggers.sample` | extreme_stress | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dissociative_tendency.resilience_mod` | -0.03 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `hypervigilance.description_key` | SCAR_hypervigilance | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `hypervigilance.reactivation_triggers` | 3 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `hypervigilance.reactivation_triggers.sample` | sudden_danger | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `hypervigilance.resilience_mod` | -0.02 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `violence_imprint.description_key` | SCAR_violence_imprint | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `violence_imprint.reactivation_triggers` | 3 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `violence_imprint.reactivation_triggers.sample` | witness_violence | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `violence_imprint.resilience_mod` | -0.05 | float | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |

## 참조하는 시스템 (Referenced By)

- [`trauma_scar`](../../systems/trauma_scar.md) - references `data/trauma_scars.json`

## 수동 노트 (Manual Notes)

<!-- MANUAL:START -->
<!-- MANUAL:END -->
