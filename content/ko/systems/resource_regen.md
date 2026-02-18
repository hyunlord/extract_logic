---
title: "Resource Regen"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/resource_regen_system.gd"
nav_order: 5
system_name: "resource_regen"
---

# Resource Regen

📄 소스: `scripts/systems/resource_regen_system.gd` | 우선순위: 5 | 틱 간격: config (GameConfig.RESOURCE_REGEN_TICK_INTERVAL)

## 개요

The **Resource Regen** system implements a domain-specific simulation model to simulate resource regen dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.RESOURCE_REGEN_TICK_INTERVAL`) at priority **5**.

**핵심 엔티티 데이터**: No entity fields were extracted.

## 틱 파이프라인

1. Run per-entity tick update loop
   📄 source: `scripts/systems/resource_regen_system.gd:L15`

## 수식

No extracted formulas for this module.

## 설정 레퍼런스

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `FOOD_REGEN_RATE` | 1.0 | Rate coefficient for change per tick. | Directly scales accumulation/decay velocity each tick. |
| `RESOURCE_REGEN_TICK_INTERVAL` | 120 | System update cadence. | Lower values increase update frequency and responsiveness. |
| `ResourceType` | (not found) | Behavior tuning constant. | Adjusts baseline system behavior under this module. |
| `WOOD_REGEN_RATE` | 0.3 | Rate coefficient for change per tick. | Directly scales accumulation/decay velocity each tick. |

## 시스템 간 상호작용

### 모듈 임포트

임포트 관계가 추출되지 않음

### 공유 엔티티 필드

공유 필드가 추론되지 않음

### 시그널

시그널 메타데이터가 추출되지 않음

### 다운스트림 영향

- 다운스트림 의존성이 추출되지 않음

## 엔티티 데이터 모델

No entity field metadata extracted for this module.
