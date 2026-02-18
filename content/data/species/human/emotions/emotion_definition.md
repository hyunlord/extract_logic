---
title: "emotion_definition Data"
description: "species/human/emotions data file documentation"
generated: true
source_files:
  - "data/species/human/emotions/emotion_definition.json"
nav_order: 10
---

# emotion_definition

📄 source: `data/species/human/emotions/emotion_definition.json` | Category: species/human/emotions | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `arousal_weights` | object | object with 5 keys |
| `arousal_weights.anger` | float | 1.0 |
| `arousal_weights.anticipation` | float | 1.0 |
| `arousal_weights.fear` | float | 1.0 |
| `arousal_weights.joy` | float | 0.3 |
| `arousal_weights.surprise` | float | 1.0 |
| `emotion_order` | array | array (8 items, string entries) |
| `emotions` | object | object with 8 keys |
| `emotions.anger` | object | object with 3 keys |
| `emotions.anger.color` | string | "#F44336" |
| `emotions.anger.name_kr` | string | "분노" |
| `emotions.anger.opposite` | string | "fear" |
| `emotions.anticipation` | object | object with 3 keys |
| `emotions.anticipation.color` | string | "#FF9800" |
| `emotions.anticipation.name_kr` | string | "기대" |
| `emotions.anticipation.opposite` | string | "surprise" |
| `emotions.disgust` | object | object with 3 keys |
| `emotions.disgust.color` | string | "#9C27B0" |
| `emotions.disgust.name_kr` | string | "혐오" |
| `emotions.disgust.opposite` | string | "trust" |
| `emotions.fear` | object | object with 3 keys |
| `emotions.fear.color` | string | "#6BAF7B" |
| `emotions.fear.name_kr` | string | "공포" |
| `emotions.fear.opposite` | string | "anger" |
| `emotions.joy` | object | object with 3 keys |
| `emotions.joy.color` | string | "#FFE135" |
| `emotions.joy.name_kr` | string | "기쁨" |
| `emotions.joy.opposite` | string | "sadness" |
| `emotions.sadness` | object | object with 3 keys |
| `emotions.sadness.color` | string | "#3F51B5" |
| `emotions.sadness.name_kr` | string | "슬픔" |
| `emotions.sadness.opposite` | string | "joy" |
| `emotions.surprise` | object | object with 3 keys |
| `emotions.surprise.color` | string | "#5B9BD5" |
| `emotions.surprise.name_kr` | string | "놀람" |
| `emotions.surprise.opposite` | string | "anticipation" |
| `emotions.trust` | object | object with 3 keys |
| `emotions.trust.color` | string | "#7BC67E" |
| `emotions.trust.name_kr` | string | "신뢰" |
| `emotions.trust.opposite` | string | "disgust" |
| `intensity_labels` | object | object with 8 keys |
| `intensity_labels.anger` | array | array (3 items, string entries) |
| `intensity_labels.anticipation` | array | array (3 items, string entries) |
| `intensity_labels.disgust` | array | array (3 items, string entries) |
| `intensity_labels.fear` | array | array (3 items, string entries) |
| `intensity_labels.joy` | array | array (3 items, string entries) |
| `intensity_labels.sadness` | array | array (3 items, string entries) |
| `intensity_labels.surprise` | array | array (3 items, string entries) |
| `intensity_labels.trust` | array | array (3 items, string entries) |
| `intensity_labels_kr` | object | object with 8 keys |
| `intensity_labels_kr.anger` | array | array (3 items, string entries) |
| `intensity_labels_kr.anticipation` | array | array (3 items, string entries) |
| `intensity_labels_kr.disgust` | array | array (3 items, string entries) |
| `intensity_labels_kr.fear` | array | array (3 items, string entries) |
| `intensity_labels_kr.joy` | array | array (3 items, string entries) |
| `intensity_labels_kr.sadness` | array | array (3 items, string entries) |
| `intensity_labels_kr.surprise` | array | array (3 items, string entries) |
| `intensity_labels_kr.trust` | array | array (3 items, string entries) |
| `labels_en` | object | object with 8 keys |
| `labels_en.anger` | string | "Anger" |
| `labels_en.anticipation` | string | "Anticipation" |
| `labels_en.disgust` | string | "Disgust" |
| `labels_en.fear` | string | "Fear" |
| `labels_en.joy` | string | "Joy" |
| `labels_en.sadness` | string | "Sadness" |
| `labels_en.surprise` | string | "Surprise" |
| `labels_en.trust` | string | "Trust" |
| `labels_kr` | object | object with 8 keys |
| `labels_kr.anger` | string | "분노" |
| `labels_kr.anticipation` | string | "기대" |
| `labels_kr.disgust` | string | "혐오" |
| `labels_kr.fear` | string | "공포" |
| `labels_kr.joy` | string | "기쁨" |
| `labels_kr.sadness` | string | "슬픔" |
| `labels_kr.surprise` | string | "놀람" |
| `labels_kr.trust` | string | "신뢰" |
| `model` | string | "plutchik" |
| `valence_weights` | object | object with 2 keys |
| `valence_weights.negative` | object | object with 3 keys |
| `valence_weights.negative.disgust` | float | 1.0 |
| `valence_weights.negative.fear` | float | 0.5 |
| `valence_weights.negative.sadness` | float | 1.0 |
| `valence_weights.positive` | object | object with 3 keys |
| `valence_weights.positive.anticipation` | float | 0.5 |
| `valence_weights.positive.joy` | float | 1.0 |
| `valence_weights.positive.trust` | float | 1.0 |

