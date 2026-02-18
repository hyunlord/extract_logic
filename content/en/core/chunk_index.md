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

## Overview
16x16 tile spatial index for O(1) chunk lookups.

## Public API

### Functions
| Function | Parameters | Returns | Line |
|----------|------------|---------|------|
| - | - | - | - |

### Signals
| Signal | Parameters |
|--------|------------|
| - | - |

## Dependencies
- Imports: -
- Used by: [`entity_manager.gd`](entity_manager.md)
