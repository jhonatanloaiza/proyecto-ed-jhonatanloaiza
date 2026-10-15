# Plan · Componente 01: Pila e Historial de acciones

## Estructura elegida

**Pila enlazada**: cada elemento vive en un nodo con una referencia al nodo de abajo; la pila guarda solo la referencia a la cima y un contador de tamaño.

El **Historial** usa dos pilas:

- `hechas`: acciones aplicadas, la más reciente en la cima.
- `deshechas`: acciones revertidas, la última deshecha en la cima.

| Operación del Historial | Qué hace con las pilas |
| --- | --- |
| `registrar(a)` | `hechas.apilar(a)` y `deshechas.vaciar()` |
| `deshacer(p)` | `a = hechas.desapilar()`, `a.revertir(p)`, `deshechas.apilar(a)` |
| `rehacer(p)` | `a = deshechas.desapilar()`, `a.hacer(p)`, `hechas.apilar(a)` |

## Complejidad

| Operación | Tiempo | Espacio extra | Por qué |
| --- | --- | --- | --- |
| `apilar` | O(1) | O(1) | se crea un nodo y pasa a ser la cima |
| `desapilar` | O(1) | O(1) | la cima pasa a ser el nodo de abajo |
| `cima` | O(1) | O(1) | se lee la referencia de la cima |
| `esta_vacia`, `tamano` | O(1) | O(1) | contador guardado |
| `vaciar` | O(1) | O(1) | se suelta la referencia a la cima (el recolector libera los nodos) |
| `registrar`, `deshacer`, `rehacer` | O(1) + costo de la acción | O(1) | dos operaciones de pila; revertir una acción toca solo las celdas que cambió |

Espacio total: O(n) para n acciones guardadas.

## Alternativas descartadas

- **Lista doble con cursor:** también O(1) por operación, pero hay que mover el cursor y cortar la lista en cada acción nueva; más código y más casos borde para el mismo resultado.
- **Pila sobre arreglo dinámico:** apilar es O(1) amortizado, pero hay que redimensionar y el enunciado prohíbe usar `list` como sustituto de la pila. La versión enlazada no necesita arreglo de soporte.

## Diseño de las acciones

Cada acción es un objeto con `hacer(partida)` y `revertir(partida)` y guarda solo lo necesario para revertirse:

- `Mover`: celda anterior del Cubo, celdas anteriores de cada Pájaro y el turno.
- `Recoger`: el objeto, su celda y los puntos sumados (más el movimiento que la produjo).
- `Usar` / `Soltar`: el objeto y su posición en el inventario.

## Dónde se usa

`dominio/partida.py` registra cada acción válida del jugador; `main.py` expone los comandos `deshacer` (`z`) y `rehacer` (`y`).

## Módulos

- `estructuras/pila.py`: `Nodo`, `Pila`, `PilaVaciaError`.
- `dominio/historial.py`: `Historial`.
- `tests/test_pila.py`, `tests/test_historial.py`.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-14 | Versión inicial: dos pilas enlazadas; lista doble con cursor descartada. |
