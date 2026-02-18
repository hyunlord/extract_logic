---
title: "Stats Recorder System"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/stats_recorder.gd"
nav_order: 90
---

# Stats Recorder System

> No module-level documentation comment was extracted.

📄 source: `scripts/systems/stats_recorder.gd` | Priority: 90 | Tick interval: 200

## Overview

This page summarizes the extracted structure and runtime behavior for `Stats Recorder`.

The extractor found 5 functions, 0 configuration references, and 0 tracked entity fields.

## Configuration

No explicit `GameConfig` references extracted.

## Entity Fields Accessed

No entity field access metadata extracted.

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 13-18 (6 lines)

### `init(entity_manager: RefCounted, building_manager: RefCounted, settlement_manager: RefCounted = null)`

**Parameters**: `entity_manager: RefCounted, building_manager: RefCounted, settlement_manager: RefCounted = null`
**Lines**: 19-24 (6 lines)

### `execute_tick(_tick: int)`

**Parameters**: `_tick: int`
**Lines**: 25-72 (48 lines)

### `get_resource_deltas()`

Get resource delta per 100 ticks (rate of change)

**Parameters**: `(none)`
**Lines**: 73-89 (17 lines)

### `get_settlement_stats()`

Get per-settlement stats

**Parameters**: `(none)`
**Lines**: 90-114 (25 lines)

## Formulas

No formulas extracted for this module.

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
