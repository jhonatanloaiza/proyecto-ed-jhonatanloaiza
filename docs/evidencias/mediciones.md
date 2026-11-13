# Mediciones

Generado con `python docs/evidencias/medicion.py` (mejor de 5 repeticiones).

## 1. Rutas: BFS (elegido para el Rastreador) contra A* (Cazador)

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

## 2. Puntajes: AVL (elegido) contra montículo (descartado)

Se insertan n puntajes y luego se obtiene el ranking completo ordenado de mayor a menor.

| n | AVL insertar (ms) | AVL ranking (ms) | Montículo insertar (ms) | Montículo ranking (ms) |
| --- | --- | --- | --- | --- |
| 1000 | 8.1 | 1.2 | 1.6 | 10.2 |
| 2000 | 17.9 | 2.4 | 3.2 | 22.9 |
| 4000 | 42.4 | 5.2 | 6.8 | 51.8 |
| 8000 | 96.5 | 9.8 | 13.9 | 116.4 |

El ranking del montículo lo vacía: para volver a mostrarlo habría que reconstruirlo.
