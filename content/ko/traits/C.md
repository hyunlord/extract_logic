---
title: "Conscientiousness (C) Traits"
description: "Trait breakdown for Conscientiousness (C)."
generated: true
source_files:
  - "extracted/trait_data.json"
  - "data/species/human/personality/trait_definitions.json"
nav_order: 15
---

# Conscientiousness (C) — 성실성

## Axis Overview

The **Conscientiousness** axis measures personality tendencies represented by the `C` axis in the HEXACO model.
**Facets**: `C_diligence` (근면 / Diligence), `C_organization` (조직화 / Organization), `C_perfectionism` (완벽주의 / Perfectionism), `C_prudence` (신중 / Prudence)

## Traits

<a id="f_organized"></a>
### Organized (정리정돈) — `f_organized`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `C_organization` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | gather | 1.05 | +5% gather weight |
| Behavior | plan | 1.15 | +15% plan weight |
| Behavior | research | 1.05 | +5% research weight |
| Emotion | orderliness_satisfaction | 1.1 | +10% orderliness satisfaction |
| Relationship | reliability_mult | 1.2 | +20% reliability mult |
| Relationship | trust_gain_mult | 1.1 | +10% trust gain mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.05 | +5% quality mult |
| Work | speed_mult | 1.05 | +5% speed mult |
| Combat | supply_management_mult | 1.15 | +15% supply management mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | stress_gain_mult | 0.9 | -10% stress gain mult |
| Stress | stress_recovery_mult | 1.05 | +5% stress recovery mult |
| Stress | violation: act_chaotic | 10 | +10 stress when act_chaotic |

**Amplified behaviors**: `build`, `gather`, `plan`, `research`
**Suppressed behaviors**: none
**Emotion sensitivities**: `orderliness_satisfaction (1.1)`
**Violation stress triggers**: `act_chaotic (+10)`

