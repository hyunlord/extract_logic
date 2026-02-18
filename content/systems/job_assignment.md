---
title: "Job Assignment System"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/job_assignment_system.gd"
nav_order: 8
---

# Job Assignment System

> No module-level documentation comment was extracted.

📄 source: `scripts/systems/job_assignment_system.gd` | Priority: 8 | Tick interval: config (GameConfig.JOB_ASSIGNMENT_TICK_INTERVAL)

## Overview

This page summarizes the extracted structure and runtime behavior for `Job Assignment`.

The extractor found 6 functions, 2 configuration references, and 5 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `JOB_ASSIGNMENT_TICK_INTERVAL` | 24 | Time-based tick intervals (scaled for TICK_HOURS=2) |
| `JOB_RATIOS` | { 	"gatherer": 0.5, 	"lumberjack": 0.25, 	"builder": 0.15, 	"miner": 0.1, } | Job ratios (target distribution) |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `age_stage` | read | Age or stage lifecycle state. |
| `current_action` | read | Current behavior/action state. |
| `entity_name` | read | entity name |
| `id` | read | Entity identity reference. |
| `job` | read | job |

## Functions

### `init(entity_manager: RefCounted, building_manager: RefCounted)`

**Parameters**: `entity_manager: RefCounted, building_manager: RefCounted`
**Lines**: 7-14 (8 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 15-75 (61 lines)

### `_get_dynamic_ratios(alive_count: int)`

**Parameters**: `alive_count: int`
**Lines**: 76-93 (18 lines)

### `_find_most_needed_job(ratios: Dictionary, job_counts: Dictionary, alive_count: int)`

**Parameters**: `ratios: Dictionary, job_counts: Dictionary, alive_count: int`
**Lines**: 94-108 (15 lines)

### `_rebalance_jobs(entities: Array, ratios: Dictionary, job_counts: Dictionary, alive_count: int, tick: int)`

**Parameters**: `entities: Array, ratios: Dictionary, job_counts: Dictionary, alive_count: int, tick: int`
**Lines**: 109-150 (42 lines)

### `_get_total_stockpile_food()`

**Parameters**: `(none)`
**Lines**: 151-158 (8 lines)

## Formulas

No formulas extracted for this module.

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
