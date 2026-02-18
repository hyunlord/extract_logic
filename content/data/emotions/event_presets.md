---
title: "event_presets Data"
description: "emotions data file documentation"
generated: true
source_files:
  - "data/emotions/event_presets.json"
nav_order: 10
---

# event_presets

📄 source: `data/emotions/event_presets.json` | Category: emotions | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `_comment` | string | "Emotion event presets — appraisal vectors for EmotionSystem impulse calculation. Based on Lazarus (1991) Appraisal T... |
| `events` | object | object with 23 keys |
| `events.ate_food` | object | object with 11 keys |
| `events.ate_food.agency` | float | 0.5 |
| `events.ate_food.category` | string | "survival" |
| `events.ate_food.controllability` | float | 0.9 |
| `events.ate_food.description` | string | "Ate food successfully" |
| `events.ate_food.future_relevance` | float | 0.1 |
| `events.ate_food.goal_congruence` | float | 0.6 |
| `events.ate_food.intensity` | int | 20 |
| `events.ate_food.norm_violation` | float | 0.0 |
| `events.ate_food.novelty` | float | 0.0 |
| `events.ate_food.pathogen` | float | 0.0 |
| `events.ate_food.social_bond` | float | 0.0 |
| `events.betrayal` | object | object with 12 keys |
| `events.betrayal.agency` | float | -1.0 |
| `events.betrayal.category` | string | "conflict" |
| `events.betrayal.controllability` | float | 0.2 |
| `events.betrayal.description` | string | "Betrayed by trusted person" |
| `events.betrayal.future_relevance` | float | 0.5 |
| `events.betrayal.goal_congruence` | float | -0.9 |
| `events.betrayal.intensity` | int | 80 |
| `events.betrayal.is_trauma` | boolean | true |
| `events.betrayal.norm_violation` | float | 0.9 |
| `events.betrayal.novelty` | float | 0.7 |
| `events.betrayal.pathogen` | float | 0.0 |
| `events.betrayal.social_bond` | float | -1.0 |
| `events.building_completed` | object | object with 11 keys |
| `events.building_completed.agency` | float | 0.7 |
| `events.building_completed.category` | string | "achievement" |
| `events.building_completed.controllability` | float | 0.8 |
| `events.building_completed.description` | string | "Building completed" |
| `events.building_completed.future_relevance` | float | 0.5 |
| `events.building_completed.goal_congruence` | float | 0.8 |
| `events.building_completed.intensity` | int | 30 |
| `events.building_completed.norm_violation` | float | 0.0 |
| `events.building_completed.novelty` | float | 0.3 |
| `events.building_completed.pathogen` | float | 0.0 |
| `events.building_completed.social_bond` | float | 0.2 |
| `events.child_born` | object | object with 11 keys |
| `events.child_born.agency` | float | 0.5 |
| `events.child_born.category` | string | "family" |
| `events.child_born.controllability` | float | 0.3 |
| `events.child_born.description` | string | "Child born" |
| `events.child_born.future_relevance` | float | 0.9 |
| `events.child_born.goal_congruence` | float | 0.9 |
| `events.child_born.intensity` | int | 60 |
| `events.child_born.norm_violation` | float | 0.0 |
| `events.child_born.novelty` | float | 0.7 |
| `events.child_born.pathogen` | float | 0.0 |
| `events.child_born.social_bond` | float | 0.9 |
| `events.child_death` | object | object with 12 keys |
| `events.child_death.agency` | float | -0.5 |
| `events.child_death.category` | string | "loss" |
| `events.child_death.controllability` | float | 0.0 |
| `events.child_death.description` | string | "Child died" |
| `events.child_death.future_relevance` | float | 0.8 |
| `events.child_death.goal_congruence` | float | -1.0 |
| `events.child_death.intensity` | int | 95 |
| `events.child_death.is_trauma` | boolean | true |
| `events.child_death.norm_violation` | float | 0.0 |
| `events.child_death.novelty` | float | 0.7 |
| `events.child_death.pathogen` | float | 0.0 |
| `events.child_death.social_bond` | float | 1.0 |
| `events.combat_threat` | object | object with 11 keys |
| `events.combat_threat.agency` | float | -0.5 |
| `events.combat_threat.category` | string | "danger" |
| `events.combat_threat.controllability` | float | 0.3 |
| `events.combat_threat.description` | string | "Combat threat" |
| `events.combat_threat.future_relevance` | float | 0.6 |
| `events.combat_threat.goal_congruence` | float | -0.8 |
| `events.combat_threat.intensity` | int | 70 |
| `events.combat_threat.norm_violation` | float | 0.0 |
| `events.combat_threat.novelty` | float | 0.4 |
| `events.combat_threat.pathogen` | float | 0.0 |
| `events.combat_threat.social_bond` | float | -0.7 |
| `events.community_festival` | object | object with 11 keys |
| `events.community_festival.agency` | float | 0.3 |
| `events.community_festival.category` | string | "social" |
| `events.community_festival.controllability` | float | 0.7 |
| `events.community_festival.description` | string | "Community festival" |
| `events.community_festival.future_relevance` | float | 0.2 |
| `events.community_festival.goal_congruence` | float | 0.6 |
| `events.community_festival.intensity` | int | 40 |
| `events.community_festival.norm_violation` | float | 0.0 |
| `events.community_festival.novelty` | float | 0.3 |
| `events.community_festival.pathogen` | float | 0.0 |
| `events.community_festival.social_bond` | float | 0.8 |
| `events.food_acquired` | object | object with 11 keys |
| `events.food_acquired.agency` | float | 0.5 |
| `events.food_acquired.category` | string | "resource" |
| `events.food_acquired.controllability` | float | 0.8 |
| `events.food_acquired.description` | string | "Food acquired" |
| `events.food_acquired.future_relevance` | float | 0.3 |
| `events.food_acquired.goal_congruence` | float | 0.7 |
| `events.food_acquired.intensity` | int | 25 |
| `events.food_acquired.norm_violation` | float | 0.0 |
| `events.food_acquired.novelty` | float | 0.1 |
| `events.food_acquired.pathogen` | float | 0.0 |
| `events.food_acquired.social_bond` | float | 0.0 |
| `events.friend_death` | object | object with 11 keys |
| `events.friend_death.agency` | float | -0.2 |
| `events.friend_death.category` | string | "loss" |
| `events.friend_death.controllability` | float | 0.0 |
| `events.friend_death.description` | string | "Friend died" |
| `events.friend_death.future_relevance` | float | 0.3 |
| `events.friend_death.goal_congruence` | float | -0.6 |
| `events.friend_death.intensity` | int | 50 |
| `events.friend_death.norm_violation` | float | 0.0 |
| `events.friend_death.novelty` | float | 0.5 |
| `events.friend_death.pathogen` | float | 0.0 |
| `events.friend_death.social_bond` | float | 0.5 |
| `events.job_assigned` | object | object with 11 keys |
| `events.job_assigned.agency` | float | -0.2 |
| `events.job_assigned.category` | string | "work" |
| `events.job_assigned.controllability` | float | 0.2 |
| `events.job_assigned.description` | string | "New job assigned" |
| `events.job_assigned.future_relevance` | float | 0.4 |
| `events.job_assigned.goal_congruence` | float | 0.3 |
| `events.job_assigned.intensity` | int | 15 |
| `events.job_assigned.norm_violation` | float | 0.0 |
| `events.job_assigned.novelty` | float | 0.3 |
| `events.job_assigned.pathogen` | float | 0.0 |
| `events.job_assigned.social_bond` | float | 0.0 |
| `events.migration_started` | object | object with 11 keys |
| `events.migration_started.agency` | float | 0.3 |
| `events.migration_started.category` | string | "exploration" |
| `events.migration_started.controllability` | float | 0.4 |
| `events.migration_started.description` | string | "Migration to new settlement" |
| `events.migration_started.future_relevance` | float | 0.9 |
| `events.migration_started.goal_congruence` | float | 0.3 |
| `events.migration_started.intensity` | int | 40 |
| `events.migration_started.norm_violation` | float | 0.0 |
| `events.migration_started.novelty` | float | 0.8 |
| `events.migration_started.pathogen` | float | 0.0 |
| `events.migration_started.social_bond` | float | -0.3 |
| `events.new_territory` | object | object with 11 keys |
| `events.new_territory.agency` | float | 0.7 |
| `events.new_territory.category` | string | "exploration" |
| `events.new_territory.controllability` | float | 0.6 |
| `events.new_territory.description` | string | "New territory discovered" |
| `events.new_territory.future_relevance` | float | 0.8 |
| `events.new_territory.goal_congruence` | float | 0.5 |
| `events.new_territory.intensity` | int | 35 |
| `events.new_territory.norm_violation` | float | 0.0 |
| `events.new_territory.novelty` | float | 0.9 |
| `events.new_territory.pathogen` | float | 0.0 |
| `events.new_territory.social_bond` | float | 0.0 |
| `events.parent_death` | object | object with 12 keys |
| `events.parent_death.agency` | float | -0.3 |
| `events.parent_death.category` | string | "loss" |
| `events.parent_death.controllability` | float | 0.0 |
| `events.parent_death.description` | string | "Parent died" |
| `events.parent_death.future_relevance` | float | 0.5 |
| `events.parent_death.goal_congruence` | float | -0.8 |
| `events.parent_death.intensity` | int | 70 |
| `events.parent_death.is_trauma` | boolean | true |
| `events.parent_death.norm_violation` | float | 0.0 |
| `events.parent_death.novelty` | float | 0.5 |
| `events.parent_death.pathogen` | float | 0.0 |
| `events.parent_death.social_bond` | float | 0.7 |
| `events.partner_death` | object | object with 12 keys |
| `events.partner_death.agency` | float | -0.5 |
| `events.partner_death.category` | string | "loss" |
| `events.partner_death.controllability` | float | 0.0 |
| `events.partner_death.description` | string | "Partner died" |
| `events.partner_death.future_relevance` | float | 0.9 |
| `events.partner_death.goal_congruence` | float | -1.0 |
| `events.partner_death.intensity` | int | 90 |
| `events.partner_death.is_trauma` | boolean | true |
| `events.partner_death.norm_violation` | float | 0.0 |
| `events.partner_death.novelty` | float | 0.8 |
| `events.partner_death.pathogen` | float | 0.0 |
| `events.partner_death.social_bond` | float | 1.0 |
| `events.partner_found` | object | object with 11 keys |
| `events.partner_found.agency` | float | 0.5 |
| `events.partner_found.category` | string | "social" |
| `events.partner_found.controllability` | float | 0.5 |
| `events.partner_found.description` | string | "Found a partner" |
| `events.partner_found.future_relevance` | float | 0.7 |
| `events.partner_found.goal_congruence` | float | 0.9 |
| `events.partner_found.intensity` | int | 40 |
| `events.partner_found.norm_violation` | float | 0.0 |
| `events.partner_found.novelty` | float | 0.6 |
| `events.partner_found.pathogen` | float | 0.0 |
| `events.partner_found.social_bond` | float | 0.8 |
| `events.rested_well` | object | object with 11 keys |
| `events.rested_well.agency` | float | 0.3 |
| `events.rested_well.category` | string | "survival" |
| `events.rested_well.controllability` | float | 0.7 |
| `events.rested_well.description` | string | "Well rested (energy recovered)" |
| `events.rested_well.future_relevance` | float | 0.1 |
| `events.rested_well.goal_congruence` | float | 0.5 |
| `events.rested_well.intensity` | int | 15 |
| `events.rested_well.norm_violation` | float | 0.0 |
| `events.rested_well.novelty` | float | 0.0 |
| `events.rested_well.pathogen` | float | 0.0 |
| `events.rested_well.social_bond` | float | 0.0 |
| `events.settlement_founded` | object | object with 11 keys |
| `events.settlement_founded.agency` | float | 0.6 |
| `events.settlement_founded.category` | string | "achievement" |
| `events.settlement_founded.controllability` | float | 0.5 |
| `events.settlement_founded.description` | string | "New settlement founded" |
| `events.settlement_founded.future_relevance` | float | 0.8 |
| `events.settlement_founded.goal_congruence` | float | 0.8 |
| `events.settlement_founded.intensity` | int | 45 |
| `events.settlement_founded.norm_violation` | float | 0.0 |
| `events.settlement_founded.novelty` | float | 0.7 |
| `events.settlement_founded.pathogen` | float | 0.0 |
| `events.settlement_founded.social_bond` | float | 0.6 |
| `events.severe_hunger` | object | object with 11 keys |
| `events.severe_hunger.agency` | float | 0.0 |
| `events.severe_hunger.category` | string | "survival" |
| `events.severe_hunger.controllability` | float | 0.3 |
| `events.severe_hunger.description` | string | "Severe hunger" |
| `events.severe_hunger.future_relevance` | float | 0.7 |
| `events.severe_hunger.goal_congruence` | float | -0.8 |
| `events.severe_hunger.intensity` | int | 50 |
| `events.severe_hunger.norm_violation` | float | 0.0 |
| `events.severe_hunger.novelty` | float | 0.1 |
| `events.severe_hunger.pathogen` | float | 0.0 |
| `events.severe_hunger.social_bond` | float | 0.0 |
| `events.social_interaction` | object | object with 11 keys |
| `events.social_interaction.agency` | float | 0.3 |
| `events.social_interaction.category` | string | "social" |
| `events.social_interaction.controllability` | float | 0.6 |
| `events.social_interaction.description` | string | "Positive social interaction" |
| `events.social_interaction.future_relevance` | float | 0.1 |
| `events.social_interaction.goal_congruence` | float | 0.4 |
| `events.social_interaction.intensity` | int | 15 |
| `events.social_interaction.norm_violation` | float | 0.0 |
| `events.social_interaction.novelty` | float | 0.1 |
| `events.social_interaction.pathogen` | float | 0.0 |
| `events.social_interaction.social_bond` | float | 0.5 |
| `events.starvation_warning` | object | object with 11 keys |
| `events.starvation_warning.agency` | float | 0.0 |
| `events.starvation_warning.category` | string | "survival" |
| `events.starvation_warning.controllability` | float | 0.1 |
| `events.starvation_warning.description` | string | "Starvation imminent" |
| `events.starvation_warning.future_relevance` | float | 0.9 |
| `events.starvation_warning.goal_congruence` | float | -1.0 |
| `events.starvation_warning.intensity` | int | 75 |
| `events.starvation_warning.norm_violation` | float | 0.0 |
| `events.starvation_warning.novelty` | float | 0.2 |
| `events.starvation_warning.pathogen` | float | 0.0 |
| `events.starvation_warning.social_bond` | float | 0.0 |
| `events.stone_acquired` | object | object with 11 keys |
| `events.stone_acquired.agency` | float | 0.5 |
| `events.stone_acquired.category` | string | "resource" |
| `events.stone_acquired.controllability` | float | 0.8 |
| `events.stone_acquired.description` | string | "Stone acquired" |
| `events.stone_acquired.future_relevance` | float | 0.2 |
| `events.stone_acquired.goal_congruence` | float | 0.5 |
| `events.stone_acquired.intensity` | int | 20 |
| `events.stone_acquired.norm_violation` | float | 0.0 |
| `events.stone_acquired.novelty` | float | 0.05 |
| `events.stone_acquired.pathogen` | float | 0.0 |
| `events.stone_acquired.social_bond` | float | 0.0 |
| `events.theft_victim` | object | object with 11 keys |
| `events.theft_victim.agency` | float | -0.8 |
| `events.theft_victim.category` | string | "conflict" |
| `events.theft_victim.controllability` | float | 0.4 |
| `events.theft_victim.description` | string | "Victim of theft" |
| `events.theft_victim.future_relevance` | float | 0.3 |
| `events.theft_victim.goal_congruence` | float | -0.7 |
| `events.theft_victim.intensity` | int | 55 |
| `events.theft_victim.norm_violation` | float | 0.8 |
| `events.theft_victim.novelty` | float | 0.5 |
| `events.theft_victim.pathogen` | float | 0.0 |
| `events.theft_victim.social_bond` | float | -0.5 |
| `events.wood_acquired` | object | object with 11 keys |
| `events.wood_acquired.agency` | float | 0.5 |
| `events.wood_acquired.category` | string | "resource" |
| `events.wood_acquired.controllability` | float | 0.8 |
| `events.wood_acquired.description` | string | "Wood acquired" |
| `events.wood_acquired.future_relevance` | float | 0.2 |
| `events.wood_acquired.goal_congruence` | float | 0.5 |
| `events.wood_acquired.intensity` | int | 20 |
| `events.wood_acquired.norm_violation` | float | 0.0 |
| `events.wood_acquired.novelty` | float | 0.05 |
| `events.wood_acquired.pathogen` | float | 0.0 |
| `events.wood_acquired.social_bond` | float | 0.0 |

