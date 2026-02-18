---
title: "dyad_definition Data"
description: "species/human/emotions data file documentation"
generated: true
source_files:
  - "data/species/human/emotions/dyad_definition.json"
nav_order: 10
---

# dyad_definition

📄 source: `data/species/human/emotions/dyad_definition.json` | Category: species/human/emotions | Type: object

## Overview

- Configures: `species/human/emotions` 데이터 도메인 설정 값. Configuration values for the `species/human/emotions` data domain.
- Read by systems/modules: species_manager
- Related documentation: [`species_manager`](../../../../core/species_manager.md)

## Interpreted Parameters

### Timing & Decay

| Parameter | Value | Type | What it controls |
|----------------------|-----------|------------|-----------------------------|
| `dyads.sentimentality.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.sentimentality.components.sample` | trust | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.sentimentality.name_kr` | 감상 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.sentimentality.type` | tertiary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |

### Thresholds & Bounds

| Parameter | Value | Type | What it controls |
|----------------------|-----------|------------|-----------------------------|
| `dyads.dominance.components` | 2 items | array | Activation boundary used by game logic. (작동 임계값) |
| `dyads.dominance.components.sample` | anger | string | Activation boundary used by game logic. (작동 임계값) |
| `dyads.dominance.name_kr` | 지배 | string | Activation boundary used by game logic. (작동 임계값) |
| `dyads.dominance.type` | tertiary | string | Activation boundary used by game logic. (작동 임계값) |

### Identifiers & Labels

| Parameter | Value | Type | What it controls |
|----------------------|-----------|------------|-----------------------------|
| `dyads.aggressiveness.name_kr` | 공격성 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.aggressiveness.type` | primary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.anxiety.name_kr` | 불안 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.anxiety.type` | tertiary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.awe.name_kr` | 경외 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.awe.type` | primary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.contempt.name_kr` | 경멸 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.contempt.type` | primary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.curiosity.name_kr` | 호기심 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.curiosity.type` | secondary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.cynicism.name_kr` | 냉소 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.cynicism.type` | secondary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.delight.name_kr` | 환희 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.delight.type` | tertiary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.despair.name_kr` | 절망 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.despair.type` | secondary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.disappointment.name_kr` | 실망 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.disappointment.type` | primary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.envy.name_kr` | 시기 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.envy.type` | secondary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.guilt.name_kr` | 죄책감 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.guilt.type` | secondary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.hope.name_kr` | 희망 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.hope.type` | secondary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.love.name_kr` | 사랑 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.love.type` | primary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.morbidness.components` | 2 items | array | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.morbidness.components.sample` | disgust | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.morbidness.name_kr` | 잔혹 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.morbidness.type` | tertiary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.optimism.name_kr` | 낙관 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.optimism.type` | primary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.outrage.name_kr` | 격분 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.outrage.type` | tertiary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.pessimism.name_kr` | 비관 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.pessimism.type` | tertiary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.pride.components` | 2 items | array | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.pride.components.sample` | anger | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.pride.name_kr` | 자부심 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.pride.type` | secondary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.remorse.name_kr` | 후회 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.remorse.type` | primary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.shame.name_kr` | 수치 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.shame.type` | tertiary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.submission.name_kr` | 복종 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.submission.type` | primary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.unbelief.name_kr` | 불신 | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |
| `dyads.unbelief.type` | secondary | string | Identifier/label used for lookup or UI presentation. (식별자/라벨) |

### Other Parameters

| Parameter | Value | Type | What it controls |
|----------------------|-----------|------------|-----------------------------|
| `dyads.aggressiveness.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.aggressiveness.components.sample` | anger | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.anxiety.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.anxiety.components.sample` | anticipation | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.awe.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.awe.components.sample` | fear | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.contempt.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.contempt.components.sample` | disgust | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.curiosity.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.curiosity.components.sample` | trust | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.cynicism.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.cynicism.components.sample` | disgust | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.delight.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.delight.components.sample` | joy | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.despair.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.despair.components.sample` | fear | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.disappointment.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.disappointment.components.sample` | surprise | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.envy.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.envy.components.sample` | sadness | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.guilt.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.guilt.components.sample` | joy | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.hope.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.hope.components.sample` | anticipation | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.love.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.love.components.sample` | joy | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.optimism.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.optimism.components.sample` | anticipation | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.outrage.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.outrage.components.sample` | surprise | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.pessimism.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.pessimism.components.sample` | sadness | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.remorse.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.remorse.components.sample` | sadness | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.shame.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.shame.components.sample` | fear | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.submission.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.submission.components.sample` | trust | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.unbelief.components` | 2 items | array | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |
| `dyads.unbelief.components.sample` | surprise | string | General configuration parameter used by the corresponding system. (해당 시스템의 일반 설정 값) |

## References

- [`species_manager`](../../../../core/species_manager.md) - references data under `data/species/`

## Manual Notes

<!-- MANUAL:START -->
<!-- MANUAL:END -->
