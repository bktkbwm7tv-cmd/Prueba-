#!/usr/bin/env python3
"""
Reusable ARGOS tool: regenerate the static/baked RADAR CENTRAL echoes and
totals (radar-stats) to match the current EVENTOS array, in both the
desktop and mobile HTML reports.

Why this exists: like the state map, the radar is re-rendered live by JS
(argosRenderRadar) on page load in a real browser, but the raw SVG baked
into the HTML — the ONLY rendering the mobile report ever gets, since it
ships no JS, and the fallback used by JS-disabled previews on desktop —
goes stale every time EVENTOS changes unless patched by hand. This
reimplements argosRenderRadar()'s exact math in Python (same argosHash,
same jitar/angle/radius formulas) so the baked SVG matches what the JS
would actually draw, instead of manually re-deriving coordinates.

Usage: update EVENTOS below to mirror the JS EVENTOS array in the report
(same order — jitter depends on array index), then run this script. It
replaces the echo markup between the radar-cross lines and </svg>, and the
radar-stats totals, in both HTML files, leaving rings/sweep/gradient intact.
"""
import re
import sys
from datetime import date

REGION_ORDER = ["Noroeste", "Noreste", "Occidente", "Centro", "Golfo", "Sureste", "Pacífico"]
SEVERITY_COLOR = {"rojo": "#ff3b3b", "amarillo": "#ffd23f", "verde": "#33d17a"}
SIZE_R = {"grande": 11, "mediano": 7.5, "pequeno": 5}

W = H = 220
CX = CY = 110
RMAX = 98
RMIN = 20
WINDOW_DAYS = 10
CORTE_FECHA = date(2026, 8, 4)

# Mirrors the JS EVENTOS array (order matters: jitter uses the array index).
EVENTOS = [
    ("ARG-88-001", "Pacífico", "verde", "grande",
     "SEMAR asegura ~3 t de cocaína y detiene a 10 personas frente a costas de Oaxaca", date(2026, 8, 3)),
    ("ARG-88-001", "Pacífico", "verde", "grande",
     "SEMAR asegura ~1.4 t de cocaína y detiene a 6 personas frente a costas de Chiapas", date(2026, 8, 3)),
    ("ARG-88-002", "Noroeste", "verde", "mediano",
     "SEMAR destruye cuatro narcolaboratorios en Topolobampo y Culiacán", date(2026, 8, 1)),
    ("ARG-88-003", "Noroeste", "amarillo", "pequeno",
     "Balacera durante partido de sóftbol en Nogales; sujetos evaden un alto policial, sin lesionados", date(2026, 8, 1)),
    ("ARG-88-005", "Centro", "verde", "pequeno",
     'Vinculación a proceso de Marisol "N" por extorsión agravada en Temoac', date(2026, 8, 1)),
    ("ARG-88-007", "Centro", "rojo", "mediano",
     "Emboscada armada contra convoy de la Guardia Nacional en Tula de Allende; 2 elementos heridos, 3-4 detenidos", date(2026, 8, 3)),
    ("ARG-88-009", "Noreste", "rojo", "mediano",
     "Agresión armada contra el Ejército en Joaquín Amaro (Operación SAGAZ); 1 agresor abatido, 2 menores detenidas", date(2026, 8, 3)),
    ("ARG-88-010", "Noreste", "rojo", "mediano",
     "Ataque con explosivo contra la Policía Municipal de Luis Moya; 1 policía muerto, 2 heridos", date(2026, 7, 31)),
    ("ARG-88-011", "Noreste", "amarillo", "mediano",
     "Enfrentamiento con FRIZ/PDI en Calera; 5 civiles armados abatidos, sin bajas institucionales", date(2026, 8, 1)),
    ("ARM-001", "Occidente", "verde", "pequeno",
     "Aseguramiento de 2 armas largas en Queréndaro (Pueblo Viejo), sin agresión", date(2026, 8, 3)),
    ("ARM-002", "Occidente", "verde", "mediano",
     "Aseguramiento en Buenavista (Tescalame): 1 arma corta, 1 larga, 4 cargadores, 9,939 cartuchos", date(2026, 8, 4)),
    ("ARM-003", "Sureste", "verde", "pequeno",
     "Aseguramiento en Benemérito de las Américas: 1 arma larga, 11 cargadores, 340 cartuchos", date(2026, 8, 2)),
    ("ARM-004", "Noroeste", "verde", "pequeno",
     "Aseguramiento en San Dimas: 2 armas largas, 18 cargadores, 536 cartuchos", date(2026, 8, 2)),
    ("ARM-005", "Sureste", "verde", "mediano",
     "Aseguramiento en Chilpancingo (Santa Bárbara): 3 armas largas, 13 cargadores, 566 cartuchos, 7 detenidos", date(2026, 8, 2)),
    ("ARM-006", "Occidente", "verde", "pequeno",
     "Aseguramiento en Jalisco (municipio no especificado): 2 armas cortas, 2 cargadores, 15 cartuchos, 1 detenido", date(2026, 8, 2)),
    ("ARM-007", "Occidente", "amarillo", "grande",
     "Aseguramiento derivado de enfrentamiento en Valle de Guadalupe: fusil Barrett, ametralladora, vehículo con blindaje artesanal, 3 armas largas, ~1,000 cartuchos", date(2026, 8, 2)),
    ("ARM-008", "Centro", "verde", "mediano",
     "Aseguramiento en dos inmuebles de Querétaro: 1 arma corta, 2 largas, 4 cargadores, 152 cartuchos, 7 detenidos", date(2026, 8, 2)),
    ("ARM-009", "Noroeste", "verde", "pequeno",
     "Aseguramiento en Cajeme (col. Cortinas): 3 armas cortas, 2 largas, 7 cargadores, 61 cartuchos, 3 detenidos (1 menor)", date(2026, 8, 2)),
    ("ARM-010", "Noroeste", "verde", "mediano",
     "Aseguramiento en Sinaloa (municipio no determinado): 2 armas largas, 25 cargadores, 2,047 cartuchos", date(2026, 8, 2)),
    ("ARM-011", "Noroeste", "verde", "pequeno",
     "Aseguramiento en Concordia (av. A. López Mateos): 4 armas largas, 19 cargadores, 573 cartuchos", date(2026, 8, 3)),
    ("ARM-012", "Noroeste", "verde", "pequeno",
     "Aseguramiento en Sonora (municipio no determinado): 1,399 cartuchos y 14 eslabones para ametralladora, sin arma asociada", date(2026, 8, 3)),
    ("ARM-013", "Noroeste", "verde", "mediano",
     "Cateo de FGR (FECOR) en Victoria de Durango (Práxedis G. Guerrero Nuevo): 1 arma larga, 22 cargadores, 411 cartuchos, 3 granadas", date(2026, 8, 3)),
    ("ARM-014", "Noreste", "amarillo", "mediano",
     "Aseguramiento derivado del enfrentamiento en Calera: 8 armas largas y 3 vehículos (2 con reporte de robo)", date(2026, 8, 1)),
]

