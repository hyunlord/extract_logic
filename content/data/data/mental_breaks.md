---
title: "mental_breaks Data"
description: "data data file documentation"
generated: true
source_files:
  - "data/mental_breaks.json"
nav_order: 10
---

# mental_breaks

📄 source: `data/mental_breaks.json` | Category: data | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `compulsive_ritual` | object | object with 11 keys |
| `compulsive_ritual.behavior_override` | object | object with 4 keys |
| `compulsive_ritual.behavior_override.ignore_jobs` | boolean | true |
| `compulsive_ritual.behavior_override.mode` | string | "repeat_action" |
| `compulsive_ritual.behavior_override.speed_multiplier` | float | 1.0 |
| `compulsive_ritual.behavior_override.target_rule` | string | "current_location" |
| `compulsive_ritual.duration_base_ticks` | int | 1 |
| `compulsive_ritual.duration_variance_ticks` | int | 3 |
| `compulsive_ritual.energy_cost` | float | 0.05 |
| `compulsive_ritual.id` | string | "compulsive_ritual" |
| `compulsive_ritual.name_en` | string | "Compulsive Ritual" |
| `compulsive_ritual.name_kr` | string | "강박 의식" |
| `compulsive_ritual.personality_weights` | object | object with 6 keys |
| `compulsive_ritual.personality_weights.A` | float | 0.0 |
| `compulsive_ritual.personality_weights.C` | float | 1.5 |
| `compulsive_ritual.personality_weights.E` | float | 0.5 |
| `compulsive_ritual.personality_weights.H` | float | 0.0 |
| `compulsive_ritual.personality_weights.O` | float | 0.5 |
| `compulsive_ritual.personality_weights.X` | float | 0.0 |
| `compulsive_ritual.severity` | string | "minor" |
| `compulsive_ritual.stress_catharsis_factor` | float | 0.85 |
| `compulsive_ritual.trait_modifiers` | object | object with 2 keys |
| `compulsive_ritual.trait_modifiers.impulsive` | float | 0.6 |
| `compulsive_ritual.trait_modifiers.ritualist` | float | 1.4 |
| `fugue` | object | object with 11 keys |
| `fugue.behavior_override` | object | object with 5 keys |
| `fugue.behavior_override.ignore_jobs` | boolean | true |
| `fugue.behavior_override.leave_settlement` | boolean | true |
| `fugue.behavior_override.mode` | string | "wander_away" |
| `fugue.behavior_override.speed_multiplier` | float | 0.8 |
| `fugue.behavior_override.target_rule` | string | "random_far_direction" |
| `fugue.duration_base_ticks` | int | 24 |
| `fugue.duration_variance_ticks` | int | 60 |
| `fugue.energy_cost` | float | 0.15 |
| `fugue.id` | string | "fugue" |
| `fugue.name_en` | string | "Dissociative Fugue" |
| `fugue.name_kr` | string | "해리성 둔주" |
| `fugue.personality_weights` | object | object with 6 keys |
| `fugue.personality_weights.A` | float | 0.0 |
| `fugue.personality_weights.C` | float | -0.3 |
| `fugue.personality_weights.E` | float | 0.5 |
| `fugue.personality_weights.H` | float | 0.0 |
| `fugue.personality_weights.O` | float | 1.5 |
| `fugue.personality_weights.X` | float | -0.5 |
| `fugue.severity` | string | "major" |
| `fugue.stress_catharsis_factor` | float | 0.8 |
| `fugue.trait_modifiers` | object | object with 2 keys |
| `fugue.trait_modifiers.loner` | float | 1.2 |
| `fugue.trait_modifiers.rebellious` | float | 1.1 |
| `grief_withdrawal` | object | object with 11 keys |
| `grief_withdrawal.behavior_override` | object | object with 5 keys |
| `grief_withdrawal.behavior_override.ignore_jobs` | boolean | true |
| `grief_withdrawal.behavior_override.mode` | string | "withdraw_to_home" |
| `grief_withdrawal.behavior_override.reject_social` | boolean | true |
| `grief_withdrawal.behavior_override.speed_multiplier` | float | 0.3 |
| `grief_withdrawal.behavior_override.target_rule` | string | "home_or_corner" |
| `grief_withdrawal.duration_base_ticks` | int | 24 |
| `grief_withdrawal.duration_variance_ticks` | int | 36 |
| `grief_withdrawal.energy_cost` | float | 0.08 |
| `grief_withdrawal.id` | string | "grief_withdrawal" |
| `grief_withdrawal.name_en` | string | "Grief Withdrawal" |
| `grief_withdrawal.name_kr` | string | "애도 칩거" |
| `grief_withdrawal.personality_weights` | object | object with 6 keys |
| `grief_withdrawal.personality_weights.A` | float | 0.5 |
| `grief_withdrawal.personality_weights.C` | float | 0.0 |
| `grief_withdrawal.personality_weights.E` | float | 1.3 |
| `grief_withdrawal.personality_weights.H` | float | 0.5 |
| `grief_withdrawal.personality_weights.O` | float | -0.3 |
| `grief_withdrawal.personality_weights.X` | float | -0.5 |
| `grief_withdrawal.severity` | string | "major" |
| `grief_withdrawal.stress_catharsis_factor` | float | 0.85 |
| `grief_withdrawal.trait_modifiers` | object | object with 2 keys |
| `grief_withdrawal.trait_modifiers.cold_blooded` | float | 0.6 |
| `grief_withdrawal.trait_modifiers.empathic` | float | 1.3 |
| `hysterical_bonding` | object | object with 11 keys |
| `hysterical_bonding.behavior_override` | object | object with 4 keys |
| `hysterical_bonding.behavior_override.ignore_jobs` | boolean | true |
| `hysterical_bonding.behavior_override.mode` | string | "cling_to_target" |
| `hysterical_bonding.behavior_override.speed_multiplier` | float | 1.0 |
| `hysterical_bonding.behavior_override.target_rule` | string | "closest_positive_relation" |
| `hysterical_bonding.duration_base_ticks` | int | 3 |
| `hysterical_bonding.duration_variance_ticks` | int | 9 |
| `hysterical_bonding.energy_cost` | float | 0.05 |
| `hysterical_bonding.id` | string | "hysterical_bonding" |
| `hysterical_bonding.name_en` | string | "Hysterical Bonding" |
| `hysterical_bonding.name_kr` | string | "불안 집착" |
| `hysterical_bonding.personality_weights` | object | object with 6 keys |
| `hysterical_bonding.personality_weights.A` | float | 0.5 |
| `hysterical_bonding.personality_weights.C` | float | 0.0 |
| `hysterical_bonding.personality_weights.E` | float | 1.0 |
| `hysterical_bonding.personality_weights.H` | float | 0.0 |
| `hysterical_bonding.personality_weights.O` | float | 0.0 |
| `hysterical_bonding.personality_weights.X` | float | 1.0 |
| `hysterical_bonding.severity` | string | "minor" |
| `hysterical_bonding.stress_catharsis_factor` | float | 0.8 |
| `hysterical_bonding.trait_modifiers` | object | object with 2 keys |
| `hysterical_bonding.trait_modifiers.loner` | float | 0.4 |
| `hysterical_bonding.trait_modifiers.social_clinger` | float | 1.4 |
| `outrage_violence` | object | object with 11 keys |
| `outrage_violence.behavior_override` | object | object with 6 keys |
| `outrage_violence.behavior_override.can_use_weapons` | boolean | true |
| `outrage_violence.behavior_override.ignore_jobs` | boolean | true |
| `outrage_violence.behavior_override.lethal` | boolean | true |
| `outrage_violence.behavior_override.mode` | string | "seek_and_destroy" |
| `outrage_violence.behavior_override.speed_multiplier` | float | 1.3 |
| `outrage_violence.behavior_override.target_rule` | string | "nearest_negative_relation" |
| `outrage_violence.duration_base_ticks` | int | 5 |
| `outrage_violence.duration_variance_ticks` | int | 7 |
| `outrage_violence.energy_cost` | float | 0.3 |
| `outrage_violence.id` | string | "outrage_violence" |
| `outrage_violence.name_en` | string | "Outrage Violence" |
| `outrage_violence.name_kr` | string | "폭력 난동" |
| `outrage_violence.personality_weights` | object | object with 6 keys |
| `outrage_violence.personality_weights.A` | float | -3.0 |
| `outrage_violence.personality_weights.C` | float | -1.0 |
| `outrage_violence.personality_weights.E` | float | 0.0 |
| `outrage_violence.personality_weights.H` | float | -1.5 |
| `outrage_violence.personality_weights.O` | float | 0.0 |
| `outrage_violence.personality_weights.X` | float | 0.5 |
| `outrage_violence.severity` | string | "extreme" |
| `outrage_violence.stress_catharsis_factor` | float | 0.6 |
| `outrage_violence.trait_modifiers` | object | object with 3 keys |
| `outrage_violence.trait_modifiers.berserker` | float | 1.6 |
| `outrage_violence.trait_modifiers.peaceful` | float | 0.3 |
| `outrage_violence.trait_modifiers.ruthless` | float | 1.4 |
| `panic` | object | object with 11 keys |
| `panic.behavior_override` | object | object with 4 keys |
| `panic.behavior_override.ignore_jobs` | boolean | true |
| `panic.behavior_override.mode` | string | "flee_hide" |
| `panic.behavior_override.speed_multiplier` | float | 1.3 |
| `panic.behavior_override.target_rule` | string | "nearest_safe_spot" |
| `panic.duration_base_ticks` | int | 2 |
| `panic.duration_variance_ticks` | int | 2 |
| `panic.energy_cost` | float | 0.15 |
| `panic.id` | string | "panic" |
| `panic.name_en` | string | "Panic" |
| `panic.name_kr` | string | "공황" |
| `panic.personality_weights` | object | object with 6 keys |
| `panic.personality_weights.A` | float | 0.1 |
| `panic.personality_weights.C` | float | -0.1 |
| `panic.personality_weights.E` | float | 1.7 |
| `panic.personality_weights.H` | float | 0.0 |
| `panic.personality_weights.O` | float | -0.1 |
| `panic.personality_weights.X` | float | -0.3 |
| `panic.severity` | string | "minor" |
| `panic.stress_catharsis_factor` | float | 0.8 |
| `panic.trait_modifiers` | object | object with 2 keys |
| `panic.trait_modifiers.brave` | float | 0.6 |
| `panic.trait_modifiers.cowardly` | float | 1.6 |
| `paranoia` | object | object with 11 keys |
| `paranoia.behavior_override` | object | object with 5 keys |
| `paranoia.behavior_override.ignore_jobs` | boolean | false |
| `paranoia.behavior_override.mode` | string | "distrust_isolate" |
| `paranoia.behavior_override.speed_multiplier` | float | 1.0 |
| `paranoia.behavior_override.target_rule` | string | "avoid_all" |
| `paranoia.behavior_override.trust_override` | float | -0.5 |
| `paranoia.duration_base_ticks` | int | 48 |
| `paranoia.duration_variance_ticks` | int | 120 |
| `paranoia.energy_cost` | float | 0.03 |
| `paranoia.id` | string | "paranoia" |
| `paranoia.name_en` | string | "Paranoia" |
| `paranoia.name_kr` | string | "편집증" |
| `paranoia.personality_weights` | object | object with 6 keys |
| `paranoia.personality_weights.A` | float | -0.5 |
| `paranoia.personality_weights.C` | float | 0.0 |
| `paranoia.personality_weights.E` | float | 1.2 |
| `paranoia.personality_weights.H` | float | -0.5 |
| `paranoia.personality_weights.O` | float | -0.5 |
| `paranoia.personality_weights.X` | float | -1.0 |
| `paranoia.severity` | string | "major" |
| `paranoia.stress_catharsis_factor` | float | 0.95 |
| `paranoia.trait_modifiers` | object | object with 2 keys |
| `paranoia.trait_modifiers.suspicious` | float | 1.4 |
| `paranoia.trait_modifiers.trusting` | float | 0.5 |
| `purge` | object | object with 11 keys |
| `purge.behavior_override` | object | object with 4 keys |
| `purge.behavior_override.ignore_jobs` | boolean | true |
| `purge.behavior_override.mode` | string | "binge_consume" |
| `purge.behavior_override.speed_multiplier` | float | 1.0 |
| `purge.behavior_override.target_rule` | string | "nearest_food_storage" |
| `purge.duration_base_ticks` | int | 3 |
| `purge.duration_variance_ticks` | int | 5 |
| `purge.energy_cost` | float | 0.05 |
| `purge.id` | string | "purge" |
| `purge.name_en` | string | "Purge" |
| `purge.name_kr` | string | "폭식/낭비" |
| `purge.personality_weights` | object | object with 6 keys |
| `purge.personality_weights.A` | float | 0.0 |
| `purge.personality_weights.C` | float | -2.0 |
| `purge.personality_weights.E` | float | 0.0 |
| `purge.personality_weights.H` | float | -0.3 |
| `purge.personality_weights.O` | float | 0.0 |
| `purge.personality_weights.X` | float | 0.5 |
| `purge.severity` | string | "minor" |
| `purge.stress_catharsis_factor` | float | 0.75 |
| `purge.trait_modifiers` | object | object with 2 keys |
| `purge.trait_modifiers.ascetic` | float | 0.5 |
| `purge.trait_modifiers.greedy` | float | 1.3 |
| `rage` | object | object with 11 keys |
| `rage.behavior_override` | object | object with 4 keys |
| `rage.behavior_override.ignore_jobs` | boolean | true |
| `rage.behavior_override.mode` | string | "attack_smash" |
| `rage.behavior_override.speed_multiplier` | float | 1.2 |
| `rage.behavior_override.target_rule` | string | "conflict_then_nearest" |
| `rage.duration_base_ticks` | int | 3 |
| `rage.duration_variance_ticks` | int | 3 |
| `rage.energy_cost` | float | 0.2 |
| `rage.id` | string | "rage" |
| `rage.name_en` | string | "Rage" |
| `rage.name_kr` | string | "분노 폭발" |
| `rage.personality_weights` | object | object with 6 keys |
| `rage.personality_weights.A` | float | -2.0 |
| `rage.personality_weights.C` | float | -0.5 |
| `rage.personality_weights.E` | float | 0.0 |
| `rage.personality_weights.H` | float | -0.5 |
| `rage.personality_weights.O` | float | 0.0 |
| `rage.personality_weights.X` | float | 0.5 |
| `rage.severity` | string | "major" |
| `rage.stress_catharsis_factor` | float | 0.65 |
| `rage.trait_modifiers` | object | object with 2 keys |
| `rage.trait_modifiers.hotheaded` | float | 1.5 |
| `rage.trait_modifiers.peaceful` | float | 0.5 |
| `shutdown` | object | object with 11 keys |
| `shutdown.behavior_override` | object | object with 4 keys |
| `shutdown.behavior_override.ignore_jobs` | boolean | true |
| `shutdown.behavior_override.mode` | string | "freeze_in_place" |
| `shutdown.behavior_override.speed_multiplier` | float | 0.0 |
| `shutdown.behavior_override.target_rule` | string | "none" |
| `shutdown.duration_base_ticks` | int | 12 |
| `shutdown.duration_variance_ticks` | int | 24 |
| `shutdown.energy_cost` | float | 0.05 |
| `shutdown.id` | string | "shutdown" |
| `shutdown.name_en` | string | "Shutdown" |
| `shutdown.name_kr` | string | "셧다운" |
| `shutdown.personality_weights` | object | object with 6 keys |
| `shutdown.personality_weights.A` | float | 0.0 |
| `shutdown.personality_weights.C` | float | -0.5 |
| `shutdown.personality_weights.E` | float | 1.4 |
| `shutdown.personality_weights.H` | float | 0.0 |
| `shutdown.personality_weights.O` | float | -0.3 |
| `shutdown.personality_weights.X` | float | -1.0 |
| `shutdown.severity` | string | "major" |
| `shutdown.stress_catharsis_factor` | float | 0.9 |
| `shutdown.trait_modifiers` | object | object with 2 keys |
| `shutdown.trait_modifiers.depressive` | float | 1.4 |
| `shutdown.trait_modifiers.loner` | float | 1.2 |

