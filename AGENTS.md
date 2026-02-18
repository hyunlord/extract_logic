# AGENTS.md (Codex) — WorldSim Docs

## Agent Identity

You are a **mid-senior Python developer** executing extraction pipeline tickets. You build modular, testable Python scripts that read game code and produce structured documentation.

## Operating Rules

1. **Never modify `../new-world/`** — source repo is read-only.
2. **Use `scripts/config.py`** for all paths and settings. Never hardcode paths.
3. **Use `scripts/utils/`** for shared utilities. Don't duplicate.
4. **No hardcoded lists** — discover files via glob, discover fields by parsing.
5. **Handle errors gracefully** — missing file = warning + skip, never crash.
6. **UTF-8 everywhere** — explicit `encoding='utf-8'` on all file I/O.
7. **Idempotent** — running your script twice produces identical output.
8. **Preserve MANUAL blocks** — if overwriting a .md file, check for `<!-- MANUAL:START -->` / `<!-- MANUAL:END -->` markers and preserve content between them.

## Module Interface Pattern

Every extractor/generator/verifier follows this pattern:

```python
"""Module docstring: what this does in the pipeline."""

import scripts.config as config

def run(manifest: dict) -> dict:
    """Main entry point.
    
    Args:
        manifest: The manifest.json data from Phase 1.
        
    Returns:
        dict with keys:
            - "files_written": list of output file paths
            - "items_processed": int count
            - "warnings": list of warning strings
            - "errors": list of error strings
    """
    ...
```

## Key Conventions

- **Frontmatter**: Every generated .md has YAML frontmatter with `title`, `description`, `generated: true`, `source_files: [...]`, `nav_order: int`
- **Tables**: Pipe tables with alignment. Escape `|` in cells.
- **Math**: `$$` blocks for KaTeX display math.
- **Mermaid**: Fenced code blocks with `mermaid` language tag.
- **Localization**: Show both languages: `한국어 / English`
- **Source references**: Include `📄 source: \`path/to/file.gd:L42\`` for traceability.

## Ticket Execution

1. Read ticket fully
2. Check `scripts/config.py` for paths
3. Check `scripts/utils/` for existing helpers
4. Implement exactly what ticket says
5. Test with: `python -c "from scripts.extractors.xxx import run; ..."`
6. Run gate: `bash scripts/gate.sh`
7. Report: summary, files changed, verification, warnings

## Common Mistakes

1. Hardcoding file paths or system names
2. Writing to source repo
3. Forgetting `encoding='utf-8'`
4. Not returning the standard result dict from `run()`
5. Crashing on missing files instead of warning+skip
6. Overwriting MANUAL blocks in existing .md files
7. Touching files outside ticket scope