FILES = ["argos-2026-08-04.html", "argos-2026-08-04-movil.html"]


def argos_hash(s):
    h = 0
    for ch in s:
        h = (h * 31 + ord(ch)) & 0xFFFFFFFF
        if h >= 0x80000000:
            h -= 0x100000000
    return abs(h)


def polar_point(cx, cy, r, ang_deg):
    import math
    a = math.radians(ang_deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def build_echoes_and_stats():
    sector = 360 / len(REGION_ORDER)
    counts = {"rojo": 0, "amarillo": 0, "verde": 0}
    counted_ids = set()
    parts = []

    for idx, (eid, region, color, impacto, hecho, fecha) in enumerate(EVENTOS):
        if eid not in counted_ids:
            counts[color] = counts.get(color, 0) + 1
            counted_ids.add(eid)

        ri = REGION_ORDER.index(region) if region in REGION_ORDER else -1
        base_angle = (ri * sector + sector / 2 if ri >= 0 else 0) - 90
        jitter_seed = argos_hash(f"{eid}-{idx}") % 100
        jitter = (jitter_seed / 100 - 0.5) * (sector * 0.7)
        angle = base_angle + jitter

        days_ago = (CORTE_FECHA - fecha).days if fecha else WINDOW_DAYS
        days_ago = max(0, days_ago)
        t = min(1, days_ago / WINDOW_DAYS)
        r = RMAX - t * (RMAX - RMIN)
        px, py = polar_point(CX, CY, r, angle)

        rad = SIZE_R.get(impacto, SIZE_R["pequeno"])
        rad_str = str(int(rad)) if rad == int(rad) else str(rad)
        color_hex = SEVERITY_COLOR.get(color, "#8fb8c8")
        cls = "eco" + (" pulse" if color == "rojo" else "")

        parts.append(
            f'<a href="#{eid}"><circle class="{cls}" cx="{px:.1f}" cy="{py:.1f}" '
            f'r="{rad_str}" fill="{color_hex}"><title>{eid} — {hecho} ({fecha.isoformat()})</title></circle></a>'
        )

    stats_html = (
        f"<div>\U0001F534 Alto impacto<br><b>{counts.get('rojo', 0)}</b></div>"
        f"<div>\U0001F7E1 Violencia operativa<br><b>{counts.get('amarillo', 0)}</b></div>"
        f"<div>\U0001F7E2 Acciones institucionales<br><b>{counts.get('verde', 0)}</b></div>"
    )
    return "".join(parts), stats_html, counts


def patch_file(path, echoes_html, stats_html):
    with open(path, encoding="utf-8") as f:
        html = f.read()

    pattern_echoes = re.compile(
        r'(<line class="radar-cross"[^>]*></line>\s*<line class="radar-cross"[^>]*></line>'
        r'<g><path class="radar-sweep-path"[\s\S]*?</path></g>)([\s\S]*?)(</svg>)'
    )
    html, n_echo = pattern_echoes.subn(
        lambda m: m.group(1) + echoes_html + m.group(3), html
    )

    pattern_stats = re.compile(
        r'(<div class="radar-stats"(?: id="[^"]*")?>)(?:<div>[\s\S]*?</div>){3}(</div>)'
    )
    html, n_stats = pattern_stats.subn(
        lambda m: m.group(1) + stats_html + m.group(2), html
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return n_echo, n_stats


if __name__ == "__main__":
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    echoes_html, stats_html, counts = build_echoes_and_stats()
    print("Totals:", counts)
    for fname in FILES:
        path = f"{base.rstrip('/')}/{fname}"
        n_echo, n_stats = patch_file(path, echoes_html, stats_html)
        print(f"{fname}: echoes patched={n_echo}, stats patched={n_stats}")
