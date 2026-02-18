---
title: "Openness to Experience (O) Traits"
description: "Trait breakdown for Openness to Experience (O)."
generated: true
source_files:
  - "extracted/trait_data.json"
  - "data/species/human/personality/trait_definitions.json"
nav_order: 16
---

# Openness to Experience (O) — 경험 개방성

## Axis Overview

The **Openness to Experience** axis measures personality tendencies represented by the `O` axis in the HEXACO model.
**Facets**: `O_aesthetic` (심미성 / Aesthetic Appreciation), `O_creativity` (창의성 / Creativity), `O_inquisitiveness` (호기심 / Inquisitiveness), `O_unconventionality` (비전통성 / Unconventionality)

## Trait Effects

<a id="f_aesthetic"></a>
### Aesthetic (심미적인) — `f_aesthetic`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `O_aesthetic_appreciation` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | craft | 1.1 | +10% craft weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | research | 1.05 | +5% research weight |
| Emotion | awe_sensitivity | 1.15 | +15% awe sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Relationship | bonding_through_art_mult | 1.15 | +15% bonding through art mult |
| Relationship | trust_gain_mult | 1 | no change |
| Work | creativity_mult | 1.05 | +5% creativity mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Combat | morale_mult | 1.02 | +2% morale mult |
| Stress | stress_gain_mult | 0.98 | -2% stress gain mult |
| Stress | stress_recovery_art_mult | 1.1 | +10% stress recovery art mult |
| Stress | violation: destroy_art | 12 | +12 stress when destroy_art |

**Amplified behaviors**: `build`, `craft`, `explore`, `research`
**Suppressed behaviors**: none
**Emotion sensitivities**: `awe_sensitivity (1.15)`, `joy_baseline (0.02)`
**Violation stress triggers**: `destroy_art (+12)`

