# Spec del sistema · versión 0.2

## Qué hace el sistema

Escape Geométrico del Sistema Corrupto es un juego por turnos en consola. Un Cubo Geométrico se mueve en una matriz de 20 × 20 con picos, recoge orbes y llaves, y debe llegar al portal de salida mientras al menos dos Pájaros Rastreadores lo persiguen por el camino más corto. El jugador puede deshacer y rehacer sus jugadas con todos sus efectos.

## Ciclo de un turno

1. El jugador ingresa un comando (mover, esperar, usar, soltar, listar, buscar, deshacer, rehacer, salir).
2. Si es una acción válida, se aplica, se registra en el historial y genera eventos.
3. Cada Pájaro, en el orden de turnos, calcula su ruta y avanza una casilla.
4. Los eventos del turno se procesan y muestran en orden.
5. Se revisa victoria o derrota; si no terminó, se dibuja el mapa y empieza el siguiente turno.

## Componentes

| # | Componente | Estructura | Capacidad | Módulo |
| --- | --- | --- | --- | --- |
| 01 | Pila e Historial | Pila enlazada (×2) | Deshacer y rehacer | `estructuras/pila.py`, `dominio/historial.py` |
| 02 | Mapa | Matriz densa | Representación del mapa | `estructuras/matriz.py`, `dominio/mapa.py` |
| 03 | Inventario | Lista enlazada simple | Inventario | `estructuras/lista_enlazada.py`, `dominio/inventario.py` |
| 04 | Turnos | Lista circular | Orden de los turnos | `estructuras/lista_circular.py` |
| 05 | Eventos | Cola enlazada | Eventos en orden | `estructuras/cola.py`, `dominio/eventos.py` |
| 06 | Índice | Tabla hash | Búsqueda de entidades | `estructuras/tabla_hash.py` |
| 07 | Rutas | Grafo implícito + BFS | Ruta de los enemigos | `estructuras/grafo.py` |
| 08 | Puntajes (Should, Entrega final) | Árbol AVL | Tabla de puntajes | `estructuras/avl.py` |
| 09 | Búsqueda guiada (Could, Entrega final) | A* con montículo | Ruta del Cazador | `estructuras/monticulo.py` |

`dominio/partida.py` coordina todos los componentes; `main.py` solo lee comandos y dibuja.

## Cómo encajan los contratos (inicial)

- La **Partida** posee el Mapa, el Inventario, los Turnos, la Cola de eventos, el Índice y el Historial.
- Las **acciones** del jugador modifican Mapa, Inventario y puntaje, y se registran en el **Historial**; al revertirse restauran exactamente lo que cambiaron.
- Las **Rutas** leen el Mapa (sin modificarlo) para calcular el siguiente paso de cada Pájaro.
- Todo cambio relevante (aparición, recolección, colisión) se encola en **Eventos**.
- El **Índice** guarda una referencia a cada entidad; como la entidad conserva su propia celda, moverla no obliga a tocar el índice.
- Una **Accion** es un turno completo (Cubo y Pájaros). El Historial la revierte y la repite sin recalcular rutas.
- El nivel 1 incluye 1 llave y 1 compuerta opcional para ejercitar `usar` (F-03); el documento de registro lo proponía sin llaves.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 0.1 | 2026-10-14 | Versión inicial para la Entrega 1. |
| 0.2 | 2026-10-30 | Numeración alineada con las carpetas de `specs/`; contratos de índice y acción actualizados; nivel 1 con llave y compuerta para ejercitar `usar`. |
