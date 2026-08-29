# ARGOS FORENSE — guía de operación

Versión 1.0

Este documento es para quien opera la plataforma. La descripción técnica está
en `argos_forense/README.md`; aquí está el ciclo de trabajo.

## El ciclo, en una frase

El rastreo **propone**, la persona **decide**, el corte **congela**.

## 1. Rastreo

Corre solo cada 60 minutos (configurable) y también a mano, desde *Inicio* o
*Bandeja*. Recorre:

1. los canales RSS **verificados** del catálogo de fuentes;
2. la búsqueda dirigida: cada término de las tres categorías cruzado con las
   32 entidades;
3. opcionalmente, la lectura directa de portales institucionales.

Todo lo que encuentra queda **PENDIENTE** en la bandeja. El rastreo no crea
eventos: no existe ninguna ruta de código por la que pueda hacerlo.

### Lo que el rastreo *no* hace

No declara que un portal no tenga novedades cuando lo que ocurrió es que no
pudo consultarlo. Cada fuente guarda su último diagnóstico —`EGRESO BLOQUEADO`,
`PORTAL NO DISPONIBLE`, `ROBOTS.TXT PROHÍBE LA CONSULTA`— y el tablero lo
muestra. Un vacío de cobertura y un vacío de hechos son cosas distintas.

## 2. Bandeja de validación

Cada registro llega con título, medio, URL, fecha, categoría detectada, entidad
probable, resumen, porcentaje de confianza y posibles duplicados.

Cinco decisiones:

| Acción | Qué hace |
|---|---|
| **Validar** | Emite el folio forense y abre la ficha del evento |
| **Descartar** | Marca DESCARTADO con motivo. **No borra nada** |
| **Posible duplicado** | Aparta el registro sin decidir todavía |
| **Vincular a evento existente** | Lo añade como fuente de un evento ya abierto |
| **Abrir fuente** | Abre la publicación original |

Antes de validar, revise **entidad** y **categoría**: las dos forman parte del
folio y el folio no se modifica después. Un registro sin entidad determinada no
puede validarse — el sistema lo rechaza en vez de inventar una.

## 3. Deduplicación

El botón *Posible duplicado* muestra los candidatos con su puntaje y el detalle
de qué criterios se compararon. El porcentaje se calcula **sólo sobre los
criterios comparables**, y el desglose dice cuáles fueron: un 91 % obtenido
sobre tres campos no vale lo que uno obtenido sobre diez.

Tres decisiones, todas humanas: **Fusionar**, **Mantener separados**,
**Vincular como fuente adicional**. El sistema nunca fusiona por su cuenta.

## 4. Niveles de corroboración

No se teclean: se derivan de las fuentes ligadas al evento y se recalculan
cada vez que se añade una.

| Nivel | Cuándo |
|---|---|
| **A — Confirmado** | Fuente institucional **competente** sobre el hecho |
| **B — Altamente corroborado** | Dos o más fuentes independientes coincidentes |
| **C — Reportado** | Una fuente identificable |
| **D — Por verificar** | Reporte inicial o de colectivo sin corroboración |

Dos precisiones que la plataforma aplica sola:

- **Competente** significa federal, o estatal de la misma entidad del hecho.
  Una fiscalía de otro estado es fuente identificable, pero no confirma un
  hecho fuera de su jurisdicción.
- **Independientes** se cuenta por dominio y por medio: dos réplicas de la
  misma nota no son dos fuentes.

Un evento en nivel D nunca se presenta como hecho confirmado: la ficha lo
declara en un aviso, y así viaja a las exportaciones y al corte.

## 5. Cortes de 72 horas

Se generan como **borrador** y una persona los publica. Al publicarlos, el
contenido queda congelado en un snapshot y sellado con SHA-256.

A partir de ahí el corte **no se modifica**. Lo que cambie después aparece en el
corte siguiente, y la comparación entre cortes lo muestra con su motivo:

```
CORTE 002 VS CORTE 001
AF-2026-SIN-CSE-0001   C → A
Motivo: Confirmado por 1 fuente institucional competente: Fiscalía…
```

El botón *Verificar sello* recalcula el hash del contenido publicado y lo
compara con el registrado. Si no coinciden, algo tocó el snapshot fuera de la
aplicación.

## 6. Qué no publica la plataforma

Ni automáticamente ni por descuido:

- coordenadas precisas y ubicación táctica;
- domicilios de víctimas, de familias o de colectivos;
- teléfonos, correos y datos personales;
- información de testigos;
- información marcada como reservada.

Cuando el texto recolectado los contiene, la evidencia se conserva íntegra
—para eso está— pero la ficha pública los sustituye por su marca y el evento
queda con **reserva operativa**. La ubicación se expone generalizada: por
omisión, el centroide de la entidad.

## 7. Atribuciones

La plataforma **nunca** deduce a qué organización pertenece un sitio. Sólo
registra atribuciones que ya hizo alguien identificable, y exige tres cosas:
quién la hizo, qué atribuyó y dónde consta. Si falta cualquiera de las tres, la
atribución se rechaza en vez de guardarse sin respaldo.

## 8. Su nombre en la bitácora

En *Configuración* se fija el nombre del operador. Firma cada validación,
corrección, descarte y fusión. La bitácora sólo admite altas: nada se edita ni
se borra, ni siquiera un error — se corrige con un movimiento nuevo que deja
ver el anterior.

## Preguntas frecuentes

**Un estado aparece sin eventos. ¿Significa que no pasó nada ahí?**
No. Significa que no hay hallazgos validados. Revise *Fuentes* para ver si los
portales de esa entidad respondieron y *Bandeja* para ver si hay registros
pendientes.

**¿Puedo corregir un folio mal emitido?**
No. El folio es inmutable. Si el evento resultó ser otra cosa, cámbiele el
estado con su motivo, o fusiónelo con el folio correcto: los dos folios
siguen consultables y la bitácora explica qué pasó.

**El rastreo no trae nada.**
Mire el panel *Último rastreo* en Inicio. Si aparecen fuentes con error, el
problema es de acceso a la red, no de ausencia de hechos.
