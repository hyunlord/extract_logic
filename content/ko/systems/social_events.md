---
title: "Social Events"
description: "Drives relationship interactions using chunk-based proximity."
generated: true
source_files:
  - "scripts/systems/social_event_system.gd"
nav_order: 37
system_name: "social_events"
---

# Social Events

📄 소스: `scripts/systems/social_event_system.gd` | 우선순위: 37 | 틱 간격: 30

## 개요

The **Social Events** system implements a domain-specific simulation model to simulate drives relationship interactions using chunk-based proximity.
It runs every **30 ticks** (0.0 game-years) at priority **37**.

**핵심 엔티티 데이터**: `current_action` (read), `id` (read), `position` (read)

> Drives relationship interactions using chunk-based proximity.

## 틱 파이프라인

1. Run per-entity tick update loop
   📄 source: `scripts/systems/social_event_system.gd:L25`
   Math context: exponential decay dynamics
2. Process social events
   📄 source: `scripts/systems/social_event_system.gd:L32`
3. Apply event
   📄 source: `scripts/systems/social_event_system.gd:L151`
   Math context: Computes a gameplay state update from mathematical relationships in the source logic.
4. Emit system signals: `couple_formed`, `ui_notification`
   📄 source: `scripts/systems/social_event_system.gd:L250`

## 수식

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
80 + interactions \ge  20
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
PROPOSAL: romantic + romantic_interest >= 80 + interactions >= 20
```

| Variable | Meaning |
| :-- | :-- |
| `romantic` | romantic |
| `romantic_interest` | romantic interest |
| `interactions` | interactions |

📄 source: `scripts/systems/social_event_system.gd:L106`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
_rng.randf()  \cdot  total
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
var roll: float = _rng.randf() * total
```

| Variable | Meaning |
| :-- | :-- |
| `roll` | roll |
| `_rng` |  rng |
| `total` | total |

📄 source: `scripts/systems/social_event_system.gd:L142`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
clampf(rel.affinity / 100.0, 0.0, 1.0)
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
var bond: float = clampf(rel.affinity / 100.0, 0.0, 1.0)
```

| Variable | Meaning |
| :-- | :-- |
| `bond` | bond |
| `rel` | rel |
| `affinity` | affinity |

📄 source: `scripts/systems/social_event_system.gd:L203`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
(romantic_interest/100)  \cdot  compatibility
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
Acceptance probability = (romantic_interest/100) * compatibility
```

| Variable | Meaning |
| :-- | :-- |
| `probability` | probability term |
| `romantic_interest` | romantic interest |
| `compatibility` | compatibility |

📄 source: `scripts/systems/social_event_system.gd:L230`

## 설정 레퍼런스

GameConfig 참조가 추출되지 않음

## 시스템 간 상호작용

### 모듈 임포트

- `scripts/core/personality_system.gd` via `preload` at `scripts/systems/social_event_system.gd:L2`

### 공유 엔티티 필드

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `current_action` | read | [`behavior`](behavior.md), [`construction`](construction.md), [`emotions`](emotions.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`movement`](movement.md), [`needs`](needs.md), [`stress`](stress.md) |
| `id` | read | [`behavior`](behavior.md), [`aging`](aging.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`population`](population.md) |
| `position` | read | [`behavior`](behavior.md), [`construction`](construction.md), [`gathering`](gathering.md), [`movement`](movement.md) |

공유 필드 읽기: `current_action`, `id`, `position`

### 시그널

| Signal | Parameters | Subscribers | Source Line |
| :-- | :-- | :-- | :-- |
| `couple_formed` | entity_a_id: int, entity_a_name: String, entity_b_id: int, entity_b_name: String, tick: int | No known subscribers | L250 |
| `ui_notification` | message: String, type: String | No known subscribers | L248 |

### 다운스트림 영향

- 다운스트림 의존성이 추출되지 않음

## 엔티티 데이터 모델

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `current_action` | read | String enum | Current behavior intent used by schedulers and downstream systems. | System-defined value domain. |
| `id` | read | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
| `position` | read | Vector2 / Vector2i | World-space location used for movement and proximity checks. | Grid/world vectors. |
