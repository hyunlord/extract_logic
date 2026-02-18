---
title: "emotion_definition Data"
description: "species/human/emotions data file documentation"
generated: true
source_files:
  - "data/species/human/emotions/emotion_definition.json"
nav_order: 10
---

# emotion_definition

📄 source (출처): `data/species/human/emotions/emotion_definition.json` | Category (분류): species/human/emotions | Type (유형): object

## 개요 (Overview)

- Configures (설정 내용): `species/human/emotions` 데이터 도메인 설정 값. Configuration values for the `species/human/emotions` data domain.
- Read by systems/modules (읽는 시스템/모듈): species_manager
- Related documentation (관련 문서): [`species_manager`](../../../../core/species_manager.md)

## 해석된 파라미터 (Interpreted Parameters)

### Weights & Multipliers (가중/배수)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `arousal_weights.anger` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `arousal_weights.anticipation` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `arousal_weights.fear` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `arousal_weights.joy` | 0.3 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `arousal_weights.surprise` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `valence_weights.negative.disgust` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `valence_weights.negative.fear` | 0.5 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `valence_weights.negative.sadness` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `valence_weights.positive.anticipation` | 0.5 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `valence_weights.positive.joy` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |
| `valence_weights.positive.trust` | 1 multiplier | float | Strength multiplier used in gameplay calculations. (계산 강도 배수) |

### Stress & Emotion (스트레스/감정)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `emotion_order` | 8 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotion_order.sample` | joy | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.anger.color` | #F44336 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.anger.name_en` | Anger | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.anger.name_kr` | 분노 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.anger.opposite` | fear | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.anticipation.color` | #FF9800 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.anticipation.name_en` | Anticipation | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.anticipation.name_kr` | 기대 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.anticipation.opposite` | surprise | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.disgust.color` | #9C27B0 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.disgust.name_en` | Disgust | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.disgust.name_kr` | 혐오 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.disgust.opposite` | trust | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.fear.color` | #6BAF7B | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.fear.name_en` | Fear | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.fear.name_kr` | 공포 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.fear.opposite` | anger | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.joy.color` | #FFE135 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.joy.name_en` | Joy | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.joy.name_kr` | 기쁨 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.joy.opposite` | sadness | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.sadness.color` | #3F51B5 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.sadness.name_en` | Sadness | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.sadness.name_kr` | 슬픔 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.sadness.opposite` | joy | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.surprise.color` | #5B9BD5 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.surprise.name_en` | Surprise | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.surprise.name_kr` | 놀람 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.surprise.opposite` | anticipation | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.trust.color` | #7BC67E | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.trust.name_en` | Trust | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.trust.name_kr` | 신뢰 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `emotions.trust.opposite` | disgust | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels.anger` | 3 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels.anger.sample` | Annoyance | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels.disgust` | 3 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels.disgust.sample` | Boredom | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels.fear` | 3 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels.fear.sample` | Apprehension | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels.joy` | 3 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels.joy.sample` | Serenity | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels.sadness` | 3 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels.sadness.sample` | Pensiveness | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels.trust` | 3 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels.trust.sample` | Acceptance | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels_kr.anger` | 3 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels_kr.anger.sample` | 짜증 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels_kr.disgust` | 3 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels_kr.disgust.sample` | 지루함 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels_kr.fear` | 3 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels_kr.fear.sample` | 우려 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels_kr.joy` | 3 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels_kr.joy.sample` | 평온 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels_kr.sadness` | 3 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels_kr.sadness.sample` | 수심 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels_kr.trust` | 3 items | array | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `intensity_labels_kr.trust.sample` | 수용 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `labels_en.anger` | Anger | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `labels_en.disgust` | Disgust | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `labels_en.fear` | Fear | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `labels_en.joy` | Joy | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `labels_en.sadness` | Sadness | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `labels_en.trust` | Trust | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `labels_kr.anger` | 분노 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `labels_kr.disgust` | 혐오 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `labels_kr.fear` | 공포 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `labels_kr.joy` | 기쁨 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `labels_kr.sadness` | 슬픔 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |
| `labels_kr.trust` | 신뢰 | string | Stress/emotion contribution in simulation updates. (스트레스/감정 기여도) |

### Identifiers & Labels (식별자/라벨)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `intensity_labels.anticipation` | 3 items | array | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `intensity_labels.anticipation.sample` | Interest | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `intensity_labels.surprise` | 3 items | array | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `intensity_labels.surprise.sample` | Distraction | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `intensity_labels_kr.anticipation` | 3 items | array | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `intensity_labels_kr.anticipation.sample` | 흥미 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `intensity_labels_kr.surprise` | 3 items | array | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `intensity_labels_kr.surprise.sample` | 산만 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `labels_en.anticipation` | Anticipation | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `labels_en.surprise` | Surprise | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `labels_kr.anticipation` | 기대 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `labels_kr.surprise` | 놀람 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |

### Other Parameters (기타)

| Parameter (매개변수) | Value (값) | Type (유형) | What it controls (게임 영향) |
|----------------------|-----------|------------|-----------------------------|
| `model` | plutchik | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |

## 참조하는 시스템 (Referenced By)

- [`species_manager`](../../../../core/species_manager.md) - references data under `data/species/`

## 수동 노트 (Manual Notes)

<!-- MANUAL:START -->
<!-- MANUAL:END -->
