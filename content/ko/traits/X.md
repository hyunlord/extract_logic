---
title: "Extraversion (X) Traits"
description: "Trait breakdown for Extraversion (X)."
generated: true
source_files:
  - "extracted/trait_data.json"
  - "data/species/human/personality/trait_definitions.json"
nav_order: 13
---

# Extraversion (X) — 외향성

## Axis Overview

The **Extraversion** axis measures personality tendencies represented by the `X` axis in the HEXACO model.
**Facets**: `X_liveliness` (활기 / Liveliness), `X_sociability` (사교성 / Sociability), `X_social_boldness` (사회적 대담함 / Social Boldness), `X_social_self_esteem` (사회적 자존감 / Social Self-Esteem)

## Traits

<a id="f_confident"></a>
### Confident (자신감 있는) — `f_confident`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X_social_self_esteem` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | leadership | 1.2 | +20% leadership weight |
| Behavior | social | 1.15 | +15% social weight |
| Emotion | joy_baseline | 0.03 | -97% joy baseline |
| Emotion | shame_sensitivity | 0.85 | -15% shame sensitivity |
| Relationship | respect_gain_mult | 1.2 | +20% respect gain mult |
| Relationship | trust_gain_mult | 1.05 | +5% trust gain mult |
| Work | learning_speed_mult | 1.05 | +5% learning speed mult |
| Work | speed_mult | 1.03 | +3% speed mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.1 | +10% morale mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | violation: act_submissive | 10 | +10 stress when act_submissive |

**Amplified behaviors**: `explore`, `leadership`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `joy_baseline (0.03)`, `shame_sensitivity (0.85)`
**Violation stress triggers**: `act_submissive (+10)`

