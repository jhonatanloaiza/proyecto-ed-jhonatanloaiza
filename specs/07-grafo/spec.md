# Spec · Componente 07: Grafo de la rejilla y rutas

- **Historias que soporta:** HU-07 (Must)

## Propósito

Calcular el camino de menos pasos entre dos celdas de la rejilla, moviéndose en 4 direcciones y evitando las celdas no transitables.

## Contrato

| Operación | Resultado |
| --- | --- |
| `GrafoRejilla(filas, columnas, transitable)` | rejilla donde `transitable(fila, columna)` dice si se puede pasar |
| `vecinos(celda)` | celdas transitables contiguas: arriba, abajo, izquierda, derecha |
| `bfs(origen, destino)` | `Busqueda` con `camino` (de origen a destino) y `explorados` (celdas visitadas) |
| `siguiente_paso(origen, destino)` | la primera celda del camino, o `None` si no hay camino o ya llegó |

## Criterios de aceptación

- **CA-GRA-01** `vecinos` no incluye celdas fuera de la rejilla ni celdas no transitables.
- **CA-GRA-02** `bfs` devuelve un camino con el menor número de pasos, que empieza en el origen y termina en el destino.
- **CA-GRA-03** Cada paso del camino va a una celda contigua y transitable.
- **CA-GRA-04** Si no hay camino, `camino` queda vacío.
- **CA-GRA-05** Si origen y destino coinciden, el camino tiene solo esa celda.
- **CA-GRA-06** `explorados` cuenta las celdas visitadas y es al menos 1.
- **CA-GRA-07** `siguiente_paso` devuelve la primera celda del camino, o `None` si no hay camino o ya está en el destino.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-30 | Versión inicial para la Entrega 2. |
