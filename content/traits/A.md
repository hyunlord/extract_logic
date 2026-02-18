---
title: "Agreeableness (A) Traits"
description: "Trait breakdown for Agreeableness (A)."
generated: true
source_files:
  - "extracted/trait_data.json"
  - "data/species/human/personality/trait_definitions.json"
nav_order: 14
---

# Agreeableness (A) — 우호성

## Axis Overview

The **Agreeableness** axis measures personality tendencies represented by the `A` axis in the HEXACO model.
**Facets**: `A_flexibility` (유연성 / Flexibility), `A_forgiveness` (용서 / Forgiveness), `A_gentleness` (온화 / Gentleness), `A_patience` (인내 / Patience)

## Traits

<a id="f_forgiving"></a>
### Forgiving (관대한) — `f_forgiving`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `A_forgiveness` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | revenge | 0.6 | -40% revenge weight |
| Behavior | social | 1.1 | +10% social weight |
| Emotion | anger_decay_mult | 1.2 | +20% anger decay mult |
| Emotion | anger_sensitivity | 0.85 | -15% anger sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Relationship | trust_repair_mult | 1.3 | +30% trust repair mult |
| Work | teamwork_efficiency_mult | 1.1 | +10% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.9 | -10% stress gain mult |
| Stress | violation: hold_grudge | 12 | +12 stress when hold_grudge |
| Stress | violation: seek_revenge | 14 | +14 stress when seek_revenge |

