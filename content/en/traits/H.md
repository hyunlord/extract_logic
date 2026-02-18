---
title: "Honesty-Humility (H) Traits"
description: "Trait breakdown for Honesty-Humility (H)."
generated: true
source_files:
  - "extracted/trait_data.json"
  - "data/species/human/personality/trait_definitions.json"
nav_order: 11
---

# Honesty-Humility (H) — 정직-겸손

## Axis Overview

The **Honesty-Humility** axis measures personality tendencies represented by the `H` axis in the HEXACO model.
**Facets**: `H_fairness` (공정성 / Fairness), `H_greed_avoidance` (탐욕 회피 / Greed Avoidance), `H_modesty` (겸손 / Modesty), `H_sincerity` (진실성 / Sincerity)

## Trait Effects

<a id="f_sincere"></a>
### Sincere (진실한) — `f_sincere`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H_sincerity` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.75 | -25% betray weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | social | 1.1 | +10% social weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | anger_sensitivity | 0.95 | -5% anger sensitivity |
| Emotion | guilt_sensitivity | 1.2 | +20% guilt sensitivity |
| Emotion | shame_sensitivity | 1.1 | +10% shame sensitivity |
| Relationship | betrayal_propensity_mult | 0.6 | -40% betrayal propensity mult |
| Relationship | trust_gain_mult | 1.25 | +25% trust gain mult |
| Relationship | trust_loss_mult | 0.85 | -15% trust loss mult |
| Work | error_rate_mult | 0.95 | -5% error rate mult |
| Work | quality_mult | 1.05 | +5% quality mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Combat | aggression_mult | 0.95 | -5% aggression mult |
| Combat | morale_mult | 1.02 | +2% morale mult |
| Combat | war_crime_propensity_mult | 0.6 | -40% war crime propensity mult |
| Stress | break_threshold_mult | 0.98 | -2% break threshold mult |
| Stress | stress_gain_mult | 1.05 | +5% stress gain mult |
| Stress | stress_recovery_mult | 1 | no change |
| Stress | violation: deceive | 12 | +12 stress when deceive |
| Stress | violation: lie | 14 | +14 stress when lie |
| Stress | violation: take_bribe | 18 | +18 stress when take_bribe |

**Amplified behaviors**: `leadership`, `social`
**Suppressed behaviors**: `betray`, `steal`
**Emotion sensitivities**: `anger_sensitivity (0.95)`, `guilt_sensitivity (1.2)`, `shame_sensitivity (1.1)`
**Violation stress triggers**: `deceive (+12)`, `lie (+14)`, `take_bribe (+18)`

