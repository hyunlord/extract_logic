---
title: "hexaco_definition Data"
description: "personality data file documentation"
generated: true
source_files:
  - "data/personality/hexaco_definition.json"
nav_order: 10
---

# hexaco_definition

📄 source: `data/personality/hexaco_definition.json` | Category: personality | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `axes` | object | object with 6 keys |
| `axes.A` | object | object with 3 keys |
| `axes.A.facets` | object | object with 4 keys |
| `axes.A.name` | string | "Agreeableness" |
| `axes.A.name_kr` | string | "우호성" |
| `axes.C` | object | object with 3 keys |
| `axes.C.facets` | object | object with 4 keys |
| `axes.C.name` | string | "Conscientiousness" |
| `axes.C.name_kr` | string | "성실성" |
| `axes.E` | object | object with 3 keys |
| `axes.E.facets` | object | object with 4 keys |
| `axes.E.name` | string | "Emotionality" |
| `axes.E.name_kr` | string | "감정성" |
| `axes.H` | object | object with 3 keys |
| `axes.H.facets` | object | object with 4 keys |
| `axes.H.name` | string | "Honesty-Humility" |
| `axes.H.name_kr` | string | "정직-겸손" |
| `axes.O` | object | object with 3 keys |
| `axes.O.facets` | object | object with 4 keys |
| `axes.O.name` | string | "Openness to Experience" |
| `axes.O.name_kr` | string | "경험 개방성" |
| `axes.X` | object | object with 3 keys |
| `axes.X.facets` | object | object with 4 keys |
| `axes.X.name` | string | "Extraversion" |
| `axes.X.name_kr` | string | "외향성" |
| `interstitial` | object | object with 1 keys |
| `interstitial.altruism` | object | object with 3 keys |
| `interstitial.altruism.name` | string | "Altruism" |
| `interstitial.altruism.name_kr` | string | "이타성" |
| `interstitial.altruism.note` | string | "Component between H and E" |

## Full Content

Large object detected: **102** total nested keys.

Top-level keys: **2**

<details>
<summary>Expand top-level preview</summary>

```json
{
  "axes": {
    "H": {
      "name": "Honesty-Humility",
      "name_kr": "정직-겸손",
      "facets": {
        "H_sincerity": {
          "name": "Sincerity",
          "name_kr": "진실성"
        },
        "H_fairness": {
          "name": "Fairness",
          "name_kr": "공정성"
        },
        "H_greed_avoidance": {
          "name": "Greed Avoidance",
          "name_kr": "탐욕 회피"
        },
        "H_modesty": {
          "name": "Modesty",
          "name_kr": "겸손"
        }
      }
    },
    "E": {
      "name": "Emotionality",
      "name_kr": "감정성",
      "facets": {
        "E_fearfulness": {
          "name": "Fearfulness",
          "name_kr": "두려움"
        },
        "E_anxiety": {
          "name": "Anxiety",
          "name_kr": "불안"
        },
        "E_dependence": {
          "name": "Dependence",
          "name_kr": "의존성"
        },
        "E_sentimentality": {
          "name": "Sentimentality",
          "name_kr": "감상성"
        }
      }
    },
    "X": {
      "name": "Extraversion",
      "name_kr": "외향성",
      "facets": {
        "X_social_self_esteem": {
          "name": "Social Self-Esteem",
          "name_kr": "사회적 자존감"
        },
        "X_social_boldness": {
          "name": "Social Boldness",
          "name_kr": "사회적 대담함"
        },
        "X_sociability": {
          "name": "Sociability",
          "name_kr": "사교성"
        },
        "X_liveliness": {
          "name": "Liveliness",
          "name_kr": "활기"
        }
      }
    },
    "A": {
      "name": "Agreeableness",
      "name_kr": "우호성",
      "facets": {
        "A_forgiveness": {
          "name": "Forgiveness",
          "name_kr": "용서"
        },
        "A_gentleness": {
          "name": "Gentleness",
          "name_kr": "온화"
        },
        "A_flexibility": {
          "name": "Flexibility",
          "name_kr": "유연성"
        },
        "A_patience": {
          "name": "Patience",
          "name_kr": "인내"
        }
      }
    },
    "C": {
      "name": "Conscientiousness",
      "name_kr": "성실성",
      "facets": {
        "C_organization": {
          "name": "Organization",
          "name_kr": "조직화"
        },
        "C_diligence": {
          "name": "Diligence",
          "name_kr": "근면"
        },
        "C_perfectionism": {
          "name": "Perfectionism",
          "name_kr": "완벽주의"
        },
        "C_prudence": {
          "name": "Prudence",
          "name_kr": "신중"
        }
      }
    },
    "O": {
      "name": "Openness to Experience",
      "name_kr": "경험 개방성",
      "facets": {
        "O_aesthetic": {
          "name": "Aesthetic Appreciation",
          "name_kr": "심미성"
        },
        "O_inquisitiveness": {
          "name": "Inquisitiveness",
          "name_kr": "호기심"
        },
        "O_creativity": {
          "name": "Creativity",
          "name_kr": "창의성"
        },
        "O_unconventionality": {
          "name": "Unconventionality",
          "name_kr": "비전통성"
        }
      }
    }
  },
  "interstitial": {
    "altruism": {
      "name": "Altruism",
      "name_kr": "이타성",
      "note": "Component between H and E"
    }
  }
}
```

</details>

## Referenced By

- None found.

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
