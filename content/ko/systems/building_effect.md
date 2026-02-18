---
title: "Building Effect"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/building_effect_system.gd"
nav_order: 15
system_name: "building_effect"
---

# Building Effect

📄 소스: `scripts/systems/building_effect_system.gd` | 우선순위: 15 | 틱 간격: config (GameConfig.BUILDING_EFFECT_TICK_INTERVAL)

## 개요

The **Building Effect** system implements a domain-specific simulation model to simulate building effect dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.BUILDING_EFFECT_TICK_INTERVAL`) at priority **15**.

**핵심 엔티티 데이터**: `energy` (read/write (inferred)), `social` (read/write (inferred))

## 틱 파이프라인

1. Run per-entity tick update loop
   📄 source: `scripts/systems/building_effect_system.gd:L17`
2. Apply campfire
   📄 source: `scripts/systems/building_effect_system.gd:L30`
3. Apply shelter
   📄 source: `scripts/systems/building_effect_system.gd:L44`

## 수식

No extracted formulas for this module.

## 설정 레퍼런스

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `BUILDING_EFFECT_TICK_INTERVAL` | 10 | System update cadence. | Lower values increase update frequency and responsiveness. |
| `BUILDING_TYPES` | { 	"stockpile": {"cost": {"wood": 2.0}, "build_ticks": 36, "radius": 8}, 	"shelter": {"cost": {"wood": 4.0, "stone": 1.0}, "build_ticks": 60, "radius": 0}, 	"campfire": {"cost": {"wood": 1.0}, "build_ticks": 24, "radius": 5}, } | Building type definitions | Adjusts baseline system behavior under this module. |

## 시스템 간 상호작용

### 모듈 임포트

임포트 관계가 추출되지 않음

### 공유 엔티티 필드

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `energy` | read/write (inferred) | [`behavior`](behavior.md), [`emotions`](emotions.md), [`mental_break`](mental_break.md), [`movement`](movement.md), [`needs`](needs.md), [`stress`](stress.md) |
| `social` | read/write (inferred) | [`behavior`](behavior.md), [`movement`](movement.md), [`needs`](needs.md), [`stress`](stress.md) |

### 시그널

시그널 메타데이터가 추출되지 않음

### 다운스트림 영향

- 다운스트림 의존성이 추출되지 않음

## 엔티티 데이터 모델

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `energy` | read/write (inferred) | float | Fatigue/rest capacity controlling action readiness. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
| `social` | read/write (inferred) | float | Social fulfillment/deficit level affecting mood and stress. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