**Synergies**: [`f_prudent`](#f_prudent), [`c_co_hl_conservative_manager`](#c_co_hl_conservative_manager), [`c_co_hh_methodical_inventor`](#c_co_hh_methodical_inventor)
**Anti-synergies**: [`f_disorganized`](#f_disorganized)

📄 source: `extracted/trait_data.json`

---

<a id="f_disorganized"></a>
### Disorganized (산만한) — `f_disorganized`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `C_organization` direction `low` threshold `0.16`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.95 | -5% build weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | plan | 0.8 | -20% plan weight |
| Emotion | frustration_sensitivity | 1.1 | +10% frustration sensitivity |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Relationship | trust_gain_mult | 0.95 | -5% trust gain mult |
| Relationship | trust_loss_mult | 1.05 | +5% trust loss mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.92 | -8% quality mult |
| Work | speed_mult | 0.95 | -5% speed mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.1 | +10% stress gain mult |
| Stress | violation: follow_schedule | 10 | +10 stress when follow_schedule |

**Amplified behaviors**: `explore`
**Suppressed behaviors**: `build`, `plan`
**Emotion sensitivities**: `frustration_sensitivity (1.1)`
**Violation stress triggers**: `follow_schedule (+10)`

**Synergies**: [`c_xc_hl_charming_improviser`](X.md#c_xc_hl_charming_improviser)
**Anti-synergies**: [`f_organized`](#f_organized), [`c_co_hh_methodical_inventor`](#c_co_hh_methodical_inventor)

📄 source: `extracted/trait_data.json`

---

<a id="f_industrious"></a>
### Industrious (근면한) — `f_industrious`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `C_diligence` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.2 | +20% build weight |
| Behavior | gather | 1.15 | +15% gather weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | rest | 0.85 | -15% rest weight |
| Emotion | guilt_idle_sensitivity | 1.1 | +10% guilt idle sensitivity |
| Emotion | pride_baseline | 0.02 | -98% pride baseline |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 1.05 | +5% trust gain mult |
| Work | quality_mult | 1.05 | +5% quality mult |
| Work | speed_mult | 1.15 | +15% speed mult |
| Work | stamina_efficiency_mult | 0.95 | -5% stamina efficiency mult |
| Combat | endurance_mult | 1.1 | +10% endurance mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Stress | stress_gain_mult | 1.05 | +5% stress gain mult |
| Stress | stress_recovery_mult | 0.95 | -5% stress recovery mult |
| Stress | violation: idle | 12 | +12 stress when idle |

**Amplified behaviors**: `build`, `gather`, `research`
**Suppressed behaviors**: `rest`
**Emotion sensitivities**: `guilt_idle_sensitivity (1.1)`, `pride_baseline (0.02)`
**Violation stress triggers**: `idle (+12)`

**Synergies**: [`f_perfectionist`](#f_perfectionist), [`f_organized`](#f_organized), [`c_labor_hero`](#c_labor_hero)
**Anti-synergies**: [`f_lazy`](#f_lazy)

📄 source: `extracted/trait_data.json`

---

<a id="f_lazy"></a>
### Lazy (게으른) — `f_lazy`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `C_diligence` direction `low` threshold `0.16`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.85 | -15% build weight |
| Behavior | gather | 0.85 | -15% gather weight |
| Behavior | research | 0.9 | -10% research weight |
| Behavior | rest | 1.25 | +25% rest weight |
| Behavior | steal | 1.05 | +5% steal weight |
| Emotion | guilt_sensitivity | 0.85 | -15% guilt sensitivity |
| Relationship | trust_gain_mult | 0.9 | -10% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | learning_speed_mult | 0.95 | -5% learning speed mult |
| Work | quality_mult | 0.95 | -5% quality mult |
| Work | speed_mult | 0.85 | -15% speed mult |
| Combat | flee_threshold_mult | 1.05 | +5% flee threshold mult |
| Combat | morale_mult | 0.95 | -5% morale mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | stress_recovery_mult | 1.1 | +10% stress recovery mult |
| Stress | violation: hard_work | 10 | +10 stress when hard_work |

**Amplified behaviors**: `rest`, `steal`
**Suppressed behaviors**: `build`, `gather`, `research`
**Emotion sensitivities**: `guilt_sensitivity (0.85)`
**Violation stress triggers**: `hard_work (+10)`

**Synergies**: [`c_co_ll_careless_waster`](#c_co_ll_careless_waster)
**Anti-synergies**: [`f_industrious`](#f_industrious), [`c_labor_hero`](#c_labor_hero)

📄 source: `extracted/trait_data.json`

---

<a id="f_perfectionist"></a>
### Perfectionist (완벽주의) — `f_perfectionist`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `C_perfectionism` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | craft | 1.1 | +10% craft weight |
| Behavior | research | 1.05 | +5% research weight |
| Emotion | frustration_sensitivity | 1.25 | +25% frustration sensitivity |
| Emotion | satisfaction_quality_sensitivity | 1.1 | +10% satisfaction quality sensitivity |
| Relationship | conflict_mult | 1.05 | +5% conflict mult |
| Relationship | criticism_given_mult | 1.15 | +15% criticism given mult |
| Work | error_rate_mult | 0.8 | -20% error rate mult |
| Work | quality_mult | 1.25 | +25% quality mult |
| Work | speed_mult | 0.9 | -10% speed mult |
| Combat | reaction_speed_mult | 0.95 | -5% reaction speed mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.15 | +15% stress gain mult |
| Stress | stress_recovery_mult | 0.95 | -5% stress recovery mult |
| Stress | violation: accept_mediocre | 12 | +12 stress when accept_mediocre |

**Amplified behaviors**: `build`, `craft`, `research`
**Suppressed behaviors**: none
**Emotion sensitivities**: `frustration_sensitivity (1.25)`, `satisfaction_quality_sensitivity (1.1)`
**Violation stress triggers**: `accept_mediocre (+12)`

**Synergies**: [`f_industrious`](#f_industrious), [`c_master_craftsman`](#c_master_craftsman), [`c_co_hh_methodical_inventor`](#c_co_hh_methodical_inventor)
**Anti-synergies**: [`f_careless`](#f_careless)

📄 source: `extracted/trait_data.json`

---

<a id="f_careless"></a>
### Careless (대충하는) — `f_careless`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `C_perfectionism` direction `low` threshold `0.14`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | craft | 0.95 | -5% craft weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Emotion | frustration_sensitivity | 0.85 | -15% frustration sensitivity |
| Relationship | trust_gain_mult | 0.95 | -5% trust gain mult |
| Relationship | trust_loss_mult | 1.05 | +5% trust loss mult |
| Work | error_rate_mult | 1.3 | +30% error rate mult |
| Work | quality_mult | 0.85 | -15% quality mult |
| Work | speed_mult | 1.05 | +5% speed mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | break_threshold_mult | 1.02 | +2% break threshold mult |
| Stress | stress_gain_mult | 0.9 | -10% stress gain mult |
| Stress | violation: double_check | 10 | +10 stress when double_check |

**Amplified behaviors**: `explore`
**Suppressed behaviors**: `craft`
**Emotion sensitivities**: `frustration_sensitivity (0.85)`
**Violation stress triggers**: `double_check (+10)`

**Synergies**: [`f_reckless`](#f_reckless), [`c_xc_hl_charming_improviser`](X.md#c_xc_hl_charming_improviser)
**Anti-synergies**: [`f_perfectionist`](#f_perfectionist), [`c_master_craftsman`](#c_master_craftsman)

📄 source: `extracted/trait_data.json`

---

<a id="f_prudent"></a>
### Prudent (신중한) — `f_prudent`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `C_prudence` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | leadership | 1.1 | +10% leadership weight |
| Behavior | plan | 1.25 | +25% plan weight |
| Behavior | steal | 0.8 | -20% steal weight |
| Emotion | fear_sensitivity | 1.05 | +5% fear sensitivity |
| Emotion | impulse_control_mult | 1.2 | +20% impulse control mult |
| Relationship | risk_sharing_mult | 1.05 | +5% risk sharing mult |
| Relationship | trust_gain_mult | 1.1 | +10% trust gain mult |
| Work | error_rate_mult | 0.9 | -10% error rate mult |
| Work | quality_mult | 1.05 | +5% quality mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Combat | flee_threshold_mult | 1.05 | +5% flee threshold mult |
| Combat | risk_taking_mult | 0.85 | -15% risk taking mult |
| Combat | tactic_planning_mult | 1.15 | +15% tactic planning mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | violation: act_impulsively | 14 | +14 stress when act_impulsively |
| Stress | violation: gamble | 12 | +12 stress when gamble |

**Amplified behaviors**: `leadership`, `plan`
**Suppressed behaviors**: `explore`, `steal`
**Emotion sensitivities**: `fear_sensitivity (1.05)`, `impulse_control_mult (1.2)`
**Violation stress triggers**: `act_impulsively (+14)`, `gamble (+12)`

**Synergies**: [`f_organized`](#f_organized), [`c_ec_lh_cool_strategist`](E.md#c_ec_lh_cool_strategist), [`c_defender`](#c_defender)
**Anti-synergies**: [`f_reckless`](#f_reckless)

📄 source: `extracted/trait_data.json`

---

<a id="f_reckless"></a>
### Reckless (충동적인) — `f_reckless`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `C_prudence` direction `low` threshold `0.12`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.1 | +10% combat weight |
| Behavior | explore | 1.2 | +20% explore weight |
| Behavior | plan | 0.8 | -20% plan weight |
| Behavior | steal | 1.2 | +20% steal weight |
| Emotion | anger_sensitivity | 1.1 | +10% anger sensitivity |
| Emotion | excitement_sensitivity | 1.2 | +20% excitement sensitivity |
| Emotion | impulse_control_mult | 0.8 | -20% impulse control mult |
| Relationship | accident_cost_mult | 1.15 | +15% accident cost mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | error_rate_mult | 1.25 | +25% error rate mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | speed_mult | 1.05 | +5% speed mult |
| Combat | aggression_mult | 1.1 | +10% aggression mult |
| Combat | flee_threshold_mult | 0.85 | -15% flee threshold mult |
| Combat | risk_taking_mult | 1.3 | +30% risk taking mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.05 | +5% stress gain mult |
| Stress | violation: wait_and_plan | 10 | +10 stress when wait_and_plan |

**Amplified behaviors**: `combat`, `explore`, `steal`
**Suppressed behaviors**: `plan`
**Emotion sensitivities**: `anger_sensitivity (1.1)`, `excitement_sensitivity (1.2)`, `impulse_control_mult (0.8)`
**Violation stress triggers**: `wait_and_plan (+10)`

**Synergies**: [`f_hot_tempered`](A.md#f_hot_tempered), [`f_bold`](X.md#f_bold), [`c_berserker`](A.md#c_berserker), [`c_co_lh_free_spirit`](#c_co_lh_free_spirit)
**Anti-synergies**: [`f_prudent`](#f_prudent), [`c_defender`](#c_defender)

📄 source: `extracted/trait_data.json`

---

<a id="c_co_hh_methodical_inventor"></a>
### Methodical Inventor (체계적 발명가) — `c_co_hh_methodical_inventor`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `C` direction `high` threshold `0.75`
- Facet `O` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.1 | +10% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.265 | +26% research weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | trust_gain_mult | 1.05 | +5% trust gain mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `build`, `craft`, `explore`, `gather`, `leadership`, `plan`, `research`
**Suppressed behaviors**: none
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_strategist_general`](#c_strategist_general), [`f_prudent`](#f_prudent), [`c_xc_lh_silent_craftsman`](X.md#c_xc_lh_silent_craftsman)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_co_hl_conservative_manager"></a>
### Conservative Manager (보수적 관리자) — `c_co_hl_conservative_manager`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `C` direction `high` threshold `0.75`
- Facet `O` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.155 | +16% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.155 | +16% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.045 | +4% research weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | trust_gain_mult | 1.05 | +5% trust gain mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `build`, `gather`, `leadership`, `plan`, `research`
**Suppressed behaviors**: none
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `novelty_fear_sensitivity (1.05)`
**Violation stress triggers**: none

**Synergies**: [`f_industrious`](#f_industrious), [`c_strategist_general`](#c_strategist_general), [`f_prudent`](#f_prudent)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_co_lh_free_spirit"></a>
### Free Spirit (자유영혼) — `c_co_lh_free_spirit`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `C` direction `low` threshold `0.25`
- Facet `O` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.9 | -10% build weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.2705 | +27% explore weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 1.035 | +3% research weight |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | speed_mult | 0.95 | -5% speed mult |
| Combat | risk_taking_mult | 1.15 | +15% risk taking mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 1.05 | +5% stress gain mult |

**Amplified behaviors**: `craft`, `explore`, `research`
**Suppressed behaviors**: `build`, `plan`
**Emotion sensitivities**: `impulse_control_mult (0.9)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_xc_hl_charming_improviser`](X.md#c_xc_hl_charming_improviser), [`c_strategist_general`](#c_strategist_general), [`c_chef`](O.md#c_chef)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_co_ll_careless_waster"></a>
### Careless Waster (방탕한 낭비가) — `c_co_ll_careless_waster`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `C` direction `low` threshold `0.25`
- Facet `O` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.945 | -5% build weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 0.855 | -15% research weight |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | speed_mult | 0.95 | -5% speed mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 1.05 | +5% stress gain mult |

**Amplified behaviors**: `explore`, `leadership`
**Suppressed behaviors**: `build`, `plan`, `research`
**Emotion sensitivities**: `impulse_control_mult (0.9)`, `novelty_fear_sensitivity (1.05)`
**Violation stress triggers**: none

**Synergies**: [`c_xc_hl_charming_improviser`](X.md#c_xc_hl_charming_improviser), [`f_reckless`](#f_reckless), [`d_cult_leader`](H.md#d_cult_leader)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_master_craftsman"></a>
### Master Craftsman (장인) — `c_master_craftsman`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `C` direction `high` threshold `0.7`
- Facet `O` direction `high` threshold `0.7`
- Facet `X` direction `low` threshold `0.3`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.32 | +32% build weight |
| Behavior | craft | 1.4333 | +43% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.3282 | +33% research weight |
| Behavior | social | 0.68 | -32% social weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 1.43 | +43% quality mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | speed_mult | 1.045 | +4% speed mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | social_stress_mult | 1.1 | +10% social stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | violation: rush_job | 12 | +12 stress when rush_job |

**Amplified behaviors**: `build`, `craft`, `explore`, `gather`, `plan`, `research`
**Suppressed behaviors**: `social`
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`, `joy_baseline (-0.01)`
**Violation stress triggers**: `rush_job (+12)`

**Synergies**: [`f_perfectionist`](#f_perfectionist), [`f_organized`](#f_organized)
**Anti-synergies**: [`f_careless`](#f_careless)

📄 source: `extracted/trait_data.json`

---

<a id="c_zealot"></a>
### Zealot (광신자) — `c_zealot`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `C` direction `high` threshold `0.7`
- Facet `O` direction `low` threshold `0.3`
- Facet `X` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.155 | +16% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | indoctrinate | 1.25 | +25% indoctrinate weight |
| Behavior | leadership | 1.3886 | +39% leadership weight |
| Behavior | negotiate | 0.9 | -10% negotiate weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.045 | +4% research weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | ingroup_trust_mult | 1.32 | +32% ingroup trust mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | outgroup_hostility_mult | 1.2 | +20% outgroup hostility mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 1.4375 | +44% change stress mult |
| Stress | stress_gain_mult | 0.931 | -7% stress gain mult |

**Amplified behaviors**: `build`, `gather`, `indoctrinate`, `leadership`, `plan`, `research`, `social`
**Suppressed behaviors**: `negotiate`
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `novelty_fear_sensitivity (1.05)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`f_traditionalist`](O.md#f_traditionalist), [`c_xo_hl_populist`](X.md#c_xo_hl_populist)
**Anti-synergies**: [`c_ao_hh_open-minded_humanitarian`](A.md#c_ao_hh_open-minded_humanitarian), [`f_nonconformist`](O.md#f_nonconformist)

📄 source: `extracted/trait_data.json`

---

<a id="c_speculator"></a>
### Speculator (투기꾼) — `c_speculator`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `C` direction `high` threshold `0.75`
- Facet `E` direction `low` threshold `0.25`
- Facet `H_greed_avoidance` direction `low` threshold `0.15`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | invest | 1.4 | +40% invest weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | steal | 1.05 | +5% steal weight |
| Behavior | trade | 1.4 | +40% trade weight |
| Emotion | envy_sensitivity | 1.2 | +20% envy sensitivity |
| Emotion | fear_sensitivity | 0.7225 | -28% fear sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.122 | +12% speed mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.855 | -15% stress gain mult |
| Stress | violation: share_profit | 12 | +12 stress when share_profit |

**Amplified behaviors**: `build`, `combat`, `explore`, `gather`, `invest`, `plan`, `research`, `steal`, `trade`
**Suppressed behaviors**: `flee`
**Emotion sensitivities**: `envy_sensitivity (1.2)`, `fear_sensitivity (0.7225)`, `impulse_control_mult (1.1)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: `share_profit (+12)`

**Synergies**: [`d_machiavellian`](H.md#d_machiavellian), [`c_born_merchant`](X.md#c_born_merchant)
**Anti-synergies**: [`c_philanthropist`](H.md#c_philanthropist)

📄 source: `extracted/trait_data.json`

---

<a id="c_architect_master"></a>
### Master Architect (건축 장인) — `c_architect_master`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `C_organization` direction `high` threshold `0.85`
- Facet `C_perfectionism` direction `high` threshold `0.85`
- Facet `O_aesthetic_appreciation` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.43 | +43% build weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.265 | +26% research weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.7225 | -28% error rate mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 1.43 | +43% quality mult |
| Work | speed_mult | 1.045 | +4% speed mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | violation: rush_job | 14 | +14 stress when rush_job |

**Amplified behaviors**: `build`, `craft`, `explore`, `gather`, `plan`, `research`
**Suppressed behaviors**: none
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: `rush_job (+14)`

**Synergies**: [`c_master_craftsman`](#c_master_craftsman), [`f_perfectionist`](#f_perfectionist)
**Anti-synergies**: [`f_careless`](#f_careless)

📄 source: `extracted/trait_data.json`

---

<a id="c_labor_hero"></a>
### Labor Hero (노동영웅) — `c_labor_hero`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `C_diligence` direction `high` threshold `0.85`
- Facet `C_organization` direction `high` threshold `0.85`
- Facet `X_liveliness` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.375 | +38% build weight |
| Behavior | gather | 1.32 | +32% gather weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | rest | 0.8 | -20% rest weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.375 | +38% speed mult |
| Work | stamina_efficiency_mult | 0.9 | -10% stamina efficiency mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | stress_gain_mult | 1.0241 | +2% stress gain mult |
| Stress | stress_recovery_mult | 0.9 | -10% stress recovery mult |

**Amplified behaviors**: `build`, `gather`, `leadership`, `plan`, `research`, `social`
**Suppressed behaviors**: `rest`
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`f_industrious`](#f_industrious), [`f_energetic`](X.md#f_energetic)
**Anti-synergies**: [`f_lazy`](#f_lazy)

📄 source: `extracted/trait_data.json`

---

<a id="c_defender"></a>
### Defensive Specialist (방어의 달인) — `c_defender`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `C` direction `high` threshold `0.75`
- Facet `A` direction `high` threshold `0.75`
- Facet `A_patience` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 1.045 | +4% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | flee_threshold_mult | 0.95 | -5% flee threshold mult |
| Combat | hold_line_mult | 1.35 | +35% hold line mult |
| Combat | risk_taking_mult | 0.85 | -15% risk taking mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | stress_gain_mult | 0.9025 | -10% stress gain mult |
| Stress | violation: charge | 12 | +12 stress when charge |

**Amplified behaviors**: `build`, `combat`, `cooperate`, `gather`, `help`, `plan`, `research`
**Suppressed behaviors**: `flee`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `impulse_control_mult (1.1)`
**Violation stress triggers**: `charge (+12)`

**Synergies**: [`f_patient`](A.md#f_patient), [`f_prudent`](#f_prudent)
**Anti-synergies**: [`c_berserker`](A.md#c_berserker), [`f_reckless`](#f_reckless)

📄 source: `extracted/trait_data.json`

---

<a id="c_strategist_general"></a>
### Battle Commander (전장지휘관) — `c_strategist_general`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `C_prudence` direction `high` threshold `0.85`
- Facet `X_social_boldness` direction `high` threshold `0.85`
- Facet `O_creativity` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 1.1 | +10% combat weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.4375 | +44% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.265 | +26% research weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.155 | +16% morale mult |
| Combat | tactic_improv_mult | 1.265 | +26% tactic improv mult |
| Combat | tactic_planning_mult | 1.485 | +49% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.931 | -7% stress gain mult |

**Amplified behaviors**: `build`, `combat`, `craft`, `explore`, `gather`, `leadership`, `plan`, `research`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_born_leader`](X.md#c_born_leader), [`c_ec_lh_cool_strategist`](E.md#c_ec_lh_cool_strategist)
**Anti-synergies**: [`c_ec_ll_reckless_drifter`](E.md#c_ec_ll_reckless_drifter)

📄 source: `extracted/trait_data.json`

---

<a id="c_settler"></a>
### Settler (정착민) — `c_settler`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `C` direction `high` threshold `0.75`
- Facet `O` direction `low` threshold `0.25`
- Facet `A` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.386 | +39% build weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | explore | 0.9 | -10% explore weight |
| Behavior | gather | 1.21 | +21% gather weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.045 | +4% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | group_cohesion_mult | 1.1 | +10% group cohesion mult |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 0.9025 | -10% stress gain mult |

**Amplified behaviors**: `build`, `cooperate`, `gather`, `help`, `leadership`, `plan`, `research`
**Suppressed behaviors**: `combat`, `explore`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `impulse_control_mult (1.1)`, `novelty_fear_sensitivity (1.05)`
**Violation stress triggers**: none

**Synergies**: [`c_co_hl_conservative_manager`](#c_co_hl_conservative_manager), [`c_survivalist`](E.md#c_survivalist)
**Anti-synergies**: [`c_nomad`](O.md#c_nomad), [`c_free_spirit_extro`](O.md#c_free_spirit_extro)

📄 source: `extracted/trait_data.json`

---

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
