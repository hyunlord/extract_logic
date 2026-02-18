---
title: "decay_parameters Data"
description: "species/human/emotions data file documentation"
generated: true
source_files:
  - "data/species/human/emotions/decay_parameters.json"
nav_order: 10
---

# decay_parameters

📄 source: `data/species/human/emotions/decay_parameters.json` | Category: species/human/emotions | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `baselines` | object | object with 9 keys |
| `baselines.anger` | object | object with 5 keys |
| `baselines.anger.axis` | string | "A" |
| `baselines.anger.base` | float | 2.0 |
| `baselines.anger.max` | float | 10.0 |
| `baselines.anger.min` | float | 0.0 |
| `baselines.anger.scale` | float | -2.0 |
| `baselines.anticipation` | object | object with 5 keys |
| `baselines.anticipation.axis` | string | "X" |
| `baselines.anticipation.base` | float | 5.0 |
| `baselines.anticipation.max` | float | 10.0 |
| `baselines.anticipation.min` | float | 0.0 |
| `baselines.anticipation.scale` | float | 1.0 |
| `baselines.comment` | string | "Slow layer baselines: clampf(base + scale * z_axis, min, max)" |
| `baselines.disgust` | object | object with 1 keys |
| `baselines.disgust.base` | float | 0.0 |
| `baselines.fear` | object | object with 5 keys |
| `baselines.fear.axis` | string | "E" |
| `baselines.fear.base` | float | 2.0 |
| `baselines.fear.max` | float | 10.0 |
| `baselines.fear.min` | float | 0.0 |
| `baselines.fear.scale` | float | 2.0 |
| `baselines.joy` | object | object with 5 keys |
| `baselines.joy.axis` | string | "X" |
| `baselines.joy.base` | float | 5.0 |
| `baselines.joy.max` | float | 15.0 |
| `baselines.joy.min` | float | 0.0 |
| `baselines.joy.scale` | float | 3.0 |
| `baselines.sadness` | object | object with 5 keys |
| `baselines.sadness.axis` | string | "E" |
| `baselines.sadness.base` | float | 2.0 |
| `baselines.sadness.max` | float | 10.0 |
| `baselines.sadness.min` | float | 0.0 |
| `baselines.sadness.scale` | float | 1.5 |
| `baselines.surprise` | object | object with 1 keys |
| `baselines.surprise.base` | float | 0.0 |
| `baselines.trust` | object | object with 5 keys |
| `baselines.trust.axis` | string | "X" |
| `baselines.trust.base` | float | 5.0 |
| `baselines.trust.max` | float | 12.0 |
| `baselines.trust.min` | float | 0.0 |
| `baselines.trust.scale` | float | 1.5 |
| `contagion` | object | object with 3 keys |
| `contagion.distance_scale` | float | 5.0 |
| `contagion.kappa` | object | object with 9 keys |
| `contagion.kappa.anger` | float | 0.12 |
| `contagion.kappa.anticipation` | float | 0.03 |
| `contagion.kappa.comment` | string | "Fan et al. 2016: anger > fear > joy" |
| `contagion.kappa.disgust` | float | 0.06 |
| `contagion.kappa.fear` | float | 0.1 |
| `contagion.kappa.joy` | float | 0.08 |
| `contagion.kappa.sadness` | float | 0.04 |
| `contagion.kappa.surprise` | float | 0.03 |
| `contagion.kappa.trust` | float | 0.06 |
| `contagion.min_source` | float | 10.0 |
| `fast_half_life_hours` | object | object with 9 keys |
| `fast_half_life_hours.anger` | float | 0.4 |
| `fast_half_life_hours.anticipation` | float | 3.0 |
| `fast_half_life_hours.comment` | string | "Verduyn & Brans 2012" |
| `fast_half_life_hours.disgust` | float | 0.1 |
| `fast_half_life_hours.fear` | float | 0.3 |
| `fast_half_life_hours.joy` | float | 0.75 |
| `fast_half_life_hours.sadness` | float | 0.5 |
| `fast_half_life_hours.surprise` | float | 0.05 |
| `fast_half_life_hours.trust` | float | 2.0 |
| `habituation_eta` | float | 0.2 |
| `half_life_adjustments` | object | object with 5 keys |
| `half_life_adjustments.anger` | object | object with 2 keys |
| `half_life_adjustments.anger.axis` | string | "A" |
| `half_life_adjustments.anger.coeff` | float | -0.25 |
| `half_life_adjustments.comment` | string | "Personality-adjusted half-life: base * exp(coeff * z_axis)" |
| `half_life_adjustments.fear` | object | object with 2 keys |
| `half_life_adjustments.fear.axis` | string | "E" |
| `half_life_adjustments.fear.coeff` | float | 0.3 |
| `half_life_adjustments.joy` | object | object with 2 keys |
| `half_life_adjustments.joy.axis` | string | "X" |
| `half_life_adjustments.joy.coeff` | float | 0.2 |
| `half_life_adjustments.sadness` | object | object with 2 keys |
| `half_life_adjustments.sadness.axis` | string | "E" |
| `half_life_adjustments.sadness.coeff` | float | 0.3 |
| `inhibition_gamma` | float | 0.3 |
| `memory_trace_default_half_life_days` | int | 30 |
| `memory_trace_ratio` | float | 0.3 |
| `memory_trace_threshold` | float | 20.0 |
| `memory_trace_trauma_half_life_days` | int | 365 |
| `mental_break` | object | object with 3 keys |
| `mental_break.behaviors` | object | object with 5 keys |
| `mental_break.behaviors.outrage_violence` | object | object with 3 keys |
| `mental_break.behaviors.panic` | object | object with 3 keys |
| `mental_break.behaviors.purge` | object | object with 3 keys |
| `mental_break.behaviors.rage` | object | object with 3 keys |
| `mental_break.behaviors.shutdown` | object | object with 3 keys |
| `mental_break.beta` | float | 60.0 |
| `mental_break.tick_prob` | float | 0.01 |
| `opposite_pairs` | object | object with 8 keys |
| `opposite_pairs.anger` | string | "fear" |
| `opposite_pairs.anticipation` | string | "surprise" |
| `opposite_pairs.disgust` | string | "trust" |
| `opposite_pairs.fear` | string | "anger" |
| `opposite_pairs.joy` | string | "sadness" |
| `opposite_pairs.sadness` | string | "joy" |
| `opposite_pairs.surprise` | string | "anticipation" |
| `opposite_pairs.trust` | string | "disgust" |
| `personality_sensitivity` | object | object with 9 keys |
| `personality_sensitivity.anger` | object | object with 2 keys |
| `personality_sensitivity.anger.axis` | string | "A" |
| `personality_sensitivity.anger.coeff` | float | -0.35 |
| `personality_sensitivity.anticipation` | array | array (2 items, object entries) |
| `personality_sensitivity.anticipation.item.axis` | string | "O" |
| `personality_sensitivity.anticipation.item.coeff` | float | 0.2 |
| `personality_sensitivity.comment` | string | "HEXACO->emotion coupling: sensitivity = exp(coeff * z_axis)" |
| `personality_sensitivity.disgust` | object | object with 2 keys |
| `personality_sensitivity.disgust.axis` | string | "H" |
| `personality_sensitivity.disgust.coeff` | float | 0.25 |
| `personality_sensitivity.fear` | object | object with 2 keys |
| `personality_sensitivity.fear.axis` | string | "E" |
| `personality_sensitivity.fear.coeff` | float | 0.4 |
| `personality_sensitivity.joy` | object | object with 2 keys |
| `personality_sensitivity.joy.axis` | string | "X" |
| `personality_sensitivity.joy.coeff` | float | 0.3 |
| `personality_sensitivity.sadness` | object | object with 2 keys |
| `personality_sensitivity.sadness.axis` | string | "E" |
| `personality_sensitivity.sadness.coeff` | float | 0.4 |
| `personality_sensitivity.surprise` | object | object with 2 keys |
| `personality_sensitivity.surprise.axis` | string | "O" |
| `personality_sensitivity.surprise.coeff` | float | 0.2 |
| `personality_sensitivity.trust` | array | array (2 items, object entries) |
| `personality_sensitivity.trust.item.axis` | string | "X" |
| `personality_sensitivity.trust.item.coeff` | float | 0.2 |
| `slow_half_life_hours` | object | object with 8 keys |
| `slow_half_life_hours.anger` | float | 12.0 |
| `slow_half_life_hours.anticipation` | float | 36.0 |
| `slow_half_life_hours.disgust` | float | 12.0 |
| `slow_half_life_hours.fear` | float | 24.0 |
| `slow_half_life_hours.joy` | float | 48.0 |
| `slow_half_life_hours.sadness` | float | 120.0 |
| `slow_half_life_hours.surprise` | float | 6.0 |
| `slow_half_life_hours.trust` | float | 72.0 |
| `stress` | object | object with 2 keys |
| `stress.tau_hours` | float | 48.0 |
| `stress.weights` | object | object with 4 keys |
| `stress.weights.anger` | float | 0.9 |
| `stress.weights.disgust` | float | 0.6 |
| `stress.weights.fear` | float | 1.0 |
| `stress.weights.sadness` | float | 1.1 |

