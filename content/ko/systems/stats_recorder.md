---
title: "Stats Recorder"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/stats_recorder.gd"
nav_order: 90
system_name: "stats_recorder"
---

# Stats Recorder

📄 source: `scripts/systems/stats_recorder.gd` | Priority: 90 | Tick interval: 200

## Overview (개요)

The **Stats Recorder** system implements a domain-specific simulation model to simulate stats recorder dynamics for entities and world state.
It runs every **200 ticks** (0.0 game-years) at priority **90**.

**Core entity data**: No entity fields were extracted.

## Tick Pipeline (틱 파이프라인)

1. Run per-entity tick update loop
   📄 source: `scripts/systems/stats_recorder.gd:L25`
2. Resolve resource deltas
   📄 source: `scripts/systems/stats_recorder.gd:L73`
3. Resolve settlement stats
   📄 source: `scripts/systems/stats_recorder.gd:L90`

## Formulas (수식)

No extracted formulas for this module.

## Configuration Reference (설정)

No explicit `GameConfig` references extracted.

## Cross-System Effects (시스템 간 상호작용)

### Imported Modules (모듈 임포트)

No import relationships extracted for this module.

### Shared Entity Fields (공유 엔티티 필드)

No cross-system shared entity field usage was inferred.

### Signals (시그널)

No emitted signals extracted for this module.

### Downstream Impact (다운스트림 영향)

- No explicit downstream dependencies extracted.

## Entity Data Model (엔티티 데이터 모델)

No entity field metadata extracted for this module.
