# Plan · Componente 07: Grafo de la rejilla

## Estructura elegida

**Grafo implícito:** los vértices son las celdas y las aristas se calculan al pedir los vecinos; no se guarda lista de adyacencia. El recorrido es **búsqueda en anchura (BFS)** con la `Cola` del componente 05 como frontera y una `Matriz` del componente 02 para los predecesores. El camino se reconstruye desde el destino con una `Pila` y se devuelve en una `ListaEnlazada`.

Todas las aristas cuestan 1, por lo que BFS garantiza el camino de menos pasos.

## Complejidad

V son las celdas y E ≤ 4V.

| Operación | Tiempo | Por qué |
| --- | --- | --- |
| `vecinos` | O(1) | máximo 4 consultas |
| `bfs`, `siguiente_paso` | O(V + E) = O(V) | cada celda se encola una sola vez |

Espacio: O(V).

## Alternativas descartadas

- **Lista de adyacencia explícita:** duplica la información del mapa y hay que actualizarla cuando se abre una compuerta.
- **A\*:** queda para HU-14 (Could). Explora menos celdas, pero necesita el montículo.

## Dónde se usa

`dominio/partida.py` llama `siguiente_paso` una vez por Pájaro en cada turno.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-30 | Versión inicial para la Entrega 2. |
