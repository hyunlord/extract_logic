---
title: "Trait System"
description: "Discrete trait emergence and effects system."
generated: true
source_files:
  - "scripts/systems/trait_system.gd"
nav_order: 100
---

# Trait System

> Discrete trait emergence and effects system. Use preload("res://scripts/systems/trait_system.gd") for access.

📄 source: `scripts/systems/trait_system.gd` | Priority: 100 | Tick interval: n/a

## Overview

Discrete trait emergence and effects system. Use preload("res://scripts/systems/trait_system.gd") for access.

The extractor found 16 functions, 0 configuration references, and 6 tracked entity fields.

## Configuration

No explicit `GameConfig` references extracted.

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `active_traits` | read | Personality and trait state. |
| `display_traits` | read | Personality and trait state. |
| `emotion_data` | read | Emotion-related state. |
| `emotions` | read | Emotion-related state. |
| `personality` | read | Personality and trait state. |
| `traits_dirty` | read | Personality and trait state. |

## Functions

### `_ensure_loaded()`

**Parameters**: `(none)`
**Lines**: 11-50 (40 lines)

### `check_traits(pd: RefCounted)`

Check which traits are active for a given PersonalityData. Returns Array of trait ID strings (all matching, before display filtering).

**Parameters**: `pd: RefCounted`
**Lines**: 51-63 (13 lines)

### `_evaluate_condition(condition: Dictionary, pd: RefCounted)`

Evaluate a trait condition against PersonalityData. Supports single conditions (facet/axis) and composite conditions ("all" array).

**Parameters**: `condition: Dictionary, pd: RefCounted`
**Lines**: 64-76 (13 lines)

### `_evaluate_single(cond: Dictionary, pd: RefCounted)`

Evaluate a single facet/axis condition. "facet" key is used for both axes ("H") and facets ("H_sincerity").

**Parameters**: `cond: Dictionary, pd: RefCounted`
**Lines**: 77-94 (18 lines)

### `evaluate_traits(entity: RefCounted)`

Evaluate entity traits and cache full/display trait dictionaries on entity_data.

**Parameters**: `entity: RefCounted`
**Lines**: 95-123 (29 lines)

### `_apply_axis_cap(traits: Array, pd: RefCounted)`

Apply per-axis cap: max 2 facet traits per HEXACO axis. Composite traits bypass this cap.

**Parameters**: `traits: Array, pd: RefCounted`
**Lines**: 124-163 (40 lines)

### `_sort_and_cap_display(traits: Array)`

Sort traits for display priority (no cap — show all). Priority: Dark > Composite > Facet.

**Parameters**: `traits: Array`
**Lines**: 164-203 (40 lines)

### `filter_display_traits(all_trait_ids: Array)`

Backward-compatible display filtering for ID arrays. Returns sorted/capped trait IDs.

**Parameters**: `all_trait_ids: Array`
**Lines**: 204-222 (19 lines)

### `get_behavior_weight(entity: RefCounted, action: String)`

Get combined behavior_weight multiplier for an action (multiplicative stacking).

**Parameters**: `entity: RefCounted, action: String`
**Lines**: 223-234 (12 lines)

### `get_emotion_modifier(entity: RefCounted, modifier_key: String)`

Get combined emotion_modifier (additive stacking around 1.0 base).

**Parameters**: `entity: RefCounted, modifier_key: String`
**Lines**: 235-246 (12 lines)

### `get_violation_stress(entity: RefCounted, action: String)`

Get total violation_stress for an action.

**Parameters**: `entity: RefCounted, action: String`
**Lines**: 247-259 (13 lines)

### `get_effect_mult(entity: RefCounted, category: String, key: String)`

Get multiplier from any effects category (multiplicative stacking).

**Parameters**: `entity: RefCounted, category: String, key: String`
**Lines**: 260-272 (13 lines)

### `on_action_performed(entity: RefCounted, action: String)`

Called when entity performs an action — applies violation stress. Phase C1 will call this from behavior_system.

**Parameters**: `entity: RefCounted, action: String`
**Lines**: 273-283 (11 lines)

### `get_trait_effects(trait_ids: Array)`

Backward compatibility helper. Returns flattened combined behavior_weights across trait IDs.

**Parameters**: `trait_ids: Array`
**Lines**: 284-305 (22 lines)

### `get_trait_definition(trait_id: String)`

Get trait definition by ID (for UI display).

**Parameters**: `trait_id: String`
**Lines**: 306-311 (6 lines)

### `get_trait_sentiment(trait_id: String)`

Get valence for a trait ("positive", "negative", "neutral").

**Parameters**: `trait_id: String`
**Lines**: 312-314 (3 lines)

## Formulas

No formulas extracted for this module.

## Dependencies

### Imports

- [`trait_system.gd`](trait.md) - via `preload` (line 4)

### Signals Emitted

- None

### Referenced By

- [`personality_generator`](personality_generator.md) - depends on this module
- [`personality_maturation`](personality_maturation.md) - depends on this module
- [`trait`](trait.md) - depends on this module
