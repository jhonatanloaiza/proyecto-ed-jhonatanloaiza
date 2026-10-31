# Análisis de complejidad · versión 1

Cubre las 7 estructuras implementadas en la Entrega 2. n es la cantidad de elementos; V, las celdas del mapa (400); E ≤ 4V, las conexiones entre celdas; k, los enemigos.

## Tabla de complejidad

| Estructura | Operación | Tiempo | Espacio extra |
| --- | --- | --- | --- |
| Pila | `apilar`, `desapilar`, `cima`, `esta_vacia`, `tamano`, `vaciar` | O(1) | O(1) |
| Cola | `encolar`, `desencolar`, `frente`, `esta_vacia`, `tamano` | O(1) | O(1) |
| Lista enlazada | `agregar`, `esta_vacia`, `tamano` | O(1) | O(1) |
| Lista enlazada | `insertar_en`, `quitar_en` | O(n); O(1) al inicio | O(1) |
| Lista enlazada | `buscar`, recorrido | O(n) | O(1) |
| Lista circular | `insertar`, `siguiente`, `esta_vacia`, `tamano` | O(1) | O(1) |
| Lista circular | `quitar`, recorrido | O(n) | O(1) |
| Matriz | crear | O(f × c) | O(f × c) |
| Matriz | `consultar`, `asignar`, `dentro`, `filas`, `columnas` | O(1) | O(1) |
| Tabla hash | `insertar` | O(1) amortizado; peor caso O(n) | O(1) |
| Tabla hash | `buscar`, `contiene`, `eliminar` | O(1) promedio; peor caso O(n) | O(1) |
| Tabla hash | `tamano` | O(1) | O(1) |
| Grafo de rejilla | `vecinos` | O(1) | O(1) |
| Grafo de rejilla | `bfs`, `siguiente_paso` | O(V + E) = O(V) | O(V) |

En el dominio, un turno cuesta O(k × V) porque cada Pájaro ejecuta un BFS. Deshacer o rehacer cuesta O(c), con c los cambios de esa acción, y no recalcula rutas.

## Justificación por estructura

**Pila (deshacer y rehacer).** Deshacer y rehacer siempre operan sobre la acción más reciente, justo lo que ofrece una pila en O(1). Con dos pilas, una acción nueva descarta lo que se podía rehacer con solo vaciar la de deshechas. Una lista doble con cursor costaría lo mismo pero exige mantener el cursor y cortar la lista.

**Cola (eventos).** La temática exige procesar los eventos en el orden en que ocurren, y una cola FIFO lo garantiza en O(1). Una cola de prioridad costaría O(log n) y no aporta nada: ningún evento es más urgente que otro. También sirve de frontera del BFS, que depende de ese mismo orden.

**Lista enlazada (inventario).** Los objetos se agregan siempre al final, en O(1) gracias a la referencia al último nodo, y se listan en orden de recogida. Quitar un objeto de cualquier posición es O(n), aceptable con pocos objetos. Una lista doble gastaría un puntero que nunca se usa, porque no se recorre al revés.

**Lista circular (turnos).** Los Pájaros se atienden en un ciclo sin fin y pueden entrar a mitad de partida, como hará el Centinela. `siguiente` e `insertar` son O(1). Una cola también lo logra, pero desencolando y volviendo a encolar en cada turno.

**Matriz (mapa).** Cada turno consulta muchas celdas, así que importa el acceso O(1). Una matriz dispersa solo ahorra memoria cuando casi todo está vacío, y con 400 celdas esa memoria es despreciable. Se usan dos matrices: terreno y objetos.

**Tabla hash (índice).** La operación dominante es buscar por identificador, O(1) en promedio. Un BST cuesta O(log n) y su ventaja, el recorrido en orden, aquí no se necesita. El factor de carga máximo de 0,75 mantiene cortas las cadenas.

**Grafo implícito con BFS (rutas).** Las aristas cuestan 1, por lo que BFS garantiza el camino de menos pasos. Los vecinos se calculan desde la matriz, sin lista de adyacencia que haya que actualizar cuando se abre una compuerta. Combina tres estructuras propias: `Cola` como frontera, `Matriz` para los predecesores y `Pila` para reconstruir el camino.

## Pendiente para la versión final

Agregar el AVL y el montículo si entran, la comparación de al menos dos decisiones contra la alternativa descartada y, si es posible, mediciones con n creciente.
