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

📄 소스: `scripts/systems/stats_recorder.gd` | 우선순위: 90 | 틱 간격: 200

## 개요

The **Stats Recorder** system implements a domain-specific simulation model to simulate stats recorder dynamics for entities and world state.
It runs every **200 ticks** (0.0 game-years) at priority **90**.

**핵심 엔티티 데이터**: No entity fields were extracted.

## 틱 파이프라인

1. Run per-entity tick update loop
   📄 source: `scripts/systems/stats_recorder.gd:L25`
2. Resolve resource deltas
   📄 source: `scripts/systems/stats_recorder.gd:L73`
3. Resolve settlement stats
   📄 source: `scripts/systems/stats_recorder.gd:L90`

## 수식

No extracted formulas for this module.

## 설정 레퍼런스

GameConfig 참조가 추출되지 않음

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