**Synergies**: [`f_fair_minded`](#f_fair_minded), [`f_modest`](#f_modest), [`f_forgiving`](A.md#f_forgiving)
**Anti-synergies**: [`f_deceptive`](#f_deceptive), [`f_corrupt`](#f_corrupt), [`d_con_artist`](#d_con_artist)

📄 source: `extracted/trait_data.json`

---

<a id="f_deceptive"></a>
### Deceptive (기만적인) — `f_deceptive`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H_sincerity` direction `low` threshold `0.14`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.4 | +40% betray weight |
| Behavior | leadership | 1.1 | +10% leadership weight |
| Behavior | social | 1.05 | +5% social weight |
| Behavior | steal | 1.25 | +25% steal weight |
| Emotion | anger_sensitivity | 1.05 | +5% anger sensitivity |
| Emotion | guilt_sensitivity | 0.7 | -30% guilt sensitivity |
| Emotion | shame_sensitivity | 0.8 | -20% shame sensitivity |
| Relationship | betrayal_propensity_mult | 1.4 | +40% betrayal propensity mult |
| Relationship | trust_gain_mult | 0.75 | -25% trust gain mult |
| Relationship | trust_loss_mult | 1.2 | +20% trust loss mult |
| Work | error_rate_mult | 1.05 | +5% error rate mult |
| Work | quality_mult | 0.95 | -5% quality mult |
| Work | speed_mult | 1.03 | +3% speed mult |
| Combat | aggression_mult | 1 | no change |
| Combat | ambush_propensity_mult | 1.3 | +30% ambush propensity mult |
| Combat | flee_threshold_mult | 0.95 | -5% flee threshold mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | stress_recovery_mult | 1.05 | +5% stress recovery mult |
| Stress | violation: confess | 10 | +10 stress when confess |
| Stress | violation: return_stolen | 16 | +16 stress when return_stolen |
| Stress | violation: tell_truth | 8 | +8 stress when tell_truth |

**Amplified behaviors**: `betray`, `leadership`, `social`, `steal`
**Suppressed behaviors**: none
**Emotion sensitivities**: `anger_sensitivity (1.05)`, `guilt_sensitivity (0.7)`, `shame_sensitivity (0.8)`
**Violation stress triggers**: `confess (+10)`, `return_stolen (+16)`, `tell_truth (+8)`

**Synergies**: [`f_corrupt`](#f_corrupt), [`f_greedy`](#f_greedy), [`f_reckless`](C.md#f_reckless)
**Anti-synergies**: [`f_sincere`](#f_sincere), [`f_fair_minded`](#f_fair_minded)

📄 source: `extracted/trait_data.json`

---

<a id="f_fair_minded"></a>
### Fair‑Minded (원칙적인) — `f_fair_minded`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H_fairness` direction `high` threshold `0.94`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | leadership | 1.1 | +10% leadership weight |
| Behavior | share | 1.15 | +15% share weight |
| Behavior | steal | 0.55 | -45% steal weight |
| Behavior | trade | 1.05 | +5% trade weight |
| Emotion | anger_injustice_sensitivity | 1.25 | +25% anger injustice sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Relationship | reciprocity_mult | 1.2 | +20% reciprocity mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Work | quality_mult | 1.05 | +5% quality mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Combat | aggression_mult | 0.95 | -5% aggression mult |
| Combat | war_crime_propensity_mult | 0.55 | -45% war crime propensity mult |
| Stress | break_threshold_mult | 0.97 | -3% break threshold mult |
| Stress | stress_gain_mult | 1.03 | +3% stress gain mult |
| Stress | violation: cheat | 18 | +18 stress when cheat |
| Stress | violation: frame_other | 20 | +20 stress when frame_other |
| Stress | violation: steal | 22 | +22 stress when steal |

**Amplified behaviors**: `leadership`, `share`, `trade`
**Suppressed behaviors**: `steal`
**Emotion sensitivities**: `anger_injustice_sensitivity (1.25)`, `guilt_sensitivity (1.15)`
**Violation stress triggers**: `cheat (+18)`, `frame_other (+20)`, `steal (+22)`

**Synergies**: [`f_sincere`](#f_sincere), [`f_forgiving`](A.md#f_forgiving), [`c_hx_hh_honest_leader`](#c_hx_hh_honest_leader)
**Anti-synergies**: [`f_corrupt`](#f_corrupt), [`d_machiavellian`](#d_machiavellian)

📄 source: `extracted/trait_data.json`

---

<a id="f_corrupt"></a>
### Corrupt (부패한) — `f_corrupt`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H_fairness` direction `low` threshold `0.12`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | steal | 1.6 | +60% steal weight |
| Behavior | take_bribe | 1.6 | +60% take bribe weight |
| Behavior | trade | 1.15 | +15% trade weight |
| Emotion | envy_sensitivity | 1.1 | +10% envy sensitivity |
| Emotion | guilt_sensitivity | 0.65 | -35% guilt sensitivity |
| Emotion | shame_sensitivity | 0.7 | -30% shame sensitivity |
| Relationship | intimidation_bias_mult | 1.1 | +10% intimidation bias mult |
| Relationship | trust_gain_mult | 0.65 | -35% trust gain mult |
| Relationship | trust_loss_mult | 1.25 | +25% trust loss mult |
| Work | error_rate_mult | 1.1 | +10% error rate mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | speed_mult | 1.05 | +5% speed mult |
| Combat | aggression_mult | 1.1 | +10% aggression mult |
| Combat | war_crime_propensity_mult | 1.35 | +35% war crime propensity mult |
| Stress | break_threshold_mult | 1.1 | +10% break threshold mult |
| Stress | stress_gain_mult | 0.85 | -15% stress gain mult |
| Stress | violation: refuse_bribe | 8 | +8 stress when refuse_bribe |
| Stress | violation: report_self | 16 | +16 stress when report_self |
| Stress | violation: share | 10 | +10 stress when share |

**Amplified behaviors**: `leadership`, `steal`, `take_bribe`, `trade`
**Suppressed behaviors**: none
**Emotion sensitivities**: `envy_sensitivity (1.1)`, `guilt_sensitivity (0.65)`, `shame_sensitivity (0.7)`
**Violation stress triggers**: `refuse_bribe (+8)`, `report_self (+16)`, `share (+10)`

**Synergies**: [`f_deceptive`](#f_deceptive), [`f_greedy`](#f_greedy), [`d_machiavellian`](#d_machiavellian)
**Anti-synergies**: [`f_fair_minded`](#f_fair_minded), [`f_sincere`](#f_sincere)

📄 source: `extracted/trait_data.json`

---

<a id="f_frugal"></a>
### Frugal (검소한) — `f_frugal`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H_greed_avoidance` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | hoard | 0.8 | -20% hoard weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | steal | 0.85 | -15% steal weight |
| Behavior | trade | 0.95 | -5% trade weight |
| Emotion | envy_sensitivity | 0.7 | -30% envy sensitivity |
| Emotion | joy_gain_sensitivity | 0.9 | -10% joy gain sensitivity |
| Relationship | status_seeking_mult | 0.7 | -30% status seeking mult |
| Relationship | trust_gain_mult | 1.05 | +5% trust gain mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Work | speed_mult | 1 | no change |
| Combat | aggression_mult | 0.95 | -5% aggression mult |
| Combat | loot_motivation_mult | 0.75 | -25% loot motivation mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | loss_stress_mult | 0.8 | -20% loss stress mult |
| Stress | stress_gain_mult | 0.9 | -10% stress gain mult |
| Stress | violation: extort | 16 | +16 stress when extort |
| Stress | violation: waste_resources | 12 | +12 stress when waste_resources |

**Amplified behaviors**: `share`
**Suppressed behaviors**: `hoard`, `steal`, `trade`
**Emotion sensitivities**: `envy_sensitivity (0.7)`, `joy_gain_sensitivity (0.9)`
**Violation stress triggers**: `extort (+16)`, `waste_resources (+12)`

**Synergies**: [`f_modest`](#f_modest), [`f_fair_minded`](#f_fair_minded)
**Anti-synergies**: [`f_greedy`](#f_greedy), [`c_spendthrift`](#c_spendthrift)

📄 source: `extracted/trait_data.json`

---

<a id="f_greedy"></a>
### Greedy (탐욕스러운) — `f_greedy`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H_greed_avoidance` direction `low` threshold `0.14`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | hoard | 1.25 | +25% hoard weight |
| Behavior | share | 0.85 | -15% share weight |
| Behavior | steal | 1.35 | +35% steal weight |
| Behavior | trade | 1.15 | +15% trade weight |
| Emotion | envy_sensitivity | 1.3 | +30% envy sensitivity |
| Emotion | joy_gain_sensitivity | 1.2 | +20% joy gain sensitivity |
| Emotion | loss_sensitivity | 1.2 | +20% loss sensitivity |
| Relationship | resource_conflict_mult | 1.2 | +20% resource conflict mult |
| Relationship | status_seeking_mult | 1.25 | +25% status seeking mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Work | speed_mult | 1.05 | +5% speed mult |
| Combat | loot_motivation_mult | 1.25 | +25% loot motivation mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | loss_stress_mult | 1.3 | +30% loss stress mult |
| Stress | stress_gain_mult | 1.05 | +5% stress gain mult |
| Stress | violation: donate | 14 | +14 stress when donate |
| Stress | violation: share | 10 | +10 stress when share |

**Amplified behaviors**: `hoard`, `steal`, `trade`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `envy_sensitivity (1.3)`, `joy_gain_sensitivity (1.2)`, `loss_sensitivity (1.2)`
**Violation stress triggers**: `donate (+14)`, `share (+10)`

**Synergies**: [`f_corrupt`](#f_corrupt), [`f_deceptive`](#f_deceptive), [`c_speculator`](C.md#c_speculator)
**Anti-synergies**: [`f_frugal`](#f_frugal), [`c_philanthropist`](#c_philanthropist)

📄 source: `extracted/trait_data.json`

---

<a id="f_modest"></a>
### Modest (겸손한) — `f_modest`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H_modesty` direction `high` threshold `0.92`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | leadership | 0.9 | -10% leadership weight |
| Behavior | social | 1 | no change |
| Emotion | pride_baseline | -0.05 | -105% pride baseline |
| Emotion | shame_sensitivity | 1.15 | +15% shame sensitivity |
| Relationship | respect_gain_mult | 1.05 | +5% respect gain mult |
| Relationship | status_seeking_mult | 0.7 | -30% status seeking mult |
| Relationship | trust_gain_mult | 1.1 | +10% trust gain mult |
| Work | quality_mult | 1.05 | +5% quality mult |
| Work | speed_mult | 1 | no change |
| Combat | aggression_mult | 0.95 | -5% aggression mult |
| Combat | flee_threshold_mult | 1.05 | +5% flee threshold mult |
| Stress | break_threshold_mult | 0.98 | -2% break threshold mult |
| Stress | stress_gain_mult | 1.05 | +5% stress gain mult |
| Stress | violation: abuse_power | 18 | +18 stress when abuse_power |
| Stress | violation: boast | 8 | +8 stress when boast |

**Amplified behaviors**: `help`
**Suppressed behaviors**: `leadership`
**Emotion sensitivities**: `pride_baseline (-0.05)`, `shame_sensitivity (1.15)`
**Violation stress triggers**: `abuse_power (+18)`, `boast (+8)`

**Synergies**: [`f_sincere`](#f_sincere), [`f_frugal`](#f_frugal), [`c_xa_lh_quiet_helper`](X.md#c_xa_lh_quiet_helper)
**Anti-synergies**: [`f_self_important`](#f_self_important), [`d_narcissist_grandiose`](#d_narcissist_grandiose)

📄 source: `extracted/trait_data.json`

---

<a id="f_self_important"></a>
### Self‑Important (거만한) — `f_self_important`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H_modesty` direction `low` threshold `0.16`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | dominate | 1.25 | +25% dominate weight |
| Behavior | leadership | 1.2 | +20% leadership weight |
| Behavior | social | 1.15 | +15% social weight |
| Emotion | anger_disrespect_sensitivity | 1.25 | +25% anger disrespect sensitivity |
| Emotion | pride_baseline | 0.06 | -94% pride baseline |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_loss_mult | 1.05 | +5% trust loss mult |
| Work | learning_from_failure_mult | 0.9 | -10% learning from failure mult |
| Work | quality_mult | 0.98 | -2% quality mult |
| Work | speed_mult | 1.05 | +5% speed mult |
| Combat | aggression_mult | 1.1 | +10% aggression mult |
| Combat | flee_threshold_mult | 0.85 | -15% flee threshold mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.05 | +5% stress gain mult |
| Stress | violation: apologize | 10 | +10 stress when apologize |
| Stress | violation: share_credit | 8 | +8 stress when share_credit |

**Amplified behaviors**: `dominate`, `leadership`, `social`
**Suppressed behaviors**: `cooperate`
**Emotion sensitivities**: `anger_disrespect_sensitivity (1.25)`, `pride_baseline (0.06)`
**Violation stress triggers**: `apologize (+10)`, `share_credit (+8)`

**Synergies**: [`d_narcissist_grandiose`](#d_narcissist_grandiose), [`c_born_leader`](X.md#c_born_leader)
**Anti-synergies**: [`f_modest`](#f_modest)

📄 source: `extracted/trait_data.json`

---

<a id="c_he_hh_tender_conscience"></a>
### Tender Conscience (자애로운 양심가) — `c_he_hh_tender_conscience`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H` direction `high` threshold `0.75`
- Facet `E` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.173 | +17% stress gain mult |

**Amplified behaviors**: `flee`, `help`, `nurture`, `share`
**Suppressed behaviors**: `betray`, `explore`, `steal`
**Emotion sensitivities**: `fear_sensitivity (1.2)`, `guilt_sensitivity (1.15)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_hx_hh_honest_leader`](#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler), [`f_dependent`](E.md#f_dependent)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_he_hl_stoic_honest"></a>
### Stoic Honest (냉정한 청렴가) — `c_he_hl_stoic_honest`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `H` direction `high` threshold `0.75`
- Facet `E` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.918 | -8% stress gain mult |

**Amplified behaviors**: `combat`, `explore`, `help`, `share`
**Suppressed behaviors**: `betray`, `flee`, `steal`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `guilt_sensitivity (1.15)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_ea_lh_volatile_bully`](E.md#c_ea_lh_volatile_bully), [`c_hx_hh_honest_leader`](#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_he_lh_anxious_swindler"></a>
### Anxious Swindler (불안한 사기꾼) — `c_he_lh_anxious_swindler`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `E` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.0925 | +9% stress gain mult |

**Amplified behaviors**: `betray`, `flee`, `nurture`, `steal`, `take_bribe`
**Suppressed behaviors**: `explore`, `share`
**Emotion sensitivities**: `fear_sensitivity (1.2)`, `guilt_sensitivity (0.8)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`f_dependent`](E.md#f_dependent), [`f_anxious`](E.md#f_anxious), [`c_eo_hh_sensitive_artist`](E.md#c_eo_hh_sensitive_artist)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_he_ll_cold_exploiter"></a>
### Cold Exploiter (냉혈한 착취자) — `c_he_ll_cold_exploiter`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `E` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | combat | 1.05 | +5% combat weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | steal | 1.43 | +43% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | trust_gain_mult | 0.765 | -24% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.855 | -15% stress gain mult |

**Amplified behaviors**: `betray`, `combat`, `explore`, `steal`, `take_bribe`
**Suppressed behaviors**: `flee`, `share`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `guilt_sensitivity (0.8)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_ea_lh_volatile_bully`](E.md#c_ea_lh_volatile_bully), [`c_he_lh_anxious_swindler`](#c_he_lh_anxious_swindler), [`c_he_hl_stoic_honest`](#c_he_hl_stoic_honest)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_hx_hh_honest_leader"></a>
### Honest Leader (청렴한 리더) — `c_hx_hh_honest_leader`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H` direction `high` threshold `0.75`
- Facet `X` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | leadership | 1.265 | +26% leadership weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | social | 1.2 | +20% social weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 1.2075 | +21% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | stress_gain_mult | 0.9996 | -0% stress gain mult |

**Amplified behaviors**: `help`, `leadership`, `share`, `social`
**Suppressed behaviors**: `betray`, `steal`
**Emotion sensitivities**: `guilt_sensitivity (1.15)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_reconciler`](A.md#c_reconciler), [`c_xc_hl_charming_improviser`](X.md#c_xc_hl_charming_improviser), [`c_strategist_general`](C.md#c_strategist_general)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_hx_hl_honest_recluse"></a>
### Honest Recluse (청렴한 은둔자) — `c_hx_hl_honest_recluse`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `H` direction `high` threshold `0.75`
- Facet `X` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | research | 1.05 | +5% research weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | social | 0.8 | -20% social weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | social_stress_mult | 1.1 | +10% social stress mult |
| Stress | stress_gain_mult | 1.02 | +2% stress gain mult |

**Amplified behaviors**: `craft`, `help`, `research`, `share`
**Suppressed behaviors**: `betray`, `social`, `steal`
**Emotion sensitivities**: `guilt_sensitivity (1.15)`, `joy_baseline (-0.01)`
**Violation stress triggers**: none

**Synergies**: [`c_hx_hh_honest_leader`](#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler), [`f_insecure`](X.md#f_insecure)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_hx_lh_charismatic_con_artist"></a>
### Charismatic Con Artist (카리스마 사기꾼) — `c_hx_lh_charismatic_con_artist`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `X` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.2 | +20% social weight |
| Behavior | steal | 1.43 | +43% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 0.765 | -24% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.931 | -7% stress gain mult |

**Amplified behaviors**: `betray`, `leadership`, `social`, `steal`, `take_bribe`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `guilt_sensitivity (0.8)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_hx_hh_honest_leader`](#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler), [`c_xc_hl_charming_improviser`](X.md#c_xc_hl_charming_improviser)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_hx_ll_sly_loner"></a>
### Sly Loner (음흉한 은둔자) — `c_hx_ll_sly_loner`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `X` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | research | 1.05 | +5% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 0.8 | -20% social weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | social_stress_mult | 1.1 | +10% social stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `betray`, `craft`, `research`, `steal`, `take_bribe`
**Suppressed behaviors**: `share`, `social`
**Emotion sensitivities**: `guilt_sensitivity (0.8)`, `joy_baseline (-0.01)`
**Violation stress triggers**: none

**Synergies**: [`f_reserved`](X.md#f_reserved), [`f_insecure`](X.md#f_insecure), [`c_he_lh_anxious_swindler`](#c_he_lh_anxious_swindler)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ha_hh_kind-hearted_honest"></a>
### Kind‑Hearted Honest (인자한 청렴인) — `c_ha_hh_kind-hearted_honest`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H` direction `high` threshold `0.75`
- Facet `A` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | help | 1.21 | +21% help weight |
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
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | stress_gain_mult | 0.969 | -3% stress gain mult |

**Amplified behaviors**: `cooperate`, `help`, `share`
**Suppressed behaviors**: `betray`, `combat`, `revenge`, `steal`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `guilt_sensitivity (1.15)`
**Violation stress triggers**: none

**Synergies**: [`f_flexible`](A.md#f_flexible), [`c_ea_lh_volatile_bully`](E.md#c_ea_lh_volatile_bully), [`c_hx_hh_honest_leader`](#c_hx_hh_honest_leader)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ha_hl_stern_judge"></a>
### Stern Judge (엄정한 재판관) — `c_ha_hl_stern_judge`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `H` direction `high` threshold `0.75`
- Facet `A` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | stress_gain_mult | 1.02 | +2% stress gain mult |

**Amplified behaviors**: `combat`, `help`, `intimidate`, `revenge`, `share`
**Suppressed behaviors**: `betray`, `cooperate`, `steal`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `guilt_sensitivity (1.15)`
**Violation stress triggers**: none

**Synergies**: [`c_hx_hh_honest_leader`](#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler), [`c_he_hl_stoic_honest`](#c_he_hl_stoic_honest)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ha_lh_smiling_exploiter"></a>
### Smiling Exploiter (미소 짓는 착취자) — `c_ha_lh_smiling_exploiter`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `A` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | steal | 1.43 | +43% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | trust_gain_mult | 0.765 | -24% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.9025 | -10% stress gain mult |

**Amplified behaviors**: `betray`, `cooperate`, `help`, `steal`, `take_bribe`
**Suppressed behaviors**: `combat`, `revenge`, `share`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `guilt_sensitivity (0.8)`
**Violation stress triggers**: none

**Synergies**: [`f_flexible`](A.md#f_flexible), [`c_ea_lh_volatile_bully`](E.md#c_ea_lh_volatile_bully), [`c_reconciler`](A.md#c_reconciler)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ha_ll_cruel_raider"></a>
### Cruel Raider (잔혹한 약탈자) — `c_ha_ll_cruel_raider`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `A` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | steal | 1.43 | +43% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | trust_gain_mult | 0.765 | -24% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `betray`, `combat`, `intimidate`, `revenge`, `steal`, `take_bribe`
**Suppressed behaviors**: `cooperate`, `share`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `guilt_sensitivity (0.8)`
**Violation stress triggers**: none

**Synergies**: [`c_he_lh_anxious_swindler`](#c_he_lh_anxious_swindler), [`d_cult_leader`](#d_cult_leader), [`c_ho_ll_corrupt_traditionalist`](#c_ho_ll_corrupt_traditionalist)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_hc_hh_honest_administrator"></a>
### Honest Administrator (청렴한 관리자) — `c_hc_hh_honest_administrator`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H` direction `high` threshold `0.75`
- Facet `C` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | leadership | 1.1 | +10% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | trust_gain_mult | 1.2075 | +21% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.133 | +13% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | stress_gain_mult | 0.969 | -3% stress gain mult |

**Amplified behaviors**: `build`, `gather`, `help`, `leadership`, `plan`, `research`, `share`
**Suppressed behaviors**: `betray`, `steal`
**Emotion sensitivities**: `guilt_sensitivity (1.15)`, `impulse_control_mult (1.1)`
**Violation stress triggers**: none

**Synergies**: [`f_industrious`](C.md#f_industrious), [`c_hx_hh_honest_leader`](#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_hc_hl_well-meaning_slacker"></a>
### Well‑Meaning Slacker (선의의 무능) — `c_hc_hl_well-meaning_slacker`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `H` direction `high` threshold `0.75`
- Facet `C` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | build | 0.9 | -10% build weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 0.9 | -10% research weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.927 | -7% quality mult |
| Work | speed_mult | 0.95 | -5% speed mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | stress_gain_mult | 1.071 | +7% stress gain mult |

**Amplified behaviors**: `explore`, `help`, `share`
**Suppressed behaviors**: `betray`, `build`, `plan`, `research`, `steal`
**Emotion sensitivities**: `guilt_sensitivity (1.15)`, `impulse_control_mult (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_hx_hh_honest_leader`](#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler), [`c_xc_hl_charming_improviser`](X.md#c_xc_hl_charming_improviser)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_hc_lh_calculating_schemer"></a>
### Calculating Schemer (냉정한 책략가) — `c_hc_lh_calculating_schemer`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `C` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.067 | +7% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.9025 | -10% stress gain mult |

**Amplified behaviors**: `betray`, `build`, `gather`, `plan`, `research`, `steal`, `take_bribe`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `guilt_sensitivity (0.8)`, `impulse_control_mult (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_strategist_general`](C.md#c_strategist_general), [`f_prudent`](C.md#f_prudent), [`c_xc_lh_silent_craftsman`](X.md#c_xc_lh_silent_craftsman)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_hc_ll_irresponsible_cheat"></a>
### Irresponsible Cheat (무책임한 사기꾼) — `c_hc_ll_irresponsible_cheat`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `C` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | build | 0.9 | -10% build weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 0.9 | -10% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.873 | -13% quality mult |
| Work | speed_mult | 0.95 | -5% speed mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.9975 | -0% stress gain mult |

**Amplified behaviors**: `betray`, `explore`, `steal`, `take_bribe`
**Suppressed behaviors**: `build`, `plan`, `research`, `share`
**Emotion sensitivities**: `guilt_sensitivity (0.8)`, `impulse_control_mult (0.9)`
**Violation stress triggers**: none

**Synergies**: [`c_xc_hl_charming_improviser`](X.md#c_xc_hl_charming_improviser), [`c_he_lh_anxious_swindler`](#c_he_lh_anxious_swindler), [`f_reckless`](C.md#f_reckless)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ho_hh_idealistic_innovator"></a>
### Idealistic Innovator (이상주의 혁신가) — `c_ho_hh_idealistic_innovator`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H` direction `high` threshold `0.75`
- Facet `O` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 1.02 | +2% stress gain mult |

**Amplified behaviors**: `craft`, `explore`, `help`, `research`, `share`
**Suppressed behaviors**: `betray`, `steal`
**Emotion sensitivities**: `guilt_sensitivity (1.15)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_hx_hh_honest_leader`](#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler), [`c_strategist_general`](C.md#c_strategist_general)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ho_hl_traditional_moralist"></a>
### Traditional Moralist (전통적 도덕가) — `c_ho_hl_traditional_moralist`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H` direction `high` threshold `0.75`
- Facet `O` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | research | 0.95 | -5% research weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 1.02 | +2% stress gain mult |

**Amplified behaviors**: `build`, `help`, `leadership`, `share`
**Suppressed behaviors**: `betray`, `research`, `steal`
**Emotion sensitivities**: `guilt_sensitivity (1.15)`, `novelty_fear_sensitivity (1.05)`
**Violation stress triggers**: none

**Synergies**: [`c_hx_hh_honest_leader`](#c_hx_hh_honest_leader), [`c_reconciler`](A.md#c_reconciler), [`c_he_hl_stoic_honest`](#c_he_hl_stoic_honest)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ho_lh_cunning_inventor"></a>
### Cunning Inventor (교활한 발명가) — `c_ho_lh_cunning_inventor`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `O` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | research | 1.15 | +15% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `betray`, `craft`, `explore`, `research`, `steal`, `take_bribe`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `guilt_sensitivity (0.8)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_strategist_general`](C.md#c_strategist_general), [`c_eo_hh_sensitive_artist`](E.md#c_eo_hh_sensitive_artist), [`c_ho_ll_corrupt_traditionalist`](#c_ho_ll_corrupt_traditionalist)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="c_ho_ll_corrupt_traditionalist"></a>
### Corrupt Traditionalist (부패한 보수) — `c_ho_ll_corrupt_traditionalist`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `O` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | build | 1.05 | +5% build weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | research | 0.95 | -5% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `betray`, `build`, `leadership`, `steal`, `take_bribe`
**Suppressed behaviors**: `research`, `share`
**Emotion sensitivities**: `guilt_sensitivity (0.8)`, `novelty_fear_sensitivity (1.05)`
**Violation stress triggers**: none

**Synergies**: [`c_he_lh_anxious_swindler`](#c_he_lh_anxious_swindler), [`d_cult_leader`](#d_cult_leader), [`c_settler`](C.md#c_settler)
**Anti-synergies**: none

📄 source: `extracted/trait_data.json`

---

<a id="d_psychopath_primary"></a>
### Primary Psychopath (사이코패스(1차)) — `d_psychopath_primary`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `E` direction `low` threshold `0.25`
- Facet `A` direction `low` threshold `0.3`
- Facet `E_sentimentality` direction `low` threshold `0.14`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.8 | +80% betray weight |
| Behavior | combat | 1.5094 | +51% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | help | 0.8 | -20% help weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | nurture | 0.6 | -40% nurture weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | steal | 1.8 | +80% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | fear_sensitivity | 0.595 | -40% fear sensitivity |
| Emotion | guilt_sensitivity | 0.48 | -52% guilt sensitivity |
| Emotion | sadness_sensitivity | 0.63 | -37% sadness sensitivity |
| Relationship | conflict_mult | 1.44 | +44% conflict mult |
| Relationship | empathy_mult | 0.6 | -40% empathy mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | trust_gain_mult | 0.6375 | -36% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 0.9215 | -8% quality mult |
| Work | speed_mult | 1.071 | +7% speed mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.4375 | +44% aggression mult |
| Combat | flee_threshold_mult | 0.765 | -24% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.386 | +39% risk taking mult |
| Combat | war_crime_propensity_mult | 1.61 | +61% war crime propensity mult |
| Stress | break_threshold_mult | 1.2075 | +21% break threshold mult |
| Stress | stress_gain_mult | 0.684 | -32% stress gain mult |
| Stress | violation: harm_innocent | 0 | +0 stress when harm_innocent |
| Stress | violation: lie | 2 | +2 stress when lie |
| Stress | violation: steal | 2 | +2 stress when steal |

**Amplified behaviors**: `betray`, `combat`, `explore`, `intimidate`, `revenge`, `steal`, `take_bribe`
**Suppressed behaviors**: `cooperate`, `flee`, `help`, `nurture`, `share`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `fear_sensitivity (0.595)`, `guilt_sensitivity (0.48)`, `sadness_sensitivity (0.63)`
**Violation stress triggers**: `harm_innocent (+0)`, `lie (+2)`, `steal (+2)`

**Synergies**: [`d_sadist`](#d_sadist), [`c_eo_lh_cold_experimenter`](E.md#c_eo_lh_cold_experimenter)
**Anti-synergies**: [`c_ea_hh_compassionate_reconciler`](E.md#c_ea_hh_compassionate_reconciler), [`f_sentimental`](E.md#f_sentimental)

📄 source: `extracted/trait_data.json`

---

<a id="d_psychopath_secondary"></a>
### Secondary Psychopath (사이코패스(2차)) — `d_psychopath_secondary`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `A` direction `low` threshold `0.3`
- Facet `E` direction `high` threshold `0.75`
- Facet `C` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.6875 | +69% betray weight |
| Behavior | build | 0.9 | -10% build weight |
| Behavior | combat | 1.38 | +38% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | explore | 0.9975 | -0% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 0.9 | -10% research weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.1 | +10% social weight |
| Behavior | steal | 1.8 | +80% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | anger_sensitivity | 1.56 | +56% anger sensitivity |
| Emotion | fear_sensitivity | 1.02 | +2% fear sensitivity |
| Emotion | guilt_sensitivity | 0.56 | -44% guilt sensitivity |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | conflict_mult | 1.5 | +50% conflict mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.265 | +26% trust loss mult |
| Work | error_rate_mult | 1.44 | +44% error rate mult |
| Work | quality_mult | 0.7857 | -21% quality mult |
| Work | speed_mult | 0.9776 | -2% speed mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.4375 | +44% aggression mult |
| Combat | flee_threshold_mult | 1.035 | +3% flee threshold mult |
| Combat | risk_taking_mult | 1.0867 | +9% risk taking mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | break_threshold_mult | 0.9025 | -10% break threshold mult |
| Stress | stress_gain_mult | 1.2045 | +20% stress gain mult |
| Stress | violation: hurt_friend | 2 | +2 stress when hurt_friend |
| Stress | violation: lie | 4 | +4 stress when lie |
| Stress | violation: steal | 4 | +4 stress when steal |

**Amplified behaviors**: `betray`, `combat`, `flee`, `intimidate`, `nurture`, `revenge`, `social`, `steal`, `take_bribe`
**Suppressed behaviors**: `build`, `cooperate`, `explore`, `plan`, `research`, `share`
**Emotion sensitivities**: `anger_sensitivity (1.56)`, `fear_sensitivity (1.02)`, `guilt_sensitivity (0.56)`, `impulse_control_mult (0.9)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: `hurt_friend (+2)`, `lie (+4)`, `steal (+4)`

**Synergies**: [`f_reckless`](C.md#f_reckless), [`f_hot_tempered`](A.md#f_hot_tempered)
**Anti-synergies**: [`f_prudent`](C.md#f_prudent), [`f_patient`](A.md#f_patient)

📄 source: `extracted/trait_data.json`

---

<a id="d_machiavellian"></a>
### Machiavellian (마키아벨리스트) — `d_machiavellian`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `C` direction `high` threshold `0.75`
- Facet `H_sincerity` direction `low` threshold `0.14`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.5 | +50% betray weight |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | negotiate | 1.25 | +25% negotiate weight |
| Behavior | plan | 1.62 | +62% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | steal | 1.625 | +62% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | guilt_sensitivity | 0.6 | -40% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Relationship | manipulation_success_mult | 1.25 | +25% manipulation success mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | trust_gain_mult | 0.7225 | -28% trust gain mult |
| Relationship | trust_loss_mult | 1.045 | +4% trust loss mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1203 | +12% quality mult |
| Work | speed_mult | 1.155 | +16% speed mult |
| Combat | tactic_planning_mult | 1.32 | +32% tactic planning mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.8123 | -19% stress gain mult |
| Stress | violation: lie | 2 | +2 stress when lie |
| Stress | violation: take_bribe | 2 | +2 stress when take_bribe |

**Amplified behaviors**: `betray`, `build`, `gather`, `leadership`, `negotiate`, `plan`, `research`, `steal`, `take_bribe`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `guilt_sensitivity (0.6)`, `impulse_control_mult (1.1)`
**Violation stress triggers**: `lie (+2)`, `take_bribe (+2)`

**Synergies**: [`c_hc_lh_calculating_schemer`](#c_hc_lh_calculating_schemer), [`d_con_artist`](#d_con_artist)
**Anti-synergies**: [`f_sincere`](#f_sincere), [`c_hc_hh_honest_administrator`](#c_hc_hh_honest_administrator)

📄 source: `extracted/trait_data.json`

---

<a id="d_narcissist_grandiose"></a>
### Grandiose Narcissist (나르시시스트(과대)) — `d_narcissist_grandiose`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `X` direction `high` threshold `0.75`
- Facet `H_modesty` direction `low` threshold `0.16`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | cooperate | 0.95 | -5% cooperate weight |
| Behavior | dominate | 1.35 | +35% dominate weight |
| Behavior | leadership | 1.495 | +49% leadership weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.56 | +56% social weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | anger_disrespect_sensitivity | 1.35 | +35% anger disrespect sensitivity |
| Emotion | guilt_sensitivity | 0.68 | -32% guilt sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | pride_baseline | 0.06 | -94% pride baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | respect_gain_mult | 1.375 | +38% respect gain mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.21 | +21% trust loss mult |
| Work | learning_from_failure_mult | 0.85 | -15% learning from failure mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Work | speed_mult | 1.05 | +5% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | flee_threshold_mult | 0.8 | -20% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | disrespect_stress_mult | 1.5 | +50% disrespect stress mult |
| Stress | stress_gain_mult | 0.9776 | -2% stress gain mult |
| Stress | violation: apologize | 14 | +14 stress when apologize |
| Stress | violation: share_credit | 12 | +12 stress when share_credit |

**Amplified behaviors**: `betray`, `dominate`, `leadership`, `social`, `steal`, `take_bribe`
**Suppressed behaviors**: `cooperate`, `share`
**Emotion sensitivities**: `anger_disrespect_sensitivity (1.35)`, `guilt_sensitivity (0.68)`, `joy_baseline (0.02)`, `pride_baseline (0.06)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: `apologize (+14)`, `share_credit (+12)`

**Synergies**: [`c_xo_hl_populist`](X.md#c_xo_hl_populist), [`c_xc_hh_competent_leader`](X.md#c_xc_hh_competent_leader)
**Anti-synergies**: [`f_modest`](#f_modest), [`c_ac_hh_reliable_teamworker`](A.md#c_ac_hh_reliable_teamworker)

📄 source: `extracted/trait_data.json`

---

<a id="d_narcissist_vulnerable"></a>
### Vulnerable Narcissist (나르시시스트(취약)) — `d_narcissist_vulnerable`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `X` direction `low` threshold `0.25`
- Facet `E` direction `high` threshold `0.75`
- Facet `H_modesty` direction `low` threshold `0.16`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.375 | +38% betray weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | leadership | 0.9 | -10% leadership weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | research | 1.05 | +5% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 0.76 | -24% social weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | anger_disrespect_sensitivity | 1.2 | +20% anger disrespect sensitivity |
| Emotion | anxiety_baseline | 0.06 | -94% anxiety baseline |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | joy_baseline | -0.01 | -101% joy baseline |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Emotion | shame_sensitivity | 1.4 | +40% shame sensitivity |
| Relationship | approval_seeking_mult | 1.4 | +40% approval seeking mult |
| Relationship | intimacy_gain_mult | 0.9 | -10% intimacy gain mult |
| Relationship | jealousy_mult | 1.3 | +30% jealousy mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.265 | +26% trust loss mult |
| Work | quality_mult | 0.9894 | -1% quality mult |
| Work | solo_efficiency_mult | 1.05 | +5% solo efficiency mult |
| Work | speed_mult | 0.931 | -7% speed mult |
| Combat | flee_threshold_mult | 1.265 | +26% flee threshold mult |
| Combat | morale_mult | 0.9 | -10% morale mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Combat | skirmish_preference_mult | 1.05 | +5% skirmish preference mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | break_threshold_mult | 0.8075 | -19% break threshold mult |
| Stress | social_stress_mult | 1.1 | +10% social stress mult |
| Stress | stress_gain_mult | 1.4202 | +42% stress gain mult |
| Stress | violation: be_ignored | 14 | +14 stress when be_ignored |
| Stress | violation: public_failure | 16 | +16 stress when public_failure |

**Amplified behaviors**: `betray`, `craft`, `flee`, `nurture`, `research`, `steal`, `take_bribe`
**Suppressed behaviors**: `explore`, `leadership`, `share`, `social`
**Emotion sensitivities**: `anger_disrespect_sensitivity (1.2)`, `anxiety_baseline (0.06)`, `fear_sensitivity (1.2)`, `guilt_sensitivity (0.8)`, `joy_baseline (-0.01)`, `sadness_sensitivity (1.1)`, `shame_sensitivity (1.4)`
**Violation stress triggers**: `be_ignored (+14)`, `public_failure (+16)`

**Synergies**: [`c_ec_hh_anxious_planner`](E.md#c_ec_hh_anxious_planner)
**Anti-synergies**: [`f_confident`](X.md#f_confident), [`f_calm`](E.md#f_calm)

📄 source: `extracted/trait_data.json`

---

<a id="d_sadist"></a>
### Sadist (사디스트) — `d_sadist`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.2`
- Facet `A` direction `low` threshold `0.2`
- Facet `E` direction `low` threshold `0.3`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | combat | 1.6301 | +63% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | help | 0.8 | -20% help weight |
| Behavior | intimidate | 1.62 | +62% intimidate weight |
| Behavior | nurture | 0.6 | -40% nurture weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Behavior | torture | 1.4 | +40% torture weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | fear_sensitivity | 0.68 | -32% fear sensitivity |
| Emotion | guilt_sensitivity | 0.56 | -44% guilt sensitivity |
| Emotion | sadism_reward_sensitivity | 1.35 | +35% sadism reward sensitivity |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | conflict_mult | 1.62 | +62% conflict mult |
| Relationship | empathy_mult | 0.6 | -40% empathy mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 0.9215 | -8% quality mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.61 | +61% aggression mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.2705 | +27% risk taking mult |
| Combat | war_crime_propensity_mult | 1.84 | +84% war crime propensity mult |
| Stress | break_threshold_mult | 1.155 | +16% break threshold mult |
| Stress | stress_from_harming_mult | 0.5 | -50% stress from harming mult |
| Stress | stress_gain_mult | 0.7268 | -27% stress gain mult |
| Stress | violation: harm_innocent | 0 | +0 stress when harm_innocent |
| Stress | violation: torture | 0 | +0 stress when torture |

**Amplified behaviors**: `betray`, `combat`, `explore`, `intimidate`, `revenge`, `steal`, `take_bribe`, `torture`
**Suppressed behaviors**: `cooperate`, `flee`, `help`, `nurture`, `share`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `fear_sensitivity (0.68)`, `guilt_sensitivity (0.56)`, `sadism_reward_sensitivity (1.35)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: `harm_innocent (+0)`, `torture (+0)`

**Synergies**: [`d_psychopath_primary`](#d_psychopath_primary), [`d_predatory_raider`](#d_predatory_raider)
**Anti-synergies**: [`c_xa_hh_social_peacemaker`](X.md#c_xa_hh_social_peacemaker), [`f_gentle`](A.md#f_gentle)

📄 source: `extracted/trait_data.json`

---

<a id="d_con_artist"></a>
### Con Artist (모사꾼) — `d_con_artist`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `X` direction `high` threshold `0.75`
- Facet `C` direction `high` threshold `0.7`
- Facet `H_sincerity` direction `low` threshold `0.14`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.75 | +75% betray weight |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.265 | +26% leadership weight |
| Behavior | negotiate | 1.35 | +35% negotiate weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.62 | +62% social weight |
| Behavior | steal | 1.8 | +80% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | guilt_sensitivity | 0.56 | -44% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | persuasion_success_mult | 1.25 | +25% persuasion success mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 0.68 | -32% trust gain mult |
| Relationship | trust_loss_mult | 1.155 | +16% trust loss mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | plan_mult | 1.25 | +25% plan mult |
| Work | quality_mult | 1.067 | +7% quality mult |
| Work | speed_mult | 1.155 | +16% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | ambush_propensity_mult | 1.25 | +25% ambush propensity mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.796 | -20% stress gain mult |
| Stress | violation: lie | 2 | +2 stress when lie |
| Stress | violation: steal | 2 | +2 stress when steal |

**Amplified behaviors**: `betray`, `build`, `gather`, `leadership`, `negotiate`, `plan`, `research`, `social`, `steal`, `take_bribe`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `guilt_sensitivity (0.56)`, `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: `lie (+2)`, `steal (+2)`

**Synergies**: [`c_hx_lh_charismatic_con_artist`](#c_hx_lh_charismatic_con_artist), [`d_machiavellian`](#d_machiavellian)
**Anti-synergies**: [`f_sincere`](#f_sincere), [`f_fair_minded`](#f_fair_minded)

📄 source: `extracted/trait_data.json`

---

<a id="d_cult_leader"></a>
### Cult Leader (사이비 교주) — `d_cult_leader`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `X` direction `high` threshold `0.75`
- Facet `C` direction `high` threshold `0.75`
- Facet `O` direction `low` threshold `0.25`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | build | 1.155 | +16% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | indoctrinate | 1.4 | +40% indoctrinate weight |
| Behavior | leadership | 1.6301 | +63% leadership weight |
| Behavior | negotiate | 1.15 | +15% negotiate weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.045 | +4% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.44 | +44% social weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | anger_challenge_sensitivity | 1.2 | +20% anger challenge sensitivity |
| Emotion | guilt_sensitivity | 0.64 | -36% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | influence_mult | 1.35 | +35% influence mult |
| Relationship | ingroup_trust_mult | 1.265 | +26% ingroup trust mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | outgroup_hostility_mult | 1.15 | +15% outgroup hostility mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | plan_mult | 1.2 | +20% plan mult |
| Work | quality_mult | 1.067 | +7% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | discipline_mult | 1.155 | +16% discipline mult |
| Combat | morale_mult | 1.26 | +26% morale mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | stress_gain_mult | 0.8402 | -16% stress gain mult |
| Stress | violation: abuse_power | 0 | +0 stress when abuse_power |
| Stress | violation: lie | 2 | +2 stress when lie |

**Amplified behaviors**: `betray`, `build`, `gather`, `indoctrinate`, `leadership`, `negotiate`, `plan`, `research`, `social`, `steal`, `take_bribe`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `anger_challenge_sensitivity (1.2)`, `guilt_sensitivity (0.64)`, `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `novelty_fear_sensitivity (1.05)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: `abuse_power (+0)`, `lie (+2)`

**Synergies**: [`c_xo_hl_populist`](X.md#c_xo_hl_populist), [`d_machiavellian`](#d_machiavellian)
**Anti-synergies**: [`c_democratic_leader`](#c_democratic_leader), [`c_ao_hh_open-minded_humanitarian`](A.md#c_ao_hh_open-minded_humanitarian)

📄 source: `extracted/trait_data.json`

---

<a id="d_opportunist"></a>
### Opportunist (기회주의자) — `d_opportunist`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.3`
- Facet `C` direction `low` threshold `0.3`
- Facet `E` direction `low` threshold `0.3`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | build | 0.9 | -10% build weight |
| Behavior | combat | 1.155 | +16% combat weight |
| Behavior | explore | 1.386 | +39% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 0.9 | -10% research weight |
| Behavior | share | 0.765 | -24% share weight |
| Behavior | steal | 1.8 | +80% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | fear_sensitivity | 0.7225 | -28% fear sensitivity |
| Emotion | guilt_sensitivity | 0.64 | -36% guilt sensitivity |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Relationship | betrayal_propensity_mult | 1.2 | +20% betrayal propensity mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Relationship | trust_gain_mult | 0.7225 | -28% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.7857 | -21% quality mult |
| Work | speed_mult | 0.9884 | -1% speed mult |
| Combat | flee_threshold_mult | 0.81 | -19% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.265 | +26% risk taking mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.808 | -19% stress gain mult |
| Stress | violation: lie | 4 | +4 stress when lie |
| Stress | violation: steal | 4 | +4 stress when steal |

**Amplified behaviors**: `betray`, `combat`, `explore`, `steal`, `take_bribe`
**Suppressed behaviors**: `build`, `flee`, `plan`, `research`, `share`
**Emotion sensitivities**: `fear_sensitivity (0.7225)`, `guilt_sensitivity (0.64)`, `impulse_control_mult (0.9)`, `sadness_sensitivity (0.9)`
**Violation stress triggers**: `lie (+4)`, `steal (+4)`

**Synergies**: [`c_ho_lh_cunning_inventor`](#c_ho_lh_cunning_inventor), [`c_ec_ll_reckless_drifter`](E.md#c_ec_ll_reckless_drifter)
**Anti-synergies**: [`c_ac_hh_reliable_teamworker`](A.md#c_ac_hh_reliable_teamworker)

📄 source: `extracted/trait_data.json`

---

<a id="d_callous"></a>
### Callous (냉담한) — `d_callous`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.3`
- Facet `E_sentimentality` direction `low` threshold `0.14`
- Facet `A` direction `low` threshold `0.35`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | combat | 1.265 | +26% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | help | 0.85 | -15% help weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | nurture | 0.7 | -30% nurture weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | guilt_sensitivity | 0.64 | -36% guilt sensitivity |
| Emotion | sadness_sensitivity | 0.7 | -30% sadness sensitivity |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | empathy_mult | 0.7 | -30% empathy mult |
| Relationship | intimacy_gain_mult | 0.8 | -20% intimacy gain mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 0.9506 | -5% quality mult |
| Work | teamwork_efficiency_mult | 0.95 | -5% teamwork efficiency mult |
| Combat | aggression_mult | 1.265 | +26% aggression mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_from_others_harm_mult | 0.7 | -30% stress from others harm mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | violation: comfort | 10 | +10 stress when comfort |
| Stress | violation: neglect_child | 6 | +6 stress when neglect_child |

**Amplified behaviors**: `betray`, `combat`, `intimidate`, `revenge`, `steal`, `take_bribe`
**Suppressed behaviors**: `cooperate`, `help`, `nurture`, `share`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `guilt_sensitivity (0.64)`, `sadness_sensitivity (0.7)`
**Violation stress triggers**: `comfort (+10)`, `neglect_child (+6)`

**Synergies**: [`c_eo_lh_cold_experimenter`](E.md#c_eo_lh_cold_experimenter), [`d_machiavellian`](#d_machiavellian)
**Anti-synergies**: [`c_caregiver`](E.md#c_caregiver), [`f_sentimental`](E.md#f_sentimental)

📄 source: `extracted/trait_data.json`

---

<a id="d_backstabber"></a>
### Backstabber (뒤통수 장인) — `d_backstabber`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.3`
- Facet `A` direction `low` threshold `0.3`
- Facet `X` direction `high` threshold `0.7`
- Facet `H_sincerity` direction `low` threshold `0.14`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.8 | +80% betray weight |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.32 | +32% social weight |
| Behavior | steal | 1.69 | +69% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | guilt_sensitivity | 0.6 | -40% guilt sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | betrayal_propensity_mult | 1.5 | +50% betrayal propensity mult |
| Relationship | conflict_mult | 1.2 | +20% conflict mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.375 | +38% trust loss mult |
| Work | quality_mult | 0.9215 | -8% quality mult |
| Work | teamwork_efficiency_mult | 0.9975 | -0% teamwork efficiency mult |
| Combat | aggression_mult | 1.15 | +15% aggression mult |
| Combat | ambush_propensity_mult | 1.3 | +30% ambush propensity mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.8379 | -16% stress gain mult |
| Stress | violation: betray | 0 | +0 stress when betray |
| Stress | violation: lie | 2 | +2 stress when lie |

**Amplified behaviors**: `betray`, `combat`, `intimidate`, `leadership`, `revenge`, `social`, `steal`, `take_bribe`
**Suppressed behaviors**: `cooperate`, `share`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `guilt_sensitivity (0.6)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: `betray (+0)`, `lie (+2)`

**Synergies**: [`d_con_artist`](#d_con_artist), [`c_xa_hl_dominating_agitator`](X.md#c_xa_hl_dominating_agitator)
**Anti-synergies**: [`c_ac_hh_reliable_teamworker`](A.md#c_ac_hh_reliable_teamworker), [`f_fair_minded`](#f_fair_minded)

📄 source: `extracted/trait_data.json`

---

<a id="d_corrupt_official"></a>
### Corrupt Official (부패한 관리) — `d_corrupt_official`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H_fairness` direction `low` threshold `0.12`
- Facet `C` direction `high` threshold `0.75`
- Facet `X` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.4375 | +44% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.2 | +20% social weight |
| Behavior | steal | 1.625 | +62% steal weight |
| Behavior | take_bribe | 1.8 | +80% take bribe weight |
| Behavior | trade | 1.2 | +20% trade weight |
| Emotion | guilt_sensitivity | 0.56 | -44% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | suspicion_gain_mult | 1.25 | +25% suspicion gain mult |
| Relationship | trust_gain_mult | 0.6375 | -36% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | plan_mult | 1.15 | +15% plan mult |
| Work | quality_mult | 1.067 | +7% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.796 | -20% stress gain mult |
| Stress | violation: lie | 2 | +2 stress when lie |
| Stress | violation: take_bribe | 0 | +0 stress when take_bribe |

**Amplified behaviors**: `betray`, `build`, `gather`, `leadership`, `plan`, `research`, `social`, `steal`, `take_bribe`, `trade`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `guilt_sensitivity (0.56)`, `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: `lie (+2)`, `take_bribe (+0)`

**Synergies**: [`d_machiavellian`](#d_machiavellian), [`c_co_hl_conservative_manager`](C.md#c_co_hl_conservative_manager)
**Anti-synergies**: [`c_hc_hh_honest_administrator`](#c_hc_hh_honest_administrator)

📄 source: `extracted/trait_data.json`

---

<a id="d_predatory_raider"></a>
### Predatory Raider (포식자 약탈자) — `d_predatory_raider`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.3`
- Facet `A` direction `low` threshold `0.3`
- Facet `E` direction `low` threshold `0.3`
- Facet `X` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | combat | 1.7509 | +75% combat weight |
| Behavior | cooperate | 0.9 | -10% cooperate weight |
| Behavior | explore | 1.32 | +32% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | intimidate | 1.2 | +20% intimidate weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | nurture | 0.7 | -30% nurture weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.2 | +20% social weight |
| Behavior | steal | 1.8 | +80% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | fear_sensitivity | 0.68 | -32% fear sensitivity |
| Emotion | guilt_sensitivity | 0.6 | -40% guilt sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 1.68 | +68% conflict mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 0.68 | -32% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 0.873 | -13% quality mult |
| Work | speed_mult | 1.071 | +7% speed mult |
| Work | teamwork_efficiency_mult | 0.9975 | -0% teamwork efficiency mult |
| Combat | aggression_mult | 1.6675 | +67% aggression mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.1025 | +10% morale mult |
| Combat | risk_taking_mult | 1.386 | +39% risk taking mult |
| Combat | war_crime_propensity_mult | 1.5525 | +55% war crime propensity mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.7541 | -25% stress gain mult |
| Stress | violation: raid | 0 | +0 stress when raid |
| Stress | violation: steal | 2 | +2 stress when steal |

**Amplified behaviors**: `betray`, `combat`, `explore`, `intimidate`, `leadership`, `revenge`, `social`, `steal`, `take_bribe`
**Suppressed behaviors**: `cooperate`, `flee`, `nurture`, `share`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `fear_sensitivity (0.68)`, `guilt_sensitivity (0.6)`, `joy_baseline (0.02)`, `sadness_sensitivity (0.9)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: `raid (+0)`, `steal (+2)`

**Synergies**: [`d_sadist`](#d_sadist), [`c_berserker`](A.md#c_berserker)
**Anti-synergies**: [`c_pacifist`](A.md#c_pacifist), [`c_ao_hl_benevolent_traditionalist`](A.md#c_ao_hl_benevolent_traditionalist)

📄 source: `extracted/trait_data.json`

---

<a id="d_histrionic"></a>
### Histrionic (히스트리오닉) — `d_histrionic`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `X` direction `high` threshold `0.75`
- Facet `E` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | dramatize | 1.4 | +40% dramatize weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | leadership | 1.265 | +26% leadership weight |
| Behavior | nurture | 1.05 | +5% nurture weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.62 | +62% social weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | excitability_sensitivity | 1.25 | +25% excitability sensitivity |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Emotion | shame_sensitivity | 0.99 | -1% shame sensitivity |
| Relationship | attention_seeking_mult | 1.4 | +40% attention seeking mult |
| Relationship | conflict_mult | 1.1 | +10% conflict mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 0.85 | -15% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 0.9215 | -8% quality mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 0.945 | -5% risk taking mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_gain_mult | 1.1777 | +18% stress gain mult |
| Stress | violation: be_ignored | 16 | +16 stress when be_ignored |

**Amplified behaviors**: `betray`, `dramatize`, `flee`, `leadership`, `nurture`, `social`, `steal`, `take_bribe`
**Suppressed behaviors**: `explore`, `share`
**Emotion sensitivities**: `excitability_sensitivity (1.25)`, `fear_sensitivity (1.2)`, `guilt_sensitivity (0.8)`, `joy_baseline (0.02)`, `sadness_sensitivity (1.1)`, `shame_sensitivity (0.99)`
**Violation stress triggers**: `be_ignored (+16)`

**Synergies**: [`c_xo_hl_populist`](X.md#c_xo_hl_populist), [`d_narcissist_grandiose`](#d_narcissist_grandiose)
**Anti-synergies**: [`f_modest`](#f_modest), [`c_xo_lh_solitary_scholar`](X.md#c_xo_lh_solitary_scholar)

📄 source: `extracted/trait_data.json`

---

<a id="c_saint"></a>
### Saintly (성인군자) — `c_saint`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H` direction `high` threshold `0.7`
- Facet `A` direction `high` threshold `0.7`
- Facet `C` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | help | 1.5125 | +51% help weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | share | 1.32 | +32% share weight |
| Behavior | steal | 0.455 | -55% steal weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Relationship | conflict_mult | 0.6375 | -36% conflict mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | trust_gain_mult | 1.4375 | +44% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.133 | +13% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | stress_gain_mult | 0.9205 | -8% stress gain mult |
| Stress | violation: abuse_power | 22 | +22 stress when abuse_power |
| Stress | violation: lie | 16 | +16 stress when lie |
| Stress | violation: steal | 24 | +24 stress when steal |

**Amplified behaviors**: `build`, `cooperate`, `gather`, `help`, `leadership`, `plan`, `research`, `share`
**Suppressed behaviors**: `betray`, `combat`, `revenge`, `steal`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `guilt_sensitivity (1.15)`, `impulse_control_mult (1.1)`
**Violation stress triggers**: `abuse_power (+22)`, `lie (+16)`, `steal (+24)`

**Synergies**: [`f_sincere`](#f_sincere), [`f_fair_minded`](#f_fair_minded), [`f_patient`](A.md#f_patient)
**Anti-synergies**: [`d_machiavellian`](#d_machiavellian), [`d_psychopath_primary`](#d_psychopath_primary)

📄 source: `extracted/trait_data.json`

---

<a id="c_saintess"></a>
### Saintly Caregiver (성녀) — `c_saintess`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H` direction `high` threshold `0.7`
- Facet `A` direction `high` threshold `0.7`
- Facet `E` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | combat | 0.8075 | -19% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | explore | 0.95 | -5% explore weight |
| Behavior | flee | 1.2 | +20% flee weight |
| Behavior | help | 1.5125 | +51% help weight |
| Behavior | nurture | 1.4175 | +42% nurture weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | fear_sensitivity | 1.2 | +20% fear sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | sadness_sensitivity | 1.1 | +10% sadness sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | intimacy_gain_mult | 1.25 | +25% intimacy gain mult |
| Relationship | reassurance_seeking_mult | 1.1 | +10% reassurance seeking mult |
| Relationship | trust_gain_mult | 1.38 | +38% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Work | speed_mult | 0.98 | -2% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | flee_threshold_mult | 1.15 | +15% flee threshold mult |
| Combat | risk_taking_mult | 0.9 | -10% risk taking mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | break_threshold_mult | 0.95 | -5% break threshold mult |
| Stress | stress_from_others_harm_mult | 1.4 | +40% stress from others harm mult |
| Stress | stress_gain_mult | 1.1143 | +11% stress gain mult |
| Stress | violation: harm_innocent | 26 | +26 stress when harm_innocent |
| Stress | violation: neglect_child | 22 | +22 stress when neglect_child |

**Amplified behaviors**: `cooperate`, `flee`, `help`, `nurture`, `share`
**Suppressed behaviors**: `betray`, `combat`, `explore`, `revenge`, `steal`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `fear_sensitivity (1.2)`, `guilt_sensitivity (1.15)`, `sadness_sensitivity (1.1)`
**Violation stress triggers**: `harm_innocent (+26)`, `neglect_child (+22)`

**Synergies**: [`f_sentimental`](E.md#f_sentimental), [`f_gentle`](A.md#f_gentle)
**Anti-synergies**: [`d_sadist`](#d_sadist), [`d_callous`](#d_callous)

📄 source: `extracted/trait_data.json`

---

<a id="c_tyrant"></a>
### Tyrant (폭군) — `c_tyrant`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.3`
- Facet `X` direction `high` threshold `0.7`
- Facet `A` direction `low` threshold `0.3`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | combat | 1.15 | +15% combat weight |
| Behavior | cooperate | 0.765 | -24% cooperate weight |
| Behavior | intimidate | 1.62 | +62% intimidate weight |
| Behavior | leadership | 1.5525 | +55% leadership weight |
| Behavior | revenge | 1.2 | +20% revenge weight |
| Behavior | share | 0.72 | -28% share weight |
| Behavior | social | 1.2 | +20% social weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | anger_sensitivity | 1.2 | +20% anger sensitivity |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 1.62 | +62% conflict mult |
| Relationship | fear_induced_compliance_mult | 1.3 | +30% fear induced compliance mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 0.7225 | -28% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Work | teamwork_efficiency_mult | 0.9975 | -0% teamwork efficiency mult |
| Combat | aggression_mult | 1.4375 | +44% aggression mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | risk_taking_mult | 1.05 | +5% risk taking mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.931 | -7% stress gain mult |
| Stress | violation: share_power | 14 | +14 stress when share_power |
| Stress | violation: show_mercy | 12 | +12 stress when show_mercy |

**Amplified behaviors**: `betray`, `combat`, `intimidate`, `leadership`, `revenge`, `social`, `steal`, `take_bribe`
**Suppressed behaviors**: `cooperate`, `share`
**Emotion sensitivities**: `anger_sensitivity (1.2)`, `guilt_sensitivity (0.8)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: `share_power (+14)`, `show_mercy (+12)`

**Synergies**: [`f_harsh`](A.md#f_harsh), [`f_self_important`](#f_self_important)
**Anti-synergies**: [`c_democratic_leader`](#c_democratic_leader), [`c_saint`](#c_saint)

📄 source: `extracted/trait_data.json`

---

<a id="c_strategist"></a>
### Strategist (책사) — `c_strategist`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `H` direction `low` threshold `0.3`
- Facet `C` direction `high` threshold `0.7`
- Facet `O` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | negotiate | 1.15 | +15% negotiate weight |
| Behavior | plan | 1.62 | +62% plan weight |
| Behavior | research | 1.4547 | +45% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | steal | 1.43 | +43% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | manipulation_success_mult | 1.15 | +15% manipulation success mult |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | trust_gain_mult | 0.765 | -24% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 1.067 | +7% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | tactic_planning_mult | 1.15 | +15% tactic planning mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.9025 | -10% stress gain mult |

**Amplified behaviors**: `betray`, `build`, `craft`, `explore`, `gather`, `negotiate`, `plan`, `research`, `steal`, `take_bribe`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `guilt_sensitivity (0.8)`, `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`f_prudent`](C.md#f_prudent), [`f_curious`](O.md#f_curious)
**Anti-synergies**: [`c_saint`](#c_saint)

📄 source: `extracted/trait_data.json`

---

<a id="c_ascetic"></a>
### Ascetic (금욕주의자) — `c_ascetic`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H` direction `high` threshold `0.7`
- Facet `C` direction `high` threshold `0.7`
- Facet `O` direction `low` threshold `0.3`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | build | 1.155 | +16% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | help | 1.1 | +10% help weight |
| Behavior | hoard | 0.85 | -15% hoard weight |
| Behavior | leadership | 1.05 | +5% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.045 | +4% research weight |
| Behavior | share | 1.155 | +16% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Behavior | trade | 0.9 | -10% trade weight |
| Emotion | envy_sensitivity | 0.8 | -20% envy sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | novelty_fear_sensitivity | 1.05 | +5% novelty fear sensitivity |
| Relationship | ingroup_trust_mult | 1.1 | +10% ingroup trust mult |
| Relationship | outgroup_suspicion_mult | 1.05 | +5% outgroup suspicion mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | trust_gain_mult | 1.15 | +15% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Work | creativity_mult | 0.9 | -10% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.133 | +13% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | discipline_mult | 1.05 | +5% discipline mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | change_stress_mult | 1.15 | +15% change stress mult |
| Stress | loss_stress_mult | 0.8 | -20% loss stress mult |
| Stress | stress_gain_mult | 0.969 | -3% stress gain mult |

**Amplified behaviors**: `build`, `gather`, `help`, `leadership`, `plan`, `research`, `share`
**Suppressed behaviors**: `betray`, `hoard`, `steal`, `trade`
**Emotion sensitivities**: `envy_sensitivity (0.8)`, `guilt_sensitivity (1.15)`, `impulse_control_mult (1.1)`, `novelty_fear_sensitivity (1.05)`
**Violation stress triggers**: none

**Synergies**: [`f_frugal`](#f_frugal), [`f_prudent`](C.md#f_prudent)
**Anti-synergies**: [`f_greedy`](#f_greedy), [`c_co_ll_careless_waster`](C.md#c_co_ll_careless_waster)

📄 source: `extracted/trait_data.json`

---

<a id="c_democratic_leader"></a>
### Democratic Leader (민주적 지도자) — `c_democratic_leader`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H` direction `high` threshold `0.7`
- Facet `X` direction `high` threshold `0.7`
- Facet `A` direction `high` threshold `0.7`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | help | 1.21 | +21% help weight |
| Behavior | leadership | 1.4375 | +44% leadership weight |
| Behavior | negotiate | 1.2 | +20% negotiate weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | share | 1.265 | +26% share weight |
| Behavior | social | 1.2 | +20% social weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | conflict_mult | 0.68 | -32% conflict mult |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 1.38 | +38% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
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

**Synergies**: [`c_reconciler`](A.md#c_reconciler), [`f_fair_minded`](#f_fair_minded)
**Anti-synergies**: [`c_tyrant`](#c_tyrant), [`d_corrupt_official`](#d_corrupt_official)

📄 source: `extracted/trait_data.json`

---

<a id="c_philanthropist"></a>
### Philanthropist (자선가) — `c_philanthropist`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H` direction `high` threshold `0.75`
- Facet `A` direction `high` threshold `0.75`
- Facet `H_greed_avoidance` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | combat | 0.95 | -5% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | help | 1.5125 | +51% help weight |
| Behavior | hoard | 0.8 | -20% hoard weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | share | 1.485 | +49% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | trust_gain_mult | 1.38 | +38% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | quality_mult | 1.03 | +3% quality mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | stress_gain_mult | 0.969 | -3% stress gain mult |
| Stress | violation: extort | 20 | +20 stress when extort |
| Stress | violation: refuse_help | 12 | +12 stress when refuse_help |

**Amplified behaviors**: `cooperate`, `help`, `share`
**Suppressed behaviors**: `betray`, `combat`, `hoard`, `revenge`, `steal`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `guilt_sensitivity (1.15)`
**Violation stress triggers**: `extort (+20)`, `refuse_help (+12)`

**Synergies**: [`c_saint`](#c_saint), [`f_frugal`](#f_frugal)
**Anti-synergies**: [`f_greedy`](#f_greedy), [`d_corrupt_official`](#d_corrupt_official)

📄 source: `extracted/trait_data.json`

---

<a id="c_miser"></a>
### Miser (구두쇠) — `c_miser`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H_greed_avoidance` direction `high` threshold `0.85`
- Facet `C_prudence` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | hoard | 1.35 | +35% hoard weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | share | 0.75 | -25% share weight |
| Behavior | trade | 1.05 | +5% trade weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | loss_sensitivity | 1.25 | +25% loss sensitivity |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | loss_stress_mult | 1.35 | +35% loss stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |
| Stress | violation: donate | 14 | +14 stress when donate |

**Amplified behaviors**: `build`, `gather`, `hoard`, `plan`, `research`, `trade`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `loss_sensitivity (1.25)`
**Violation stress triggers**: `donate (+14)`

**Synergies**: [`c_co_hl_conservative_manager`](C.md#c_co_hl_conservative_manager), [`f_frugal`](#f_frugal)
**Anti-synergies**: [`c_spendthrift`](#c_spendthrift)

📄 source: `extracted/trait_data.json`

---

<a id="c_spendthrift"></a>
### Spendthrift (낭비가) — `c_spendthrift`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H_greed_avoidance` direction `low` threshold `0.15`
- Facet `C_prudence` direction `low` threshold `0.15`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 0.9 | -10% build weight |
| Behavior | explore | 1.05 | +5% explore weight |
| Behavior | hoard | 0.7 | -30% hoard weight |
| Behavior | plan | 0.85 | -15% plan weight |
| Behavior | research | 0.9 | -10% research weight |
| Behavior | trade | 1.1 | +10% trade weight |
| Behavior | waste_resources | 1.4 | +40% waste resources weight |
| Emotion | impulse_control_mult | 0.9 | -10% impulse control mult |
| Emotion | joy_gain_sensitivity | 1.15 | +15% joy gain sensitivity |
| Emotion | loss_sensitivity | 1.1 | +10% loss sensitivity |
| Relationship | reliability_mult | 0.85 | -15% reliability mult |
| Work | error_rate_mult | 1.2 | +20% error rate mult |
| Work | quality_mult | 0.9 | -10% quality mult |
| Work | speed_mult | 0.95 | -5% speed mult |
| Combat | tactic_planning_mult | 0.9 | -10% tactic planning mult |
| Stress | loss_stress_mult | 1.15 | +15% loss stress mult |
| Stress | stress_gain_mult | 1.05 | +5% stress gain mult |

**Amplified behaviors**: `explore`, `trade`, `waste_resources`
**Suppressed behaviors**: `build`, `hoard`, `plan`, `research`
**Emotion sensitivities**: `impulse_control_mult (0.9)`, `joy_gain_sensitivity (1.15)`, `loss_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_free_spirit_extro`](O.md#c_free_spirit_extro)
**Anti-synergies**: [`c_miser`](#c_miser), [`f_frugal`](#f_frugal)

📄 source: `extracted/trait_data.json`

---

<a id="c_spymaster"></a>
### Spymaster (첩보장) — `c_spymaster`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `H` direction `low` threshold `0.3`
- Facet `C_prudence` direction `high` threshold `0.85`
- Facet `O_inquisitiveness` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | craft | 1.05 | +5% craft weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.3282 | +33% research weight |
| Behavior | sabotage | 1.2 | +20% sabotage weight |
| Behavior | social | 1.05 | +5% social weight |
| Behavior | spy | 1.45 | +45% spy weight |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | interest_sensitivity | 1.1 | +10% interest sensitivity |
| Relationship | open_mindedness_mult | 1.1 | +10% open mindedness mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | suspicion_gain_mult | 1.1 | +10% suspicion gain mult |
| Work | creativity_mult | 1.15 | +15% creativity mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | learning_speed_mult | 1.1 | +10% learning speed mult |
| Work | quality_mult | 1.1 | +10% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Combat | ambush_propensity_mult | 1.2 | +20% ambush propensity mult |
| Combat | tactic_improv_mult | 1.1 | +10% tactic improv mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Stress | change_stress_mult | 0.9 | -10% change stress mult |
| Stress | stress_gain_mult | 0.95 | -5% stress gain mult |

**Amplified behaviors**: `build`, `craft`, `explore`, `gather`, `plan`, `research`, `sabotage`, `social`, `spy`
**Suppressed behaviors**: none
**Emotion sensitivities**: `impulse_control_mult (1.1)`, `interest_sensitivity (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_strategist`](#c_strategist), [`d_machiavellian`](#d_machiavellian)
**Anti-synergies**: [`c_saint`](#c_saint), [`f_sincere`](#f_sincere)

📄 source: `extracted/trait_data.json`

---

<a id="c_mercenary"></a>
### Mercenary (용병 기질) — `c_mercenary`

**Type**: personality | **Valence**: ➖ neutral

**Activation Condition**:
- Facet `H` direction `low` threshold `0.3`
- Facet `E` direction `low` threshold `0.25`
- Facet `X` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | combat | 1.26 | +26% combat weight |
| Behavior | explore | 1.1 | +10% explore weight |
| Behavior | flee | 0.9 | -10% flee weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | loyalty | 0.85 | -15% loyalty weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.2 | +20% social weight |
| Behavior | steal | 1.3 | +30% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Behavior | trade | 1.1 | +10% trade weight |
| Emotion | fear_sensitivity | 0.85 | -15% fear sensitivity |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | sadness_sensitivity | 0.9 | -10% sadness sensitivity |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | intimidation_resistance_mult | 1.1 | +10% intimidation resistance mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 0.765 | -24% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | quality_mult | 0.97 | -3% quality mult |
| Work | speed_mult | 1.02 | +2% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | flee_threshold_mult | 0.9 | -10% flee threshold mult |
| Combat | morale_mult | 1.1025 | +10% morale mult |
| Combat | risk_taking_mult | 1.1 | +10% risk taking mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | break_threshold_mult | 1.05 | +5% break threshold mult |
| Stress | stress_gain_mult | 0.8379 | -16% stress gain mult |
| Stress | violation: fight_for_free | 12 | +12 stress when fight_for_free |

**Amplified behaviors**: `betray`, `combat`, `explore`, `leadership`, `social`, `steal`, `take_bribe`, `trade`
**Suppressed behaviors**: `flee`, `loyalty`, `share`
**Emotion sensitivities**: `fear_sensitivity (0.85)`, `guilt_sensitivity (0.8)`, `joy_baseline (0.02)`, `sadness_sensitivity (0.9)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: `fight_for_free (+12)`

**Synergies**: [`c_adventurer`](E.md#c_adventurer), [`d_predatory_raider`](#d_predatory_raider)
**Anti-synergies**: [`c_saint`](#c_saint), [`c_pacifist`](A.md#c_pacifist)

📄 source: `extracted/trait_data.json`

---

<a id="c_backroom_broker"></a>
### Backroom Broker (암거래 중개인) — `c_backroom_broker`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.3`
- Facet `X` direction `high` threshold `0.7`
- Facet `C_prudence` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | smuggle | 1.4 | +40% smuggle weight |
| Behavior | social | 1.2 | +20% social weight |
| Behavior | steal | 1.495 | +49% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Behavior | trade | 1.25 | +25% trade weight |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 0.7225 | -28% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.067 | +7% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.8844 | -12% stress gain mult |

**Amplified behaviors**: `betray`, `build`, `gather`, `leadership`, `plan`, `research`, `smuggle`, `social`, `steal`, `take_bribe`, `trade`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `guilt_sensitivity (0.8)`, `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: none

**Synergies**: [`d_machiavellian`](#d_machiavellian), [`d_con_artist`](#d_con_artist)
**Anti-synergies**: [`c_hc_hh_honest_administrator`](#c_hc_hh_honest_administrator)

📄 source: `extracted/trait_data.json`

---

<a id="c_thief"></a>
### Thief (도둑 기질) — `c_thief`

**Type**: personality | **Valence**: ❌ negative

**Activation Condition**:
- Facet `H` direction `low` threshold `0.25`
- Facet `C_prudence` direction `high` threshold `0.75`
- Facet `X_social_boldness` direction `high` threshold `0.75`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 1.25 | +25% betray weight |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | leadership | 1.15 | +15% leadership weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | share | 0.9 | -10% share weight |
| Behavior | social | 1.2 | +20% social weight |
| Behavior | spy | 1.15 | +15% spy weight |
| Behavior | steal | 1.8 | +80% steal weight |
| Behavior | take_bribe | 1.3 | +30% take bribe weight |
| Behavior | trade | 1.05 | +5% trade weight |
| Emotion | guilt_sensitivity | 0.8 | -20% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Emotion | joy_baseline | 0.02 | -98% joy baseline |
| Emotion | shame_sensitivity | 0.9 | -10% shame sensitivity |
| Relationship | initiative_mult | 1.2 | +20% initiative mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | respect_gain_mult | 1.1 | +10% respect gain mult |
| Relationship | trust_gain_mult | 0.7225 | -28% trust gain mult |
| Relationship | trust_loss_mult | 1.1 | +10% trust loss mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.067 | +7% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | morale_mult | 1.05 | +5% morale mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Combat | war_crime_propensity_mult | 1.15 | +15% war crime propensity mult |
| Stress | stress_gain_mult | 0.8844 | -12% stress gain mult |
| Stress | violation: steal | 0 | +0 stress when steal |

**Amplified behaviors**: `betray`, `build`, `gather`, `leadership`, `plan`, `research`, `social`, `spy`, `steal`, `take_bribe`, `trade`
**Suppressed behaviors**: `share`
**Emotion sensitivities**: `guilt_sensitivity (0.8)`, `impulse_control_mult (1.1)`, `joy_baseline (0.02)`, `shame_sensitivity (0.9)`
**Violation stress triggers**: `steal (+0)`

**Synergies**: [`c_spymaster`](#c_spymaster), [`d_con_artist`](#d_con_artist)
**Anti-synergies**: [`c_saint`](#c_saint), [`f_fair_minded`](#f_fair_minded)

📄 source: `extracted/trait_data.json`

---

<a id="c_peacekeeper"></a>
### Peacekeeper (치안 유지자) — `c_peacekeeper`

**Type**: personality | **Valence**: ✅ positive

**Activation Condition**:
- Facet `H` direction `high` threshold `0.7`
- Facet `C` direction `high` threshold `0.7`
- Facet `A_flexibility` direction `high` threshold `0.85`

**Effects**:

| Category | Effect | Value | Meaning |
| --- | --- | --- | --- |
| Behavior | betray | 0.8 | -20% betray weight |
| Behavior | build | 1.1 | +10% build weight |
| Behavior | combat | 0.9975 | -0% combat weight |
| Behavior | cooperate | 1.2 | +20% cooperate weight |
| Behavior | gather | 1.1 | +10% gather weight |
| Behavior | help | 1.21 | +21% help weight |
| Behavior | negotiate | 1.1 | +10% negotiate weight |
| Behavior | patrol | 1.35 | +35% patrol weight |
| Behavior | plan | 1.2 | +20% plan weight |
| Behavior | research | 1.1 | +10% research weight |
| Behavior | revenge | 0.7 | -30% revenge weight |
| Behavior | share | 1.1 | +10% share weight |
| Behavior | steal | 0.7 | -30% steal weight |
| Emotion | anger_decay_mult | 1.1 | +10% anger decay mult |
| Emotion | anger_sensitivity | 0.9 | -10% anger sensitivity |
| Emotion | guilt_sensitivity | 1.15 | +15% guilt sensitivity |
| Emotion | impulse_control_mult | 1.1 | +10% impulse control mult |
| Relationship | conflict_mult | 0.85 | -15% conflict mult |
| Relationship | reliability_mult | 1.15 | +15% reliability mult |
| Relationship | trust_gain_mult | 1.265 | +26% trust gain mult |
| Relationship | trust_loss_mult | 0.9 | -10% trust loss mult |
| Relationship | trust_repair_mult | 1.1 | +10% trust repair mult |
| Work | error_rate_mult | 0.85 | -15% error rate mult |
| Work | quality_mult | 1.133 | +13% quality mult |
| Work | speed_mult | 1.1 | +10% speed mult |
| Work | teamwork_efficiency_mult | 1.05 | +5% teamwork efficiency mult |
| Combat | aggression_mult | 0.9 | -10% aggression mult |
| Combat | discipline_mult | 1.15 | +15% discipline mult |
| Combat | tactic_planning_mult | 1.1 | +10% tactic planning mult |
| Combat | war_crime_propensity_mult | 0.7 | -30% war crime propensity mult |
| Stress | stress_gain_mult | 0.9205 | -8% stress gain mult |

**Amplified behaviors**: `build`, `cooperate`, `gather`, `help`, `negotiate`, `patrol`, `plan`, `research`, `share`
**Suppressed behaviors**: `betray`, `combat`, `revenge`, `steal`
**Emotion sensitivities**: `anger_decay_mult (1.1)`, `anger_sensitivity (0.9)`, `guilt_sensitivity (1.15)`, `impulse_control_mult (1.1)`
**Violation stress triggers**: none

**Synergies**: [`c_hc_hh_honest_administrator`](#c_hc_hh_honest_administrator), [`c_diplomat`](A.md#c_diplomat)
**Anti-synergies**: [`d_corrupt_official`](#d_corrupt_official)

📄 source: `extracted/trait_data.json`

---

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
