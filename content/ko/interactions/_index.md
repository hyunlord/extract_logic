---
title: "System Interaction Index"
description: "Master calculation-pipeline dependency graph"
generated: true
source_files:
  - "extracted/references.json"
  - "extracted/systems.json"
  - "extracted/formulas.json"
  - "extracted/stressor_data.json"
  - "extracted/decay_config.json"
  - "extracted/emotion_presets.json"
nav_order: 1
---

# System Interaction Index

한국어 / English: 시스템 계산 의존 그래프 / System calculation dependency graph.

Generated 7 calculation-pipeline interaction pages.

## 시스템 의존 그래프
```mermaid
graph TD
    PERS[Personality System] -->|sensitivity, baselines| EMOT[Emotion System]
    PERS -->|modifier weights| STRESS[Stress System]
    EVENTS[Game Events] -->|appraisal vectors| EMOT
    EMOT -->|emotion values| STRESS
    STRESS -->|allostatic load| MORT[Mortality System]
    STRESS -->|mental break| EMOT
    MORT -->|death event| STRESS
    MORT -->|death event| EMOT
```

## 상호작용 페이지
| Interaction Pair | Output Page |
|---|---|
| `Personality → Emotion` | [personality-emotion.md](personality-emotion.md) |
| `Personality → Stress` | [personality-stress.md](personality-stress.md) |
| `Emotion → Stress` | [emotion-stress.md](emotion-stress.md) |
| `Stress → Mortality` | [stress-mortality.md](stress-mortality.md) |
| `Personality → Mortality` | [personality-mortality.md](personality-mortality.md) |
| `Events → Emotion` | [events-emotion.md](events-emotion.md) |
| `Stress → Emotion` | [stress-emotion.md](stress-emotion.md) |

## 피드백 루프
- stress -> mental break -> emotion inject -> more stress
- death event -> bereavement stressor -> stress -> allostatic load -> mortality

## 수동 노트
<!-- MANUAL:START -->
<!-- MANUAL:END -->
