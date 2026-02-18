---
title: "Chronicle"
description: "Chronicles significant events in the simulation for historical viewing."
generated: true
source_files:
  - "scripts/systems/chronicle_system.gd"
nav_order: 999
system_name: "chronicle"
---

# Chronicle

📄 source: `scripts/systems/chronicle_system.gd` | Priority: n/a | Tick interval: n/a

## Overview (개요)

The **Chronicle** system implements a domain-specific simulation model to simulate chronicles significant events in the simulation for historical viewing.
It runs **at an unspecified cadence** at priority **n/a**.

**Core entity data**: `entity_name` (read/write (inferred)), `is_alive` (read/write (inferred))

> Chronicles significant events in the simulation for historical viewing.

## Tick Pipeline (틱 파이프라인)

1. Resolve world events
   📄 source: `scripts/systems/chronicle_system.gd:L80`
2. Resolve personal events
   📄 source: `scripts/systems/chronicle_system.gd:L93`
3. Resolve event count
   📄 source: `scripts/systems/chronicle_system.gd:L98`
4. Resolve entity name
   📄 source: `scripts/systems/chronicle_system.gd:L148`

## Formulas (수식)

No extracted formulas for this module.

## Configuration Reference (설정)

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `TICKS_PER_YEAR` | 4380 | Simulation-time conversion or cadence. | Adjusts baseline system behavior under this module. |

## Cross-System Effects (시스템 간 상호작용)

### Imported Modules (모듈 임포트)

- `scripts/core/game_calendar.gd` via `preload` at `scripts/systems/chronicle_system.gd:L6`

### Shared Entity Fields (공유 엔티티 필드)

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `entity_name` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`population`](population.md), [`stress`](stress.md) |
| `is_alive` | read/write (inferred) | [`family`](family.md) |

### Signals (시그널)

No emitted signals extracted for this module.

### Downstream Impact (다운스트림 영향)

- No explicit downstream dependencies extracted.

## Entity Data Model (엔티티 데이터 모델)

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `entity_name` | read/write (inferred) | Variant | Entity name. | System-defined value domain. |
| `is_alive` | read/write (inferred) | bool | Is alive. | System-defined value domain. |
