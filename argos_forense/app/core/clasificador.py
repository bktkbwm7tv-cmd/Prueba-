"""Clasificación por categoría y cálculo de confianza de detección (§5, §8).

El clasificador **propone**; no decide. Su salida alimenta la bandeja de
validación y nada de lo que produce llega solo al registro definitivo (§4).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .geo import normalizar

# --- §5. Términos de búsqueda, tal y como los fija la instrucción maestra ----
# `nucleo`: términos que por sí solos identifican la categoría.
# `apoyo`: términos que sólo suman cuando ya hay un término núcleo.
TERMINOS: dict[str, dict[str, tuple[str, ...]]] = {
    "FOS": {
        "nucleo": (
            "fosa clandestina",
            "fosas clandestinas",
            "entierro clandestino",
            "inhumacion clandestina",
            "inhumaciones clandestinas",
            "restos oseos",
            "osamenta",
            "osamentas",
            "cuerpos enterrados",
            "predio con restos",
            "fragmentos humanos",
            "puntos positivos de busqueda",
            "punto positivo",
            "hallazgo de cuerpos",
            "restos humanos",
        ),
        "apoyo": (
            "busqueda de restos",
            "colectivo de busqueda",
            "buscadoras",
            "servicio medico forense",
            "semefo",
            "comision de busqueda",
            "identificacion forense",
            "bolsas con restos",
            "cavidad",
            "predio",
        ),
    },
    "CAM": {
        "nucleo": (
            "campamento criminal",
            "campamento clandestino",
            "campamento delictivo",
            "campamento de grupo criminal",
            "campamento asegurado",
            "campamento abandonado",
            "campamento con armamento",
            "centro de entrenamiento",
            "campo de entrenamiento",
            "centro de adiestramiento",
            "campo de adiestramiento",
        ),
        "apoyo": (
            "parapetos",
            "parapeto",
            "puestos de vigilancia",
            "puesto de vigilancia",
            "punto de vigilancia",
            "halcones",
            "campamento",
            "monte",
            "brecha",
            "hamacas",
            "casas de campaña",
            "adiestramiento",
        ),
    },
    "CSE": {
        "nucleo": (
            "casa de seguridad",
            "casas de seguridad",
            "inmueble utilizado para cautiverio",
            "inmueble utilizado por grupo criminal",
            "inmueble usado por grupo delictivo",
            "inmueble utilizado para secuestro",
            "personas privadas de la libertad",
            "privadas de la libertad",
            "personas liberadas de inmueble",
        ),
        "apoyo": (
            "inmueble asegurado",
            "inmueble con armas",
            "inmueble con drogas",
            "cateo",
            "catearon",
            "domicilio asegurado",
            "rescatadas",
            "rescatados",
            "liberadas",
            "liberados",
            "plagio",
            "secuestro",
            "victimas de secuestro",
        ),
    },
}

# Subcategorías: matiz operativo, nunca una inferencia sobre autoría.
SUBCATEGORIAS: dict[str, tuple[tuple[str, tuple[str, ...]], ...]] = {
    "FOS": (
        ("Punto positivo de búsqueda", ("punto positivo", "puntos positivos de busqueda")),
        ("Fosa con restos localizados", ("fosa clandestina", "fosas clandestinas", "cuerpos enterrados")),
        ("Hallazgo de restos óseos", ("restos oseos", "osamenta", "osamentas", "fragmentos humanos")),
        ("Hallazgo de cuerpos", ("hallazgo de cuerpos", "restos humanos")),
    ),
    "CAM": (
        ("Centro de adiestramiento", ("centro de entrenamiento", "campo de entrenamiento", "centro de adiestramiento", "campo de adiestramiento")),
        ("Campamento con armamento", ("campamento con armamento", "campamento asegurado")),
        ("Campamento abandonado", ("campamento abandonado",)),
        ("Campamento vinculado a grupo criminal", ("campamento criminal", "campamento clandestino", "campamento delictivo", "campamento de grupo criminal")),
        ("Puesto de vigilancia / parapetos", ("parapeto", "parapetos", "puesto de vigilancia", "puestos de vigilancia")),
    ),
    "CSE": (
        ("Inmueble de cautiverio con personas liberadas",
         ("personas liberadas de inmueble", "personas privadas de la libertad", "privadas de la libertad",
          "rescatadas", "rescatados", "rescatan", "liberadas", "liberados", "liberan")),
        ("Inmueble vinculado a secuestro", ("inmueble utilizado para secuestro", "plagio", "secuestro")),
        ("Inmueble asegurado con armas o droga", ("inmueble con armas", "inmueble con drogas", "inmueble asegurado")),
        ("Casa de seguridad asegurada", ("casa de seguridad", "casas de seguridad")),
    ),
}

# Términos que descartan: la nota habla de otra cosa aunque comparta vocabulario.
RUIDO = (
    "campamento de refugiados",
    "campamento minero",
    "campamento de damnificados",
    "campamento turistico",
    "campamento de verano",
    "casa de seguridad social",
    "fosa septica",
    "fosa comun del panteon",
    "restos arqueologicos",
    "restos prehispanicos",
    "zona arqueologica",
)


@dataclass
class Clasificacion:
    categoria: str | None = None
    subcategoria: str | None = None
    confianza: int = 0
    terminos: list[str] = field(default_factory=list)
    puntajes: dict[str, int] = field(default_factory=dict)
    ruido: list[str] = field(default_factory=list)

    @property
    def clasificado(self) -> bool:
        return self.categoria is not None


def _encontrar(plano: str, terminos: tuple[str, ...]) -> list[str]:
    return [t for t in terminos if t in plano]


def clasificar(titulo: str, resumen: str = "", texto: str = "") -> Clasificacion:
    """Clasifica una publicación en FOS / CAM / CSE.

    El título pesa el doble que el cuerpo: es donde el medio nombra el hecho.
    """
    plano_titulo = f" {normalizar(titulo)} "
    plano_cuerpo = f" {normalizar(resumen + ' ' + texto)} "
    plano = plano_titulo + plano_cuerpo

    ruido = _encontrar(plano, RUIDO)

    puntajes: dict[str, int] = {}
    hallados: dict[str, list[str]] = {}
    for categoria, grupos in TERMINOS.items():
        nucleo_t = _encontrar(plano_titulo, grupos["nucleo"])
        nucleo_c = _encontrar(plano_cuerpo, grupos["nucleo"])
        if not nucleo_t and not nucleo_c:
            continue
        apoyo = _encontrar(plano, grupos["apoyo"])
        puntaje = 40 * len(set(nucleo_t)) + 18 * len(set(nucleo_c) - set(nucleo_t)) + 5 * len(set(apoyo))
        puntajes[categoria] = puntaje
        hallados[categoria] = sorted(set(nucleo_t) | set(nucleo_c) | set(apoyo))

    if not puntajes:
        return Clasificacion(confianza=0, ruido=ruido, puntajes={})

    categoria = max(puntajes, key=lambda c: puntajes[c])
    confianza = min(92, puntajes[categoria])
    if ruido:
        # No se descarta automáticamente: se rebaja y la bandeja lo ve.
        confianza = max(5, confianza - 35)

    subcategoria = None
    for etiqueta, marcas in SUBCATEGORIAS.get(categoria, ()):
        if any(m in plano for m in marcas):
            subcategoria = etiqueta
            break

    return Clasificacion(
        categoria=categoria,
        subcategoria=subcategoria,
        confianza=int(confianza),
        terminos=hallados[categoria],
        puntajes=puntajes,
        ruido=ruido,
    )


# --- Datos numéricos citables --------------------------------------------
# Sólo se extrae lo que el texto dice literalmente. Nunca se infiere.
_NUMEROS = {
    "un": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6,
    "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11, "doce": 12,
}


def _a_entero(token: str) -> int | None:
    token = token.strip().lower()
    if token.isdigit():
        return int(token)
    return _NUMEROS.get(token)


def extraer_cifras(texto: str) -> dict[str, int]:
    """Cifras que el texto publica expresamente (cuerpos, restos, liberados, detenidos)."""
    plano = normalizar(texto)
    alternativa = r"(\d{1,4}|" + "|".join(_NUMEROS) + r")"
    patrones = {
        "num_cuerpos": rf"{alternativa} (?:cuerpos|cadaveres)\b",
        "num_bolsas": rf"{alternativa} bolsas\b",
        "personas_liberadas": rf"{alternativa} personas (?:liberadas|rescatadas)\b",
        "personas_detenidas": rf"{alternativa} (?:personas )?(?:detenidas|detenidos)\b",
        "num_fosas": rf"{alternativa} fosas\b",
    }
    salida: dict[str, int] = {}
    for campo, patron in patrones.items():
        m = re.search(patron, plano)
        if m:
            valor = _a_entero(m.group(1))
            if valor is not None:
                salida[campo] = valor
    return salida
