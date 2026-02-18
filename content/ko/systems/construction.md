---
title: "Construction"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/construction_system.gd"
nav_order: 28
system_name: "construction"
---

# Construction

📄 소스: `scripts/systems/construction_system.gd` | 우선순위: 28 | 틱 간격: config (GameConfig.CONSTRUCTION_TICK_INTERVAL)

## 개요

The **Construction** system implements a domain-specific simulation model to simulate construction dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.CONSTRUCTION_TICK_INTERVAL`) at priority **28**.

**핵심 엔티티 데이터**: `action_target` (read/write (inferred)), `age_stage` (read/write (inferred)), `buildings_built` (read/write (inferred)), `current_action` (read/write (inferred)), `position` (read/write (inferred))

## 틱 파이프라인

1. Run per-entity tick update loop
   📄 source: `scripts/systems/construction_system.gd:L15`

## 수식

No extracted formulas for this module.

## 설정 레퍼런스

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `BUILDING_TYPES` | { 	"stockpile": {"cost": {"wood": 2.0}, "build_ticks": 36, "radius": 8}, 	"shelter": {"cost": {"wood": 4.0, "stone": 1.0}, "build_ticks": 60, "radius": 0}, 	"campfire": {"cost": {"wood": 1.0}, "build_ticks": 24, "radius": 5}, } | Building type definitions | Adjusts baseline system behavior under this module. |
| `CONSTRUCTION_TICK_INTERVAL` | 5 | System update cadence. | Lower values increase update frequency and responsiveness. |

## 시스템 간 상호작용

### 모듈 임포트

임포트 관계가 추출되지 않음

### 공유 엔티티 필드

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `action_target` | read/write (inferred) | [`behavior`](behavior.md), [`migration`](migration.md), [`movement`](movement.md) |
| `age_stage` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`childcare`](childcare.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md) |
| `current_action` | read/write (inferred) | [`behavior`](behavior.md), [`emotions`](emotions.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`movement`](movement.md), [`needs`](needs.md), [`social_events`](social_events.md), [`stress`](stress.md) |
| `position` | read/write (inferred) | [`behavior`](behavior.md), [`gathering`](gathering.md), [`movement`](movement.md), [`social_events`](social_events.md) |

### 시그널

시그널 메타데이터가 추출되지 않음

### 다운스트림 영향

- 다운스트림 의존성이 추출되지 않음

## 엔티티 데이터 모델

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `action_target` | read/write (inferred) | Variant | Current behavior intent used by schedulers and downstream systems. | System-defined value domain. |
| `age_stage` | read/write (inferred) | String enum | Lifecycle progression used for stage-specific behavior and events. | Named categorical states. |
| `buildings_built` | read/write (inferred) | Variant | Buildings built. | System-defined value domain. |
| `current_action` | read/write (inferred) | String enum | Current behavior intent used by schedulers and downstream systems. | System-defined value domain. |
| `position` | read/write (inferred) | Vector2 / Vector2i | World-space location used for movement and proximity checks. | Grid/world vectors. |
