---
title: "Job Assignment"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/job_assignment_system.gd"
nav_order: 8
system_name: "job_assignment"
---

# Job Assignment

📄 소스: `scripts/systems/job_assignment_system.gd` | 우선순위: 8 | 틱 간격: config (GameConfig.JOB_ASSIGNMENT_TICK_INTERVAL)

## 개요

The **Job Assignment** system implements a domain-specific simulation model to simulate job assignment dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.JOB_ASSIGNMENT_TICK_INTERVAL`) at priority **8**.

**핵심 엔티티 데이터**: `age_stage` (read/write (inferred)), `current_action` (read/write (inferred)), `entity_name` (read/write (inferred)), `id` (read/write (inferred)), `job` (read/write (inferred))

## 틱 파이프라인

1. Run per-entity tick update loop
   📄 source: `scripts/systems/job_assignment_system.gd:L15`
2. Resolve dynamic ratios
   📄 source: `scripts/systems/job_assignment_system.gd:L76`
3. Resolve total stockpile food
   📄 source: `scripts/systems/job_assignment_system.gd:L151`

## 수식

No extracted formulas for this module.

## 설정 레퍼런스

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `JOB_ASSIGNMENT_TICK_INTERVAL` | 24 | System update cadence. | Lower values increase update frequency and responsiveness. |
| `JOB_RATIOS` | { 	"gatherer": 0.5, 	"lumberjack": 0.25, 	"builder": 0.15, 	"miner": 0.1, } | Job ratios (target distribution) | Adjusts baseline system behavior under this module. |

## 시스템 간 상호작용

### 모듈 임포트

임포트 관계가 추출되지 않음

### 공유 엔티티 필드

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `age_stage` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`childcare`](childcare.md), [`construction`](construction.md), [`family`](family.md), [`gathering`](gathering.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md) |
| `current_action` | read/write (inferred) | [`behavior`](behavior.md), [`construction`](construction.md), [`emotions`](emotions.md), [`gathering`](gathering.md), [`migration`](migration.md), [`movement`](movement.md), [`needs`](needs.md), [`social_events`](social_events.md), [`stress`](stress.md) |
| `entity_name` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`chronicle`](chronicle.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`population`](population.md), [`stress`](stress.md) |
| `id` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`migration`](migration.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`population`](population.md), [`social_events`](social_events.md) |
| `job` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md) |

### 시그널

시그널 메타데이터가 추출되지 않음

### 다운스트림 영향

- 다운스트림 의존성이 추출되지 않음

## 엔티티 데이터 모델

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `age_stage` | read/write (inferred) | String enum | Lifecycle progression used for stage-specific behavior and events. | Named categorical states. |
| `current_action` | read/write (inferred) | String enum | Current behavior intent used by schedulers and downstream systems. | System-defined value domain. |
| `entity_name` | read/write (inferred) | Variant | Entity name. | System-defined value domain. |
| `id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
| `job` | read/write (inferred) | Variant | Job. | System-defined value domain. |
