---
title: "stressor_events Data"
description: "data data file documentation"
generated: true
source_files:
  - "data/stressor_events.json"
nav_order: 10
---

# stressor_events

📄 source: `data/stressor_events.json` | Category: data | Type: object

## Schema

| Key | Type | Description |
|-----|------|-------------|
| `_comment` | string | "==========================================================" |
| `_comment10` | string | "카테고리 3: 생존/신체 (Survival & Physical)" |
| `_comment11` | string | "==========================================================" |
| `_comment12` | string | "==========================================================" |
| `_comment13` | string | "카테고리 4: 심리적 사건 (Psychological)" |
| `_comment14` | string | "==========================================================" |
| `_comment15` | string | "==========================================================" |
| `_comment16` | string | "카테고리 5: 긍정적 사건 / 유스트레스 (Eustress)" |
| `_comment17` | string | "Holmes & Rahe: 긍정 사건도 stress 유발 가능 (결혼 50점)" |
| `_comment18` | string | "==========================================================" |
| `_comment2` | string | "카테고리 1: 사망/상실 (Death & Loss)" |
| `_comment3` | string | "학술: Holmes & Rahe — 배우자 사망은 최고 스트레스 사건" |
| `_comment4` | string | "COR: is_loss=true → 2.5배 적용" |
| `_comment5` | string | "==========================================================" |
| `_comment6` | string | "==========================================================" |
| `_comment7` | string | "카테고리 2: 사회적 사건 (Social Events)" |
| `_comment8` | string | "==========================================================" |
| `_comment9` | string | "==========================================================" |
| `acquaintance_death` | object | object with 11 keys |
| `acquaintance_death.base_decay_rate` | float | 0.05 |
| `acquaintance_death.base_instant` | float | 60.0 |
| `acquaintance_death.base_per_tick` | float | 1.5 |
| `acquaintance_death.category` | string | "death" |
| `acquaintance_death.context_modifiers` | object | object with 1 keys |
| `acquaintance_death.context_modifiers.same_settlement` | float | 1.1 |
| `acquaintance_death.emotion_inject` | object | object with 2 keys |
| `acquaintance_death.emotion_inject.fear_fast` | int | 10 |
| `acquaintance_death.emotion_inject.sadness_fast` | int | 20 |
| `acquaintance_death.is_loss` | boolean | false |
| `acquaintance_death.name_en` | string | "Acquaintance Death" |
| `acquaintance_death.name_kr` | string | "지인 사망" |
| `acquaintance_death.personality_modifiers` | object | object with 2 keys |
| `acquaintance_death.personality_modifiers.E_sentimentality` | object | object with 2 keys |
| `acquaintance_death.personality_modifiers.traits` | object | object with 3 keys |
| `acquaintance_death.relationship_scaling` | object | object with 3 keys |
| `acquaintance_death.relationship_scaling.max_mult` | float | 1.0 |
| `acquaintance_death.relationship_scaling.method` | string | "bond_strength" |
| `acquaintance_death.relationship_scaling.min_mult` | float | 0.1 |
| `argument` | object | object with 11 keys |
| `argument.base_decay_rate` | float | 0.08 |
| `argument.base_instant` | float | 40.0 |
| `argument.base_per_tick` | float | 1.0 |
| `argument.category` | string | "social" |
| `argument.context_modifiers` | object | object with 3 keys |
| `argument.context_modifiers.public_argument` | float | 1.25 |
| `argument.context_modifiers.with_parent` | float | 1.15 |
| `argument.context_modifiers.with_partner` | float | 1.2 |
| `argument.emotion_inject` | object | object with 3 keys |
| `argument.emotion_inject.anger_fast` | int | 30 |
| `argument.emotion_inject.sadness_fast` | int | 10 |
| `argument.emotion_inject.trust_slow` | int | -8 |
| `argument.is_loss` | boolean | false |
| `argument.name_en` | string | "Argument" |
| `argument.name_kr` | string | "말다툼" |
| `argument.personality_modifiers` | object | object with 4 keys |
| `argument.personality_modifiers.A_axis` | object | object with 2 keys |
| `argument.personality_modifiers.A_patience` | object | object with 2 keys |
| `argument.personality_modifiers.E_anxiety` | object | object with 2 keys |
| `argument.personality_modifiers.traits` | object | object with 4 keys |
| `argument.relationship_scaling` | object | object with 3 keys |
| `argument.relationship_scaling.max_mult` | float | 1.5 |
| `argument.relationship_scaling.method` | string | "bond_strength" |
| `argument.relationship_scaling.min_mult` | float | 0.5 |
| `betrayal_discovered` | object | object with 11 keys |
| `betrayal_discovered.base_decay_rate` | float | 0.02 |
| `betrayal_discovered.base_instant` | float | 200.0 |
| `betrayal_discovered.base_per_tick` | float | 5.0 |
| `betrayal_discovered.category` | string | "social" |
| `betrayal_discovered.context_modifiers` | object | object with 2 keys |
| `betrayal_discovered.context_modifiers.by_close_friend` | float | 1.3 |
| `betrayal_discovered.context_modifiers.by_partner` | float | 1.5 |
| `betrayal_discovered.emotion_inject` | object | object with 5 keys |
| `betrayal_discovered.emotion_inject.anger_fast` | int | 60 |
| `betrayal_discovered.emotion_inject.disgust_fast` | int | 30 |
| `betrayal_discovered.emotion_inject.sadness_fast` | int | 40 |
| `betrayal_discovered.emotion_inject.surprise_fast` | int | 25 |
| `betrayal_discovered.emotion_inject.trust_slow` | int | -40 |
| `betrayal_discovered.is_loss` | boolean | true |
| `betrayal_discovered.name_en` | string | "Betrayal Discovered" |
| `betrayal_discovered.name_kr` | string | "배신 발각" |
| `betrayal_discovered.personality_modifiers` | object | object with 4 keys |
| `betrayal_discovered.personality_modifiers.A_axis` | object | object with 2 keys |
| `betrayal_discovered.personality_modifiers.E_anxiety` | object | object with 2 keys |
| `betrayal_discovered.personality_modifiers.H_sincerity` | object | object with 2 keys |
| `betrayal_discovered.personality_modifiers.traits` | object | object with 4 keys |
| `betrayal_discovered.relationship_scaling` | object | object with 3 keys |
| `betrayal_discovered.relationship_scaling.max_mult` | float | 1.8 |
| `betrayal_discovered.relationship_scaling.method` | string | "bond_strength" |
| `betrayal_discovered.relationship_scaling.min_mult` | float | 0.3 |
| `building_completed` | object | object with 11 keys |
| `building_completed.base_decay_rate` | float | 0.0 |
| `building_completed.base_instant` | float | -25.0 |
| `building_completed.base_per_tick` | float | 0.0 |
| `building_completed.category` | string | "eustress" |
| `building_completed.context_modifiers` | object | object with 1 keys |
| `building_completed.context_modifiers.first_building` | float | 1.3 |
| `building_completed.emotion_inject` | object | object with 3 keys |
| `building_completed.emotion_inject.anticipation_fast` | int | 15 |
| `building_completed.emotion_inject.joy_fast` | int | 20 |
| `building_completed.emotion_inject.trust_fast` | int | 8 |
| `building_completed.is_loss` | boolean | false |
| `building_completed.name_en` | string | "Building Completed" |
| `building_completed.name_kr` | string | "건축 완료" |
| `building_completed.personality_modifiers` | object | object with 2 keys |
| `building_completed.personality_modifiers.C_diligence` | object | object with 2 keys |
| `building_completed.personality_modifiers.traits` | object | object with 2 keys |
| `building_completed.relationship_scaling` | object | object with 1 keys |
| `building_completed.relationship_scaling.method` | string | "none" |
| `child_death` | object | object with 11 keys |
| `child_death.base_decay_rate` | float | 0.008 |
| `child_death.base_instant` | float | 550.0 |
| `child_death.base_per_tick` | float | 12.0 |
| `child_death.category` | string | "death" |
| `child_death.context_modifiers` | object | object with 6 keys |
| `child_death.context_modifiers.child_age_child` | float | 1.15 |
| `child_death.context_modifiers.child_age_infant` | float | 0.85 |
| `child_death.context_modifiers.child_age_teen` | float | 1.25 |
| `child_death.context_modifiers.child_age_toddler` | float | 1.0 |
| `child_death.context_modifiers.only_child` | float | 1.2 |
| `child_death.context_modifiers.witnessed_death` | float | 1.35 |
| `child_death.emotion_inject` | object | object with 5 keys |
| `child_death.emotion_inject.anger_fast` | int | 35 |
| `child_death.emotion_inject.fear_fast` | int | 20 |
| `child_death.emotion_inject.joy_slow` | int | -50 |
| `child_death.emotion_inject.sadness_fast` | int | 90 |
| `child_death.emotion_inject.trust_slow` | int | -20 |
| `child_death.is_loss` | boolean | true |
| `child_death.name_en` | string | "Child Death" |
| `child_death.name_kr` | string | "자녀 사망" |
| `child_death.personality_modifiers` | object | object with 4 keys |
| `child_death.personality_modifiers.A_gentleness` | object | object with 2 keys |
| `child_death.personality_modifiers.E_axis` | object | object with 2 keys |
| `child_death.personality_modifiers.E_sentimentality` | object | object with 2 keys |
| `child_death.personality_modifiers.traits` | object | object with 7 keys |
| `child_death.relationship_scaling` | object | object with 3 keys |
| `child_death.relationship_scaling.max_mult` | float | 1.4 |
| `child_death.relationship_scaling.method` | string | "bond_strength" |
| `child_death.relationship_scaling.min_mult` | float | 0.3 |
| `childbirth_father` | object | object with 11 keys |
| `childbirth_father.base_decay_rate` | float | 0.0 |
| `childbirth_father.base_instant` | float | -80.0 |
| `childbirth_father.base_per_tick` | float | 0.0 |
| `childbirth_father.category` | string | "eustress" |
| `childbirth_father.context_modifiers` | object | object with 1 keys |
| `childbirth_father.context_modifiers.first_child` | float | 1.2 |
| `childbirth_father.emotion_inject` | object | object with 3 keys |
| `childbirth_father.emotion_inject.anticipation_fast` | int | 20 |
| `childbirth_father.emotion_inject.joy_fast` | int | 50 |
| `childbirth_father.emotion_inject.trust_fast` | int | 20 |
| `childbirth_father.is_loss` | boolean | false |
| `childbirth_father.name_en` | string | "Child Born (Father)" |
| `childbirth_father.name_kr` | string | "자녀 출생 (아버지)" |
| `childbirth_father.personality_modifiers` | object | object with 2 keys |
| `childbirth_father.personality_modifiers.E_sentimentality` | object | object with 2 keys |
| `childbirth_father.personality_modifiers.traits` | object | object with 2 keys |
| `childbirth_father.relationship_scaling` | object | object with 1 keys |
| `childbirth_father.relationship_scaling.method` | string | "none" |
| `childbirth_mother` | object | object with 11 keys |
| `childbirth_mother.base_decay_rate` | float | 0.0 |
| `childbirth_mother.base_instant` | float | -120.0 |
| `childbirth_mother.base_per_tick` | float | 0.0 |
| `childbirth_mother.category` | string | "eustress" |
| `childbirth_mother.context_modifiers` | object | object with 2 keys |
| `childbirth_mother.context_modifiers.complication` | float | 0.3 |
| `childbirth_mother.context_modifiers.first_child` | float | 1.2 |
| `childbirth_mother.emotion_inject` | object | object with 4 keys |
| `childbirth_mother.emotion_inject.anticipation_fast` | int | 25 |
| `childbirth_mother.emotion_inject.fear_fast` | int | 15 |
| `childbirth_mother.emotion_inject.joy_fast` | int | 70 |
| `childbirth_mother.emotion_inject.trust_fast` | int | 30 |
| `childbirth_mother.is_loss` | boolean | false |
| `childbirth_mother.name_en` | string | "Giving Birth" |
| `childbirth_mother.name_kr` | string | "출산 (산모)" |
| `childbirth_mother.personality_modifiers` | object | object with 2 keys |
| `childbirth_mother.personality_modifiers.E_sentimentality` | object | object with 2 keys |
| `childbirth_mother.personality_modifiers.traits` | object | object with 1 keys |
| `childbirth_mother.relationship_scaling` | object | object with 1 keys |
| `childbirth_mother.relationship_scaling.method` | string | "none" |
| `close_friend_death` | object | object with 11 keys |
| `close_friend_death.base_decay_rate` | float | 0.02 |
| `close_friend_death.base_instant` | float | 200.0 |
| `close_friend_death.base_per_tick` | float | 5.0 |
| `close_friend_death.category` | string | "death" |
| `close_friend_death.context_modifiers` | object | object with 0 keys |
| `close_friend_death.emotion_inject` | object | object with 2 keys |
| `close_friend_death.emotion_inject.sadness_fast` | int | 45 |
| `close_friend_death.emotion_inject.trust_slow` | int | -10 |
| `close_friend_death.is_loss` | boolean | true |
| `close_friend_death.name_en` | string | "Close Friend Death" |
| `close_friend_death.name_kr` | string | "절친 사망" |
| `close_friend_death.personality_modifiers` | object | object with 3 keys |
| `close_friend_death.personality_modifiers.E_sentimentality` | object | object with 2 keys |
| `close_friend_death.personality_modifiers.X_sociability` | object | object with 2 keys |
| `close_friend_death.personality_modifiers.traits` | object | object with 3 keys |
| `close_friend_death.relationship_scaling` | object | object with 3 keys |
| `close_friend_death.relationship_scaling.max_mult` | float | 1.5 |
| `close_friend_death.relationship_scaling.method` | string | "bond_strength" |
| `close_friend_death.relationship_scaling.min_mult` | float | 0.2 |
| `combat_engaged` | object | object with 11 keys |
| `combat_engaged.base_decay_rate` | float | 0.12 |
| `combat_engaged.base_instant` | float | 80.0 |
| `combat_engaged.base_per_tick` | float | 15.0 |
| `combat_engaged.category` | string | "survival" |
| `combat_engaged.context_modifiers` | object | object with 2 keys |
| `combat_engaged.context_modifiers.defending_settlement` | float | 0.8 |
| `combat_engaged.context_modifiers.outnumbered` | float | 1.4 |
| `combat_engaged.emotion_inject` | object | object with 3 keys |
| `combat_engaged.emotion_inject.anger_fast` | int | 35 |
| `combat_engaged.emotion_inject.fear_fast` | int | 40 |
| `combat_engaged.emotion_inject.surprise_fast` | int | 15 |
| `combat_engaged.is_loss` | boolean | false |
| `combat_engaged.name_en` | string | "Combat Engaged" |
| `combat_engaged.name_kr` | string | "전투 참여" |
| `combat_engaged.personality_modifiers` | object | object with 2 keys |
| `combat_engaged.personality_modifiers.E_fearfulness` | object | object with 2 keys |
| `combat_engaged.personality_modifiers.traits` | object | object with 6 keys |
| `combat_engaged.relationship_scaling` | object | object with 1 keys |
| `combat_engaged.relationship_scaling.method` | string | "none" |
| `exile_banishment` | object | object with 11 keys |
| `exile_banishment.base_decay_rate` | float | 0.015 |
| `exile_banishment.base_instant` | float | 300.0 |
| `exile_banishment.base_per_tick` | float | 8.0 |
| `exile_banishment.category` | string | "social" |
| `exile_banishment.context_modifiers` | object | object with 2 keys |
| `exile_banishment.context_modifiers.family_left_behind` | float | 1.4 |
| `exile_banishment.context_modifiers.unjust_exile` | float | 1.35 |
| `exile_banishment.emotion_inject` | object | object with 4 keys |
| `exile_banishment.emotion_inject.anger_fast` | int | 45 |
| `exile_banishment.emotion_inject.fear_fast` | int | 35 |
| `exile_banishment.emotion_inject.sadness_fast` | int | 50 |
| `exile_banishment.emotion_inject.trust_slow` | int | -35 |
| `exile_banishment.is_loss` | boolean | true |
| `exile_banishment.name_en` | string | "Exile / Banishment" |
| `exile_banishment.name_kr` | string | "추방" |
| `exile_banishment.personality_modifiers` | object | object with 3 keys |
| `exile_banishment.personality_modifiers.E_dependence` | object | object with 2 keys |
| `exile_banishment.personality_modifiers.X_sociability` | object | object with 2 keys |
| `exile_banishment.personality_modifiers.traits` | object | object with 4 keys |
| `exile_banishment.relationship_scaling` | object | object with 1 keys |
| `exile_banishment.relationship_scaling.method` | string | "none" |
| `forced_action_by_god` | object | object with 11 keys |
| `forced_action_by_god.base_decay_rate` | float | 0.0 |
| `forced_action_by_god.base_instant` | float | 60.0 |
| `forced_action_by_god.base_per_tick` | float | 0.0 |
| `forced_action_by_god.category` | string | "psychological" |
| `forced_action_by_god.context_modifiers` | object | object with 2 keys |
| `forced_action_by_god.context_modifiers.against_personality` | float | 1.5 |
| `forced_action_by_god.context_modifiers.dangerous_task` | float | 1.4 |
| `forced_action_by_god.emotion_inject` | object | object with 3 keys |
| `forced_action_by_god.emotion_inject.anger_fast` | int | 25 |
| `forced_action_by_god.emotion_inject.fear_fast` | int | 15 |
| `forced_action_by_god.emotion_inject.trust_slow` | int | -10 |
| `forced_action_by_god.is_loss` | boolean | false |
| `forced_action_by_god.name_en` | string | "Forced by God Command" |
| `forced_action_by_god.name_kr` | string | "신의 강제 명령" |
| `forced_action_by_god.personality_modifiers` | object | object with 3 keys |
| `forced_action_by_god.personality_modifiers.C_axis` | object | object with 2 keys |
| `forced_action_by_god.personality_modifiers.O_unconventionality` | object | object with 2 keys |
| `forced_action_by_god.personality_modifiers.traits` | object | object with 3 keys |
| `forced_action_by_god.relationship_scaling` | object | object with 1 keys |
| `forced_action_by_god.relationship_scaling.method` | string | "none" |
| `maternal_death_partner` | object | object with 11 keys |
| `maternal_death_partner.base_decay_rate` | float | 0.008 |
| `maternal_death_partner.base_instant` | float | 500.0 |
| `maternal_death_partner.base_per_tick` | float | 12.0 |
| `maternal_death_partner.category` | string | "death" |
| `maternal_death_partner.context_modifiers` | object | object with 2 keys |
| `maternal_death_partner.context_modifiers.newborn_also_died` | float | 1.4 |
| `maternal_death_partner.context_modifiers.newborn_survived` | float | 0.9 |
| `maternal_death_partner.emotion_inject` | object | object with 5 keys |
| `maternal_death_partner.emotion_inject.anger_fast` | int | 30 |
| `maternal_death_partner.emotion_inject.fear_fast` | int | 40 |
| `maternal_death_partner.emotion_inject.joy_slow` | int | -50 |
| `maternal_death_partner.emotion_inject.sadness_fast` | int | 90 |
| `maternal_death_partner.emotion_inject.trust_slow` | int | -30 |
| `maternal_death_partner.is_loss` | boolean | true |
| `maternal_death_partner.name_en` | string | "Partner Died in Childbirth" |
| `maternal_death_partner.name_kr` | string | "출산 중 파트너 사망" |
| `maternal_death_partner.personality_modifiers` | object | object with 3 keys |
| `maternal_death_partner.personality_modifiers.E_axis` | object | object with 2 keys |
| `maternal_death_partner.personality_modifiers.E_sentimentality` | object | object with 2 keys |
| `maternal_death_partner.personality_modifiers.traits` | object | object with 3 keys |
| `maternal_death_partner.relationship_scaling` | object | object with 3 keys |
| `maternal_death_partner.relationship_scaling.max_mult` | float | 1.3 |
| `maternal_death_partner.relationship_scaling.method` | string | "bond_strength" |
| `maternal_death_partner.relationship_scaling.min_mult` | float | 0.6 |
| `overcrowding` | object | object with 11 keys |
| `overcrowding.base_decay_rate` | float | 0.06 |
| `overcrowding.base_instant` | float | 0.0 |
| `overcrowding.base_per_tick` | float | 2.0 |
| `overcrowding.category` | string | "psychological" |
| `overcrowding.context_modifiers` | object | object with 0 keys |
| `overcrowding.emotion_inject` | object | object with 2 keys |
| `overcrowding.emotion_inject.anger_fast` | int | 8 |
| `overcrowding.emotion_inject.disgust_fast` | int | 5 |
| `overcrowding.is_loss` | boolean | false |
| `overcrowding.name_en` | string | "Overcrowding" |
| `overcrowding.name_kr` | string | "과밀 스트레스" |
| `overcrowding.personality_modifiers` | object | object with 2 keys |
| `overcrowding.personality_modifiers.X_sociability` | object | object with 2 keys |
| `overcrowding.personality_modifiers.traits` | object | object with 3 keys |
| `overcrowding.relationship_scaling` | object | object with 1 keys |
| `overcrowding.relationship_scaling.method` | string | "none" |
| `parent_death` | object | object with 11 keys |
| `parent_death.base_decay_rate` | float | 0.012 |
| `parent_death.base_instant` | float | 350.0 |
| `parent_death.base_per_tick` | float | 8.0 |
| `parent_death.category` | string | "death" |
| `parent_death.context_modifiers` | object | object with 6 keys |
| `parent_death.context_modifiers.agent_is_adult` | float | 1.0 |
| `parent_death.context_modifiers.agent_is_child` | float | 1.85 |
| `parent_death.context_modifiers.agent_is_elder` | float | 0.75 |
| `parent_death.context_modifiers.agent_is_teen` | float | 1.4 |
| `parent_death.context_modifiers.last_surviving_parent` | float | 1.3 |
| `parent_death.context_modifiers.was_estranged` | float | 0.35 |
| `parent_death.emotion_inject` | object | object with 4 keys |
| `parent_death.emotion_inject.fear_fast` | int | 25 |
| `parent_death.emotion_inject.joy_slow` | int | -30 |
| `parent_death.emotion_inject.sadness_fast` | int | 70 |
| `parent_death.emotion_inject.trust_slow` | int | -15 |
| `parent_death.is_loss` | boolean | true |
| `parent_death.name_en` | string | "Parent Death" |
| `parent_death.name_kr` | string | "부모 사망" |
| `parent_death.personality_modifiers` | object | object with 4 keys |
| `parent_death.personality_modifiers.E_axis` | object | object with 2 keys |
| `parent_death.personality_modifiers.E_dependence` | object | object with 2 keys |
| `parent_death.personality_modifiers.E_sentimentality` | object | object with 2 keys |
| `parent_death.personality_modifiers.traits` | object | object with 7 keys |
| `parent_death.relationship_scaling` | object | object with 3 keys |
| `parent_death.relationship_scaling.max_mult` | float | 1.3 |
| `parent_death.relationship_scaling.method` | string | "bond_strength" |
| `parent_death.relationship_scaling.min_mult` | float | 0.4 |
| `partner_death` | object | object with 11 keys |
| `partner_death.base_decay_rate` | float | 0.01 |
| `partner_death.base_instant` | float | 450.0 |
| `partner_death.base_per_tick` | float | 10.0 |
| `partner_death.category` | string | "death" |
| `partner_death.context_modifiers` | object | object with 4 keys |
| `partner_death.context_modifiers.has_children_together` | float | 1.15 |
| `partner_death.context_modifiers.sudden_unexpected` | float | 1.2 |
| `partner_death.context_modifiers.was_estranged` | float | 0.4 |
| `partner_death.context_modifiers.witnessed_death` | float | 1.3 |
| `partner_death.emotion_inject` | object | object with 5 keys |
| `partner_death.emotion_inject.anger_fast` | int | 20 |
| `partner_death.emotion_inject.fear_fast` | int | 30 |
| `partner_death.emotion_inject.joy_slow` | int | -40 |
| `partner_death.emotion_inject.sadness_fast` | int | 80 |
| `partner_death.emotion_inject.trust_slow` | int | -25 |
| `partner_death.is_loss` | boolean | true |
| `partner_death.name_en` | string | "Partner Death" |
| `partner_death.name_kr` | string | "파트너 사망" |
| `partner_death.personality_modifiers` | object | object with 5 keys |
| `partner_death.personality_modifiers.A_axis` | object | object with 2 keys |
| `partner_death.personality_modifiers.E_axis` | object | object with 2 keys |
| `partner_death.personality_modifiers.E_dependence` | object | object with 2 keys |
| `partner_death.personality_modifiers.E_sentimentality` | object | object with 2 keys |
| `partner_death.personality_modifiers.traits` | object | object with 11 keys |
| `partner_death.relationship_scaling` | object | object with 3 keys |
| `partner_death.relationship_scaling.max_mult` | float | 1.3 |
| `partner_death.relationship_scaling.method` | string | "bond_strength" |
| `partner_death.relationship_scaling.min_mult` | float | 0.5 |
| `partnership_breakup` | object | object with 11 keys |
| `partnership_breakup.base_decay_rate` | float | 0.02 |
| `partnership_breakup.base_instant` | float | 250.0 |
| `partnership_breakup.base_per_tick` | float | 6.0 |
| `partnership_breakup.category` | string | "social" |
| `partnership_breakup.context_modifiers` | object | object with 2 keys |
| `partnership_breakup.context_modifiers.initiated_by_other` | float | 1.3 |
| `partnership_breakup.context_modifiers.initiated_by_self` | float | 0.6 |
| `partnership_breakup.emotion_inject` | object | object with 4 keys |
| `partnership_breakup.emotion_inject.anger_fast` | int | 30 |
| `partnership_breakup.emotion_inject.joy_slow` | int | -30 |
| `partnership_breakup.emotion_inject.sadness_fast` | int | 60 |
| `partnership_breakup.emotion_inject.trust_slow` | int | -25 |
| `partnership_breakup.is_loss` | boolean | true |
| `partnership_breakup.name_en` | string | "Partnership Breakup" |
| `partnership_breakup.name_kr` | string | "결별" |
| `partnership_breakup.personality_modifiers` | object | object with 3 keys |
| `partnership_breakup.personality_modifiers.E_dependence` | object | object with 2 keys |
| `partnership_breakup.personality_modifiers.E_sentimentality` | object | object with 2 keys |
| `partnership_breakup.personality_modifiers.traits` | object | object with 3 keys |
| `partnership_breakup.relationship_scaling` | object | object with 3 keys |
| `partnership_breakup.relationship_scaling.max_mult` | float | 1.4 |
| `partnership_breakup.relationship_scaling.method` | string | "bond_strength" |
| `partnership_breakup.relationship_scaling.min_mult` | float | 0.4 |
| `predator_encounter` | object | object with 11 keys |
| `predator_encounter.base_decay_rate` | float | 0.06 |
| `predator_encounter.base_instant` | float | 130.0 |
| `predator_encounter.base_per_tick` | float | 5.0 |
| `predator_encounter.category` | string | "survival" |
| `predator_encounter.context_modifiers` | object | object with 4 keys |
| `predator_encounter.context_modifiers.agent_is_child` | float | 1.8 |
| `predator_encounter.context_modifiers.alone` | float | 1.25 |
| `predator_encounter.context_modifiers.in_group` | float | 0.75 |
| `predator_encounter.context_modifiers.near_children` | float | 1.4 |
| `predator_encounter.emotion_inject` | object | object with 3 keys |
| `predator_encounter.emotion_inject.anger_fast` | int | 10 |
| `predator_encounter.emotion_inject.fear_fast` | int | 65 |
| `predator_encounter.emotion_inject.surprise_fast` | int | 30 |
| `predator_encounter.is_loss` | boolean | false |
| `predator_encounter.name_en` | string | "Predator Encounter" |
| `predator_encounter.name_kr` | string | "포식자 조우" |
| `predator_encounter.personality_modifiers` | object | object with 3 keys |
| `predator_encounter.personality_modifiers.E_anxiety` | object | object with 2 keys |
| `predator_encounter.personality_modifiers.E_fearfulness` | object | object with 2 keys |
| `predator_encounter.personality_modifiers.traits` | object | object with 4 keys |
| `predator_encounter.relationship_scaling` | object | object with 1 keys |
| `predator_encounter.relationship_scaling.method` | string | "none" |
| `rejection_social` | object | object with 11 keys |
| `rejection_social.base_decay_rate` | float | 0.04 |
| `rejection_social.base_instant` | float | 80.0 |
| `rejection_social.base_per_tick` | float | 2.0 |
| `rejection_social.category` | string | "social" |
| `rejection_social.context_modifiers` | object | object with 2 keys |
| `rejection_social.context_modifiers.public_rejection` | float | 1.3 |
| `rejection_social.context_modifiers.romantic_rejection` | float | 1.4 |
| `rejection_social.emotion_inject` | object | object with 4 keys |
| `rejection_social.emotion_inject.anger_fast` | int | 15 |
| `rejection_social.emotion_inject.fear_fast` | int | 10 |
| `rejection_social.emotion_inject.sadness_fast` | int | 35 |
| `rejection_social.emotion_inject.trust_slow` | int | -12 |
| `rejection_social.is_loss` | boolean | false |
| `rejection_social.name_en` | string | "Social Rejection" |
| `rejection_social.name_kr` | string | "사회적 거부" |
| `rejection_social.personality_modifiers` | object | object with 4 keys |
| `rejection_social.personality_modifiers.E_anxiety` | object | object with 2 keys |
| `rejection_social.personality_modifiers.E_dependence` | object | object with 2 keys |
| `rejection_social.personality_modifiers.X_social_self_esteem` | object | object with 2 keys |
| `rejection_social.personality_modifiers.traits` | object | object with 4 keys |
| `rejection_social.relationship_scaling` | object | object with 1 keys |
| `rejection_social.relationship_scaling.method` | string | "none" |
| `severe_injury` | object | object with 11 keys |
| `severe_injury.base_decay_rate` | float | 0.03 |
| `severe_injury.base_instant` | float | 150.0 |
| `severe_injury.base_per_tick` | float | 4.0 |
| `severe_injury.category` | string | "survival" |
| `severe_injury.context_modifiers` | object | object with 1 keys |
| `severe_injury.context_modifiers.permanent_disability` | float | 1.5 |
| `severe_injury.emotion_inject` | object | object with 3 keys |
| `severe_injury.emotion_inject.anger_fast` | int | 20 |
| `severe_injury.emotion_inject.fear_fast` | int | 45 |
| `severe_injury.emotion_inject.sadness_fast` | int | 25 |
| `severe_injury.is_loss` | boolean | false |
| `severe_injury.name_en` | string | "Severe Injury" |
| `severe_injury.name_kr` | string | "중상" |
| `severe_injury.personality_modifiers` | object | object with 3 keys |
| `severe_injury.personality_modifiers.E_anxiety` | object | object with 2 keys |
| `severe_injury.personality_modifiers.E_fearfulness` | object | object with 2 keys |
| `severe_injury.personality_modifiers.traits` | object | object with 4 keys |
| `severe_injury.relationship_scaling` | object | object with 1 keys |
| `severe_injury.relationship_scaling.method` | string | "none" |
| `sibling_death` | object | object with 11 keys |
| `sibling_death.base_decay_rate` | float | 0.015 |
| `sibling_death.base_instant` | float | 250.0 |
| `sibling_death.base_per_tick` | float | 6.0 |
| `sibling_death.category` | string | "death" |
| `sibling_death.context_modifiers` | object | object with 1 keys |
| `sibling_death.context_modifiers.agent_is_child` | float | 1.5 |
| `sibling_death.emotion_inject` | object | object with 3 keys |
| `sibling_death.emotion_inject.fear_fast` | int | 15 |
| `sibling_death.emotion_inject.sadness_fast` | int | 55 |
| `sibling_death.emotion_inject.trust_slow` | int | -10 |
| `sibling_death.is_loss` | boolean | true |
| `sibling_death.name_en` | string | "Sibling Death" |
| `sibling_death.name_kr` | string | "형제자매 사망" |
| `sibling_death.personality_modifiers` | object | object with 3 keys |
| `sibling_death.personality_modifiers.E_axis` | object | object with 2 keys |
| `sibling_death.personality_modifiers.E_sentimentality` | object | object with 2 keys |
| `sibling_death.personality_modifiers.traits` | object | object with 3 keys |
| `sibling_death.relationship_scaling` | object | object with 3 keys |
| `sibling_death.relationship_scaling.max_mult` | float | 1.3 |
| `sibling_death.relationship_scaling.method` | string | "bond_strength" |
| `sibling_death.relationship_scaling.min_mult` | float | 0.3 |
| `starvation_crisis` | object | object with 11 keys |
| `starvation_crisis.base_decay_rate` | float | 0.05 |
| `starvation_crisis.base_instant` | float | 100.0 |
| `starvation_crisis.base_per_tick` | float | 6.0 |
| `starvation_crisis.category` | string | "survival" |
| `starvation_crisis.context_modifiers` | object | object with 2 keys |
| `starvation_crisis.context_modifiers.has_dependents` | float | 1.35 |
| `starvation_crisis.context_modifiers.settlement_wide_famine` | float | 1.25 |
| `starvation_crisis.emotion_inject` | object | object with 3 keys |
| `starvation_crisis.emotion_inject.anger_fast` | int | 25 |
| `starvation_crisis.emotion_inject.fear_fast` | int | 40 |
| `starvation_crisis.emotion_inject.sadness_fast` | int | 15 |
| `starvation_crisis.is_loss` | boolean | false |
| `starvation_crisis.name_en` | string | "Starvation Crisis" |
| `starvation_crisis.name_kr` | string | "기아 위기" |
| `starvation_crisis.personality_modifiers` | object | object with 3 keys |
| `starvation_crisis.personality_modifiers.C_prudence` | object | object with 2 keys |
| `starvation_crisis.personality_modifiers.E_anxiety` | object | object with 2 keys |
| `starvation_crisis.personality_modifiers.traits` | object | object with 3 keys |
| `starvation_crisis.relationship_scaling` | object | object with 1 keys |
| `starvation_crisis.relationship_scaling.method` | string | "none" |
| `stillborn` | object | object with 11 keys |
| `stillborn.base_decay_rate` | float | 0.015 |
| `stillborn.base_instant` | float | 350.0 |
| `stillborn.base_per_tick` | float | 8.0 |
| `stillborn.category` | string | "death" |
| `stillborn.context_modifiers` | object | object with 1 keys |
| `stillborn.context_modifiers.first_pregnancy` | float | 1.25 |
| `stillborn.emotion_inject` | object | object with 3 keys |
| `stillborn.emotion_inject.anger_fast` | int | 20 |
| `stillborn.emotion_inject.joy_slow` | int | -40 |
| `stillborn.emotion_inject.sadness_fast` | int | 75 |
| `stillborn.is_loss` | boolean | true |
| `stillborn.name_en` | string | "Stillborn" |
| `stillborn.name_kr` | string | "사산" |
| `stillborn.personality_modifiers` | object | object with 3 keys |
| `stillborn.personality_modifiers.E_axis` | object | object with 2 keys |
| `stillborn.personality_modifiers.E_sentimentality` | object | object with 2 keys |
| `stillborn.personality_modifiers.traits` | object | object with 4 keys |
| `stillborn.relationship_scaling` | object | object with 1 keys |
| `stillborn.relationship_scaling.method` | string | "none" |
| `successful_hunt` | object | object with 11 keys |
| `successful_hunt.base_decay_rate` | float | 0.0 |
| `successful_hunt.base_instant` | float | -30.0 |
| `successful_hunt.base_per_tick` | float | 0.0 |
| `successful_hunt.category` | string | "eustress" |
| `successful_hunt.context_modifiers` | object | object with 1 keys |
| `successful_hunt.context_modifiers.during_famine` | float | 1.5 |
| `successful_hunt.emotion_inject` | object | object with 3 keys |
| `successful_hunt.emotion_inject.anticipation_fast` | int | 10 |
| `successful_hunt.emotion_inject.joy_fast` | int | 25 |
| `successful_hunt.emotion_inject.trust_fast` | int | 10 |
| `successful_hunt.is_loss` | boolean | false |
| `successful_hunt.name_en` | string | "Successful Hunt" |
| `successful_hunt.name_kr` | string | "사냥 성공" |
| `successful_hunt.personality_modifiers` | object | object with 1 keys |
| `successful_hunt.personality_modifiers.traits` | object | object with 2 keys |
| `successful_hunt.relationship_scaling` | object | object with 1 keys |
| `successful_hunt.relationship_scaling.method` | string | "none" |
| `theft_victim` | object | object with 11 keys |
| `theft_victim.base_decay_rate` | float | 0.04 |
| `theft_victim.base_instant` | float | 100.0 |
| `theft_victim.base_per_tick` | float | 2.0 |
| `theft_victim.category` | string | "social" |
| `theft_victim.context_modifiers` | object | object with 1 keys |
| `theft_victim.context_modifiers.food_stolen_while_starving` | float | 1.8 |
| `theft_victim.emotion_inject` | object | object with 3 keys |
| `theft_victim.emotion_inject.anger_fast` | int | 40 |
| `theft_victim.emotion_inject.disgust_fast` | int | 20 |
| `theft_victim.emotion_inject.trust_slow` | int | -15 |
| `theft_victim.is_loss` | boolean | true |
| `theft_victim.name_en` | string | "Theft Victim" |
| `theft_victim.name_kr` | string | "도난 피해" |
| `theft_victim.personality_modifiers` | object | object with 3 keys |
| `theft_victim.personality_modifiers.E_anxiety` | object | object with 2 keys |
| `theft_victim.personality_modifiers.H_fairness` | object | object with 2 keys |
| `theft_victim.personality_modifiers.traits` | object | object with 3 keys |
| `theft_victim.relationship_scaling` | object | object with 3 keys |
| `theft_victim.relationship_scaling.max_mult` | float | 1.5 |
| `theft_victim.relationship_scaling.method` | string | "bond_strength" |
| `theft_victim.relationship_scaling.min_mult` | float | 0.8 |

## Full Content

Large object detected: **741** total nested keys.

Top-level keys: **42**

<details>
<summary>Expand top-level preview</summary>

```json
{
  "_comment": "==========================================================",
  "_comment10": "카테고리 3: 생존/신체 (Survival & Physical)",
  "_comment11": "==========================================================",
  "_comment12": "==========================================================",
  "_comment13": "카테고리 4: 심리적 사건 (Psychological)",
  "_comment14": "==========================================================",
  "_comment15": "==========================================================",
  "_comment16": "카테고리 5: 긍정적 사건 / 유스트레스 (Eustress)",
  "_comment17": "Holmes & Rahe: 긍정 사건도 stress 유발 가능 (결혼 50점)",
  "_comment18": "=========================================================="
}
```

</details>

## Referenced By

- [`stress`](../../systems/stress.md) - references `data/stressor_events.json`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
