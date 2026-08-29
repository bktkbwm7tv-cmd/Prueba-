"""Separación OSINT / información operativa (§20) y regla de atribución (§21).

Dos funciones distintas conviven aquí:

  · `revisar()` detecta en un texto recolectado lo que §20 prohíbe publicar
    automáticamente. No borra la evidencia — la evidencia se conserva íntegra
    (§15) —, marca el registro para que la ficha pública no lo exponga.
  · `redactar()` produce la versión publicable de un texto.
  · `atribucion_valida()` impide que el sistema atribuya un sitio a una
    organización criminal si ninguna fuente identificable lo hizo.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .geo import normalizar

# --- Patrones de dato sensible ---------------------------------------------
RE_TELEFONO = re.compile(r"(?<![\d.])(?:\+?52[\s\-.]?)?(?:\(?\d{2,3}\)?[\s\-.]?)?\d{3,4}[\s\-.]?\d{4}(?!\d)")
RE_CORREO = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
RE_COORDENADA = re.compile(
    r"(?<![\d.])[-+]?\d{1,2}[.,]\d{4,}(?:\s*[°º])?(?:\s*[NnSs])?\s*[,;/ ]\s*"
    r"[-+]?\d{1,3}[.,]\d{4,}(?:\s*[°º])?(?:\s*[EeWwOo])?(?![\d.])"
)
RE_COORD_GMS = re.compile(r"\d{1,3}\s*[°º]\s*\d{1,2}\s*['′]\s*[\d.]+\s*[\"″]?\s*[NSEWO]", re.IGNORECASE)
RE_DOMICILIO = re.compile(
    r"\b(?:calle|avenida|av\.|blvd\.?|boulevard|callej[oó]n|privada|andador|carretera)\s+[^.,;\n]{3,50}"
    r"\s*(?:n[uú]mero|no\.?|#)\s*\d+[a-zA-Z]?\b",
    re.IGNORECASE,
)
RE_PLACA = re.compile(r"\b[A-Z]{3}[-\s]?\d{2,4}[-\s]?[A-Z]?\b")

# Señales de que el texto habla de un operativo en desarrollo: no se publica
# ubicación de un despliegue vivo.
OPERATIVO_EN_CURSO = (
    "operativo en curso",
    "se mantiene el operativo",
    "continua el despliegue",
    "continua la busqueda en el lugar",
    "acordonada la zona",
    "en estos momentos",
    "se mantiene el cerco",
)

# Señales de dato de víctima, testigo o colectivo que §20 protege.
PERSONAS_PROTEGIDAS = (
    "domicilio de la victima",
    "domicilio de la familia",
    "domicilio del colectivo",
    "sede del colectivo",
    "casa de la buscadora",
    "testigo protegido",
    "identidad del testigo",
    "denunciante anonimo",
)

RESERVADA = (
    "informacion reservada",
    "carpeta de investigacion reservada",
    "version publica reservada",
    "documento clasificado",
)


@dataclass
class RevisionOpsec:
    hallazgos: list[dict] = field(default_factory=list)
    reserva_operativa: bool = False

    @property
    def limpio(self) -> bool:
        return not self.hallazgos

    @property
    def tipos(self) -> list[str]:
        return sorted({h["tipo"] for h in self.hallazgos})

    def como_dict(self) -> dict:
        return {
            "reserva_operativa": self.reserva_operativa,
            "tipos": self.tipos,
            "hallazgos": self.hallazgos,
        }


def _añadir(rev: RevisionOpsec, tipo: str, muestra: str, regla: str) -> None:
    rev.hallazgos.append({"tipo": tipo, "muestra": muestra[:60], "regla": regla})


def revisar(*textos: str) -> RevisionOpsec:
    """Marca lo que §20 prohíbe publicar automáticamente."""
    rev = RevisionOpsec()
    texto = "\n".join(t for t in textos if t)
    if not texto.strip():
        return rev
    plano = normalizar(texto)

    for m in RE_COORDENADA.finditer(texto):
        _añadir(rev, "COORDENADA_PRECISA", m.group(0), "§20 coordenadas precisas")
    for m in RE_COORD_GMS.finditer(texto):
        _añadir(rev, "COORDENADA_PRECISA", m.group(0), "§20 coordenadas precisas")
    for m in RE_TELEFONO.finditer(texto):
        _añadir(rev, "TELEFONO", m.group(0), "§20 teléfonos")
    for m in RE_CORREO.finditer(texto):
        _añadir(rev, "CORREO", m.group(0), "§20 información personal sensible")
    for m in RE_DOMICILIO.finditer(texto):
        _añadir(rev, "DOMICILIO", m.group(0), "§20 domicilios")
    for t in OPERATIVO_EN_CURSO:
        if t in plano:
            _añadir(rev, "OPERATIVO_EN_CURSO", t, "§20 operaciones en desarrollo")
            rev.reserva_operativa = True
    for t in PERSONAS_PROTEGIDAS:
        if t in plano:
            _añadir(rev, "PERSONA_PROTEGIDA", t, "§20 víctimas, testigos y colectivos")
            rev.reserva_operativa = True
    for t in RESERVADA:
        if t in plano:
            _añadir(rev, "INFORMACION_RESERVADA", t, "§20 información reservada")
            rev.reserva_operativa = True

    if any(h["tipo"] in {"COORDENADA_PRECISA", "DOMICILIO"} for h in rev.hallazgos):
        rev.reserva_operativa = True
    return rev


MARCAS = {
    "COORDENADA_PRECISA": "[COORDENADA RESERVADA — §20]",
    "TELEFONO": "[TELÉFONO RESERVADO — §20]",
    "CORREO": "[CONTACTO RESERVADO — §20]",
    "DOMICILIO": "[DOMICILIO RESERVADO — §20]",
    "PLACA": "[PLACA RESERVADA — §20]",
}


def redactar(texto: str) -> str:
    """Versión publicable: sustituye el dato sensible por su marca, no lo borra en silencio."""
    if not texto:
        return texto
    salida = RE_COORDENADA.sub(MARCAS["COORDENADA_PRECISA"], texto)
    salida = RE_COORD_GMS.sub(MARCAS["COORDENADA_PRECISA"], salida)
    salida = RE_DOMICILIO.sub(MARCAS["DOMICILIO"], salida)
    salida = RE_CORREO.sub(MARCAS["CORREO"], salida)
    salida = RE_TELEFONO.sub(MARCAS["TELEFONO"], salida)
    return salida


# --- §20: precisión geográfica publicable ----------------------------------
def generalizar_punto(
    lat: float | None,
    lon: float | None,
    precision_geo: str | None,
    exponer_exacto: bool,
    decimales: int = 2,
) -> tuple[float | None, float | None, str]:
    """Nunca devuelve el punto exacto salvo autorización expresa.

    Con `exponer_exacto=False` (el valor por omisión del sistema) un punto de
    precisión PUNTO se degrada a rejilla de ~1 km: sirve para el mapa nacional y
    no sirve para llegar al sitio.
    """
    if lat is None or lon is None:
        return None, None, "SIN_GEORREFERENCIA"
    if precision_geo == "PUNTO" and not exponer_exacto:
        return round(lat, decimales), round(lon, decimales), "APROXIMADO_GENERALIZADO"
    return round(lat, 4), round(lon, 4), precision_geo or "CENTROIDE_ENTIDAD"


# --- §21: atribución a grupos criminales -----------------------------------
class AtribucionInvalida(ValueError):
    pass


def atribucion_valida(atribucion: dict) -> dict:
    """Sólo se admite una atribución si viene con quién la hizo y dónde consta.

    El sistema no infiere autoría: si falta el atribuyente o la fuente, la
    atribución se rechaza en vez de guardarse sin respaldo.
    """
    texto = (atribucion or {}).get("texto", "").strip()
    atribuido_por = (atribucion or {}).get("atribuido_por", "").strip()
    url = (atribucion or {}).get("url", "").strip()
    if not texto:
        raise AtribucionInvalida("La atribución no tiene texto.")
    if not atribuido_por:
        raise AtribucionInvalida(
            "§21: toda atribución debe declarar quién la hizo. Formato: "
            "«La autoridad X atribuyó públicamente el sitio a…»"
        )
    if not url:
        raise AtribucionInvalida("§21: la atribución debe estar ligada a su fuente (URL).")
    return {
        "texto": texto,
        "atribuido_por": atribuido_por,
        "url": url,
        "formato": f"{atribuido_por} atribuyó públicamente: {texto}",
    }
