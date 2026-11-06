#!/usr/bin/env python3
"""Bashkon src/index.html + styles.css + app.js në një skedar të vetëm: dist/pipeline_b2b.html"""
from pathlib import Path
s = Path(__file__).parent / "src"
html = (s / "index.html").read_text(encoding="utf-8")
html = html.replace("/*{{STYLES}}*/", (s / "styles.css").read_text(encoding="utf-8"))
html = html.replace("/*{{APP}}*/", (s / "app.js").read_text(encoding="utf-8"))
out = Path(__file__).parent / "dist" / "pipeline_b2b.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8")
print("U krijua", out)
