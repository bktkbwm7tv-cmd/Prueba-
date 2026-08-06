#!/usr/bin/env python3
"""
Reusable ARGOS tool: recolor the static/baked state-map SVGs to match the
current EVENTOS array, in both the desktop and mobile HTML reports.

Why this exists: argos-map / argos-map-arm are re-rendered live by JS on
page load, but the raw SVG baked into the HTML file (used as a fallback for
JS-disabled previews such as iOS Quick Look, and the ONLY rendering path for
the mobile report, which ships no JS at all) is a static snapshot. Every
time EVENTOS changes, this snapshot goes stale unless it's patched by hand.

Usage: edit STATE_COLORS below to match the top-severity color per state
implied by the current EVENTOS array (rojo > amarillo > verde, per
argosTopEventFor in the JS engine), then run this script. It patches every
occurrence of each data-sid across both map instances (main + armamento) in
both HTML files, idempotently.

This does NOT touch the <a href="#ARG-ID"> wrapping or tooltip <title> —
only the fill / fill-opacity so the static fallback shows correct colors.
The JS-rendered version (desktop, in a real browser) regenerates the full
markup including links on load, so this is strictly a fallback-correctness
patch, not a replacement for updating EVENTOS.
"""
import re
import sys

COLOR = {
    "rojo": "#ff3b3b",
    "amarillo": "#ffd23f",
    "verde": "#33d17a",
    "gris": "#26314a",
}

# Authoritative state -> severity color, derived from the EVENTOS array.
# Update this dict each corte before running the script. States that had a
# color in the previous edition but have no event this corte must be listed
# explicitly as "gris" — the script only touches states present in this dict.
STATE_COLORS = {
    "MX-SIN": "rojo",
    "MX-CHH": "amarillo",
    "MX-GUA": "amarillo",
    "MX-GRO": "verde",
    "MX-CAM": "verde",
    "MX-TAM": "verde",
    "MX-SLP": "verde",
    "MX-HID": "verde",
    "MX-MOR": "verde",
    "MX-OAX": "gris",
    "MX-CHP": "gris",
    "MX-SON": "gris",
    "MX-ZAC": "gris",
    "MX-MIC": "gris",
    "MX-QUE": "gris",
    "MX-DUR": "gris",
    "MX-JAL": "gris",
}

FILES = [
    "argos-2026-08-06.html",
    "argos-2026-08-06-movil.html",
]


def patch_file(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()

    total = 0
    for sid, severity in STATE_COLORS.items():
        color = COLOR[severity]
        opacity = "0.55" if severity == "gris" else "0.88"
        pattern = re.compile(
            r'(data-sid="' + re.escape(sid) + r'"[^>]*?fill=")[^"]*("[^>]*?fill-opacity=")[^"]*(")'
        )

        def repl(m):
            return m.group(1) + color + m.group(2) + opacity + m.group(3)

        html, n = pattern.subn(repl, html)
        total += n

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return total


if __name__ == "__main__":
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    for fname in FILES:
        path = f"{base.rstrip('/')}/{fname}"
        n = patch_file(path)
        print(f"{fname}: {n} fill/fill-opacity pairs patched")
