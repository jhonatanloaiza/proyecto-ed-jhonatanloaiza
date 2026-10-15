# Escape Geométrico del Sistema Corrupto

Proyecto integrador · Estructuras de Datos (ID 706132) · Universidad Cooperativa de Colombia · II-2026

- **Temática:** A · Motor de juego 2D con pathfinding
- **Modalidad:** individual
- **Lenguaje:** Python 3.11 o superior (juego por consola)

## Contexto narrativo

Un Cubo Geométrico atrapado en una matriz de seguridad de 20 × 20 celdas debe llegar al portal de salida, turno a turno, mientras Pájaros Rastreadores calculan la ruta más corta para atraparlo.

## Estado

Entrega 1 (14 de octubre de 2026): especificación y diseño en `specs/`.

## Cómo ejecutar

Requisitos: Python 3.11 o superior y `pytest`.

```bash
python main.py
```

```bash
python -m pytest
```

## Estructura

- `specs/`: artefactos SDD (constitución, historias, MoSCoW, estructuras, specs por componente).
- `estructuras/`: un módulo por estructura de datos.
- `dominio/`: lógica del juego.
- `tests/`: pruebas con pytest.
- `docs/`: documentos y evidencias.