**Synergies**: [`f_bold`](#f_bold), [`c_xc_hh_competent_leader`](#c_xc_hh_competent_leader)
**Anti-synergies**: [`f_insecure`](#f_insecure)

📄 source: `extracted/trait_data.json`

---

<a id="f_insecure"></a>
### Insecure (위축된) — `f_insecure`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `X_social_self_esteem` direction `low` threshold `0.16`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | leadership | 0.75 | -25% leadership weight |
| Behavior | research | 1.05 | +5% research weight |
| Behavior | social | 0.9 | -10% social weight |
| Emotion | fear_sensitivity | 1.1 | +10% fear sensitivity |
| Emotion | shame_sensitivity | 1.3 | +30% shame sensitivity |
| Relationship | approval_seeking_mult | 1.25 | +25% approval seeking mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Work | speed_mult | 0.97 | -3% speed mult |
| Combat | flee_threshold_mult | 1.1 | +10% flee threshold mult |
| Combat | morale_mult | 0.9 | -10% morale mult |
| Stress | break_threshold_mult | 0.9 | -10% break threshold mult |
| Stress | stress_gain_mult | 1.2 | +20% stress gain mult |
| Stress | stress_recovery_mult | 0.95 | -5% stress recovery mult |
| Stress | violation: public_speech | 12 | +12 stress when public_speech |
| Stress | violation: take_lead | 10 | +10 stress when take_lead |

**Amplified behaviors**: `research`
**Suppressed behaviors**: `leadership`, `social`
**Emotion sensitivities**: `fear_sensitivity (1.1)`, `shame_sensitivity (1.3)`
**Violation stress triggers**: `public_speech (+12)`, `take_lead (+10)`

**Synergies**: [`f_shy`](#f_shy), [`c_wallflower`](#c_wallflower)
**Anti-synergies**: [`f_confident`](#f_confident)

📄 source: `extracted/trait_data.json`

---

<a id="f_bold"></a>
### Bold (대담한) — `f_bold`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X_social_boldness` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | explore | 1.15 | +15% explore weight |
| Behavior | leadership | 1.1 | +10% leadership weight |
| Behavior | negotiate | 1.2 | +20% negotiate weight |
| Behavior | social | 1.15 | +15% social weight |
| Emotion | excitement_sensitivity | 1.1 | +10% excitement sensitivity |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Relationship | conflict_mult | 1.05 | +5% conflict mult |
| Relationship | initiative_mult | 1.25 | +25% initiative mult |
| Work | quality_mult | 0.98 | -2% quality mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.2 | +20% risk taking mult |
| Stress | break_threshold_mult | 1.02 | +2% break threshold mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | violation: avoid_spotlight | 8 | +8 stress when avoid_spotlight |

**Amplified behaviors**: `explore`, `leadership`, `negotiate`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `excitement_sensitivity (1.1)`, `fear_sensitivity (0.85)`
**Violation stress triggers**: `avoid_spotlight (+8)`

**Synergies**: [`f_fearless`](E.md#f_fearless), [`c_ex_lh_daredevil`](E.md#c_ex_lh_daredevil)
**Anti-synergies**: [`f_shy`](#f_shy)

📄 source: `extracted/trait_data.json`

---

<a id="f_shy"></a>
### Shy (수줍은) — `f_shy`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `X_social_boldness` direction `low` threshold `0.16`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | leadership | 0.85 | -15% leadership weight |
| Behavior | research | 1.05 | +5% research weight |
| Behavior | social | 0.75 | -25% social weight |
| Emotion | embarrassment_sensitivity | 1.3 | +30% embarrassment sensitivity |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Relationship | conflict_avoidance_mult | 1.15 | +15% conflict avoidance mult |
| Relationship | initiative_mult | 0.7 | -30% initiative mult |
| Relationship | trust_gain_mult | 0.98 | -2% trust gain mult |
| Work | quality_mult | 1.05 | +5% quality mult |
| Work | speed_mult | 0.97 | -3% speed mult |
| Combat | flee_threshold_mult | 1.1 | +10% flee threshold mult |
| Combat | morale_mult | 0.95 | -5% morale mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | social_stress_mult | 1.3 | +30% social stress mult |
| Stress | stress_gain_mult | 1.1 | +10% stress gain mult |
| Stress | violation: approach_stranger | 12 | +12 stress when approach_stranger |
| Stress | violation: public_speech | 14 | +14 stress when public_speech |

**Amplified behaviors**: `research`
**Suppressed behaviors**: `leadership`, `social`
**Emotion sensitivities**: `embarrassment_sensitivity (1.3)`, `fear_sensitivity (1.2)`
**Violation stress triggers**: `approach_stranger (+12)`, `public_speech (+14)`

**Synergies**: [`f_insecure`](#f_insecure), [`c_wallflower`](#c_wallflower)
**Anti-synergies**: [`f_bold`](#f_bold)

📄 source: `extracted/trait_data.json`

---

<a id="f_gregarious"></a>
### Gregarious (사교적인) — `f_gregarious`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X_sociability` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | social | 1.25 | +25% social weight |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | loneliness_sensitivity | 1.2 | +20% loneliness sensitivity |
| Relationship | group_cohesion_mult | 1.2 | +20% group cohesion mult |
| Relationship | intimacy_gain_mult | 1.15 | +15% intimacy gain mult |
| Relationship | trust_gain_mult | 1.05 | +5% trust gain mult |
| Work | solo_efficiency_mult | 0.95 | -5% solo efficiency mult |
| Work | teamwork_efficiency_mult | 1.15 | +15% teamwork efficiency mult |
| Combat | morale_when_grouped_mult | 1.1 | +10% morale when grouped mult |
| Stress | isolation_stress_mult | 1.2 | +20% isolation stress mult |
| Stress | stress_gain_mult | 0.98 | -2% stress gain mult |
| Stress | stress_recovery_social_mult | 1.2 | +20% stress recovery social mult |
| Stress | violation: isolate_self | 10 | +10 stress when isolate_self |

**Amplified behaviors**: `explore`, `leadership`, `nurture`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `joy_baseline (0.02)`, `loneliness_sensitivity (1.2)`
**Violation stress triggers**: `isolate_self (+10)`

**Synergies**: [`f_forgiving`](A.md#f_forgiving), [`c_xa_hh_social_peacemaker`](#c_xa_hh_social_peacemaker)
**Anti-synergies**: [`f_solitary`](#f_solitary)

📄 source: `extracted/trait_data.json`

---

<a id="f_solitary"></a>
### Solitary (고독한) — `f_solitary`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `X_sociability` direction `low` threshold `0.14`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | social | 0.75 | -25% social weight |
| Emotion | irritability_crowd_sensitivity | 1.1 | +10% irritability crowd sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | intimacy_gain_mult | 0.85 | -15% intimacy gain mult |
| Relationship | social_energy_cost_mult | 1.15 | +15% social energy cost mult |
| Relationship | trust_gain_mult | 0.95 | -5% trust gain mult |
| Work | solo_efficiency_mult | 1.1 | +10% solo efficiency mult |
| Work | teamwork_efficiency_mult | 0.9 | -10% teamwork efficiency mult |
| Combat | skirmish_preference_mult | 1.1 | +10% skirmish preference mult |
| Stress | isolation_stress_mult | 0.85 | -15% isolation stress mult |
| Stress | social_stress_mult | 1.15 | +15% social stress mult |
| Stress | stress_gain_mult | 0.98 | -2% stress gain mult |
| Stress | violation: attend_party | 10 | +10 stress when attend_party |

**Amplified behaviors**: `craft`, `explore`, `research`
**Suppressed behaviors**: `social`
**Emotion sensitivities**: `irritability_crowd_sensitivity (1.1)`, `joy_baseline (-0.01)`
**Violation stress triggers**: `attend_party (+10)`

**Synergies**: [`c_xo_lh_solitary_scholar`](#c_xo_lh_solitary_scholar), [`c_xc_lh_silent_craftsman`](#c_xc_lh_silent_craftsman)
**Anti-synergies**: [`f_gregarious`](#f_gregarious)

📄 source: `extracted/trait_data.json`

---

<a id="f_energetic"></a>
### Energetic (활기찬) — `f_energetic`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X_liveliness` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | social | 1.1 | +10% social weight |
| Emotion | excitability_sensitivity | 1.1 | +10% excitability sensitivity |
| Emotion | joy_baseline | 0.04 | -96% joy baseline |
| Relationship | mood_contagion_positive_mult | 1.15 | +15% mood contagion positive mult |
| Relationship | trust_gain_mult | 1.02 | +2% trust gain mult |
| Work | quality_mult | 0.98 | -2% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | stamina_efficiency_mult | 0.95 | -5% stamina efficiency mult |
| Combat | aggression_mult | 1.05 | +5% aggression mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Stress | stress_gain_mult | 0.98 | -2% stress gain mult |
| Stress | stress_recovery_mult | 1.05 | +5% stress recovery mult |
| Stress | violation: stay_idle | 10 | +10 stress when stay_idle |

**Amplified behaviors**: `build`, `combat`, `explore`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `excitability_sensitivity (1.1)`, `joy_baseline (0.04)`
**Violation stress triggers**: `stay_idle (+10)`

**Synergies**: [`f_industrious`](C.md#f_industrious), [`c_labor_hero`](C.md#c_labor_hero)
**Anti-synergies**: [`f_reserved`](#f_reserved)

📄 source: `extracted/trait_data.json`

---

<a id="f_reserved"></a>
### Reserved (차분한) — `f_reserved`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `X_liveliness` direction `low` threshold `0.14`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | research | 1.05 | +5% research weight |
| Behavior | social | 0.9 | -10% social weight |
| Emotion | joy_baseline | -0.02 | -102% joy baseline |
| Emotion | sadness_baseline | 0.02 | -98% sadness baseline |
| Relationship | first_impression_mult | 0.95 | -5% first impression mult |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Work | speed_mult | 0.95 | -5% speed mult |
| Combat | aggression_mult | 0.95 | -5% aggression mult |
| Combat | flee_threshold_mult | 1 | no change |
| Stress | stress_gain_mult | 1 | no change |
| Stress | stress_recovery_mult | 0.95 | -5% stress recovery mult |
| Stress | violation: force_extroversion | 10 | +10 stress when force_extroversion |

**Amplified behaviors**: `research`
**Suppressed behaviors**: `explore`, `social`
**Emotion sensitivities**: `joy_baseline (-0.02)`, `sadness_baseline (0.02)`
**Violation stress triggers**: `force_extroversion (+10)`

**Synergies**: [`c_xo_lh_solitary_scholar`](#c_xo_lh_solitary_scholar), [`f_organized`](C.md#f_organized)
**Anti-synergies**: [`f_energetic`](#f_energetic)

📄 source: `extracted/trait_data.json`

---

<a id="c_xa_hh_social_peacemaker"></a>
### Social Peacemaker (사교적 평화주의자) — `c_xa_hh_social_peacemaker`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X` direction `high` threshold `0.75`
- Facet `A` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | teamwork_efficiency_mult | 1.1025 | +10% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Stress | stress_gain_mult | 0.931 | -7% stress gain mult |

**Amplified behaviors**: `cooperate`, `help`, `leadership`, `social`
**Suppressed behaviors**: `combat`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`f_flexible`](A.md#f_flexible), [`c_xc_hl_charming_improviser`](#c_xc_hl_charming_improviser), [`c_strategist_general`](C.md#c_strategist_general)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_xa_hl_dominating_agitator"></a>
### Dominating Agitator (대중 선동가) — `c_xa_hl_dominating_agitator`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `X` direction `high` threshold `0.75`
- Facet `A` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | teamwork_efficiency_mult | 0.9975 | -0% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Stress | stress_gain_mult | 0.98 | -2% stress gain mult |

**Amplified behaviors**: `combat`, `intimidate`, `leadership`, `revenge`, `social`
**Suppressed behaviors**: `cooperate`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_hx_hh_honest_leader`](H.md#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler), [`c_xc_hl_charming_improviser`](#c_xc_hl_charming_improviser)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_xa_lh_quiet_helper"></a>
### Quiet Helper (조용한 조력자) — `c_xa_lh_quiet_helper`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X` direction `low` threshold `0.25`
- Facet `A` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | research | 1.05 | +5% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | social | 0.8 | -20% social weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Stress | social_stress_mult | 1.1 | +10% social stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `cooperate`, `craft`, `help`, `research`
**Suppressed behaviors**: `combat`, `revenge`, `social`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `joy_baseline (-0.01)`
**Violation stress triggers**: none

**Synergies**: [`f_flexible`](A.md#f_flexible), [`c_ea_lh_volatile_bully`](E.md#c_ea_lh_volatile_bully), [`f_reserved`](#f_reserved)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_xa_ll_isolated_brawler"></a>
### Isolated Brawler (고립된 싸움꾼) — `c_xa_ll_isolated_brawler`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `X` direction `low` threshold `0.25`
- Facet `A` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | research | 1.05 | +5% research weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | social | 0.8 | -20% social weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Stress | social_stress_mult | 1.1 | +10% social stress mult |
| Stress | stress_gain_mult | 1 | no change |

**Amplified behaviors**: `combat`, `craft`, `intimidate`, `research`, `revenge`
**Suppressed behaviors**: `cooperate`, `social`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `joy_baseline (-0.01)`
**Violation stress triggers**: none

**Synergies**: [`f_reserved`](#f_reserved), [`f_insecure`](#f_insecure), [`c_xc_lh_silent_craftsman`](#c_xc_lh_silent_craftsman)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_xc_hh_competent_leader"></a>
### Competent Leader (유능한 지도자) — `c_xc_hh_competent_leader`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X` direction `high` threshold `0.75`
- Facet `C` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.265 | +26% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 1.05 | +5% trust gain mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | stress_gain_mult | 0.931 | -7% stress gain mult |

**Amplified behaviors**: `build`, `gather`, `leadership`, `plan`, `research`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_xc_hl_charming_improviser`](#c_xc_hl_charming_improviser), [`c_strategist_general`](C.md#c_strategist_general), [`f_prudent`](C.md#f_prudent)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_xc_hl_charming_improviser"></a>
### Charming Improviser (매력적인 즉흥가) — `c_xc_hl_charming_improviser`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `X` direction `high` threshold `0.75`
- Facet `C` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.9 | -10% build weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 0.9 | -10% research weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | speed_mult | 0.95 | -5% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | stress_gain_mult | 1.029 | +3% stress gain mult |

**Amplified behaviors**: `explore`, `leadership`, `social`
**Suppressed behaviors**: `build`, `plan`, `research`
**Emotion sensitivities**: `impulse_control_mult (0.9)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_hx_hh_honest_leader`](H.md#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler), [`c_strategist_general`](C.md#c_strategist_general)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_xc_lh_silent_craftsman"></a>
### Silent Craftsman (묵묵한 장인) — `c_xc_lh_silent_craftsman`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X` direction `low` threshold `0.25`
- Facet `C` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.155 | +16% research weight |
| Behavior | social | 0.8 | -20% social weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | social_stress_mult | 1.1 | +10% social stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `build`, `craft`, `gather`, `plan`, `research`
**Suppressed behaviors**: `social`
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `joy_baseline (-0.01)`
**Violation stress triggers**: none

**Synergies**: [`f_industrious`](C.md#f_industrious), [`f_reserved`](#f_reserved), [`f_insecure`](#f_insecure)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_xc_ll_apathetic_recluse"></a>
### Apathetic Recluse (무기력한 은둔자) — `c_xc_ll_apathetic_recluse`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `X` direction `low` threshold `0.25`
- Facet `C` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.9 | -10% build weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 0.945 | -5% research weight |
| Behavior | social | 0.72 | -28% social weight |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | speed_mult | 0.95 | -5% speed mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | social_stress_mult | 1.21 | +21% social stress mult |
| Stress | stress_gain_mult | 1.05 | +5% stress gain mult |

**Amplified behaviors**: `craft`, `explore`
**Suppressed behaviors**: `build`, `plan`, `research`, `social`
**Emotion sensitivities**: `impulse_control_mult (0.9)`, `joy_baseline (-0.01)`
**Violation stress triggers**: none

**Synergies**: [`f_reserved`](#f_reserved), [`f_insecure`](#f_insecure), [`c_xc_hl_charming_improviser`](#c_xc_hl_charming_improviser)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_xo_hh_charismatic_visionary"></a>
### Charismatic Visionary (카리스마 비전가) — `c_xo_hh_charismatic_visionary`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X` direction `high` threshold `0.75`
- Facet `O` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | leadership | 1.265 | +26% leadership weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 1.05 | +5% trust gain mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.98 | -2% stress gain mult |

**Amplified behaviors**: `craft`, `explore`, `leadership`, `research`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `interest_sensitivity (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_xc_hl_charming_improviser`](#c_xc_hl_charming_improviser), [`c_strategist_general`](C.md#c_strategist_general), [`c_eo_hh_sensitive_artist`](E.md#c_eo_hh_sensitive_artist)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_xo_hl_populist"></a>
### Populist (대중 정치꾼) — `c_xo_hl_populist`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `X` direction `high` threshold `0.75`
- Facet `O` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | leadership | 1.2075 | +21% leadership weight |
| Behavior | research | 0.95 | -5% research weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 0.98 | -2% stress gain mult |

**Amplified behaviors**: `build`, `leadership`, `social`
**Suppressed behaviors**: `research`
**Emotion sensitivities**: `joy_baseline (0.02)`, `novelty_fear_sensitivity (1.05)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_hx_hh_honest_leader`](H.md#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler), [`c_xc_hl_charming_improviser`](#c_xc_hl_charming_improviser)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_xo_lh_solitary_scholar"></a>
### Solitary Scholar (고독한 학자) — `c_xo_lh_solitary_scholar`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X` direction `low` threshold `0.25`
- Facet `O` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | craft | 1.1025 | +10% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | research | 1.2075 | +21% research weight |
| Behavior | social | 0.8 | -20% social weight |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | social_stress_mult | 1.1 | +10% social stress mult |

**Amplified behaviors**: `craft`, `explore`, `research`
**Suppressed behaviors**: `social`
**Emotion sensitivities**: `interest_sensitivity (1.1)`, `joy_baseline (-0.01)`
**Violation stress triggers**: none

**Synergies**: [`f_reserved`](#f_reserved), [`f_insecure`](#f_insecure), [`c_strategist_general`](C.md#c_strategist_general)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_xo_ll_wallflower"></a>
### Wallflower (벽꽃) — `c_xo_ll_wallflower`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `X` direction `low` threshold `0.25`
- Facet `O` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | research | 0.9975 | -0% research weight |
| Behavior | social | 0.72 | -28% social weight |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | social_stress_mult | 1.21 | +21% social stress mult |

**Amplified behaviors**: `build`, `craft`, `leadership`
**Suppressed behaviors**: `research`, `social`
**Emotion sensitivities**: `joy_baseline (-0.01)`, `novelty_fear_sensitivity (1.05)`
**Violation stress triggers**: none

**Synergies**: [`f_reserved`](#f_reserved), [`f_insecure`](#f_insecure), [`c_xc_lh_silent_craftsman`](#c_xc_lh_silent_craftsman)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_hermit_sage"></a>
### Hermit Sage (은둔현자) — `c_hermit_sage`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X` direction `low` threshold `0.3`
- Facet `O` direction `high` threshold `0.7`
- Facet `C` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | craft | 1.2128 | +21% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.7267 | +73% research weight |
| Behavior | social | 0.56 | -44% social weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.32 | +32% learning speed mult |
| Work | quality_mult | 1.21 | +21% quality mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | social_stress_mult | 1.32 | +32% social stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `build`, `craft`, `explore`, `gather`, `plan`, `research`
**Suppressed behaviors**: `social`
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`, `joy_baseline (-0.01)`
**Violation stress triggers**: none

**Synergies**: [`f_solitary`](#f_solitary), [`f_curious`](O.md#f_curious), [`f_organized`](C.md#f_organized)
**Anti-synergies**: [`d_histrionic`](H.md#d_histrionic)

📄 source: `extracted/trait_data.json`

---

<a id="c_polymath"></a>
### Polymath (다재다능) — `c_polymath`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X` direction `high` threshold `0.7`
- Facet `C` direction `high` threshold `0.7`
- Facet `O` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.155 | +16% build weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.3915 | +39% research weight |
| Behavior | social | 1.32 | +32% social weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.21 | +21% respect gain mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.265 | +26% learning speed mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.155 | +16% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.931 | -7% stress gain mult |

**Amplified behaviors**: `build`, `craft`, `explore`, `gather`, `leadership`, `plan`, `research`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`f_curious`](O.md#f_curious), [`f_organized`](C.md#f_organized)
**Anti-synergies**: [`f_apathetic`](O.md#f_apathetic)

📄 source: `extracted/trait_data.json`

---

<a id="c_wallflower"></a>
### Wallflower (벽꽃) — `c_wallflower`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `X` direction `low` threshold `0.3`
- Facet `E` direction `high` threshold `0.7`
- Facet `A` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | help | 1.21 | +21% help weight |
| Behavior | nurture | 1.155 | +16% nurture weight |
| Behavior | research | 1.05 | +5% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | social | 0.68 | -32% social weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | initiative_mult | 0.8 | -20% initiative mult |
| Relationship | intimacy_gain_mult | 0.99 | -1% intimacy gain mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | social_stress_mult | 1.375 | +38% social stress mult |
| Stress | stress_gain_mult | 1.0925 | +9% stress gain mult |

**Amplified behaviors**: `cooperate`, `craft`, `flee`, `help`, `nurture`, `research`
**Suppressed behaviors**: `combat`, `explore`, `revenge`, `social`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `fear_sensitivity (1.2)`, `joy_baseline (-0.01)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`f_shy`](#f_shy), [`f_sentimental`](E.md#f_sentimental)
**Anti-synergies**: [`d_histrionic`](H.md#d_histrionic)

📄 source: `extracted/trait_data.json`

---

<a id="c_born_leader"></a>
### Born Leader (타고난 지도자) — `c_born_leader`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X` direction `high` threshold `0.7`
- Facet `C` direction `high` threshold `0.7`
- Facet `E` direction `low` threshold `0.3`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.495 | +49% leadership weight |
| Behavior | plan | 1.44 | +44% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.122 | +12% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.2679 | +27% morale mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | break_threshold_mult | 1.155 | +16% break threshold mult |
| Stress | stress_gain_mult | 0.7709 | -23% stress gain mult |

**Amplified behaviors**: `build`, `combat`, `explore`, `gather`, `leadership`, `plan`, `research`, `social`
**Suppressed behaviors**: `flee`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `sadness_sensitivity (0.9)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`f_confident`](#f_confident), [`f_calm`](E.md#f_calm), [`f_prudent`](C.md#f_prudent)
**Anti-synergies**: [`f_insecure`](#f_insecure), [`f_anxious`](E.md#f_anxious)

📄 source: `extracted/trait_data.json`

---

<a id="c_trickster"></a>
### Trickster (트릭스터) — `c_trickster`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `X` direction `high` threshold `0.7`
- Facet `O` direction `high` threshold `0.7`
- Facet `H` direction `low` threshold `0.3`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.21 | +21% explore weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | negotiate | 1.15 | +15% negotiate weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.44 | +44% social weight |
| Behavior | steal | 1.43 | +43% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | humor_mult | 1.2 | +20% humor mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 0.8075 | -19% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.931 | -7% stress gain mult |
| Stress | violation: lie | 6 | +6 stress when lie |

**Amplified behaviors**: `betray`, `craft`, `explore`, `leadership`, `negotiate`, `research`, `social`, `steal`, `take_bribe`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `guilt_sensitivity (0.8)`, `interest_sensitivity (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: `lie (+6)`

**Synergies**: [`f_deceptive`](H.md#f_deceptive), [`f_creative`](O.md#f_creative)
**Anti-synergies**: [`f_sincere`](H.md#f_sincere)

📄 source: `extracted/trait_data.json`

---

<a id="c_born_merchant"></a>
### Born Merchant (타고난 상인) — `c_born_merchant`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X` direction `high` threshold `0.75`
- Facet `A_flexibility` direction `high` threshold `0.85`
- Facet `C_prudence` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | negotiate | 1.3 | +30% negotiate weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | social | 1.38 | +38% social weight |
| Behavior | trade | 1.45 | +45% trade weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | conflict_resolution_mult | 1.1 | +10% conflict resolution mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 1.1 | +10% trust gain mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | teamwork_efficiency_mult | 1.1025 | +10% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Stress | stress_gain_mult | 0.931 | -7% stress gain mult |
| Stress | violation: cheat | 14 | +14 stress when cheat |

**Amplified behaviors**: `cooperate`, `help`, `leadership`, `negotiate`, `social`, `trade`
**Suppressed behaviors**: `combat`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: `cheat (+14)`

**Synergies**: [`c_diplomat`](A.md#c_diplomat), [`c_xc_hh_competent_leader`](#c_xc_hh_competent_leader)
**Anti-synergies**: [`f_corrupt`](H.md#f_corrupt)

📄 source: `extracted/trait_data.json`

---

<a id="c_builder_foreman"></a>
### Builder Foreman (현장 반장) — `c_builder_foreman`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X` direction `high` threshold `0.75`
- Facet `C_organization` direction `high` threshold `0.85`
- Facet `A_patience` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.375 | +38% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.3225 | +32% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | error_rate_mult | 0.765 | -24% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.21 | +21% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | stress_gain_mult | 0.931 | -7% stress gain mult |

**Amplified behaviors**: `build`, `gather`, `leadership`, `plan`, `research`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_xc_hh_competent_leader`](#c_xc_hh_competent_leader), [`f_organized`](C.md#f_organized)
**Anti-synergies**: [`f_disorganized`](C.md#f_disorganized), [`f_hot_tempered`](A.md#f_hot_tempered)

📄 source: `extracted/trait_data.json`

---

<a id="c_assassin_instinct"></a>
### Assassin Instinct (암살자 기질) — `c_assassin_instinct`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `X` direction `low` threshold `0.25`
- Facet `C` direction `high` threshold `0.75`
- Facet `H_sincerity` direction `low` threshold `0.15`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | assassinate | 1.5 | +50% assassinate weight |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 1.1 | +10% combat weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.155 | +16% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 0.68 | -32% social weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.067 | +7% quality mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | ambush_propensity_mult | 1.35 | +35% ambush propensity mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | social_stress_mult | 1.1 | +10% social stress mult |
| Stress | stress_gain_mult | 0.9025 | -10% stress gain mult |
| Stress | violation: kill_innocent | 4 | +4 stress when kill_innocent |

**Amplified behaviors**: `assassinate`, `betray`, `build`, `combat`, `craft`, `gather`, `plan`, `research`, `steal`, `take_bribe`
**Suppressed behaviors**: `share`, `social`
**Emotion sensitivities**: `guilt_sensitivity (0.8)`, `impulse_control_mult (1.1)`, `joy_baseline (-0.01)`
**Violation stress triggers**: `kill_innocent (+4)`

**Synergies**: [`c_spymaster`](H.md#c_spymaster), [`d_con_artist`](H.md#d_con_artist)
**Anti-synergies**: [`c_pacifist`](A.md#c_pacifist)

📄 source: `extracted/trait_data.json`

---

<a id="c_gossip"></a>
### Gossip (가십러) — `c_gossip`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `X_sociability` direction `high` threshold `0.85`
- Facet `H_sincerity` direction `low` threshold `0.15`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.56 | +56% social weight |
| Behavior | spy | 1.1 | +10% spy weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | rumor_spread_mult | 1.35 | +35% rumor spread mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.155 | +16% trust loss mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.931 | -7% stress gain mult |

**Amplified behaviors**: `betray`, `leadership`, `social`, `spy`, `steal`, `take_bribe`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `guilt_sensitivity (0.8)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_spymaster`](H.md#c_spymaster), [`c_xo_hl_populist`](#c_xo_hl_populist)
**Anti-synergies**: [`f_sincere`](H.md#f_sincere)

📄 source: `extracted/trait_data.json`

---

<a id="c_storyteller"></a>
### Storyteller (이야기꾼) — `c_storyteller`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `X` direction `high` threshold `0.75`
- Facet `O_creativity` direction `high` threshold `0.85`
- Facet `E_sentimentality` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | entertain | 1.4 | +40% entertain weight |
| Behavior | explore | 1.045 | +4% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | social | 1.5 | +50% social weight |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | group_cohesion_mult | 1.15 | +15% group cohesion mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 1.127 | +13% stress gain mult |
| Stress | stress_recovery_social_mult | 1.15 | +15% stress recovery social mult |

**Amplified behaviors**: `craft`, `entertain`, `explore`, `flee`, `leadership`, `nurture`, `research`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `fear_sensitivity (1.2)`, `interest_sensitivity (1.1)`, `joy_baseline (0.02)`, `sadness_sensitivity (1.1)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_artist`](O.md#c_artist), [`f_energetic`](#f_energetic)
**Anti-synergies**: [`c_wallflower`](#c_wallflower)

📄 source: `extracted/trait_data.json`

---

<a id="c_agitator"></a>
### Agitator (선동가) — `c_agitator`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `X` direction `high` threshold `0.75`
- Facet `A` direction `low` threshold `0.25`
- Facet `O_unconventionality` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | incite | 1.4 | +40% incite weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | sabotage | 1.1 | +10% sabotage weight |
| Behavior | social | 1.5 | +50% social weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 1.38 | +38% conflict mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | teamwork_efficiency_mult | 0.9975 | -0% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.98 | -2% stress gain mult |

**Amplified behaviors**: `combat`, `craft`, `explore`, `incite`, `intimidate`, `leadership`, `research`, `revenge`, `sabotage`, `social`
**Suppressed behaviors**: `cooperate`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `interest_sensitivity (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_revolutionary`](O.md#c_revolutionary), [`d_backstabber`](H.md#d_backstabber)
**Anti-synergies**: [`c_peacekeeper`](H.md#c_peacekeeper), [`c_reconciler`](A.md#c_reconciler)

📄 source: `extracted/trait_data.json`

---

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