## Full Content

Large object detected: **282** total nested keys.

Top-level keys: **2**

<details>
<summary>Expand top-level preview</summary>

```json
{
  "_comment": "Emotion event presets — appraisal vectors for EmotionSystem impulse calculation. Based on Lazarus (1991) Appraisal Theory + Scherer (2009) CPM. Fields: goal_congruence (-1~+1), novelty (0~1), controllability (0~1), agency (-1~+1), norm_violation (0~1), pathogen (0~1), social_bond (-1~+1), future_relevance (0~1), intensity (0~100), is_trauma (bool).",
  "events": {
    "food_acquired": {
      "description": "Food acquired",
      "category": "resource",
      "intensity": 25,
      "goal_congruence": 0.7,
      "novelty": 0.1,
      "controllability": 0.8,
      "agency": 0.5,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.0,
      "future_relevance": 0.3
    },
    "wood_acquired": {
      "description": "Wood acquired",
      "category": "resource",
      "intensity": 20,
      "goal_congruence": 0.5,
      "novelty": 0.05,
      "controllability": 0.8,
      "agency": 0.5,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.0,
      "future_relevance": 0.2
    },
    "stone_acquired": {
      "description": "Stone acquired",
      "category": "resource",
      "intensity": 20,
      "goal_congruence": 0.5,
      "novelty": 0.05,
      "controllability": 0.8,
      "agency": 0.5,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.0,
      "future_relevance": 0.2
    },
    "severe_hunger": {
      "description": "Severe hunger",
      "category": "survival",
      "intensity": 50,
      "goal_congruence": -0.8,
      "novelty": 0.1,
      "controllability": 0.3,
      "agency": 0.0,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.0,
      "future_relevance": 0.7
    },
    "starvation_warning": {
      "description": "Starvation imminent",
      "category": "survival",
      "intensity": 75,
      "goal_congruence": -1.0,
      "novelty": 0.2,
      "controllability": 0.1,
      "agency": 0.0,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.0,
      "future_relevance": 0.9
    },
    "ate_food": {
      "description": "Ate food successfully",
      "category": "survival",
      "intensity": 20,
      "goal_congruence": 0.6,
      "novelty": 0.0,
      "controllability": 0.9,
      "agency": 0.5,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.0,
      "future_relevance": 0.1
    },
    "partner_found": {
      "description": "Found a partner",
      "category": "social",
      "intensity": 40,
      "goal_congruence": 0.9,
      "novelty": 0.6,
      "controllability": 0.5,
      "agency": 0.5,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.8,
      "future_relevance": 0.7
    },
    "partner_death": {
      "description": "Partner died",
      "category": "loss",
      "intensity": 90,
      "is_trauma": true,
      "goal_congruence": -1.0,
      "novelty": 0.8,
      "controllability": 0.0,
      "agency": -0.5,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 1.0,
      "future_relevance": 0.9
    },
    "child_death": {
      "description": "Child died",
      "category": "loss",
      "intensity": 95,
      "is_trauma": true,
      "goal_congruence": -1.0,
      "novelty": 0.7,
      "controllability": 0.0,
      "agency": -0.5,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 1.0,
      "future_relevance": 0.8
    },
    "parent_death": {
      "description": "Parent died",
      "category": "loss",
      "intensity": 70,
      "is_trauma": true,
      "goal_congruence": -0.8,
      "novelty": 0.5,
      "controllability": 0.0,
      "agency": -0.3,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.7,
      "future_relevance": 0.5
    },
    "friend_death": {
      "description": "Friend died",
      "category": "loss",
      "intensity": 50,
      "goal_congruence": -0.6,
      "novelty": 0.5,
      "controllability": 0.0,
      "agency": -0.2,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.5,
      "future_relevance": 0.3
    },
    "child_born": {
      "description": "Child born",
      "category": "family",
      "intensity": 60,
      "goal_congruence": 0.9,
      "novelty": 0.7,
      "controllability": 0.3,
      "agency": 0.5,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.9,
      "future_relevance": 0.9
    },
    "building_completed": {
      "description": "Building completed",
      "category": "achievement",
      "intensity": 30,
      "goal_congruence": 0.8,
      "novelty": 0.3,
      "controllability": 0.8,
      "agency": 0.7,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.2,
      "future_relevance": 0.5
    },
    "social_interaction": {
      "description": "Positive social interaction",
      "category": "social",
      "intensity": 15,
      "goal_congruence": 0.4,
      "novelty": 0.1,
      "controllability": 0.6,
      "agency": 0.3,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.5,
      "future_relevance": 0.1
    },
    "new_territory": {
      "description": "New territory discovered",
      "category": "exploration",
      "intensity": 35,
      "goal_congruence": 0.5,
      "novelty": 0.9,
      "controllability": 0.6,
      "agency": 0.7,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.0,
      "future_relevance": 0.8
    },
    "migration_started": {
      "description": "Migration to new settlement",
      "category": "exploration",
      "intensity": 40,
      "goal_congruence": 0.3,
      "novelty": 0.8,
      "controllability": 0.4,
      "agency": 0.3,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": -0.3,
      "future_relevance": 0.9
    },
    "settlement_founded": {
      "description": "New settlement founded",
      "category": "achievement",
      "intensity": 45,
      "goal_congruence": 0.8,
      "novelty": 0.7,
      "controllability": 0.5,
      "agency": 0.6,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.6,
      "future_relevance": 0.8
    },
    "theft_victim": {
      "description": "Victim of theft",
      "category": "conflict",
      "intensity": 55,
      "goal_congruence": -0.7,
      "novelty": 0.5,
      "controllability": 0.4,
      "agency": -0.8,
      "norm_violation": 0.8,
      "pathogen": 0.0,
      "social_bond": -0.5,
      "future_relevance": 0.3
    },
    "betrayal": {
      "description": "Betrayed by trusted person",
      "category": "conflict",
      "intensity": 80,
      "is_trauma": true,
      "goal_congruence": -0.9,
      "novelty": 0.7,
      "controllability": 0.2,
      "agency": -1.0,
      "norm_violation": 0.9,
      "pathogen": 0.0,
      "social_bond": -1.0,
      "future_relevance": 0.5
    },
    "combat_threat": {
      "description": "Combat threat",
      "category": "danger",
      "intensity": 70,
      "goal_congruence": -0.8,
      "novelty": 0.4,
      "controllability": 0.3,
      "agency": -0.5,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": -0.7,
      "future_relevance": 0.6
    },
    "community_festival": {
      "description": "Community festival",
      "category": "social",
      "intensity": 40,
      "goal_congruence": 0.6,
      "novelty": 0.3,
      "controllability": 0.7,
      "agency": 0.3,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.8,
      "future_relevance": 0.2
    },
    "job_assigned": {
      "description": "New job assigned",
      "category": "work",
      "intensity": 15,
      "goal_congruence": 0.3,
      "novelty": 0.3,
      "controllability": 0.2,
      "agency": -0.2,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.0,
      "future_relevance": 0.4
    },
    "rested_well": {
      "description": "Well rested (energy recovered)",
      "category": "survival",
      "intensity": 15,
      "goal_congruence": 0.5,
      "novelty": 0.0,
      "controllability": 0.7,
      "agency": 0.3,
      "norm_violation": 0.0,
      "pathogen": 0.0,
      "social_bond": 0.0,
      "future_relevance": 0.1
    }
  }
}
```

</details>

## Referenced By

- [`emotions`](../../systems/emotions.md) - references `data/emotions/event_presets.json`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
