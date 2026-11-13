# Plan · Componente 07: Grafo de la rejilla

## Estructura elegida

**Grafo implícito:** los vértices son las celdas y las aristas se calculan al pedir los vecinos; no se guarda lista de adyacencia. El recorrido es **búsqueda en anchura (BFS)** con la `Cola` del componente 05 como frontera y una `Matriz` del componente 02 para los predecesores. El camino se reconstruye desde el destino con una `Pila` y se devuelve en una `ListaEnlazada`.

Todas las aristas cuestan 1, por lo que BFS garantiza el camino de menos pasos.

## A* (versión 1.1)

`a_estrella` usa el `MonticuloMinimo` del componente 09 como frontera, ordenado por `(g + h, h)`, una `Matriz` con el costo g de cada celda y otra con las celdas cerradas.

**Heurística: distancia Manhattan,** `|f1 − f2| + |c1 − c2|`. Es **admisible**: con movimientos en 4 direcciones de costo 1, ninguna ruta puede ser más corta que esa distancia, así que nunca sobrestima. También es **consistente**, porque cambia como máximo en 1 entre celdas vecinas. Por eso A* devuelve el camino óptimo sin reabrir celdas cerradas. Desempatar por h prefiere las celdas más cercanas al destino y reduce la exploración.

## Complejidad

V son las celdas y E ≤ 4V.

| Operación | Tiempo | Por qué |
| --- | --- | --- |
| `vecinos` | O(1) | máximo 4 consultas |
| `bfs`, `siguiente_paso` | O(V + E) = O(V) | cada celda se encola una sola vez |
| `a_estrella` | O(E log V) = O(V log V) | cada mejora de costo inserta en el montículo; en la práctica explora menos celdas que BFS |

Espacio: O(V).

## Alternativas descartadas

- **Lista de adyacencia explícita:** duplica la información del mapa y hay que actualizarla cuando se abre una compuerta.
- **A\* para todos los Pájaros:** en un mapa de 400 celdas BFS ya es rápido, y su código es más simple de verificar. A* se reserva para el Cazador, lo que permite comparar ambas búsquedas en el mismo mapa.

## Dónde se usa

`dominio/partida.py` llama `siguiente_paso` una vez por Pájaro en cada turno.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-30 | Versión inicial para la Entrega 2. |
| 1.1 | 2026-11-13 | Se agrega A* con heurística Manhattan para HU-14. |
