---
title: "Emotionality (E) Traits"
description: "Trait breakdown for Emotionality (E)."
generated: true
source_files:
  - "extracted/trait_data.json"
  - "data/species/human/personality/trait_definitions.json"
nav_order: 12
---

# Emotionality (E) — 감정성

## Axis Overview

The **Emotionality** axis measures personality tendencies represented by the `E` axis in the HEXACO model.
**Facets**: `E_anxiety` (불안 / Anxiety), `E_dependence` (의존성 / Dependence), `E_fearfulness` (두려움 / Fearfulness), `E_sentimentality` (감상성 / Sentimentality)

## Traits

<a id="f_fearful"></a>
### Fearful (겁 많은) — `f_fearful`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `E_fearfulness` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1 | no change |
| Behavior | combat | 0.8 | -20% combat weight |
| Behavior | explore | 0.75 | -25% explore weight |
| Behavior | flee | 1.3 | +30% flee weight |
| Behavior | gather | 1.05 | +5% gather weight |
| Emotion | fear_decay_mult | 0.85 | -15% fear decay mult |
| Emotion | fear_sensitivity | 1.4 | +40% fear sensitivity |
| Relationship | protect_seeking_mult | 1.2 | +20% protect seeking mult |
| Relationship | trust_gain_mult | 1.05 | +5% trust gain mult |
| Work | quality_mult | 1.02 | +2% quality mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Combat | flee_threshold_mult | 1.25 | +25% flee threshold mult |
| Combat | morale_mult | 0.95 | -5% morale mult |
| Combat | risk_taking_mult | 0.75 | -25% risk taking mult |
| Stress | break_threshold_mult | 0.9 | -10% break threshold mult |
| Stress | stress_gain_mult | 1.25 | +25% stress gain mult |
| Stress | violation: charge | 18 | +18 stress when charge |
| Stress | violation: stay_in_danger | 16 | +16 stress when stay_in_danger |

**Amplified behaviors**: `flee`, `gather`
**Suppressed behaviors**: `combat`, `explore`
**Emotion sensitivities**: `fear_decay_mult (0.85)`, `fear_sensitivity (1.4)`
**Violation stress triggers**: `charge (+18)`, `stay_in_danger (+16)`

