---
title: "Core Modules"
description: "Core module overview and quick reference"
generated: true
source_files:
  - "scripts/core/building_data.gd"
  - "scripts/core/building_manager.gd"
  - "scripts/core/chunk_index.gd"
  - "scripts/core/deceased_registry.gd"
  - "scripts/core/emotion_data.gd"
  - "scripts/core/entity_data.gd"
  - "scripts/core/entity_manager.gd"
  - "scripts/core/event_logger.gd"
  - "scripts/core/game_calendar.gd"
  - "scripts/core/game_config.gd"
  - "scripts/core/locale.gd"
  - "scripts/core/name_generator.gd"
  - "scripts/core/pathfinder.gd"
  - "scripts/core/personality_data.gd"
  - "scripts/core/personality_system.gd"
  - "scripts/core/relationship_data.gd"
  - "scripts/core/relationship_manager.gd"
  - "scripts/core/resource_map.gd"
  - "scripts/core/save_manager.gd"
  - "scripts/core/settlement_data.gd"
  - "scripts/core/settlement_manager.gd"
  - "scripts/core/simulation_bus.gd"
  - "scripts/core/simulation_engine.gd"
  - "scripts/core/simulation_system.gd"
  - "scripts/core/species_manager.gd"
  - "scripts/core/world_data.gd"
  - "scripts/core/world_generator.gd"
nav_order: 1
---

# Core Modules

Total: 27 modules

| Module | File | Lines | Description |
|--------|------|-------|-------------|
| [Building Data](building_data.md) | `scripts/core/building_data.gd` | 43 | - |
| [Building Manager](building_manager.md) | `scripts/core/building_manager.gd` | 125 | - |
| [Chunk Index](chunk_index.md) | `scripts/core/chunk_index.gd` | 86 | 16x16 tile spatial index for O(1) chunk lookups. |
| [Deceased Registry](deceased_registry.md) | `scripts/core/deceased_registry.gd` | 103 | Registry of deceased entities for historical viewing. |
| [Emotion Data](emotion_data.md) | `scripts/core/emotion_data.gd` | 365 | Plutchik 8 basic emotions with 3-layer temporal dynamics. |
| [Entity Data](entity_data.md) | `scripts/core/entity_data.gd` | 237 | - |
| [Entity Manager](entity_manager.md) | `scripts/core/entity_manager.gd` | 190 | - |
| [Event Logger](event_logger.md) | `scripts/core/event_logger.gd` | 174 | - |
| [Game Calendar](game_calendar.md) | `scripts/core/game_calendar.gd` | 299 | Gregorian calendar system for simulation time conversion. |
| [Game Config](game_config.md) | `scripts/core/game_config.gd` | 322 | World constants Simulation parameters Time conversion (1 tick = 2 game hours) Age stage thresholds (in simulation ticks) — 6 stages infant ≤2y, toddler 3-5y, child 6-11y, teen 12-14y, adult 15-55y, elder 56+ UI Scale (adjustable at runtime, saved with game) |
| [Locale](locale.md) | `scripts/core/locale.gd` | 129 | Autoload: Locale All text lookups go through this singleton. |
| [Name Generator](name_generator.md) | `scripts/core/name_generator.gd` | 293 | - |
| [Pathfinder](pathfinder.md) | `scripts/core/pathfinder.gd` | 87 | A* pathfinding with 8-directional movement and Chebyshev heuristic |
| [Personality Data](personality_data.md) | `scripts/core/personality_data.gd` | 139 | HEXACO 24-facet personality data container. |
| [Personality System](personality_system.md) | `scripts/core/personality_system.gd` | 45 | Personality utility functions: compatibility and affinity scaling. |
| [Relationship Data](relationship_data.md) | `scripts/core/relationship_data.gd` | 13 | Relationship between two entities. |
| [Relationship Manager](relationship_manager.md) | `scripts/core/relationship_manager.gd` | 176 | Sparse relationship storage. |
| [Resource Map](resource_map.md) | `scripts/core/resource_map.gd` | 161 | - |
| [Save Manager](save_manager.md) | `scripts/core/save_manager.gd` | 592 | Binary save/load system (version 2). |
| [Settlement Data](settlement_data.md) | `scripts/core/settlement_data.gd` | 46 | - |
| [Settlement Manager](settlement_manager.md) | `scripts/core/settlement_manager.gd` | 120 | - |
| [Simulation Bus](simulation_bus.md) | `scripts/core/simulation_bus.gd` | 42 | Core simulation events |
| [Simulation Engine](simulation_engine.md) | `scripts/core/simulation_engine.gd` | 78 | - |
| [Simulation System](simulation_system.md) | `scripts/core/simulation_system.gd` | 15 | - |
| [Species Manager](species_manager.md) | `scripts/core/species_manager.gd` | 82 | Species data loader singleton (Autoload). |
| [World Data](world_data.md) | `scripts/core/world_data.gd` | 118 | - |
| [World Generator](world_generator.md) | `scripts/core/world_generator.gd` | 75 | Generate a procedural world using FastNoiseLite |
