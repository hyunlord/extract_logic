---
title: "trait_definitions_fixed Data"
description: "personality data file documentation"
generated: true
source_files:
  - "data/personality/trait_definitions_fixed.json"
nav_order: 10
---

# trait_definitions_fixed

📄 source: `data/personality/trait_definitions_fixed.json` | Category: personality | Type: array

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `items` | int | 187 |
| `item` | object | object with 12 keys |
| `item.anti_synergies` | array | array (3 items, string entries) |
| `item.condition` | object | object with 3 keys |
| `item.condition.direction` | string | "high" |
| `item.condition.facet` | string | "H_sincerity" |
| `item.condition.threshold` | float | 0.92 |
| `item.description_en` | string | "Prefers telling the truth as-is and feels strong aversion to deception or backroom deals." |
| `item.description_kr` | string | "사실을 왜곡하기보다 있는 그대로 말하려 하며, 속임수나 뒷거래에 강한 거부감을 느낀다." |
| `item.effects` | object | object with 6 keys |
| `item.effects.behavior_weights` | object | object with 4 keys |
| `item.effects.behavior_weights.betray` | float | 0.75 |
| `item.effects.behavior_weights.leadership` | float | 1.05 |
| `item.effects.behavior_weights.social` | float | 1.1 |
| `item.effects.behavior_weights.steal` | float | 0.7 |
| `item.effects.combat_modifiers` | object | object with 3 keys |
| `item.effects.combat_modifiers.aggression_mult` | float | 0.95 |
| `item.effects.combat_modifiers.morale_mult` | float | 1.02 |
| `item.effects.combat_modifiers.war_crime_propensity_mult` | float | 0.6 |
| `item.effects.emotion_modifiers` | object | object with 3 keys |
| `item.effects.emotion_modifiers.anger_sensitivity` | float | 0.95 |
| `item.effects.emotion_modifiers.guilt_sensitivity` | float | 1.2 |
| `item.effects.emotion_modifiers.shame_sensitivity` | float | 1.1 |
| `item.effects.relationship_modifiers` | object | object with 3 keys |
| `item.effects.relationship_modifiers.betrayal_propensity_mult` | float | 0.6 |
| `item.effects.relationship_modifiers.trust_gain_mult` | float | 1.25 |
| `item.effects.relationship_modifiers.trust_loss_mult` | float | 0.85 |
| `item.effects.stress_modifiers` | object | object with 4 keys |
| `item.effects.stress_modifiers.break_threshold_mult` | float | 0.98 |
| `item.effects.stress_modifiers.stress_gain_mult` | float | 1.05 |
| `item.effects.stress_modifiers.stress_recovery_mult` | float | 1.0 |
| `item.effects.stress_modifiers.violation_stress` | object | object with 3 keys |
| `item.effects.work_modifiers` | object | object with 3 keys |
| `item.effects.work_modifiers.error_rate_mult` | float | 0.95 |
| `item.effects.work_modifiers.quality_mult` | float | 1.05 |
| `item.effects.work_modifiers.speed_mult` | float | 0.98 |
| `item.id` | string | "f_sincere" |
| `item.name_en` | string | "Sincere" |
| `item.name_kr` | string | "진실한" |
| `item.opposite_actions` | array | array (3 items, string entries) |
| `item.synergies` | array | array (3 items, string entries) |
| `item.type` | string | "personality" |
| `item.valence` | string | "positive" |

## Full Content

Large array detected: **187** items.

Showing sampled content (3 item(s)):

<details>
<summary>Expand sampled content</summary>

