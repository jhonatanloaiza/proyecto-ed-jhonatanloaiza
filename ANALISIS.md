# Análisis de complejidad · versión final

Cubre las 9 estructuras del proyecto. n es la cantidad de elementos; V, las celdas del mapa (400); E ≤ 4V, las conexiones entre celdas; k, los enemigos.

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
| Árbol AVL | `insertar`, `maximo` | O(log n) | O(log n) por la recursión |
| Árbol AVL | `descendente` | O(n) | O(log n) en la pila |
| Árbol AVL | `altura`, `tamano`, `esta_vacia` | O(1) | O(1) |
| Montículo mínimo | `insertar`, `extraer_minimo` | O(log n) | O(1) |
| Montículo mínimo | `minimo`, `tamano`, `esta_vacia` | O(1) | O(1) |
| Grafo de rejilla | `vecinos` | O(1) | O(1) |
| Grafo de rejilla | `bfs`, `siguiente_paso` | O(V + E) = O(V) | O(V) |
| Grafo de rejilla | `a_estrella`, `siguiente_paso(guiado=True)` | O(E log V) = O(V log V) | O(V) |

En el dominio, un turno cuesta O(k × V log V) en el peor caso, porque cada Pájaro calcula su ruta. Deshacer o rehacer cuesta O(c), con c los cambios de esa acción, sin recalcular rutas. Registrar un puntaje cuesta O(log n) y mostrar el ranking, O(n).

## Justificación por estructura

**Pila (deshacer y rehacer).** Deshacer y rehacer siempre operan sobre la acción más reciente, justo lo que ofrece una pila en O(1). Con dos pilas, una acción nueva descarta lo que se podía rehacer con solo vaciar la de deshechas. Una lista doble con cursor costaría lo mismo pero exige mantener el cursor y cortar la lista.

**Cola (eventos).** La temática exige procesar los eventos en el orden en que ocurren, y una cola FIFO lo garantiza en O(1). Una cola de prioridad costaría O(log n) y no aporta nada, porque ningún evento es más urgente que otro. También es la frontera del BFS.

**Lista enlazada (inventario).** Los objetos se agregan siempre al final en O(1), gracias a la referencia al último nodo, y se listan en orden de recogida. Quitar uno de cualquier posición es O(n), aceptable con pocos objetos. Una lista doble gastaría un puntero que nunca se usa.

**Lista circular (turnos).** Los Pájaros se atienden en un ciclo sin fin y el Centinela entra a mitad de partida. `siguiente` e `insertar` son O(1), y deshacer su aparición lo saca con `quitar`. Una cola lograría lo mismo desencolando y volviendo a encolar en cada turno.

**Matriz (mapa).** Cada turno consulta muchas celdas, así que importa el acceso O(1). Una matriz dispersa solo ahorra memoria cuando casi todo está vacío, y con 400 celdas esa memoria es despreciable.

**Tabla hash (índice).** La operación dominante es buscar por identificador: O(1) en promedio. Un BST cuesta O(log n) y su ventaja, el recorrido en orden, aquí no se necesita. El factor de carga máximo de 0,75 mantiene cortas las cadenas.

**Árbol AVL (puntajes).** Se registra un puntaje por partida y el ranking se muestra completo y ordenado, quizá muchas veces. El AVL inserta en O(log n) garantizado y entrega el ranking en O(n) sin destruirse.

**Montículo mínimo (frontera de A\*).** A* necesita sacar una y otra vez la celda con menor `g + h`. El montículo lo hace en O(log n) por operación, mientras que una lista ordenada pagaría O(n) en cada inserción.

**Grafo implícito con BFS y A\* (rutas).** Las aristas cuestan 1, así que BFS garantiza el camino de menos pasos. A* usa la distancia Manhattan, que es admisible (nunca sobrestima en 4 direcciones) y consistente, por lo que también encuentra el óptimo explorando menos. Los vecinos se calculan desde la matriz, sin lista de adyacencia que haya que actualizar al abrir una compuerta.

## Comparación de decisiones contra la alternativa descartada

Los datos salen de `docs/evidencias/medicion.py`. Los tiempos dependen de la máquina; lo que importa es cómo crecen.

### 1. Rutas: BFS (elegido para el Rastreador) contra A* (Cazador)

Rejilla abierta de n × n, de la esquina superior izquierda a la inferior derecha.

| n | celdas | pasos | BFS explora | A* explora | BFS (ms) | A* (ms) |
| --- | --- | --- | --- | --- | --- | --- |
| 20 | 400 | 38 | 400 | 39 | 3.16 | 0.92 |
| 40 | 1600 | 78 | 1600 | 79 | 12.97 | 2.09 |
| 80 | 6400 | 158 | 6400 | 159 | 52.23 | 4.62 |
| 160 | 25600 | 318 | 25600 | 319 | 211.51 | 10.67 |

Niveles del juego: cada Pájaro hacia la posición inicial del Cubo.

| Nivel | Pájaro | pasos | BFS explora | A* explora |
| --- | --- | --- | --- | --- |
| Sector de Arranque | R1 | 18 | 147 | 25 |
| Sector de Arranque | R2 | 12 | 117 | 13 |
| Memoria Fragmentada | R1 | 8 | 32 | 9 |
| Memoria Fragmentada | R2 | 5 | 20 | 6 |
| Núcleo Corrupto | R1 | 6 | 18 | 9 |
| Núcleo Corrupto | H1 | 6 | 22 | 7 |
| Núcleo Corrupto | R2 | 4 | 16 | 7 |

### 2. Puntajes: AVL (elegido) contra montículo (descartado)

Se insertan n puntajes y luego se obtiene el ranking completo ordenado de mayor a menor.

| n | AVL insertar (ms) | AVL ranking (ms) | Montículo insertar (ms) | Montículo ranking (ms) |
| --- | --- | --- | --- | --- |
| 1000 | 8.1 | 1.2 | 1.6 | 10.2 |
| 2000 | 17.9 | 2.4 | 3.2 | 22.9 |
| 4000 | 42.4 | 5.2 | 6.8 | 51.8 |
| 8000 | 96.5 | 9.8 | 13.9 | 116.4 |

El ranking del montículo lo vacía: para volver a mostrarlo habría que reconstruirlo.

### Lectura de los resultados

**BFS contra A\*.** En campo abierto BFS explora las n² celdas, mientras que A* explora cerca de 2n, solo las del camino. Al cuadruplicar el área, el tiempo de BFS se multiplica por unos 4, como corresponde a O(V), y el de A* crece mucho menos. En los niveles del juego A* explora entre 2 y 6 veces menos celdas, siempre con el mismo número de pasos. Los Rastreadores conservan BFS porque en 400 celdas cuesta unos 3 ms por turno y su código es más simple de verificar. Si el mapa creciera, cambiar todos los Pájaros a A* sería la mejora natural. Esto confirma la decisión de la Entrega 1 de tener ambos y medirlos.

**AVL contra montículo.** El montículo inserta unas 5 a 7 veces más rápido, porque cada inserción solo sube por una rama sin rotar. Pero para entregar el ranking completo debe extraer todo en O(n log n), unas 10 veces más lento que el recorrido O(n) del AVL, y además queda vacío. En el juego se inserta un puntaje por partida y el ranking se consulta muchas veces, así que domina la operación de listar: la decisión del AVL se mantiene.
