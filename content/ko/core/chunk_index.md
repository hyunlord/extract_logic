---
title: "Chunk Index"
description: "16x16 tile spatial index for O(1) chunk lookups."
generated: true
source_files:
  - "scripts/core/chunk_index.gd"
nav_order: 3
---

# Chunk Index

> 16x16 tile spatial index for O(1) chunk lookups. Avoids O(n²) proximity checks by only scanning nearby chunks. chunk_key (Vector2i) -> Array[int] (entity IDs)

📄 source: `scripts/core/chunk_index.gd` | 86 lines | extends: RefCounted

## 개요 (Overview)
16x16 tile spatial index for O(1) chunk lookups.

## 공개 API (Public API)

### Functions
| Function | Parameters | Returns | Line |
|----------|------------|---------|------|
| - | - | - | - |

### Signals
| Signal | Parameters |
|--------|------------|
| - | - |

## 의존성 (Dependencies)
- Imports: -
- Used by: [`entity_manager.gd`](entity_manager.md)
