# Priorización MoSCoW

## Cálculo de capacidad

| Dato | Valor |
| --- | --- |
| Periodo de desarrollo | 15 oct – 11 nov 2026 (4 semanas) |
| Horas disponibles por semana | 8 h |
| Capacidad bruta | 4 × 8 = 32 h |
| Reserva para imprevistos y depuración (20 %) | 6,4 h |
| **Capacidad neta para Must** | **25,6 h** |

Regla: la suma de los Must no supera la capacidad neta. Should y Could solo entran con lo que sobre de la capacidad bruta.

## Must (obligatorios del dominio)

| HU | Título | Estimación |
| --- | --- | --- |
| HU-01 | Iniciar una partida | 3 h |
| HU-02 | Mover al Cubo | 2 h |
| HU-03 | Recoger objetos | 2 h |
| HU-04 | Gestionar el inventario | 2 h |
| HU-05 | Deshacer una jugada | 3 h |
| HU-06 | Rehacer una jugada | 1 h |
| HU-07 | Persecución de los Pájaros Rastreadores | 4 h |
| HU-08 | Ver los eventos del turno en orden | 2 h |
| HU-09 | Saber si gané o perdí | 1 h |
| HU-10 | Buscar una entidad | 2 h |
| HU-11 | Jugar desde la consola | 2 h |
| **Total Must** | | **24 h ≤ 25,6 h** |

Todas las Must corresponden a los elementos mínimos de la Temática A, que son el contrato con el docente.

## Should (importantes, entran si hay tiempo)

| HU | Título | Estimación | Razón |
| --- | --- | --- | --- |
| HU-12 | Consultar los mejores puntajes | 3 h | Da valor a la búsqueda de F-08 y justifica un árbol balanceado. |
| HU-13 | Aparición del Pájaro Centinela | 2 h | Ejercita la entrada de personajes a mitad de partida en el orden de turnos. |

## Could (deseables)

| HU | Título | Estimación | Razón |
| --- | --- | --- | --- |
| HU-14 | Pájaro Cazador con búsqueda guiada | 4 h | Permite comparar A* con BFS; queda después de los Should. |
| HU-15 | Elegir nivel | 2 h | El nivel 1 ya cumple todos los mínimos. |

## Won't (no se harán en este proyecto)

| Idea | Razón |
| --- | --- |
| Interfaz gráfica en ventana | La temática exige consola y no se evalúan gráficos; consumiría horas sin aporte a las estructuras. |
| Guardar y cargar partidas en archivo | No pertenece a ninguna funcionalidad F-01 a F-08 y la capacidad no alcanza. |
| Música y efectos con librerías de audio | Las únicas dependencias permitidas son `pytest` y `matplotlib`. |
| Modo multijugador | Cambia el modelo de turnos y no lo pide la temática. |

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-14 | Versión inicial para la Entrega 1. |
