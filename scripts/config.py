"""Pipeline configuration — single source of truth for all paths and settings.

All scripts import this module. No hardcoded paths anywhere else.
"""

import os

# ── Source Repository (READ ONLY) ──────────────────────────────────────
# Default: sibling directory ../new-world relative to this repo root
# Override: set WORLDSIM_SOURCE environment variable
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_REPO = os.environ.get(
    "WORLDSIM_SOURCE",
    os.path.join(_REPO_ROOT, "..", "new-world"),
)

# ── Discovery Glob Patterns (relative to SOURCE_REPO) ─────────────────
SYSTEM_GLOBS = ["scripts/systems/*.gd"]
CORE_GLOBS = ["scripts/core/*.gd"]
AI_GLOBS = ["scripts/ai/*.gd"]
DATA_GLOBS = ["data/**/*.json"]
LOCALE_GLOBS = ["localization/**/*.json"]
SCENE_GLOBS = ["scenes/**/*.gd"]

# Files to explicitly ignore during discovery (relative to SOURCE_REPO)
IGNORE_FILES = {
    "scripts/gate.sh",
    "scripts/gate.ps1",
}

# ── Output Directories (relative to repo root) ────────────────────────
EXTRACTED_DIR = os.path.join(_REPO_ROOT, "extracted")
CONTENT_DIR = os.path.join(_REPO_ROOT, "content")
EXPORTS_DIR = os.path.join(_REPO_ROOT, "exports")
MKDOCS_YML = os.path.join(_REPO_ROOT, "mkdocs.yml")

# ── Content Subdirectories ─────────────────────────────────────────────
CONTENT_SYSTEMS = os.path.join(CONTENT_DIR, "systems")
CONTENT_DATA = os.path.join(CONTENT_DIR, "data")
CONTENT_INTERACTIONS = os.path.join(CONTENT_DIR, "interactions")
CONTENT_GLOSSARY = os.path.join(CONTENT_DIR, "glossary")
CONTENT_CORE = os.path.join(CONTENT_DIR, "core")
CONTENT_MANUAL = os.path.join(CONTENT_DIR, "_manual")

# ── Export Settings ────────────────────────────────────────────────────
EXPORT_MAX_BYTES = 150_000  # Hard warning threshold
EXPORT_TARGET_BYTES = 100_000  # Soft target

# ── Verification Thresholds ────────────────────────────────────────────
COVERAGE_MIN_PERCENT = 90  # Fail if <90% of source files documented
MAX_ALLOWED_TODOS = 0  # No TODOs in generated (non-manual) pages

# ── MkDocs Static Config ──────────────────────────────────────────────
# Only theme/extensions are static. Nav is always auto-generated.
MKDOCS_STATIC_CONFIG = {
    "site_name": "WorldSim Documentation",
    "site_description": "Complete system reference for the WorldSim civilization simulation game",
    "theme": {
        "name": "material",
        "language": "ko",
        "palette": [
            {
                "scheme": "slate",
                "primary": "deep purple",
                "accent": "amber",
                "toggle": {"icon": "material/brightness-7", "name": "라이트 모드"},
            },
            {
                "scheme": "default",
                "primary": "deep purple",
                "accent": "amber",
                "toggle": {"icon": "material/brightness-4", "name": "다크 모드"},
            },
        ],
        "features": [
            "navigation.tabs",
            "navigation.sections",
            "navigation.expand",
            "navigation.top",
            "search.suggest",
            "search.highlight",
            "content.tabs.link",
            "content.code.copy",
        ],
        "icon": {"repo": "fontawesome/brands/github"},
    },
    "repo_url": "https://github.com/hyunlord/new-world",
    "repo_name": "hyunlord/new-world",
    "markdown_extensions": [
        {"pymdownx.arithmatex": {"generic": True}},
        {
            "pymdownx.superfences": {
                "custom_fences": [
                    {
                        "name": "mermaid",
                        "class": "mermaid",
                        "format": "!!python/name:pymdownx.superfences.fence_code_format",
                    }
                ]
            }
        },
        {"pymdownx.tabbed": {"alternate_style": True}},
        "pymdownx.details",
        {"pymdownx.highlight": {"anchor_linenums": True}},
        "pymdownx.inlinehilite",
        "pymdownx.snippets",
        "pymdownx.critic",
        "pymdownx.keys",
        {"pymdownx.tasklist": {"custom_checkbox": True}},
        "admonition",
        "tables",
        "attr_list",
        "md_in_html",
        "def_list",
        {"toc": {"permalink": True}},
    ],
    "extra_javascript": ["https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js"],
    "plugins": [{"search": {"lang": ["ko", "en"]}}, "tags"],
}

# ── Nav Section Order ──────────────────────────────────────────────────
# Defines the order of top-level nav sections.
# Pages within each section are sorted by nav_order from frontmatter.
NAV_SECTION_ORDER = [
    ("개요", "index.md"),  # Single page, not a directory
    ("설정 레퍼런스", "config-reference.md"),  # Single page
    ("시스템", "systems"),
    ("데이터", "data"),
    ("시스템 상호작용", "interactions"),
    ("용어 사전", "glossary"),
    ("코어", "core"),
]


# ── Helper Functions ───────────────────────────────────────────────────
def source_path(*parts: str) -> str:
    """Build absolute path within the source repo."""
    return os.path.join(SOURCE_REPO, *parts)


def ensure_dir(path: str) -> None:
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)


def ensure_all_dirs() -> None:
    """Create all output directories."""
    for d in [
        EXTRACTED_DIR,
        CONTENT_DIR,
        CONTENT_SYSTEMS,
        CONTENT_DATA,
        CONTENT_INTERACTIONS,
        CONTENT_GLOSSARY,
        CONTENT_CORE,
        CONTENT_MANUAL,
        EXPORTS_DIR,
    ]:
        ensure_dir(d)