**Synergies**: [`f_prudent`](C.md#f_prudent), [`c_survivalist`](#c_survivalist)
**Anti-synergies**: [`f_fearless`](#f_fearless), [`c_berserker`](A.md#c_berserker)

📄 source: `extracted/trait_data.json`

---

<a id="f_fearless"></a>
### Fearless (겁 없는) — `f_fearless`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `E_fearfulness` direction `low` threshold `0.12`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | explore | 1.25 | +25% explore weight |
| Behavior | flee | 0.75 | -25% flee weight |
| Emotion | fear_decay_mult | 1.1 | +10% fear decay mult |
| Emotion | fear_sensitivity | 0.75 | -25% fear sensitivity |
| Relationship | intimidation_resistance_mult | 1.2 | +20% intimidation resistance mult |
| Relationship | trust_gain_mult | 0.98 | -2% trust gain mult |
| Work | quality_mult | 0.98 | -2% quality mult |
| Work | speed_mult | 1.05 | +5% speed mult |
| Combat | flee_threshold_mult | 0.8 | -20% flee threshold mult |
| Combat | morale_mult | 1.1 | +10% morale mult |
| Combat | risk_taking_mult | 1.25 | +25% risk taking mult |
| Stress | break_threshold_mult | 1.1 | +10% break threshold mult |
| Stress | stress_gain_mult | 0.9 | -10% stress gain mult |
| Stress | violation: avoid_risk | 10 | +10 stress when avoid_risk |
| Stress | violation: retreat | 12 | +12 stress when retreat |

**Amplified behaviors**: `combat`, `explore`
**Suppressed behaviors**: `flee`
**Emotion sensitivities**: `fear_decay_mult (1.1)`, `fear_sensitivity (0.75)`
**Violation stress triggers**: `avoid_risk (+10)`, `retreat (+12)`

**Synergies**: [`f_bold`](X.md#f_bold), [`c_ex_lh_daredevil`](#c_ex_lh_daredevil)
**Anti-synergies**: [`f_fearful`](#f_fearful)

📄 source: `extracted/trait_data.json`

---

<a id="f_anxious"></a>
### Anxious (불안한) — `f_anxious`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `E_anxiety` direction `high` threshold `0.9`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | explore | 0.85 | -15% explore weight |
| Behavior | plan | 1.25 | +25% plan weight |
| Behavior | research | 1.05 | +5% research weight |
| Behavior | social | 0.95 | -5% social weight |
| Emotion | anxiety_baseline | 0.05 | -95% anxiety baseline |
| Emotion | fear_sensitivity | 1.25 | +25% fear sensitivity |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | reassurance_seeking_mult | 1.25 | +25% reassurance seeking mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | error_rate_mult | 0.9 | -10% error rate mult |
| Work | quality_mult | 1.05 | +5% quality mult |
| Work | speed_mult | 0.92 | -8% speed mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | morale_mult | 0.95 | -5% morale mult |
| Stress | break_threshold_mult | 0.85 | -15% break threshold mult |
| Stress | stress_gain_mult | 1.3 | +30% stress gain mult |
| Stress | stress_recovery_mult | 0.9 | -10% stress recovery mult |
| Stress | violation: enter_unknown | 14 | +14 stress when enter_unknown |
| Stress | violation: improvise | 12 | +12 stress when improvise |

**Amplified behaviors**: `plan`, `research`
**Suppressed behaviors**: `explore`, `social`
**Emotion sensitivities**: `anxiety_baseline (0.05)`, `fear_sensitivity (1.25)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: `enter_unknown (+14)`, `improvise (+12)`

**Synergies**: [`f_organized`](C.md#f_organized), [`c_ec_hh_anxious_planner`](#c_ec_hh_anxious_planner)
**Anti-synergies**: [`f_calm`](#f_calm)

📄 source: `extracted/trait_data.json`

---

<a id="f_calm"></a>
### Calm (침착한) — `f_calm`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `E_anxiety` direction `low` threshold `0.16`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | social | 1.05 | +5% social weight |
| Emotion | anxiety_baseline | -0.03 | -103% anxiety baseline |
| Emotion | fear_decay_mult | 1.1 | +10% fear decay mult |
| Emotion | fear_sensitivity | 0.8 | -20% fear sensitivity |
| Relationship | conflict_mult | 0.95 | -5% conflict mult |
| Relationship | trust_gain_mult | 1.05 | +5% trust gain mult |
| Work | quality_mult | 1 | no change |
| Work | speed_mult | 1.05 | +5% speed mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.1 | +10% morale mult |
| Stress | break_threshold_mult | 1.1 | +10% break threshold mult |
| Stress | stress_gain_mult | 0.85 | -15% stress gain mult |
| Stress | stress_recovery_mult | 1.15 | +15% stress recovery mult |
| Stress | violation: panic | 10 | +10 stress when panic |

**Amplified behaviors**: `combat`, `explore`, `social`
**Suppressed behaviors**: none
**Emotion sensitivities**: `anxiety_baseline (-0.03)`, `fear_decay_mult (1.1)`, `fear_sensitivity (0.8)`
**Violation stress triggers**: `panic (+10)`

**Synergies**: [`f_prudent`](C.md#f_prudent), [`c_born_leader`](X.md#c_born_leader)
**Anti-synergies**: [`f_anxious`](#f_anxious)

📄 source: `extracted/trait_data.json`

---

<a id="f_dependent"></a>
### Dependent (의존적인) — `f_dependent`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `E_dependence` direction `high` threshold `0.9`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | explore | 0.85 | -15% explore weight |
| Behavior | leadership | 0.9 | -10% leadership weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | fear_sensitivity | 1.1 | +10% fear sensitivity |
| Emotion | sadness_baseline | 0.03 | -97% sadness baseline |
| Relationship | attachment_gain_mult | 1.3 | +30% attachment gain mult |
| Relationship | jealousy_mult | 1.2 | +20% jealousy mult |
| Relationship | trust_gain_mult | 1.1 | +10% trust gain mult |
| Relationship | trust_loss_mult | 1.15 | +15% trust loss mult |
| Work | solo_efficiency_mult | 0.95 | -5% solo efficiency mult |
| Work | teamwork_efficiency_mult | 1.1 | +10% teamwork efficiency mult |
| Combat | flee_threshold_mult | 1.1 | +10% flee threshold mult |
| Combat | stay_near_allies_mult | 1.25 | +25% stay near allies mult |
| Stress | isolation_stress_mult | 1.4 | +40% isolation stress mult |
| Stress | stress_gain_mult | 1.1 | +10% stress gain mult |
| Stress | stress_recovery_mult | 1.05 | +5% stress recovery mult |
| Stress | violation: go_solo | 12 | +12 stress when go_solo |
| Stress | violation: refuse_help | 10 | +10 stress when refuse_help |

**Amplified behaviors**: `nurture`, `social`
**Suppressed behaviors**: `explore`, `leadership`
**Emotion sensitivities**: `fear_sensitivity (1.1)`, `sadness_baseline (0.03)`
**Violation stress triggers**: `go_solo (+12)`, `refuse_help (+10)`

**Synergies**: [`f_gregarious`](X.md#f_gregarious), [`c_caregiver`](#c_caregiver)
**Anti-synergies**: [`f_self_reliant`](#f_self_reliant)

📄 source: `extracted/trait_data.json`

---

<a id="f_self_reliant"></a>
### Self‑Reliant (독립적인) — `f_self_reliant`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `E_dependence` direction `low` threshold `0.16`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | social | 0.9 | -10% social weight |
| Emotion | fear_baseline | -0.02 | -102% fear baseline |
| Emotion | sadness_baseline | -0.01 | -101% sadness baseline |
| Relationship | attachment_gain_mult | 0.85 | -15% attachment gain mult |
| Relationship | help_seeking_mult | 0.75 | -25% help seeking mult |
| Relationship | trust_loss_mult | 0.95 | -5% trust loss mult |
| Work | solo_efficiency_mult | 1.1 | +10% solo efficiency mult |
| Work | teamwork_efficiency_mult | 0.9 | -10% teamwork efficiency mult |
| Combat | morale_when_isolated_mult | 1.1 | +10% morale when isolated mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Stress | isolation_stress_mult | 0.8 | -20% isolation stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | stress_recovery_mult | 1.05 | +5% stress recovery mult |
| Stress | violation: cling | 10 | +10 stress when cling |
| Stress | violation: seek_reassurance | 8 | +8 stress when seek_reassurance |

**Amplified behaviors**: `explore`, `leadership`
**Suppressed behaviors**: `social`
**Emotion sensitivities**: `fear_baseline (-0.02)`, `sadness_baseline (-0.01)`
**Violation stress triggers**: `cling (+10)`, `seek_reassurance (+8)`

**Synergies**: [`f_solitary`](X.md#f_solitary), [`c_survivalist`](#c_survivalist)
**Anti-synergies**: [`f_dependent`](#f_dependent)

📄 source: `extracted/trait_data.json`

---

<a id="f_sentimental"></a>
### Sentimental (다정한) — `f_sentimental`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `E_sentimentality` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 0.9 | -10% combat weight |
| Behavior | help | 1.2 | +20% help weight |
| Behavior | nurture | 1.25 | +25% nurture weight |
| Behavior | social | 1.05 | +5% social weight |
| Behavior | steal | 0.85 | -15% steal weight |
| Emotion | joy_bonding_sensitivity | 1.2 | +20% joy bonding sensitivity |
| Emotion | sadness_sensitivity | 1.25 | +25% sadness sensitivity |
| Relationship | empathy_mult | 1.3 | +30% empathy mult |
| Relationship | intimacy_gain_mult | 1.25 | +25% intimacy gain mult |
| Relationship | trust_gain_mult | 1.1 | +10% trust gain mult |
| Work | care_task_quality_mult | 1.15 | +15% care task quality mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Combat | aggression_mult | 0.85 | -15% aggression mult |
| Combat | flee_threshold_mult | 1.1 | +10% flee threshold mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_from_others_harm_mult | 1.3 | +30% stress from others harm mult |
| Stress | stress_gain_mult | 1.1 | +10% stress gain mult |
| Stress | violation: harm_innocent | 20 | +20 stress when harm_innocent |
| Stress | violation: neglect_child | 18 | +18 stress when neglect_child |

**Amplified behaviors**: `help`, `nurture`, `social`
**Suppressed behaviors**: `combat`, `steal`
**Emotion sensitivities**: `joy_bonding_sensitivity (1.2)`, `sadness_sensitivity (1.25)`
**Violation stress triggers**: `harm_innocent (+20)`, `neglect_child (+18)`

**Synergies**: [`f_gentle`](A.md#f_gentle), [`f_forgiving`](A.md#f_forgiving), [`c_caregiver`](#c_caregiver)
**Anti-synergies**: [`f_tough_minded`](#f_tough_minded), [`d_psychopath_primary`](H.md#d_psychopath_primary)

📄 source: `extracted/trait_data.json`

---

<a id="f_tough_minded"></a>
### Tough‑Minded (무정한) — `f_tough_minded`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `E_sentimentality` direction `low` threshold `0.14`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.1 | +10% combat weight |
| Behavior | help | 0.9 | -10% help weight |
| Behavior | nurture | 0.85 | -15% nurture weight |
| Emotion | fear_sensitivity | 0.9 | -10% fear sensitivity |
| Emotion | sadness_sensitivity | 0.8 | -20% sadness sensitivity |
| Relationship | empathy_mult | 0.75 | -25% empathy mult |
| Relationship | intimacy_gain_mult | 0.85 | -15% intimacy gain mult |
| Relationship | trust_gain_mult | 0.95 | -5% trust gain mult |
| Work | quality_mult | 0.98 | -2% quality mult |
| Work | speed_mult | 1.03 | +3% speed mult |
| Combat | aggression_mult | 1.1 | +10% aggression mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_from_others_harm_mult | 0.8 | -20% stress from others harm mult |
| Stress | stress_gain_mult | 0.9 | -10% stress gain mult |
| Stress | violation: comfort | 8 | +8 stress when comfort |
| Stress | violation: show_vulnerability | 10 | +10 stress when show_vulnerability |

**Amplified behaviors**: `combat`
**Suppressed behaviors**: `help`, `nurture`
**Emotion sensitivities**: `fear_sensitivity (0.9)`, `sadness_sensitivity (0.8)`
**Violation stress triggers**: `comfort (+8)`, `show_vulnerability (+10)`

**Synergies**: [`f_fearless`](#f_fearless), [`c_ec_lh_cool_strategist`](#c_ec_lh_cool_strategist)
**Anti-synergies**: [`f_sentimental`](#f_sentimental)

📄 source: `extracted/trait_data.json`

---

<a id="c_ex_hh_emotional_socialite"></a>
### Emotional Socialite (감정형 사교가) — `c_ex_hh_emotional_socialite`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `E` direction `high` threshold `0.75`
- Facet `X` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.127 | +13% stress gain mult |

**Amplified behaviors**: `flee`, `leadership`, `nurture`, `social`
**Suppressed behaviors**: `explore`
**Emotion sensitivities**: `fear_sensitivity (1.2)`, `joy_baseline (0.02)`, `sadness_sensitivity (1.1)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_hx_hh_honest_leader`](H.md#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler), [`c_xc_hl_charming_improviser`](X.md#c_xc_hl_charming_improviser)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ex_hl_timid_recluse"></a>
### Timid Recluse (소심한 은둔자) — `c_ex_hl_timid_recluse`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `E` direction `high` threshold `0.75`
- Facet `X` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | research | 1.05 | +5% research weight |
| Behavior | social | 0.72 | -28% social weight |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | social_stress_mult | 1.21 | +21% social stress mult |
| Stress | stress_gain_mult | 1.15 | +15% stress gain mult |

**Amplified behaviors**: `craft`, `flee`, `nurture`, `research`
**Suppressed behaviors**: `explore`, `social`
**Emotion sensitivities**: `fear_sensitivity (1.2)`, `joy_baseline (-0.01)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`f_reserved`](X.md#f_reserved), [`f_insecure`](X.md#f_insecure), [`f_dependent`](#f_dependent)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ex_lh_daredevil"></a>
### Daredevil (대담한 모험가) — `c_ex_lh_daredevil`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `E` direction `low` threshold `0.25`
- Facet `X` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | explore | 1.21 | +21% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.1025 | +10% morale mult |
| Combat | risk_taking_mult | 1.265 | +26% risk taking mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.882 | -12% stress gain mult |

**Amplified behaviors**: `combat`, `explore`, `leadership`, `social`
**Suppressed behaviors**: `flee`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `joy_baseline (0.02)`, `sadness_sensitivity (0.9)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_ea_lh_volatile_bully`](#c_ea_lh_volatile_bully), [`c_hx_hh_honest_leader`](H.md#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ex_ll_stoic_loner"></a>
### Stoic Loner (냉정한 독립가) — `c_ex_ll_stoic_loner`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `E` direction `low` threshold `0.25`
- Facet `X` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | research | 1.05 | +5% research weight |
| Behavior | social | 0.8 | -20% social weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | social_stress_mult | 1.1 | +10% social stress mult |
| Stress | stress_gain_mult | 0.9 | -10% stress gain mult |

**Amplified behaviors**: `combat`, `craft`, `explore`, `research`
**Suppressed behaviors**: `flee`, `social`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `joy_baseline (-0.01)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_ea_lh_volatile_bully`](#c_ea_lh_volatile_bully), [`f_reserved`](X.md#f_reserved), [`f_insecure`](X.md#f_insecure)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ea_hh_compassionate_reconciler"></a>
### Compassionate Reconciler (다정한 화해자) — `c_ea_hh_compassionate_reconciler`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `E` direction `high` threshold `0.75`
- Facet `A` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.0925 | +9% stress gain mult |

**Amplified behaviors**: `cooperate`, `flee`, `help`, `nurture`
**Suppressed behaviors**: `combat`, `explore`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `fear_sensitivity (1.2)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`f_flexible`](A.md#f_flexible), [`c_ea_lh_volatile_bully`](#c_ea_lh_volatile_bully), [`c_reconciler`](A.md#c_reconciler)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ea_hl_timid_helper"></a>
### Timid Helper (소심한 조력자) — `c_ea_hl_timid_helper`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `E` direction `high` threshold `0.75`
- Facet `A` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.945 | -5% risk taking mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.15 | +15% stress gain mult |

**Amplified behaviors**: `combat`, `flee`, `intimidate`, `nurture`, `revenge`
**Suppressed behaviors**: `cooperate`, `explore`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `fear_sensitivity (1.2)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`f_dependent`](#f_dependent), [`c_he_lh_anxious_swindler`](H.md#c_he_lh_anxious_swindler), [`f_anxious`](#f_anxious)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ea_lh_volatile_bully"></a>
### Volatile Bully (변덕스러운 폭군) — `c_ea_lh_volatile_bully`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `E` direction `low` threshold `0.25`
- Facet `A` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 0.9975 | -0% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.855 | -15% stress gain mult |

**Amplified behaviors**: `cooperate`, `explore`, `help`
**Suppressed behaviors**: `combat`, `flee`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `fear_sensitivity (0.85)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`f_flexible`](A.md#f_flexible), [`c_reconciler`](A.md#c_reconciler), [`c_chef`](O.md#c_chef)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ea_ll_callous_abuser"></a>
### Callous Abuser (냉혈한 학대자) — `c_ea_ll_callous_abuser`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `E` direction `low` threshold `0.25`
- Facet `A` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.2075 | +21% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | steal | 1.1 | +10% steal weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | trust_gain_mult | 0.9 | -10% trust gain mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.155 | +16% risk taking mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.9 | -10% stress gain mult |

**Amplified behaviors**: `combat`, `explore`, `intimidate`, `revenge`, `steal`
**Suppressed behaviors**: `cooperate`, `flee`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `fear_sensitivity (0.85)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_ea_lh_volatile_bully`](#c_ea_lh_volatile_bully), [`c_he_hl_stoic_honest`](H.md#c_he_hl_stoic_honest), [`c_ec_lh_cool_strategist`](#c_ec_lh_cool_strategist)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ec_hh_anxious_planner"></a>
### Anxious Planner (걱정 많은 계획가) — `c_ec_hh_anxious_planner`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `E` direction `high` threshold `0.75`
- Facet `C` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.078 | +8% speed mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.0925 | +9% stress gain mult |

**Amplified behaviors**: `build`, `flee`, `gather`, `nurture`, `plan`, `research`
**Suppressed behaviors**: `explore`
**Emotion sensitivities**: `fear_sensitivity (1.2)`, `impulse_control_mult (1.1)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_strategist_general`](C.md#c_strategist_general), [`f_dependent`](#f_dependent), [`f_prudent`](C.md#f_prudent)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ec_hl_anxious_drifter"></a>
### Anxious Drifter (불안한 방랑자) — `c_ec_hl_anxious_drifter`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `E` direction `high` threshold `0.75`
- Facet `C` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.9 | -10% build weight |
| Behavior | explore | 0.9975 | -0% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 0.9 | -10% research weight |
| Behavior | social | 0.9 | -10% social weight |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | speed_mult | 0.931 | -7% speed mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | social_stress_mult | 1.1 | +10% social stress mult |
| Stress | stress_gain_mult | 1.2075 | +21% stress gain mult |

**Amplified behaviors**: `flee`, `nurture`
**Suppressed behaviors**: `build`, `explore`, `plan`, `research`, `social`
**Emotion sensitivities**: `fear_sensitivity (1.2)`, `impulse_control_mult (0.9)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_xc_hl_charming_improviser`](X.md#c_xc_hl_charming_improviser), [`f_dependent`](#f_dependent), [`c_he_lh_anxious_swindler`](H.md#c_he_lh_anxious_swindler)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ec_lh_cool_strategist"></a>
### Cool Strategist (침착한 전략가) — `c_ec_lh_cool_strategist`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `E` direction `low` threshold `0.25`
- Facet `C` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
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

**Amplified behaviors**: `build`, `combat`, `explore`, `gather`, `plan`, `research`
**Suppressed behaviors**: `flee`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `impulse_control_mult (1.1)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_strategist_general`](C.md#c_strategist_general), [`f_prudent`](C.md#f_prudent), [`c_xc_lh_silent_craftsman`](X.md#c_xc_lh_silent_craftsman)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ec_ll_reckless_drifter"></a>
### Reckless Drifter (무모한 방랑자) — `c_ec_ll_reckless_drifter`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `E` direction `low` threshold `0.25`
- Facet `C` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.9 | -10% build weight |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | explore | 1.2705 | +27% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 0.9 | -10% research weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | speed_mult | 0.969 | -3% speed mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.265 | +26% risk taking mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.945 | -5% stress gain mult |

**Amplified behaviors**: `combat`, `explore`
**Suppressed behaviors**: `build`, `flee`, `plan`, `research`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `impulse_control_mult (0.9)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_ea_lh_volatile_bully`](#c_ea_lh_volatile_bully), [`c_xc_hl_charming_improviser`](X.md#c_xc_hl_charming_improviser), [`c_he_hl_stoic_honest`](H.md#c_he_hl_stoic_honest)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_eo_hh_sensitive_artist"></a>
### Sensitive Artist (감성 예술가) — `c_eo_hh_sensitive_artist`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `E` direction `high` threshold `0.75`
- Facet `O` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.045 | +4% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | research | 1.15 | +15% research weight |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 1.15 | +15% stress gain mult |

**Amplified behaviors**: `craft`, `explore`, `flee`, `nurture`, `research`
**Suppressed behaviors**: none
**Emotion sensitivities**: `fear_sensitivity (1.2)`, `interest_sensitivity (1.1)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_strategist_general`](C.md#c_strategist_general), [`f_dependent`](#f_dependent), [`c_he_lh_anxious_swindler`](H.md#c_he_lh_anxious_swindler)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_eo_hl_anxious_traditionalist"></a>
### Anxious Traditionalist (불안한 전통주의자) — `c_eo_hl_anxious_traditionalist`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `E` direction `high` threshold `0.75`
- Facet `O` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | research | 0.95 | -5% research weight |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 1.15 | +15% stress gain mult |

**Amplified behaviors**: `build`, `flee`, `leadership`, `nurture`
**Suppressed behaviors**: `explore`, `research`
**Emotion sensitivities**: `fear_sensitivity (1.2)`, `novelty_fear_sensitivity (1.05)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`f_dependent`](#f_dependent), [`c_he_lh_anxious_swindler`](H.md#c_he_lh_anxious_swindler), [`f_anxious`](#f_anxious)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_eo_lh_cold_experimenter"></a>
### Cold Experimenter (실험적 냉혈가) — `c_eo_lh_cold_experimenter`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `E` direction `low` threshold `0.25`
- Facet `O` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.21 | +21% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | research | 1.15 | +15% research weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.9 | -10% stress gain mult |

**Amplified behaviors**: `combat`, `craft`, `explore`, `research`
**Suppressed behaviors**: `flee`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `interest_sensitivity (1.1)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_ea_lh_volatile_bully`](#c_ea_lh_volatile_bully), [`c_strategist_general`](C.md#c_strategist_general), [`c_chef`](O.md#c_chef)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_eo_ll_unfeeling_realist"></a>
### Unfeeling Realist (무감각한 현실주의자) — `c_eo_ll_unfeeling_realist`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `E` direction `low` threshold `0.25`
- Facet `O` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | research | 0.95 | -5% research weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 0.9 | -10% stress gain mult |

**Amplified behaviors**: `build`, `combat`, `explore`, `leadership`
**Suppressed behaviors**: `flee`, `research`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `novelty_fear_sensitivity (1.05)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_ea_lh_volatile_bully`](#c_ea_lh_volatile_bully), [`c_he_hl_stoic_honest`](H.md#c_he_hl_stoic_honest), [`d_cult_leader`](H.md#d_cult_leader)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_cold_dictator"></a>
### Cold‑Blooded Dictator (냉혈한 독재자) — `c_cold_dictator`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `E` direction `low` threshold `0.3`
- Facet `X` direction `high` threshold `0.7`
- Facet `A` direction `low` threshold `0.3`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.3283 | +33% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | intimidate | 1.44 | +44% intimidate weight |
| Behavior | leadership | 1.4375 | +44% leadership weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | fear_sensitivity | 0.68 | -32% fear sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Work | teamwork_efficiency_mult | 0.9975 | -0% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.2679 | +27% morale mult |
| Combat | risk_taking_mult | 1.2705 | +27% risk taking mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.7938 | -21% stress gain mult |

**Amplified behaviors**: `combat`, `explore`, `intimidate`, `leadership`, `revenge`, `social`
**Suppressed behaviors**: `cooperate`, `flee`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `fear_sensitivity (0.68)`, `joy_baseline (0.02)`, `sadness_sensitivity (0.9)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`f_fearless`](#f_fearless), [`f_harsh`](A.md#f_harsh)
**Anti-synergies**: [`c_reconciler`](A.md#c_reconciler)

📄 source: `extracted/trait_data.json`

---

<a id="c_caregiver"></a>
### Caregiver (양육자) — `c_caregiver`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `E` direction `high` threshold `0.7`
- Facet `A` direction `high` threshold `0.7`
- Facet `C` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | heal | 1.25 | +25% heal weight |
| Behavior | help | 1.32 | +32% help weight |
| Behavior | nurture | 1.4175 | +42% nurture weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | intimacy_gain_mult | 1.2 | +20% intimacy gain mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | care_task_quality_mult | 1.2 | +20% care task quality mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.078 | +8% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.0379 | +4% stress gain mult |

**Amplified behaviors**: `build`, `cooperate`, `flee`, `gather`, `heal`, `help`, `nurture`, `plan`, `research`
**Suppressed behaviors**: `combat`, `explore`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `fear_sensitivity (1.2)`, `impulse_control_mult (1.1)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`f_sentimental`](#f_sentimental), [`f_gentle`](A.md#f_gentle), [`c_saintess`](H.md#c_saintess)
**Anti-synergies**: [`d_callous`](H.md#d_callous), [`d_sadist`](H.md#d_sadist)

📄 source: `extracted/trait_data.json`

---

<a id="c_adventurer"></a>
### Adventurer (모험가) — `c_adventurer`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `E` direction `low` threshold `0.3`
- Facet `X` direction `high` threshold `0.7`
- Facet `O` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.155 | +16% combat weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.6335 | +63% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | research | 1.2075 | +21% research weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.1025 | +10% morale mult |
| Combat | risk_taking_mult | 1.375 | +38% risk taking mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Stress | boredom_stress_mult | 1.25 | +25% boredom stress mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.882 | -12% stress gain mult |

**Amplified behaviors**: `combat`, `craft`, `explore`, `leadership`, `research`, `social`
**Suppressed behaviors**: `flee`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `interest_sensitivity (1.1)`, `joy_baseline (0.02)`, `sadness_sensitivity (0.9)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`f_bold`](X.md#f_bold), [`f_creative`](O.md#f_creative)
**Anti-synergies**: [`f_fearful`](#f_fearful)

📄 source: `extracted/trait_data.json`

---

<a id="c_survivalist"></a>
### Survivalist (생존 전문가) — `c_survivalist`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `E` direction `high` threshold `0.7`
- Facet `C` direction `high` threshold `0.7`
- Facet `O` direction `low` threshold `0.3`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.2128 | +21% build weight |
| Behavior | explore | 0.855 | -15% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | gather | 1.21 | +21% gather weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | plan | 1.38 | +38% plan weight |
| Behavior | research | 1.045 | +4% research weight |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.078 | +8% speed mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | flee_threshold_mult | 1.3225 | +32% flee threshold mult |
| Combat | risk_taking_mult | 0.765 | -24% risk taking mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 1.1471 | +15% stress gain mult |

**Amplified behaviors**: `build`, `flee`, `gather`, `leadership`, `nurture`, `plan`, `research`
**Suppressed behaviors**: `explore`
**Emotion sensitivities**: `fear_sensitivity (1.2)`, `impulse_control_mult (1.1)`, `novelty_fear_sensitivity (1.05)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`f_prudent`](C.md#f_prudent), [`f_fearful`](#f_fearful)
**Anti-synergies**: [`c_adventurer`](#c_adventurer)

📄 source: `extracted/trait_data.json`

---

<a id="c_assault_captain"></a>
### Assault Captain (돌격대장) — `c_assault_captain`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `E` direction `low` threshold `0.25`
- Facet `A` direction `low` threshold `0.25`
- Facet `X_social_boldness` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 1.6301 | +63% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.72 | -28% flee weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | social | 1.2 | +20% social weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Work | teamwork_efficiency_mult | 0.9975 | -0% teamwork efficiency mult |
| Combat | aggression_mult | 1.5525 | +55% aggression mult |
| Combat | flee_threshold_mult | 0.765 | -24% flee threshold mult |
| Combat | morale_mult | 1.1025 | +10% morale mult |
| Combat | risk_taking_mult | 1.4438 | +44% risk taking mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.882 | -12% stress gain mult |
| Stress | violation: retreat | 12 | +12 stress when retreat |

**Amplified behaviors**: `combat`, `explore`, `intimidate`, `leadership`, `revenge`, `social`
**Suppressed behaviors**: `cooperate`, `flee`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `fear_sensitivity (0.85)`, `joy_baseline (0.02)`, `sadness_sensitivity (0.9)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: `retreat (+12)`

**Synergies**: [`c_berserker`](A.md#c_berserker), [`f_bold`](X.md#f_bold)
**Anti-synergies**: [`c_pacifist`](A.md#c_pacifist)

📄 source: `extracted/trait_data.json`

---

<a id="c_healer"></a>
### Healer (치유자) — `c_healer`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `E` direction `high` threshold `0.75`
- Facet `A` direction `high` threshold `0.75`
- Facet `E_sentimentality` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | combat | 0.855 | -15% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | heal | 1.5 | +50% heal weight |
| Behavior | help | 1.32 | +32% help weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | care_task_quality_mult | 1.25 | +25% care task quality mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.0925 | +9% stress gain mult |

**Amplified behaviors**: `cooperate`, `flee`, `heal`, `help`, `nurture`
**Suppressed behaviors**: `combat`, `explore`, `revenge`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `fear_sensitivity (1.2)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_caregiver`](#c_caregiver), [`c_saintess`](H.md#c_saintess)
**Anti-synergies**: [`d_callous`](H.md#d_callous)

📄 source: `extracted/trait_data.json`

---

<a id="c_scout"></a>
### Scout (정찰꾼) — `c_scout`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `E` direction `low` threshold `0.25`
- Facet `O` direction `high` threshold `0.75`
- Facet `C_prudence` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 1.1025 | +10% combat weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.6335 | +63% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | gather | 1.155 | +16% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.265 | +26% research weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.21 | +21% learning speed mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.122 | +12% speed mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.21 | +21% risk taking mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.855 | -15% stress gain mult |

**Amplified behaviors**: `build`, `combat`, `craft`, `explore`, `gather`, `plan`, `research`
**Suppressed behaviors**: `flee`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_adventurer`](#c_adventurer), [`c_survivalist`](#c_survivalist)
**Anti-synergies**: [`f_fearful`](#f_fearful)

📄 source: `extracted/trait_data.json`

---

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