**Synergies**: [`f_creative`](#f_creative), [`c_artist`](#c_artist)
**Anti-synergies**: [`f_utilitarian`](#f_utilitarian)

📄 source: `extracted/trait_data.json`

---

<a id="f_utilitarian"></a>
### Utilitarian (실용적인) — `f_utilitarian`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `O_aesthetic_appreciation` direction `low` threshold `0.14`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | research | 0.98 | -2% research weight |
| Emotion | awe_sensitivity | 0.9 | -10% awe sensitivity |
| Relationship | pragmatic_reliability_mult | 1.05 | +5% pragmatic reliability mult |
| Work | quality_mult | 0.98 | -2% quality mult |
| Work | speed_mult | 1.05 | +5% speed mult |
| Combat | tactic_planning_mult | 1.05 | +5% tactic planning mult |
| Stress | stress_gain_mult | 0.98 | -2% stress gain mult |
| Stress | stress_recovery_routine_mult | 1.05 | +5% stress recovery routine mult |
| Stress | violation: waste_time_on_beauty | 10 | +10 stress when waste_time_on_beauty |

**Amplified behaviors**: `build`, `craft`
**Suppressed behaviors**: `research`
**Emotion sensitivities**: `awe_sensitivity (0.9)`
**Violation stress triggers**: `waste_time_on_beauty (+10)`

**Synergies**: [`c_pragmatist`](#c_pragmatist), [`c_co_hl_conservative_manager`](C.md#c_co_hl_conservative_manager)
**Anti-synergies**: [`f_aesthetic`](#f_aesthetic)

📄 source: `extracted/trait_data.json`

---

<a id="f_curious"></a>
### Curious (호기심 많은) — `f_curious`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `O_inquisitiveness` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | explore | 1.15 | +15% explore weight |
| Behavior | gather | 1 | no change |
| Behavior | research | 1.25 | +25% research weight |
| Behavior | social | 1 | no change |
| Emotion | boredom_sensitivity | 1.2 | +20% boredom sensitivity |
| Emotion | interest_sensitivity | 1.25 | +25% interest sensitivity |
| Relationship | info_sharing_mult | 1.1 | +10% info sharing mult |
| Work | learning_speed_mult | 1.2 | +20% learning speed mult |
| Work | quality_mult | 1.05 | +5% quality mult |
| Work | research_speed_mult | 1.1 | +10% research speed mult |
| Combat | tactic_adapt_mult | 1.05 | +5% tactic adapt mult |
| Stress | stress_gain_mult | 0.98 | -2% stress gain mult |
| Stress | uncertainty_stress_mult | 0.9 | -10% uncertainty stress mult |
| Stress | violation: avoid_learning | 10 | +10 stress when avoid_learning |

**Amplified behaviors**: `explore`, `research`
**Suppressed behaviors**: none
**Emotion sensitivities**: `boredom_sensitivity (1.2)`, `interest_sensitivity (1.25)`
**Violation stress triggers**: `avoid_learning (+10)`

**Synergies**: [`f_creative`](#f_creative), [`c_inventor`](#c_inventor), [`c_encyclopedia`](#c_encyclopedia)
**Anti-synergies**: [`f_apathetic`](#f_apathetic)

📄 source: `extracted/trait_data.json`

---

<a id="f_apathetic"></a>
### Apathetic (무관심한) — `f_apathetic`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `O_inquisitiveness` direction `low` threshold `0.16`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | explore | 0.9 | -10% explore weight |
| Behavior | gather | 1.05 | +5% gather weight |
| Behavior | research | 0.8 | -20% research weight |
| Emotion | boredom_sensitivity | 1.2 | +20% boredom sensitivity |
| Emotion | interest_sensitivity | 0.75 | -25% interest sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | conversation_engagement_mult | 0.85 | -15% conversation engagement mult |
| Work | learning_speed_mult | 0.85 | -15% learning speed mult |
| Work | quality_mult | 0.98 | -2% quality mult |
| Work | speed_mult | 1 | no change |
| Combat | tactic_planning_mult | 0.95 | -5% tactic planning mult |
| Stress | change_stress_mult | 1.1 | +10% change stress mult |
| Stress | stress_gain_mult | 1 | no change |
| Stress | violation: study | 10 | +10 stress when study |

**Amplified behaviors**: `build`, `gather`
**Suppressed behaviors**: `explore`, `research`
**Emotion sensitivities**: `boredom_sensitivity (1.2)`, `interest_sensitivity (0.75)`, `joy_baseline (-0.01)`
**Violation stress triggers**: `study (+10)`

**Synergies**: [`c_settler`](C.md#c_settler)
**Anti-synergies**: [`f_curious`](#f_curious), [`c_inventor`](#c_inventor), [`c_visionary`](#c_visionary)

📄 source: `extracted/trait_data.json`

---

<a id="f_creative"></a>
### Creative (창의적인) — `f_creative`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `O_creativity` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | social | 1.05 | +5% social weight |
| Emotion | constraint_frustration_sensitivity | 1.2 | +20% constraint frustration sensitivity |
| Emotion | joy_creation_sensitivity | 1.15 | +15% joy creation sensitivity |
| Relationship | inspire_others_mult | 1.15 | +15% inspire others mult |
| Work | creativity_mult | 1.25 | +25% creativity mult |
| Work | problem_solving_mult | 1.15 | +15% problem solving mult |
| Work | quality_mult | 1.05 | +5% quality mult |
| Work | speed_mult | 1 | no change |
| Combat | tactic_improv_mult | 1.2 | +20% tactic improv mult |
| Stress | stress_gain_mult | 1.02 | +2% stress gain mult |
| Stress | stress_recovery_creative_mult | 1.05 | +5% stress recovery creative mult |
| Stress | violation: follow_strict_rules | 12 | +12 stress when follow_strict_rules |

**Amplified behaviors**: `build`, `explore`, `research`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `constraint_frustration_sensitivity (1.2)`, `joy_creation_sensitivity (1.15)`
**Violation stress triggers**: `follow_strict_rules (+12)`

**Synergies**: [`f_curious`](#f_curious), [`c_inventor`](#c_inventor), [`c_co_lh_free_spirit`](C.md#c_co_lh_free_spirit), [`c_visionary`](#c_visionary)
**Anti-synergies**: [`f_conventional`](#f_conventional)

📄 source: `extracted/trait_data.json`

---

<a id="f_conventional"></a>
### Conventional (평범한) — `f_conventional`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `O_creativity` direction `low` threshold `0.14`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | research | 0.9 | -10% research weight |
| Emotion | novelty_anxiety_sensitivity | 1.1 | +10% novelty anxiety sensitivity |
| Relationship | reliability_mult | 1.05 | +5% reliability mult |
| Work | creativity_mult | 0.85 | -15% creativity mult |
| Work | quality_mult | 1 | no change |
| Work | speed_mult | 1.05 | +5% speed mult |
| Combat | tactic_improv_mult | 0.85 | -15% tactic improv mult |
| Combat | tactic_planning_mult | 1.05 | +5% tactic planning mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 1 | no change |
| Stress | violation: try_new_method | 10 | +10 stress when try_new_method |

**Amplified behaviors**: `build`
**Suppressed behaviors**: `explore`, `research`
**Emotion sensitivities**: `novelty_anxiety_sensitivity (1.1)`
**Violation stress triggers**: `try_new_method (+10)`

**Synergies**: [`c_settler`](C.md#c_settler), [`c_co_hl_conservative_manager`](C.md#c_co_hl_conservative_manager)
**Anti-synergies**: [`f_creative`](#f_creative), [`c_co_lh_free_spirit`](C.md#c_co_lh_free_spirit)

📄 source: `extracted/trait_data.json`

---

<a id="f_nonconformist"></a>
### Nonconformist (비순응적) — `f_nonconformist`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `O_unconventionality` direction `high` threshold `0.94`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | explore | 1.15 | +15% explore weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | social | 1.05 | +5% social weight |
| Emotion | constraint_anger_sensitivity | 1.15 | +15% constraint anger sensitivity |
| Relationship | norm_breaking_tolerance_mult | 1.2 | +20% norm breaking tolerance mult |
| Relationship | outgroup_bonding_mult | 1.1 | +10% outgroup bonding mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | organization_mult | 0.95 | -5% organization mult |
| Combat | unconventional_tactics_mult | 1.15 | +15% unconventional tactics mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | rule_stress_mult | 1.3 | +30% rule stress mult |
| Stress | violation: obey_blindly | 12 | +12 stress when obey_blindly |

**Amplified behaviors**: `explore`, `research`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `constraint_anger_sensitivity (1.15)`
**Violation stress triggers**: `obey_blindly (+12)`

**Synergies**: [`f_creative`](#f_creative), [`c_revolutionary`](#c_revolutionary), [`c_heretic`](#c_heretic)
**Anti-synergies**: [`f_traditionalist`](#f_traditionalist)

📄 source: `extracted/trait_data.json`

---

<a id="f_traditionalist"></a>
### Traditionalist (보수적인) — `f_traditionalist`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `O_unconventionality` direction `low` threshold `0.12`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | research | 0.95 | -5% research weight |
| Behavior | social | 1.05 | +5% social weight |
| Emotion | novelty_fear_sensitivity | 1.15 | +15% novelty fear sensitivity |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | outgroup_suspicion_mult | 1.1 | +10% outgroup suspicion mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | organization_mult | 1.05 | +5% organization mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | risk_taking_mult | 0.95 | -5% risk taking mult |
| Stress | change_stress_mult | 1.2 | +20% change stress mult |
| Stress | stress_recovery_routine_mult | 1.1 | +10% stress recovery routine mult |
| Stress | violation: break_tradition | 12 | +12 stress when break_tradition |

**Amplified behaviors**: `build`, `leadership`, `social`
**Suppressed behaviors**: `research`
**Emotion sensitivities**: `novelty_fear_sensitivity (1.15)`
**Violation stress triggers**: `break_tradition (+12)`

**Synergies**: [`c_co_hl_conservative_manager`](C.md#c_co_hl_conservative_manager), [`c_settler`](C.md#c_settler), [`c_zealot`](C.md#c_zealot)
**Anti-synergies**: [`f_nonconformist`](#f_nonconformist)

📄 source: `extracted/trait_data.json`

---

<a id="c_visionary"></a>
### Visionary (선각자) — `c_visionary`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `O` direction `high` threshold `0.7`
- Facet `X` direction `high` threshold `0.7`
- Facet `C` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.265 | +26% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.265 | +26% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.5812 | +58% research weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | inspire_others_mult | 1.25 | +25% inspire others mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | creativity_mult | 1.3225 | +32% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.32 | +32% learning speed mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
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

**Synergies**: [`f_curious`](#f_curious), [`f_creative`](#f_creative)
**Anti-synergies**: [`f_apathetic`](#f_apathetic)

📄 source: `extracted/trait_data.json`

---

<a id="c_free_spirit_extro"></a>
### Free Spirit (자유영혼(사교형)) — `c_free_spirit_extro`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `O` direction `high` threshold `0.7`
- Facet `C` direction `low` threshold `0.3`
- Facet `X` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.81 | -19% build weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.4438 | +44% explore weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 1.035 | +3% research weight |
| Behavior | social | 1.32 | +32% social weight |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | creativity_mult | 1.38 | +38% creativity mult |
| Work | error_rate_mult | 1.32 | +32% error rate mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | speed_mult | 0.95 | -5% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | rule_stress_mult | 1.3 | +30% rule stress mult |
| Stress | stress_gain_mult | 1.029 | +3% stress gain mult |

**Amplified behaviors**: `craft`, `explore`, `leadership`, `research`, `social`
**Suppressed behaviors**: `build`, `plan`
**Emotion sensitivities**: `impulse_control_mult (0.9)`, `interest_sensitivity (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`f_nonconformist`](#f_nonconformist), [`f_energetic`](X.md#f_energetic)
**Anti-synergies**: [`f_organized`](C.md#f_organized)

📄 source: `extracted/trait_data.json`

---

<a id="c_scientist"></a>
### Scientist (과학자) — `c_scientist`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `O` direction `high` threshold `0.7`
- Facet `C` direction `high` threshold `0.7`
- Facet `X` direction `low` threshold `0.3`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | craft | 1.1025 | +10% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.7931 | +79% research weight |
| Behavior | social | 0.64 | -36% social weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.375 | +38% learning speed mult |
| Work | quality_mult | 1.21 | +21% quality mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | social_stress_mult | 1.265 | +26% social stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `build`, `craft`, `explore`, `gather`, `plan`, `research`
**Suppressed behaviors**: `social`
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`, `joy_baseline (-0.01)`
**Violation stress triggers**: none

**Synergies**: [`f_curious`](#f_curious), [`f_organized`](C.md#f_organized)
**Anti-synergies**: [`f_apathetic`](#f_apathetic)

📄 source: `extracted/trait_data.json`

---

<a id="c_revolutionary"></a>
### Revolutionary (혁명가) — `c_revolutionary`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `O` direction `high` threshold `0.7`
- Facet `X` direction `high` threshold `0.7`
- Facet `A` direction `low` threshold `0.3`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | leadership | 1.3225 | +32% leadership weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | sabotage | 1.15 | +15% sabotage weight |
| Behavior | social | 1.44 | +44% social weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 1.32 | +32% conflict mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | outgroup_bonding_mult | 1.15 | +15% outgroup bonding mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | teamwork_efficiency_mult | 0.9975 | -0% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | rule_stress_mult | 1.25 | +25% rule stress mult |
| Stress | stress_gain_mult | 0.98 | -2% stress gain mult |

**Amplified behaviors**: `combat`, `craft`, `explore`, `intimidate`, `leadership`, `research`, `revenge`, `sabotage`, `social`
**Suppressed behaviors**: `cooperate`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `interest_sensitivity (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`f_nonconformist`](#f_nonconformist), [`c_xa_hl_dominating_agitator`](X.md#c_xa_hl_dominating_agitator)
**Anti-synergies**: [`c_co_hl_conservative_manager`](C.md#c_co_hl_conservative_manager), [`f_traditionalist`](#f_traditionalist)

📄 source: `extracted/trait_data.json`

---

<a id="c_artist"></a>
### Artist (예술가) — `c_artist`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `O` direction `high` threshold `0.7`
- Facet `E` direction `high` threshold `0.7`
- Facet `X` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | craft | 1.155 | +16% craft weight |
| Behavior | explore | 1.2017 | +20% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | social | 1.44 | +44% social weight |
| Emotion | awe_sensitivity | 1.2 | +20% awe sensitivity |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | sadness_sensitivity | 1.21 | +21% sadness sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | bonding_through_art_mult | 1.25 | +25% bonding through art mult |
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

**Amplified behaviors**: `craft`, `explore`, `flee`, `leadership`, `nurture`, `research`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `awe_sensitivity (1.2)`, `fear_sensitivity (1.2)`, `interest_sensitivity (1.1)`, `joy_baseline (0.02)`, `sadness_sensitivity (1.21)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`f_aesthetic`](#f_aesthetic), [`f_energetic`](X.md#f_energetic)
**Anti-synergies**: [`f_utilitarian`](#f_utilitarian)

📄 source: `extracted/trait_data.json`

---

<a id="c_collector"></a>
### Collector (수집가) — `c_collector`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `O_aesthetic_appreciation` direction `high` threshold `0.85`
- Facet `C_organization` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | collect | 1.4 | +40% collect weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | hoard | 1.1 | +10% hoard weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.265 | +26% research weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 1.155 | +16% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | violation: destroy_valuable | 14 | +14 stress when destroy_valuable |

**Amplified behaviors**: `build`, `collect`, `craft`, `explore`, `gather`, `hoard`, `plan`, `research`
**Suppressed behaviors**: none
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: `destroy_valuable (+14)`

**Synergies**: [`c_artist`](#c_artist), [`f_aesthetic`](#f_aesthetic)
**Anti-synergies**: [`c_co_ll_careless_waster`](C.md#c_co_ll_careless_waster)

📄 source: `extracted/trait_data.json`

---

<a id="c_engineer"></a>
### Engineer (기술자) — `c_engineer`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `O_inquisitiveness` direction `high` threshold `0.85`
- Facet `C_prudence` direction `high` threshold `0.85`
- Facet `A_flexibility` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.21 | +21% build weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | repair | 1.25 | +25% repair weight |
| Behavior | research | 1.5812 | +58% research weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.765 | -24% error rate mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | problem_solving_mult | 1.2 | +20% problem solving mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `build`, `craft`, `explore`, `gather`, `plan`, `repair`, `research`
**Suppressed behaviors**: none
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_co_hh_methodical_inventor`](C.md#c_co_hh_methodical_inventor), [`c_scientist`](#c_scientist)
**Anti-synergies**: [`f_apathetic`](#f_apathetic)

📄 source: `extracted/trait_data.json`

---

<a id="c_chef"></a>
### Chef (요리사 기질) — `c_chef`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `O_aesthetic_appreciation` direction `high` threshold `0.85`
- Facet `A_gentleness` direction `high` threshold `0.85`
- Facet `C_perfectionism` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cook | 1.4 | +40% cook weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.05 | +5% gather weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | bonding_through_food_mult | 1.2 | +20% bonding through food mult |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 1.15 | +15% quality mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `cook`, `cooperate`, `craft`, `explore`, `gather`, `help`, `research`
**Suppressed behaviors**: `combat`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_caregiver`](E.md#c_caregiver), [`c_artist`](#c_artist)
**Anti-synergies**: [`f_careless`](C.md#f_careless)

📄 source: `extracted/trait_data.json`

---

<a id="c_mystic"></a>
### Mystic (신비주의자) — `c_mystic`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `O_unconventionality` direction `high` threshold `0.85`
- Facet `E_sentimentality` direction `high` threshold `0.85`
- Facet `X` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.045 | +4% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | research | 1.0925 | +9% research weight |
| Behavior | ritual | 1.4 | +40% ritual weight |
| Behavior | social | 1.32 | +32% social weight |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | influence_mult | 1.15 | +15% influence mult |
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

**Amplified behaviors**: `craft`, `explore`, `flee`, `leadership`, `nurture`, `research`, `ritual`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `fear_sensitivity (1.2)`, `interest_sensitivity (1.1)`, `joy_baseline (0.02)`, `sadness_sensitivity (1.1)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_zealot`](C.md#c_zealot), [`c_storyteller`](X.md#c_storyteller)
**Anti-synergies**: [`c_scientist`](#c_scientist), [`c_skeptic`](#c_skeptic)

📄 source: `extracted/trait_data.json`

---

<a id="c_skeptic"></a>
### Skeptic (회의론자) — `c_skeptic`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `O_inquisitiveness` direction `high` threshold `0.85`
- Facet `A_flexibility` direction `high` threshold `0.85`
- Facet `H_sincerity` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | debate | 1.25 | +25% debate weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | help | 1.21 | +21% help weight |
| Behavior | research | 1.38 | +38% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | outgroup_bonding_mult | 1.1 | +10% outgroup bonding mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.969 | -3% stress gain mult |
| Stress | violation: accept_dogma | 12 | +12 stress when accept_dogma |

**Amplified behaviors**: `cooperate`, `craft`, `debate`, `explore`, `help`, `research`, `share`
**Suppressed behaviors**: `betray`, `combat`, `revenge`, `steal`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `guilt_sensitivity (1.15)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: `accept_dogma (+12)`

**Synergies**: [`c_scientist`](#c_scientist), [`c_engineer`](#c_engineer)
**Anti-synergies**: [`c_zealot`](C.md#c_zealot), [`c_mystic`](#c_mystic)

📄 source: `extracted/trait_data.json`

---

<a id="c_pragmatist"></a>
### Pragmatist (실용주의자) — `c_pragmatist`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `O` direction `low` threshold `0.25`
- Facet `C` direction `high` threshold `0.75`
- Facet `E` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.2705 | +27% build weight |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | plan | 1.44 | +44% plan weight |
| Behavior | research | 0.9927 | -1% research weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1781 | +18% speed mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 0.855 | -15% stress gain mult |

**Amplified behaviors**: `build`, `combat`, `explore`, `gather`, `leadership`, `plan`
**Suppressed behaviors**: `flee`, `research`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `impulse_control_mult (1.1)`, `novelty_fear_sensitivity (1.05)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_co_hl_conservative_manager`](C.md#c_co_hl_conservative_manager), [`c_defender`](C.md#c_defender)
**Anti-synergies**: [`c_free_spirit_extro`](#c_free_spirit_extro), [`c_artist`](#c_artist)

📄 source: `extracted/trait_data.json`

---

<a id="c_nomad"></a>
### Nomad (떠돌이) — `c_nomad`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `O` direction `high` threshold `0.75`
- Facet `C` direction `low` threshold `0.25`
- Facet `E` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.765 | -24% build weight |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.7152 | +72% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | gather | 1.05 | +5% gather weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 1.035 | +3% research weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | speed_mult | 0.969 | -3% speed mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | boredom_stress_mult | 1.25 | +25% boredom stress mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.945 | -5% stress gain mult |

**Amplified behaviors**: `combat`, `craft`, `explore`, `gather`, `research`
**Suppressed behaviors**: `build`, `flee`, `plan`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `impulse_control_mult (0.9)`, `interest_sensitivity (1.1)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_adventurer`](E.md#c_adventurer), [`c_free_spirit_extro`](#c_free_spirit_extro)
**Anti-synergies**: [`c_settler`](C.md#c_settler)

📄 source: `extracted/trait_data.json`

---

<a id="c_scholar_scribe"></a>
### Scribe (서기관) — `c_scholar_scribe`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `O_inquisitiveness` direction `high` threshold `0.85`
- Facet `C_organization` direction `high` threshold `0.85`
- Facet `X` direction `low` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | craft | 1.1025 | +10% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | record | 1.4 | +40% record weight |
| Behavior | research | 1.5939 | +59% research weight |
| Behavior | social | 0.8 | -20% social weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 1.21 | +21% quality mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | social_stress_mult | 1.1 | +10% social stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `build`, `craft`, `explore`, `gather`, `plan`, `record`, `research`
**Suppressed behaviors**: `social`
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`, `joy_baseline (-0.01)`
**Violation stress triggers**: none

**Synergies**: [`c_scientist`](#c_scientist), [`c_hermit_sage`](X.md#c_hermit_sage)
**Anti-synergies**: [`c_gossip`](X.md#c_gossip)

📄 source: `extracted/trait_data.json`

---

<a id="c_inventor"></a>
### Inventor (발명가) — `c_inventor`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `O_creativity` direction `high` threshold `0.85`
- Facet `O_inquisitiveness` direction `high` threshold `0.85`
- Facet `C` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.155 | +16% build weight |
| Behavior | craft | 1.2075 | +21% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.7077 | +71% research weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | creativity_mult | 1.495 | +49% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.21 | +21% learning speed mult |
| Work | problem_solving_mult | 1.2 | +20% problem solving mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | violation: obey_blindly | 12 | +12 stress when obey_blindly |

**Amplified behaviors**: `build`, `craft`, `explore`, `gather`, `plan`, `research`
**Suppressed behaviors**: none
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: `obey_blindly (+12)`

**Synergies**: [`c_co_hh_methodical_inventor`](C.md#c_co_hh_methodical_inventor), [`c_scientist`](#c_scientist), [`f_creative`](#f_creative)
**Anti-synergies**: [`f_apathetic`](#f_apathetic), [`f_conventional`](#f_conventional)

📄 source: `extracted/trait_data.json`

---

<a id="c_encyclopedia"></a>
### Encyclopedia (백과사전) — `c_encyclopedia`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `O_inquisitiveness` direction `high` threshold `0.85`
- Facet `C_organization` direction `high` threshold `0.85`
- Facet `X` direction `low` threshold `0.3`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | craft | 1.1025 | +10% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | record | 1.3 | +30% record weight |
| Behavior | research | 1.6603 | +66% research weight |
| Behavior | social | 0.8 | -20% social weight |
| Behavior | teach | 1.2 | +20% teach weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.265 | +26% learning speed mult |
| Work | quality_mult | 1.155 | +16% quality mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | social_stress_mult | 1.1 | +10% social stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `build`, `craft`, `explore`, `gather`, `plan`, `record`, `research`, `teach`
**Suppressed behaviors**: `social`
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`, `joy_baseline (-0.01)`
**Violation stress triggers**: none

**Synergies**: [`c_scholar_scribe`](#c_scholar_scribe), [`c_scientist`](#c_scientist)
**Anti-synergies**: [`c_gossip`](X.md#c_gossip)

📄 source: `extracted/trait_data.json`

---

<a id="c_heretic"></a>
### Heretic (이단자) — `c_heretic`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `O_unconventionality` direction `high` threshold `0.85`
- Facet `H` direction `high` threshold `0.7`
- Facet `O` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | debate | 1.3 | +30% debate weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | incite | 1.05 | +5% incite weight |
| Behavior | research | 1.265 | +26% research weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | ingroup_trust_mult | 0.95 | -5% ingroup trust mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | outgroup_bonding_mult | 1.15 | +15% outgroup bonding mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | rule_stress_mult | 1.15 | +15% rule stress mult |
| Stress | stress_gain_mult | 1.02 | +2% stress gain mult |

**Amplified behaviors**: `craft`, `debate`, `explore`, `help`, `incite`, `research`, `share`
**Suppressed behaviors**: `betray`, `steal`
**Emotion sensitivities**: `guilt_sensitivity (1.15)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_revolutionary`](#c_revolutionary), [`c_skeptic`](#c_skeptic)
**Anti-synergies**: [`c_zealot`](C.md#c_zealot), [`d_cult_leader`](H.md#d_cult_leader)

📄 source: `extracted/trait_data.json`

---

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
