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

📄 소스: `scripts/systems/chronicle_system.gd` | 우선순위: n/a | 틱 간격: n/a

## 개요

The **Chronicle** system implements a domain-specific simulation model to simulate chronicles significant events in the simulation for historical viewing.
It runs **at an unspecified cadence** at priority **n/a**.

**핵심 엔티티 데이터**: `entity_name` (read/write (inferred)), `is_alive` (read/write (inferred))

> Chronicles significant events in the simulation for historical viewing.

## 틱 파이프라인

1. Resolve world events
   📄 source: `scripts/systems/chronicle_system.gd:L80`
2. Resolve personal events
   📄 source: `scripts/systems/chronicle_system.gd:L93`
3. Resolve event count
   📄 source: `scripts/systems/chronicle_system.gd:L98`
4. Resolve entity name
   📄 source: `scripts/systems/chronicle_system.gd:L148`

## 수식

No extracted formulas for this module.

## 설정 레퍼런스

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `TICKS_PER_YEAR` | 4380 | Simulation-time conversion or cadence. | Adjusts baseline system behavior under this module. |

## 시스템 간 상호작용

### 모듈 임포트

- `scripts/core/game_calendar.gd` via `preload` at `scripts/systems/chronicle_system.gd:L6`

### 공유 엔티티 필드

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `entity_name` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`population`](population.md), [`stress`](stress.md) |
| `is_alive` | read/write (inferred) | [`family`](family.md) |

### 시그널

시그널 메타데이터가 추출되지 않음

### 다운스트림 영향

- 다운스트림 의존성이 추출되지 않음

## 엔티티 데이터 모델

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `entity_name` | read/write (inferred) | Variant | Entity name. | System-defined value domain. |
| `is_alive` | read/write (inferred) | bool | Is alive. | System-defined value domain. |