## Full Content

Large object detected: **86** total nested keys.

Top-level keys: **9**

<details>
<summary>Expand top-level preview</summary>

```json
{
  "arousal_weights": {
    "fear": 1.0,
    "surprise": 1.0,
    "anger": 1.0,
    "anticipation": 1.0,
    "joy": 0.3
  },
  "emotion_order": [
    "joy",
    "trust",
    "fear",
    "surprise",
    "sadness",
    "disgust",
    "anger",
    "anticipation"
  ],
  "emotions": {
    "joy": {
      "name_kr": "기쁨",
      "color": "#FFE135",
      "opposite": "sadness"
    },
    "trust": {
      "name_kr": "신뢰",
      "color": "#7BC67E",
      "opposite": "disgust"
    },
    "fear": {
      "name_kr": "공포",
      "color": "#6BAF7B",
      "opposite": "anger"
    },
    "surprise": {
      "name_kr": "놀람",
      "color": "#5B9BD5",
      "opposite": "anticipation"
    },
    "sadness": {
      "name_kr": "슬픔",
      "color": "#3F51B5",
      "opposite": "joy"
    },
    "disgust": {
      "name_kr": "혐오",
      "color": "#9C27B0",
      "opposite": "trust"
    },
    "anger": {
      "name_kr": "분노",
      "color": "#F44336",
      "opposite": "fear"
    },
    "anticipation": {
      "name_kr": "기대",
      "color": "#FF9800",
      "opposite": "surprise"
    }
  },
  "intensity_labels": {
    "joy": [
      "Serenity",
      "Joy",
      "Ecstasy"
    ],
    "trust": [
      "Acceptance",
      "Trust",
      "Admiration"
    ],
    "fear": [
      "Apprehension",
      "Fear",
      "Terror"
    ],
    "surprise": [
      "Distraction",
      "Surprise",
      "Amazement"
    ],
    "sadness": [
      "Pensiveness",
      "Sadness",
      "Grief"
    ],
    "disgust": [
      "Boredom",
      "Disgust",
      "Loathing"
    ],
    "anger": [
      "Annoyance",
      "Anger",
      "Rage"
    ],
    "anticipation": [
      "Interest",
      "Anticipation",
      "Vigilance"
    ]
  },
  "intensity_labels_kr": {
    "joy": [
      "평온",
      "기쁨",
      "황홀"
    ],
    "trust": [
      "수용",
      "신뢰",
      "경외"
    ],
    "fear": [
      "우려",
      "공포",
      "경악"
    ],
    "surprise": [
      "산만",
      "놀람",
      "경이"
    ],
    "sadness": [
      "수심",
      "슬픔",
      "비통"
    ],
    "disgust": [
      "지루함",
      "혐오",
      "증오"
    ],
    "anger": [
      "짜증",
      "분노",
      "격노"
    ],
    "anticipation": [
      "흥미",
      "기대",
      "경계"
    ]
  },
  "labels_en": {
    "joy": "Joy",
    "trust": "Trust",
    "fear": "Fear",
    "surprise": "Surprise",
    "sadness": "Sadness",
    "disgust": "Disgust",
    "anger": "Anger",
    "anticipation": "Anticipation"
  },
  "labels_kr": {
    "joy": "기쁨",
    "trust": "신뢰",
    "fear": "공포",
    "surprise": "놀람",
    "sadness": "슬픔",
    "disgust": "혐오",
    "anger": "분노",
    "anticipation": "기대"
  },
  "model": "plutchik",
  "valence_weights": {
    "positive": {
      "joy": 1.0,
      "trust": 1.0,
      "anticipation": 0.5
    },
    "negative": {
      "sadness": 1.0,
      "disgust": 1.0,
      "fear": 0.5
    }
  }
}
```

</details>

## Referenced By

- [`species_manager`](../../../../core/species_manager.md) - references data under `data/species/`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