**Amplified behaviors**: `cooperate`, `social`
**Suppressed behaviors**: `combat`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.2)`, `anger_sensitivity (0.85)`
**Violation stress triggers**: `hold_grudge (+12)`, `seek_revenge (+14)`

**Synergies**: [`f_gentle`](#f_gentle), [`f_sentimental`](E.md#f_sentimental), [`c_reconciler`](#c_reconciler)
**Anti-synergies**: [`f_vengeful`](#f_vengeful)

📄 source: `extracted/trait_data.json`

---

<a id="f_vengeful"></a>
### Vengeful (앙심 품은) — `f_vengeful`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `A_forgiveness` direction `low` threshold `0.16`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | cooperate | 0.85 | -15% cooperate weight |
| Behavior | revenge | 1.6 | +60% revenge weight |
| Emotion | anger_decay_mult | 0.85 | -15% anger decay mult |
| Emotion | anger_sensitivity | 1.3 | +30% anger sensitivity |
| Relationship | conflict_mult | 1.25 | +25% conflict mult |
| Relationship | grudge_decay_mult | 0.7 | -30% grudge decay mult |
| Relationship | trust_loss_mult | 1.2 | +20% trust loss mult |
| Relationship | trust_repair_mult | 0.75 | -25% trust repair mult |
| Work | teamwork_efficiency_mult | 0.9 | -10% teamwork efficiency mult |
| Combat | aggression_mult | 1.2 | +20% aggression mult |
| Combat | flee_threshold_mult | 0.95 | -5% flee threshold mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.1 | +10% stress gain mult |
| Stress | violation: forgive | 10 | +10 stress when forgive |
| Stress | violation: show_mercy | 12 | +12 stress when show_mercy |

**Amplified behaviors**: `combat`, `revenge`
**Suppressed behaviors**: `cooperate`
**Emotion sensitivities**: `anger_decay_mult (0.85)`, `anger_sensitivity (1.3)`
**Violation stress triggers**: `forgive (+10)`, `show_mercy (+12)`

**Synergies**: [`f_hot_tempered`](#f_hot_tempered), [`c_berserker`](#c_berserker)
**Anti-synergies**: [`f_forgiving`](#f_forgiving), [`c_reconciler`](#c_reconciler)

📄 source: `extracted/trait_data.json`

---

<a id="f_gentle"></a>
### Gentle (온화한) — `f_gentle`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `A_gentleness` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 0.9 | -10% combat weight |
| Behavior | help | 1.15 | +15% help weight |
| Behavior | intimidate | 0.7 | -30% intimidate weight |
| Behavior | nurture | 1.1 | +10% nurture weight |
| Behavior | steal | 0.85 | -15% steal weight |
| Emotion | anger_sensitivity | 0.85 | -15% anger sensitivity |
| Emotion | compassion_sensitivity | 1.2 | +20% compassion sensitivity |
| Relationship | conflict_mult | 0.8 | -20% conflict mult |
| Relationship | intimidation_bias_mult | 0.7 | -30% intimidation bias mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.85 | -15% aggression mult |
| Combat | flee_threshold_mult | 1.05 | +5% flee threshold mult |
| Stress | stress_from_harming_mult | 1.3 | +30% stress from harming mult |
| Stress | stress_gain_mult | 1 | no change |
| Stress | violation: bully | 18 | +18 stress when bully |
| Stress | violation: torture | 22 | +22 stress when torture |

**Amplified behaviors**: `help`, `nurture`
**Suppressed behaviors**: `combat`, `intimidate`, `steal`
**Emotion sensitivities**: `anger_sensitivity (0.85)`, `compassion_sensitivity (1.2)`
**Violation stress triggers**: `bully (+18)`, `torture (+22)`

**Synergies**: [`f_forgiving`](#f_forgiving), [`c_caregiver`](E.md#c_caregiver)
**Anti-synergies**: [`f_harsh`](#f_harsh), [`d_sadist`](H.md#d_sadist)

📄 source: `extracted/trait_data.json`

---

<a id="f_harsh"></a>
### Harsh (거친) — `f_harsh`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `A_gentleness` direction `low` threshold `0.12`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.25 | +25% combat weight |
| Behavior | intimidate | 1.3 | +30% intimidate weight |
| Behavior | nurture | 0.85 | -15% nurture weight |
| Behavior | steal | 1.1 | +10% steal weight |
| Emotion | anger_baseline | 0.03 | -97% anger baseline |
| Emotion | anger_sensitivity | 1.25 | +25% anger sensitivity |
| Relationship | conflict_mult | 1.3 | +30% conflict mult |
| Relationship | fear_induced_compliance_mult | 1.2 | +20% fear induced compliance mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Work | quality_mult | 0.95 | -5% quality mult |
| Work | speed_mult | 1 | no change |
| Combat | aggression_mult | 1.3 | +30% aggression mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | violation: apologize | 12 | +12 stress when apologize |
| Stress | violation: show_kindness | 10 | +10 stress when show_kindness |

**Amplified behaviors**: `combat`, `intimidate`, `steal`
**Suppressed behaviors**: `nurture`
**Emotion sensitivities**: `anger_baseline (0.03)`, `anger_sensitivity (1.25)`
**Violation stress triggers**: `apologize (+12)`, `show_kindness (+10)`

**Synergies**: [`f_fearless`](E.md#f_fearless), [`c_strict_commander`](#c_strict_commander), [`d_bully`](#d_bully)
**Anti-synergies**: [`f_gentle`](#f_gentle), [`c_pacifist`](#c_pacifist)

📄 source: `extracted/trait_data.json`

---

<a id="f_flexible"></a>
### Flexible (유연한) — `f_flexible`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `A_flexibility` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | cooperate | 1.15 | +15% cooperate weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | negotiate | 1.2 | +20% negotiate weight |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | frustration_sensitivity | 0.9 | -10% frustration sensitivity |
| Relationship | conflict_resolution_mult | 1.25 | +25% conflict resolution mult |
| Relationship | trust_gain_mult | 1.05 | +5% trust gain mult |
| Work | learning_speed_mult | 1.02 | +2% learning speed mult |
| Work | task_switching_efficiency_mult | 1.05 | +5% task switching efficiency mult |
| Combat | tactic_adapt_mult | 1.15 | +15% tactic adapt mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | stress_recovery_mult | 1.05 | +5% stress recovery mult |
| Stress | violation: refuse_compromise | 10 | +10 stress when refuse_compromise |

**Amplified behaviors**: `cooperate`, `leadership`, `negotiate`
**Suppressed behaviors**: none
**Emotion sensitivities**: `anger_sensitivity (0.9)`, `frustration_sensitivity (0.9)`
**Violation stress triggers**: `refuse_compromise (+10)`

**Synergies**: [`c_mediator_king`](#c_mediator_king), [`c_reconciler`](#c_reconciler)
**Anti-synergies**: [`f_stubborn`](#f_stubborn)

📄 source: `extracted/trait_data.json`

---

<a id="f_stubborn"></a>
### Stubborn (완고한) — `f_stubborn`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `A_flexibility` direction `low` threshold `0.16`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | cooperate | 0.95 | -5% cooperate weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | negotiate | 0.85 | -15% negotiate weight |
| Emotion | anger_sensitivity | 1.1 | +10% anger sensitivity |
| Emotion | pride_baseline | 0.02 | -98% pride baseline |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | resistance_to_persuasion_mult | 1.25 | +25% resistance to persuasion mult |
| Work | error_correction_mult | 0.9 | -10% error correction mult |
| Work | learning_speed_mult | 0.95 | -5% learning speed mult |
| Work | persistence_mult | 1.1 | +10% persistence mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | hold_line_mult | 1.15 | +15% hold line mult |
| Stress | break_threshold_mult | 0.98 | -2% break threshold mult |
| Stress | stress_gain_mult | 1.05 | +5% stress gain mult |
| Stress | violation: back_down | 12 | +12 stress when back_down |

**Amplified behaviors**: `leadership`
**Suppressed behaviors**: `cooperate`, `negotiate`
**Emotion sensitivities**: `anger_sensitivity (1.1)`, `pride_baseline (0.02)`
**Violation stress triggers**: `back_down (+12)`

**Synergies**: [`c_defender`](C.md#c_defender), [`c_strict_commander`](#c_strict_commander)
**Anti-synergies**: [`f_flexible`](#f_flexible)

📄 source: `extracted/trait_data.json`

---

<a id="f_patient"></a>
### Patient (인내심 있는) — `f_patient`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `A_patience` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | research | 1.05 | +5% research weight |
| Behavior | social | 1.05 | +5% social weight |
| Emotion | anger_decay_mult | 1.25 | +25% anger decay mult |
| Emotion | anger_sensitivity | 0.75 | -25% anger sensitivity |
| Relationship | conflict_mult | 0.8 | -20% conflict mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | error_rate_mult | 0.9 | -10% error rate mult |
| Work | quality_mult | 1.05 | +5% quality mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Combat | flee_threshold_mult | 1 | no change |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | break_threshold_mult | 1.1 | +10% break threshold mult |
| Stress | stress_gain_mult | 0.85 | -15% stress gain mult |
| Stress | stress_recovery_mult | 1.1 | +10% stress recovery mult |
| Stress | violation: lose_temper | 12 | +12 stress when lose_temper |

**Amplified behaviors**: `build`, `research`, `social`
**Suppressed behaviors**: `combat`
**Emotion sensitivities**: `anger_decay_mult (1.25)`, `anger_sensitivity (0.75)`
**Violation stress triggers**: `lose_temper (+12)`

**Synergies**: [`f_prudent`](C.md#f_prudent), [`f_organized`](C.md#f_organized), [`c_defender`](C.md#c_defender)
**Anti-synergies**: [`f_hot_tempered`](#f_hot_tempered)

📄 source: `extracted/trait_data.json`

---

<a id="f_hot_tempered"></a>
### Hot‑Tempered (다혈질) — `f_hot_tempered`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `A_patience` direction `low` threshold `0.12`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | social | 0.9 | -10% social weight |
| Emotion | anger_decay_mult | 0.8 | -20% anger decay mult |
| Emotion | anger_sensitivity | 1.45 | +45% anger sensitivity |
| Relationship | conflict_mult | 1.4 | +40% conflict mult |
| Relationship | intimacy_loss_mult | 1.2 | +20% intimacy loss mult |
| Relationship | trust_loss_mult | 1.15 | +15% trust loss mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.92 | -8% quality mult |
| Work | speed_mult | 1.05 | +5% speed mult |
| Combat | aggression_mult | 1.25 | +25% aggression mult |
| Combat | flee_threshold_mult | 0.95 | -5% flee threshold mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Stress | break_threshold_mult | 0.9 | -10% break threshold mult |
| Stress | stress_gain_mult | 1.15 | +15% stress gain mult |
| Stress | stress_recovery_mult | 0.95 | -5% stress recovery mult |
| Stress | violation: stay_calm | 12 | +12 stress when stay_calm |

**Amplified behaviors**: `combat`, `explore`
**Suppressed behaviors**: `cooperate`, `social`
**Emotion sensitivities**: `anger_decay_mult (0.8)`, `anger_sensitivity (1.45)`
**Violation stress triggers**: `stay_calm (+12)`

**Synergies**: [`f_reckless`](C.md#f_reckless), [`f_vengeful`](#f_vengeful), [`c_berserker`](#c_berserker)
**Anti-synergies**: [`f_patient`](#f_patient), [`c_reconciler`](#c_reconciler)

📄 source: `extracted/trait_data.json`

---

<a id="c_ac_hh_reliable_teamworker"></a>
### Reliable Teamworker (성실한 협력가) — `c_ac_hh_reliable_teamworker`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `A` direction `high` threshold `0.75`
- Facet `C` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
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
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | stress_gain_mult | 0.9025 | -10% stress gain mult |

**Amplified behaviors**: `build`, `cooperate`, `gather`, `help`, `plan`, `research`
**Suppressed behaviors**: `combat`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `impulse_control_mult (1.1)`
**Violation stress triggers**: none

**Synergies**: [`f_flexible`](#f_flexible), [`c_strategist_general`](C.md#c_strategist_general), [`f_prudent`](C.md#f_prudent)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ac_hl_kind_dreamer"></a>
### Kind Dreamer (친절한 낭만가) — `c_ac_hl_kind_dreamer`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `A` direction `high` threshold `0.75`
- Facet `C` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.9 | -10% build weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 0.9 | -10% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | speed_mult | 0.95 | -5% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | stress_gain_mult | 0.9975 | -0% stress gain mult |

**Amplified behaviors**: `cooperate`, `explore`, `help`
**Suppressed behaviors**: `build`, `combat`, `plan`, `research`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `impulse_control_mult (0.9)`
**Violation stress triggers**: none

**Synergies**: [`f_flexible`](#f_flexible), [`c_ea_lh_volatile_bully`](E.md#c_ea_lh_volatile_bully), [`c_reconciler`](#c_reconciler)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ac_lh_strict_commander"></a>
### Strict Commander (엄격한 지휘관) — `c_ac_lh_strict_commander`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `A` direction `low` threshold `0.25`
- Facet `C` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `build`, `combat`, `gather`, `intimidate`, `plan`, `research`, `revenge`
**Suppressed behaviors**: `cooperate`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `impulse_control_mult (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_strategist_general`](C.md#c_strategist_general), [`f_prudent`](C.md#f_prudent), [`c_xc_lh_silent_craftsman`](X.md#c_xc_lh_silent_craftsman)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ac_ll_unruly_brute"></a>
### Unruly Brute (무절제 난폭자) — `c_ac_ll_unruly_brute`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `A` direction `low` threshold `0.25`
- Facet `C` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.9 | -10% build weight |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 0.9 | -10% research weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | speed_mult | 0.95 | -5% speed mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | stress_gain_mult | 1.05 | +5% stress gain mult |

**Amplified behaviors**: `combat`, `explore`, `intimidate`, `revenge`
**Suppressed behaviors**: `build`, `cooperate`, `plan`, `research`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `impulse_control_mult (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_xc_hl_charming_improviser`](X.md#c_xc_hl_charming_improviser), [`f_reckless`](C.md#f_reckless), [`c_hc_ll_irresponsible_cheat`](H.md#c_hc_ll_irresponsible_cheat)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ao_hh_open-minded_humanitarian"></a>
### Open‑Minded Humanitarian (관대한 탐구자) — `c_ao_hh_open-minded_humanitarian`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `A` direction `high` threshold `0.75`
- Facet `O` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `cooperate`, `craft`, `explore`, `help`, `research`
**Suppressed behaviors**: `combat`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`f_flexible`](#f_flexible), [`c_ea_lh_volatile_bully`](E.md#c_ea_lh_volatile_bully), [`c_reconciler`](#c_reconciler)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ao_hl_benevolent_traditionalist"></a>
### Benevolent Traditionalist (자애로운 전통가) — `c_ao_hl_benevolent_traditionalist`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `A` direction `high` threshold `0.75`
- Facet `O` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | research | 0.95 | -5% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `build`, `cooperate`, `help`, `leadership`
**Suppressed behaviors**: `combat`, `research`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `novelty_fear_sensitivity (1.05)`
**Violation stress triggers**: none

**Synergies**: [`f_flexible`](#f_flexible), [`c_ea_lh_volatile_bully`](E.md#c_ea_lh_volatile_bully), [`c_reconciler`](#c_reconciler)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ao_lh_cynical_heretic"></a>
### Cynical Heretic (냉소적 이단자) — `c_ao_lh_cynical_heretic`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `A` direction `low` threshold `0.25`
- Facet `O` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 1 | no change |

**Amplified behaviors**: `combat`, `craft`, `explore`, `intimidate`, `research`, `revenge`
**Suppressed behaviors**: `cooperate`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_strategist_general`](C.md#c_strategist_general), [`c_chef`](O.md#c_chef), [`c_xo_lh_solitary_scholar`](X.md#c_xo_lh_solitary_scholar)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ao_ll_rigid_oppressor"></a>
### Rigid Oppressor (완고한 억압자) — `c_ao_ll_rigid_oppressor`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `A` direction `low` threshold `0.25`
- Facet `O` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | research | 0.95 | -5% research weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 1 | no change |

**Amplified behaviors**: `build`, `combat`, `intimidate`, `leadership`, `revenge`
**Suppressed behaviors**: `cooperate`, `research`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `novelty_fear_sensitivity (1.05)`
**Violation stress triggers**: none

**Synergies**: [`d_cult_leader`](H.md#d_cult_leader), [`c_co_hl_conservative_manager`](C.md#c_co_hl_conservative_manager), [`c_ho_ll_corrupt_traditionalist`](H.md#c_ho_ll_corrupt_traditionalist)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="d_bully"></a>
### Bully (폭력적 가해자) — `d_bully`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `A` direction `low` threshold `0.25`
- Facet `X` direction `high` threshold `0.7`
- Facet `H` direction `low` threshold `0.3`
- Facet `A_gentleness` direction `low` threshold `0.12`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | combat | 1.38 | +38% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | dominate | 1.4 | +40% dominate weight |
| Behavior | help | 0.8 | -20% help weight |
| Behavior | intimidate | 1.8 | +80% intimidate weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.2 | +20% social weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | anger_sensitivity | 1.5 | +50% anger sensitivity |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 1.74 | +74% conflict mult |
| Relationship | fear_induced_compliance_mult | 1.3 | +30% fear induced compliance mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 0.68 | -32% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Work | teamwork_efficiency_mult | 0.8479 | -15% teamwork efficiency mult |
| Combat | aggression_mult | 1.4375 | +44% aggression mult |
| Combat | morale_mult | 1.1025 | +10% morale mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.8844 | -12% stress gain mult |
| Stress | violation: apologize | 12 | +12 stress when apologize |
| Stress | violation: show_mercy | 10 | +10 stress when show_mercy |

**Amplified behaviors**: `betray`, `combat`, `dominate`, `intimidate`, `leadership`, `revenge`, `social`, `steal`, `take_bribe`
**Suppressed behaviors**: `cooperate`, `help`, `share`
**Emotion sensitivities**: `anger_sensitivity (1.5)`, `guilt_sensitivity (0.8)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: `apologize (+12)`, `show_mercy (+10)`

**Synergies**: [`d_sadist`](H.md#d_sadist), [`c_ac_lh_strict_commander`](#c_ac_lh_strict_commander)
**Anti-synergies**: [`c_ea_hh_compassionate_reconciler`](E.md#c_ea_hh_compassionate_reconciler), [`f_gentle`](#f_gentle)

📄 source: `extracted/trait_data.json`

---

<a id="c_reconciler"></a>
### Reconciler (화해자) — `c_reconciler`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `A` direction `high` threshold `0.7`
- Facet `X` direction `high` threshold `0.7`
- Facet `H` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | help | 1.21 | +21% help weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | negotiate | 1.2 | +20% negotiate weight |
| Behavior | revenge | 0.42 | -58% revenge weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | social | 1.5 | +50% social weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 0.6375 | -36% conflict mult |
| Relationship | conflict_resolution_mult | 1.4 | +40% conflict resolution mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Relationship | trust_repair_mult | 1.485 | +49% trust repair mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Work | teamwork_efficiency_mult | 1.1025 | +10% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | stress_gain_mult | 0.9496 | -5% stress gain mult |

**Amplified behaviors**: `cooperate`, `help`, `leadership`, `negotiate`, `share`, `social`
**Suppressed behaviors**: `betray`, `combat`, `revenge`, `steal`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `guilt_sensitivity (1.15)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`f_flexible`](#f_flexible), [`f_forgiving`](#f_forgiving)
**Anti-synergies**: [`f_vengeful`](#f_vengeful), [`c_tyrant`](H.md#c_tyrant)

📄 source: `extracted/trait_data.json`

---

<a id="c_berserker"></a>
### Berserker (광전사) — `c_berserker`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `A` direction `low` threshold `0.3`
- Facet `E` direction `low` threshold `0.3`
- Facet `C` direction `low` threshold `0.3`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.9 | -10% build weight |
| Behavior | combat | 1.8 | +80% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | explore | 1.155 | +16% explore weight |
| Behavior | flee | 0.63 | -37% flee weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | plan | 0.595 | -40% plan weight |
| Behavior | research | 0.9 | -10% research weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Emotion | anger_sensitivity | 1.56 | +56% anger sensitivity |
| Emotion | fear_sensitivity | 0.595 | -40% fear sensitivity |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | speed_mult | 0.969 | -3% speed mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.84 | +84% aggression mult |
| Combat | flee_threshold_mult | 0.63 | -37% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.5593 | +56% risk taking mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.8978 | -10% stress gain mult |
| Stress | violation: hold_back | 12 | +12 stress when hold_back |
| Stress | violation: retreat | 14 | +14 stress when retreat |

**Amplified behaviors**: `combat`, `explore`, `intimidate`, `revenge`
**Suppressed behaviors**: `build`, `cooperate`, `flee`, `plan`, `research`
**Emotion sensitivities**: `anger_sensitivity (1.56)`, `fear_sensitivity (0.595)`, `impulse_control_mult (0.9)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: `hold_back (+12)`, `retreat (+14)`

**Synergies**: [`f_hot_tempered`](#f_hot_tempered), [`f_reckless`](C.md#f_reckless)
**Anti-synergies**: [`f_prudent`](C.md#f_prudent), [`c_defender`](C.md#c_defender)

📄 source: `extracted/trait_data.json`

---

<a id="c_diplomat"></a>
### Diplomat (외교관) — `c_diplomat`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `A` direction `high` threshold `0.75`
- Facet `X` direction `high` threshold `0.75`
- Facet `C_prudence` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 0.855 | -15% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | negotiate | 1.45 | +45% negotiate weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | social | 1.44 | +44% social weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | conflict_resolution_mult | 1.25 | +25% conflict resolution mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 1.1 | +10% trust gain mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.1025 | +10% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | stress_gain_mult | 0.8844 | -12% stress gain mult |

**Amplified behaviors**: `build`, `cooperate`, `gather`, `help`, `leadership`, `negotiate`, `plan`, `research`, `social`
**Suppressed behaviors**: `combat`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_reconciler`](#c_reconciler), [`c_born_merchant`](X.md#c_born_merchant)
**Anti-synergies**: [`c_tyrant`](H.md#c_tyrant), [`f_harsh`](#f_harsh)

📄 source: `extracted/trait_data.json`

---

<a id="c_pacifist"></a>
### Pacifist (평화주의자) — `c_pacifist`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `A` direction `high` threshold `0.75`
- Facet `H` direction `high` threshold `0.75`
- Facet `A_gentleness` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | combat | 0.665 | -34% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | help | 1.3915 | +39% help weight |
| Behavior | negotiate | 1.2 | +20% negotiate weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.63 | -37% aggression mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | stress_gain_mult | 0.969 | -3% stress gain mult |
| Stress | violation: combat | 18 | +18 stress when combat |
| Stress | violation: kill | 22 | +22 stress when kill |

**Amplified behaviors**: `cooperate`, `help`, `negotiate`, `share`
**Suppressed behaviors**: `betray`, `combat`, `revenge`, `steal`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `guilt_sensitivity (1.15)`
**Violation stress triggers**: `combat (+18)`, `kill (+22)`

**Synergies**: [`c_diplomat`](#c_diplomat), [`c_reconciler`](#c_reconciler)
**Anti-synergies**: [`c_berserker`](#c_berserker), [`d_predatory_raider`](H.md#d_predatory_raider)

📄 source: `extracted/trait_data.json`

---

<a id="c_counselor"></a>
### Counselor (카운슬러) — `c_counselor`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `A` direction `high` threshold `0.75`
- Facet `E_sentimentality` direction `high` threshold `0.85`
- Facet `O_inquisitiveness` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.045 | +4% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | help | 1.375 | +38% help weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | social | 1.1 | +10% social weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | conflict_resolution_mult | 1.15 | +15% conflict resolution mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | trust_repair_mult | 1.375 | +38% trust repair mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 1.0925 | +9% stress gain mult |
| Stress | stress_recovery_social_mult | 1.15 | +15% stress recovery social mult |

**Amplified behaviors**: `cooperate`, `craft`, `explore`, `flee`, `help`, `nurture`, `research`, `social`
**Suppressed behaviors**: `combat`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `fear_sensitivity (1.2)`, `interest_sensitivity (1.1)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_reconciler`](#c_reconciler), [`c_caregiver`](E.md#c_caregiver)
**Anti-synergies**: [`d_bully`](#d_bully), [`d_callous`](H.md#d_callous)

📄 source: `extracted/trait_data.json`

---

<a id="c_animal_tamer"></a>
### Animal Tamer (동물 조련사) — `c_animal_tamer`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `A_gentleness` direction `high` threshold `0.85`
- Facet `X_sociability` direction `high` threshold `0.85`
- Facet `C_prudence` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | nurture | 1.1 | +10% nurture weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | social | 1.2 | +20% social weight |
| Behavior | tame_animal | 1.5 | +50% tame animal weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | risk_management_mult | 1.1 | +10% risk management mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.1025 | +10% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | stress_gain_mult | 0.8844 | -12% stress gain mult |

**Amplified behaviors**: `build`, `cooperate`, `gather`, `help`, `leadership`, `nurture`, `plan`, `research`, `social`, `tame_animal`
**Suppressed behaviors**: `combat`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_survivalist`](E.md#c_survivalist), [`c_caregiver`](E.md#c_caregiver)
**Anti-synergies**: [`f_harsh`](#f_harsh)

📄 source: `extracted/trait_data.json`

---

<a id="c_strict_commander"></a>
### Strict Commander (엄격한 지휘관) — `c_strict_commander`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `A` direction `low` threshold `0.25`
- Facet `C` direction `high` threshold `0.75`
- Facet `X` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 1.265 | +26% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | leadership | 1.4375 | +44% leadership weight |
| Behavior | negotiate | 0.9 | -10% negotiate weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 1.38 | +38% conflict mult |
| Relationship | fear_induced_compliance_mult | 1.2 | +20% fear induced compliance mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 0.9975 | -0% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | discipline_mult | 1.2 | +20% discipline mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | stress_gain_mult | 0.931 | -7% stress gain mult |

**Amplified behaviors**: `build`, `combat`, `gather`, `intimidate`, `leadership`, `plan`, `research`, `revenge`, `social`
**Suppressed behaviors**: `cooperate`, `negotiate`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_strategist_general`](C.md#c_strategist_general), [`d_bully`](#d_bully)
**Anti-synergies**: [`c_democratic_leader`](H.md#c_democratic_leader), [`c_reconciler`](#c_reconciler)

📄 source: `extracted/trait_data.json`

---

<a id="c_mediator_king"></a>
### Mediator King (중재왕) — `c_mediator_king`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `A` direction `high` threshold `0.7`
- Facet `X` direction `high` threshold `0.7`
- Facet `C` direction `high` threshold `0.7`
- Facet `H` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | help | 1.21 | +21% help weight |
| Behavior | leadership | 1.4375 | +44% leadership weight |
| Behavior | negotiate | 1.35 | +35% negotiate weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | social | 1.2 | +20% social weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | conflict_resolution_mult | 1.5 | +50% conflict resolution mult |
| Relationship | group_cohesion_mult | 1.15 | +15% group cohesion mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 1.38 | +38% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.133 | +13% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.1025 | +10% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | stress_gain_mult | 0.9021 | -10% stress gain mult |

**Amplified behaviors**: `build`, `cooperate`, `gather`, `help`, `leadership`, `negotiate`, `plan`, `research`, `share`, `social`
**Suppressed behaviors**: `betray`, `combat`, `revenge`, `steal`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `guilt_sensitivity (1.15)`, `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_reconciler`](#c_reconciler), [`c_democratic_leader`](H.md#c_democratic_leader)
**Anti-synergies**: [`c_tyrant`](H.md#c_tyrant), [`d_corrupt_official`](H.md#d_corrupt_official)

📄 source: `extracted/trait_data.json`

---

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
