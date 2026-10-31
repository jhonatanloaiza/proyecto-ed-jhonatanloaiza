# Escape Geométrico del Sistema Corrupto

Proyecto integrador · Estructuras de Datos (ID 706132) · Universidad Cooperativa de Colombia · II-2026

- **Temática:** A · Motor de juego 2D con pathfinding
- **Modalidad:** individual
- **Lenguaje:** Python 3.11 o superior (juego por consola)

## Contexto narrativo

Un Cubo Geométrico atrapado en una matriz de seguridad de 20 × 20 celdas debe llegar al portal de salida, turno a turno, mientras Pájaros Rastreadores calculan la ruta más corta para atraparlo.

## Estado

Entrega 2: 7 estructuras implementadas e integradas; el juego se puede jugar completo por consola. Ver `ANALISIS.md` y `specs/trazabilidad.md`.

## Cómo ejecutar

Requisitos: Python 3.11 o superior y `pytest`.

```bash
python main.py
```

```bash
python -m pytest
```

## Cómo jugar

Elige `1` en el menú. Llega al portal `@` sin que te atrape un Pájaro `V`.

| Comando | Acción |
| --- | --- |
| `w` `a` `s` `d` | mover arriba, izquierda, abajo, derecha |
| `e` | esperar |
| `i` | ver el inventario |
| `u ID` | usar un objeto (por ejemplo `u k1`) |
| `x ID` | soltar un objeto |
| `b ID` | buscar una entidad (por ejemplo `b r1`) |
| `z` / `y` | deshacer / rehacer |
| `r` / `q` | reiniciar / salir |

## Estructura

- `specs/`: artefactos SDD (constitución, historias, MoSCoW, estructuras, specs por componente).
- `estructuras/`: un módulo por estructura de datos.
- `dominio/`: lógica del juego.
- `tests/`: pruebas con pytest.
- `docs/`: documentos y evidencias.
