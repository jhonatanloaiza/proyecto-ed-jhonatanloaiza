# Decisión de estructuras

Una fila por capacidad del dominio. Todas las estructuras se implementan desde cero en `estructuras/`.

| Capacidad | Estructura | Por qué esta | Alternativa descartada | Complejidad clave | Dónde se usa |
| --- | --- | --- | --- | --- | --- |
| Representación del mapa | Matriz densa (arreglo 2D de 20 × 20) | Los picos ocupan como máximo el 25 % y el resto de celdas también se consulta (objetos, portal, enemigos); se pregunta por una celda muchas veces por turno, y el acceso por fila y columna es O(1). 400 celdas es memoria despreciable. | Matriz dispersa: ahorra memoria solo si casi todo está vacío, pero cada consulta cuesta O(k) o requiere tabla hash; aquí el mapa es pequeño y se consulta mucho. | consultar celda O(1) · actualizar celda O(1) | Mapa, validación de movimientos, dibujo en consola |
| Inventario del jugador | Lista enlazada simple con referencia al último nodo | Se agrega siempre al final (O(1)) y se lista en orden de recogida; usar o soltar quita un objeto de cualquier posición tras buscarlo (O(n), con n pequeño). | Lista doble: el puntero hacia atrás no se aprovecha porque nunca se recorre al revés. Arreglo dinámico: quitar del medio desplaza elementos, también O(n), sin ventaja. | agregar O(1) · buscar/quitar O(n) · listar O(n) | HU-03, HU-04 |
| Orden de los turnos | Lista circular | Los turnos giran sin fin (Rastreador 1 → Rastreador 2 → … → vuelve al primero) y el Centinela entra a mitad de partida; avanzar al siguiente e insertar son O(1). | Cola: también O(1), pero cada turno exige desencolar y volver a encolar; la lista circular expresa el ciclo de forma natural. | siguiente O(1) · insertar O(1) · quitar O(n) | HU-07, HU-13 |
| Deshacer y rehacer | Dos pilas enlazadas (hechas y deshechas) | Deshacer y rehacer siempre operan sobre la acción más reciente: apilar y desapilar son O(1). Una acción nueva vacía la pila de deshechas. | Lista doble con cursor: también O(1), pero exige mantener el cursor y cortar la lista en cada acción nueva; más código para el mismo resultado. | apilar O(1) · desapilar O(1) · vaciar O(1) | HU-05, HU-06 |
| Eventos del juego | Cola enlazada (FIFO) | Los eventos se procesan en el orden en que ocurren (lo exige la temática); encolar y desencolar son O(1). | Cola de prioridad: no hay eventos más urgentes que otros y alteraría el orden de llegada; además cuesta O(log n). | encolar O(1) · desencolar O(1) | HU-08 |
| Índice de entidades | Tabla hash con encadenamiento | La operación que más se repite es buscar por identificador (`R1`, `O3`), en O(1) promedio. | BST: búsqueda O(log n) y recorrido en orden que aquí no se necesita. | buscar O(1) prom. · insertar O(1) prom. · eliminar O(1) prom. | HU-10, búsqueda de enemigos y objetos |
| Tabla de puntajes | Árbol AVL | Se insertan puntajes y se muestran ordenados de mayor a menor; el AVL garantiza inserción O(log n) y el recorrido en orden da el ranking en O(n). | Montículo máximo: obtiene el máximo en O(1), pero listar todos ordenados cuesta O(n log n) y destruye el montículo. | insertar O(log n) · recorrido en orden O(n) | HU-12 |
| Ruta de los enemigos | Grafo implícito sobre la matriz + BFS (Rastreador); A* con montículo mínimo (Cazador) | Movimiento en 4 direcciones con costo 1: BFS da el camino de menos pasos en O(V + E) sin guardar aristas (los vecinos se calculan desde la matriz). A* usa la distancia Manhattan, que es admisible porque nunca sobrestima los pasos reales, y explora menos celdas. | Grafo con lista de adyacencia explícita: duplica la información de la matriz y hay que actualizarla si cambian las compuertas. | BFS O(V + E) · montículo insertar/extraer O(log n) | HU-07, HU-14 |

## Soporte interno declarado

- La matriz usa internamente un arreglo de Python de tamaño fijo creado una sola vez (acceso por índice); no se usan operaciones de lista como sustituto de otra estructura.
- El montículo y la tabla hash usan un arreglo de tamaño fijo como almacenamiento de cubetas y posiciones, como permite el enunciado.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-14 | Versión inicial para la Entrega 1. |