```json
[
  {
    "id": "f_sincere",
    "name_kr": "진실한",
    "name_en": "Sincere",
    "type": "personality",
    "valence": "positive",
    "condition": {
      "facet": "H_sincerity",
      "direction": "high",
      "threshold": 0.92
    },
    "effects": {
      "behavior_weights": {
        "social": 1.1,
        "steal": 0.7,
        "betray": 0.75,
        "leadership": 1.05
      },
      "emotion_modifiers": {
        "guilt_sensitivity": 1.2,
        "shame_sensitivity": 1.1,
        "anger_sensitivity": 0.95
      },
      "relationship_modifiers": {
        "trust_gain_mult": 1.25,
        "trust_loss_mult": 0.85,
        "betrayal_propensity_mult": 0.6
      },
      "work_modifiers": {
        "quality_mult": 1.05,
        "speed_mult": 0.98,
        "error_rate_mult": 0.95
      },
      "combat_modifiers": {
        "aggression_mult": 0.95,
        "war_crime_propensity_mult": 0.6,
        "morale_mult": 1.02
      },
      "stress_modifiers": {
        "stress_gain_mult": 1.05,
        "stress_recovery_mult": 1.0,
        "break_threshold_mult": 0.98,
        "violation_stress": {
          "lie": 14,
          "deceive": 12,
          "take_bribe": 18
        }
      }
    },
    "opposite_actions": [
      "lie",
      "deceive",
      "take_bribe"
    ],
    "synergies": [
      "f_fair_minded",
      "f_modest",
      "f_forgiving"
    ],
    "anti_synergies": [
      "f_deceptive",
      "f_corrupt",
      "d_con_artist"
    ],
    "description_kr": "사실을 왜곡하기보다 있는 그대로 말하려 하며, 속임수나 뒷거래에 강한 거부감을 느낀다.",
    "description_en": "Prefers telling the truth as-is and feels strong aversion to deception or backroom deals."
  },
  {
    "id": "f_deceptive",
    "name_kr": "기만적인",
    "name_en": "Deceptive",
    "type": "personality",
    "valence": "negative",
    "condition": {
      "facet": "H_sincerity",
      "direction": "low",
      "threshold": 0.14
    },
    "effects": {
      "behavior_weights": {
        "social": 1.05,
        "steal": 1.25,
        "betray": 1.4,
        "leadership": 1.1
      },
      "emotion_modifiers": {
        "guilt_sensitivity": 0.7,
        "shame_sensitivity": 0.8,
        "anger_sensitivity": 1.05
      },
      "relationship_modifiers": {
        "trust_gain_mult": 0.75,
        "trust_loss_mult": 1.2,
        "betrayal_propensity_mult": 1.4
      },
      "work_modifiers": {
        "quality_mult": 0.95,
        "speed_mult": 1.03,
        "error_rate_mult": 1.05
      },
      "combat_modifiers": {
        "aggression_mult": 1.0,
        "ambush_propensity_mult": 1.3,
        "flee_threshold_mult": 0.95
      },
      "stress_modifiers": {
        "stress_gain_mult": 0.95,
        "stress_recovery_mult": 1.05,
        "break_threshold_mult": 1.05,
        "violation_stress": {
          "confess": 10,
          "tell_truth": 8,
          "return_stolen": 16
        }
      }
    },
    "opposite_actions": [
      "confess",
      "tell_truth",
      "return_stolen"
    ],
    "synergies": [
      "f_corrupt",
      "f_greedy",
      "f_reckless"
    ],
    "anti_synergies": [
      "f_sincere",
      "f_fair_minded"
    ],
    "description_kr": "말을 상황에 맞춰 바꾸고, 필요하면 거짓말이나 속임수도 도구로 사용한다.",
    "description_en": "Adapts the truth to the situation and may use lying or manipulation as a tool when needed."
  },
  {
    "id": "f_fair_minded",
    "name_kr": "원칙적인",
    "name_en": "Fair‑Minded",
    "type": "personality",
    "valence": "positive",
    "condition": {
      "facet": "H_fairness",
      "direction": "high",
      "threshold": 0.94
    },
    "effects": {
      "behavior_weights": {
        "steal": 0.55,
        "share": 1.15,
        "leadership": 1.1,
        "trade": 1.05
      },
      "emotion_modifiers": {
        "anger_injustice_sensitivity": 1.25,
        "guilt_sensitivity": 1.15
      },
      "relationship_modifiers": {
        "trust_gain_mult": 1.15,
        "trust_loss_mult": 0.9,
        "reciprocity_mult": 1.2
      },
      "work_modifiers": {
        "quality_mult": 1.05,
        "speed_mult": 0.98
      },
      "combat_modifiers": {
        "war_crime_propensity_mult": 0.55,
        "aggression_mult": 0.95
      },
      "stress_modifiers": {
        "stress_gain_mult": 1.03,
        "break_threshold_mult": 0.97,
        "violation_stress": {
          "steal": 22,
          "cheat": 18,
          "frame_other": 20
        }
      }
    },
    "opposite_actions": [
      "steal",
      "cheat",
      "frame_other"
    ],
    "synergies": [
      "f_sincere",
      "f_forgiving",
      "c_hx_hh_honest_leader"
    ],
    "anti_synergies": [
      "f_corrupt",
      "d_machiavellian"
    ],
    "description_kr": "규칙과 약속을 지키려 하며, 부정행위나 특권을 강하게 싫어한다.",
    "description_en": "Tries to keep rules and promises, strongly disliking cheating or unfair privilege."
  }
]
```

</details>

### Example Entry

```json
{
  "id": "f_sincere",
  "name_kr": "진실한",
  "name_en": "Sincere",
  "type": "personality",
  "valence": "positive",
  "condition": {
    "facet": "H_sincerity",
    "direction": "high",
    "threshold": 0.92
  },
  "effects": {
    "behavior_weights": {
      "social": 1.1,
      "steal": 0.7,
      "betray": 0.75,
      "leadership": 1.05
    },
    "emotion_modifiers": {
      "guilt_sensitivity": 1.2,
      "shame_sensitivity": 1.1,
      "anger_sensitivity": 0.95
    },
    "relationship_modifiers": {
      "trust_gain_mult": 1.25,
      "trust_loss_mult": 0.85,
      "betrayal_propensity_mult": 0.6
    },
    "work_modifiers": {
      "quality_mult": 1.05,
      "speed_mult": 0.98,
      "error_rate_mult": 0.95
    },
    "combat_modifiers": {
      "aggression_mult": 0.95,
      "war_crime_propensity_mult": 0.6,
      "morale_mult": 1.02
    },
    "stress_modifiers": {
      "stress_gain_mult": 1.05,
      "stress_recovery_mult": 1.0,
      "break_threshold_mult": 0.98,
      "violation_stress": {
        "lie": 14,
        "deceive": 12,
        "take_bribe": 18
      }
    }
  },
  "opposite_actions": [
    "lie",
    "deceive",
    "take_bribe"
  ],
  "synergies": [
    "f_fair_minded",
    "f_modest",
    "f_forgiving"
  ],
  "anti_synergies": [
    "f_deceptive",
    "f_corrupt",
    "d_con_artist"
  ],
  "description_kr": "사실을 왜곡하기보다 있는 그대로 말하려 하며, 속임수나 뒷거래에 강한 거부감을 느낀다.",
  "description_en": "Prefers telling the truth as-is and feels strong aversion to deception or backroom deals."
}
```

## Referenced By

- None found.

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
