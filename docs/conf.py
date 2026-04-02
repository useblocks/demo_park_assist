import os

# docs/conf.py – Sphinx Configuration for Park Assist Demo
# ──────────────────────────────────────────────────────────────────────────────

project   = "Park Assist Demo"
author    = "useblocks Workshop"
version   = "0.1"
release   = "0.1.0"
copyright = "2026, useblocks Workshop"

extensions = [
    "sphinx_needs",
    "sphinx_codelinks",
    "sphinxcontrib.plantuml",
    "sphinxcontrib.mermaid",
]

# ── PlantUML ──────────────────────────────────────────────────────────────────
plantuml = "java -jar %s" % os.path.join(os.path.dirname(__file__), "utils", "plantuml.jar")
plantuml_output_format = "svg_img"

src_trace_config_from_toml = "ubproject.toml"

# ── HTML output ───────────────────────────────────────────────────────────────
html_theme = "furo"
html_static_path = ['_static']
html_css_files = ['furo.css']

# ── Mermaid ───────────────────────────────────────────────────────────────────
mermaid_version = "11"

# ── Sphinx-Needs: load configuration from ubproject.toml ─────────────────────
needs_from_toml = "ubproject.toml"