## Full Content

Large object detected: **164** total nested keys.

Top-level keys: **15**

<details>
<summary>Expand top-level preview</summary>

```json
{
  "baselines": {
    "comment": "Slow layer baselines: clampf(base + scale * z_axis, min, max)",
    "joy": {
      "base": 5.0,
      "scale": 3.0,
      "axis": "X",
      "min": 0.0,
      "max": 15.0
    },
    "fear": {
      "base": 2.0,
      "scale": 2.0,
      "axis": "E",
      "min": 0.0,
      "max": 10.0
    },
    "sadness": {
      "base": 2.0,
      "scale": 1.5,
      "axis": "E",
      "min": 0.0,
      "max": 10.0
    },
    "anger": {
      "base": 2.0,
      "scale": -2.0,
      "axis": "A",
      "min": 0.0,
      "max": 10.0
    },
    "trust": {
      "base": 5.0,
      "scale": 1.5,
      "axis": "X",
      "min": 0.0,
      "max": 12.0
    },
    "anticipation": {
      "base": 5.0,
      "scale": 1.0,
      "axis": "X",
      "min": 0.0,
      "max": 10.0
    },
    "disgust": {
      "base": 0.0
    },
    "surprise": {
      "base": 0.0
    }
  },
  "contagion": {
    "kappa": {
      "comment": "Fan et al. 2016: anger > fear > joy",
      "anger": 0.12,
      "fear": 0.1,
      "joy": 0.08,
      "disgust": 0.06,
      "trust": 0.06,
      "sadness": 0.04,
      "surprise": 0.03,
      "anticipation": 0.03
    },
    "distance_scale": 5.0,
    "min_source": 10.0
  },
  "fast_half_life_hours": {
    "comment": "Verduyn & Brans 2012",
    "joy": 0.75,
    "trust": 2.0,
    "fear": 0.3,
    "surprise": 0.05,
    "sadness": 0.5,
    "disgust": 0.1,
    "anger": 0.4,
    "anticipation": 3.0
  },
  "habituation_eta": 0.2,
  "half_life_adjustments": {
    "comment": "Personality-adjusted half-life: base * exp(coeff * z_axis)",
    "fear": {
      "axis": "E",
      "coeff": 0.3
    },
    "sadness": {
      "axis": "E",
      "coeff": 0.3
    },
    "joy": {
      "axis": "X",
      "coeff": 0.2
    },
    "anger": {
      "axis": "A",
      "coeff": -0.25
    }
  },
  "inhibition_gamma": 0.3,
  "memory_trace_default_half_life_days": 30,
  "memory_trace_ratio": 0.3,
  "memory_trace_threshold": 20.0,
  "memory_trace_trauma_half_life_days": 365
}
```

</details>

## Referenced By

- [`species_manager`](../../../../core/species_manager.md) - references data under `data/species/`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