## Full Content

Large object detected: **246** total nested keys.

Top-level keys: **10**

<details>
<summary>Expand top-level preview</summary>

```json
{
  "compulsive_ritual": {
    "id": "compulsive_ritual",
    "name_kr": "강박 의식",
    "name_en": "Compulsive Ritual",
    "severity": "minor",
    "behavior_override": {
      "mode": "repeat_action",
      "ignore_jobs": true,
      "speed_multiplier": 1.0,
      "target_rule": "current_location"
    },
    "duration_base_ticks": 1,
    "duration_variance_ticks": 3,
    "stress_catharsis_factor": 0.85,
    "energy_cost": 0.05,
    "personality_weights": {
      "H": 0.0,
      "E": 0.5,
      "X": 0.0,
      "A": 0.0,
      "C": 1.5,
      "O": 0.5
    },
    "trait_modifiers": {
      "ritualist": 1.4,
      "impulsive": 0.6
    }
  },
  "fugue": {
    "id": "fugue",
    "name_kr": "해리성 둔주",
    "name_en": "Dissociative Fugue",
    "severity": "major",
    "behavior_override": {
      "mode": "wander_away",
      "ignore_jobs": true,
      "speed_multiplier": 0.8,
      "target_rule": "random_far_direction",
      "leave_settlement": true
    },
    "duration_base_ticks": 24,
    "duration_variance_ticks": 60,
    "stress_catharsis_factor": 0.8,
    "energy_cost": 0.15,
    "personality_weights": {
      "H": 0.0,
      "E": 0.5,
      "X": -0.5,
      "A": 0.0,
      "C": -0.3,
      "O": 1.5
    },
    "trait_modifiers": {
      "loner": 1.2,
      "rebellious": 1.1
    }
  },
  "grief_withdrawal": {
    "id": "grief_withdrawal",
    "name_kr": "애도 칩거",
    "name_en": "Grief Withdrawal",
    "severity": "major",
    "behavior_override": {
      "mode": "withdraw_to_home",
      "ignore_jobs": true,
      "speed_multiplier": 0.3,
      "target_rule": "home_or_corner",
      "reject_social": true
    },
    "duration_base_ticks": 24,
    "duration_variance_ticks": 36,
    "stress_catharsis_factor": 0.85,
    "energy_cost": 0.08,
    "personality_weights": {
      "H": 0.5,
      "E": 1.3,
      "X": -0.5,
      "A": 0.5,
      "C": 0.0,
      "O": -0.3
    },
    "trait_modifiers": {
      "empathic": 1.3,
      "cold_blooded": 0.6
    }
  },
  "hysterical_bonding": {
    "id": "hysterical_bonding",
    "name_kr": "불안 집착",
    "name_en": "Hysterical Bonding",
    "severity": "minor",
    "behavior_override": {
      "mode": "cling_to_target",
      "ignore_jobs": true,
      "speed_multiplier": 1.0,
      "target_rule": "closest_positive_relation"
    },
    "duration_base_ticks": 3,
    "duration_variance_ticks": 9,
    "stress_catharsis_factor": 0.8,
    "energy_cost": 0.05,
    "personality_weights": {
      "H": 0.0,
      "E": 1.0,
      "X": 1.0,
      "A": 0.5,
      "C": 0.0,
      "O": 0.0
    },
    "trait_modifiers": {
      "social_clinger": 1.4,
      "loner": 0.4
    }
  },
  "outrage_violence": {
    "id": "outrage_violence",
    "name_kr": "폭력 난동",
    "name_en": "Outrage Violence",
    "severity": "extreme",
    "behavior_override": {
      "mode": "seek_and_destroy",
      "ignore_jobs": true,
      "speed_multiplier": 1.3,
      "target_rule": "nearest_negative_relation",
      "can_use_weapons": true,
      "lethal": true
    },
    "duration_base_ticks": 5,
    "duration_variance_ticks": 7,
    "stress_catharsis_factor": 0.6,
    "energy_cost": 0.3,
    "personality_weights": {
      "H": -1.5,
      "E": 0.0,
      "X": 0.5,
      "A": -3.0,
      "C": -1.0,
      "O": 0.0
    },
    "trait_modifiers": {
      "berserker": 1.6,
      "ruthless": 1.4,
      "peaceful": 0.3
    }
  },
  "panic": {
    "id": "panic",
    "name_kr": "공황",
    "name_en": "Panic",
    "severity": "minor",
    "behavior_override": {
      "mode": "flee_hide",
      "ignore_jobs": true,
      "speed_multiplier": 1.3,
      "target_rule": "nearest_safe_spot"
    },
    "duration_base_ticks": 2,
    "duration_variance_ticks": 2,
    "stress_catharsis_factor": 0.8,
    "energy_cost": 0.15,
    "personality_weights": {
      "H": 0.0,
      "E": 1.7,
      "X": -0.3,
      "A": 0.1,
      "C": -0.1,
      "O": -0.1
    },
    "trait_modifiers": {
      "cowardly": 1.6,
      "brave": 0.6
    }
  },
  "paranoia": {
    "id": "paranoia",
    "name_kr": "편집증",
    "name_en": "Paranoia",
    "severity": "major",
    "behavior_override": {
      "mode": "distrust_isolate",
      "ignore_jobs": false,
      "speed_multiplier": 1.0,
      "target_rule": "avoid_all",
      "trust_override": -0.5
    },
    "duration_base_ticks": 48,
    "duration_variance_ticks": 120,
    "stress_catharsis_factor": 0.95,
    "energy_cost": 0.03,
    "personality_weights": {
      "H": -0.5,
      "E": 1.2,
      "X": -1.0,
      "A": -0.5,
      "C": 0.0,
      "O": -0.5
    },
    "trait_modifiers": {
      "suspicious": 1.4,
      "trusting": 0.5
    }
  },
  "purge": {
    "id": "purge",
    "name_kr": "폭식/낭비",
    "name_en": "Purge",
    "severity": "minor",
    "behavior_override": {
      "mode": "binge_consume",
      "ignore_jobs": true,
      "speed_multiplier": 1.0,
      "target_rule": "nearest_food_storage"
    },
    "duration_base_ticks": 3,
    "duration_variance_ticks": 5,
    "stress_catharsis_factor": 0.75,
    "energy_cost": 0.05,
    "personality_weights": {
      "H": -0.3,
      "E": 0.0,
      "X": 0.5,
      "A": 0.0,
      "C": -2.0,
      "O": 0.0
    },
    "trait_modifiers": {
      "greedy": 1.3,
      "ascetic": 0.5
    }
  },
  "rage": {
    "id": "rage",
    "name_kr": "분노 폭발",
    "name_en": "Rage",
    "severity": "major",
    "behavior_override": {
      "mode": "attack_smash",
      "ignore_jobs": true,
      "speed_multiplier": 1.2,
      "target_rule": "conflict_then_nearest"
    },
    "duration_base_ticks": 3,
    "duration_variance_ticks": 3,
    "stress_catharsis_factor": 0.65,
    "energy_cost": 0.2,
    "personality_weights": {
      "H": -0.5,
      "E": 0.0,
      "X": 0.5,
      "A": -2.0,
      "C": -0.5,
      "O": 0.0
    },
    "trait_modifiers": {
      "hotheaded": 1.5,
      "peaceful": 0.5
    }
  },
  "shutdown": {
    "id": "shutdown",
    "name_kr": "셧다운",
    "name_en": "Shutdown",
    "severity": "major",
    "behavior_override": {
      "mode": "freeze_in_place",
      "ignore_jobs": true,
      "speed_multiplier": 0.0,
      "target_rule": "none"
    },
    "duration_base_ticks": 12,
    "duration_variance_ticks": 24,
    "stress_catharsis_factor": 0.9,
    "energy_cost": 0.05,
    "personality_weights": {
      "H": 0.0,
      "E": 1.4,
      "X": -1.0,
      "A": 0.0,
      "C": -0.5,
      "O": -0.3
    },
    "trait_modifiers": {
      "loner": 1.2,
      "depressive": 1.4
    }
  }
}
```

</details>

## Referenced By

- [`mental_break`](../../systems/mental_break.md) - references `data/mental_breaks.json`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
