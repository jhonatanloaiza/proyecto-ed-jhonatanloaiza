# Plan · Componente 02: Matriz

## Estructura elegida

Matriz densa guardada en un solo arreglo de tamaño `filas × columnas`. La celda `(f, c)` está en la posición `f × columnas + c`.

**Soporte interno declarado:** se usa una `list` de Python solo como arreglo de tamaño fijo: se crea una vez y nunca crece. No sustituye a otra estructura declarada.

## Complejidad

| Operación | Tiempo | Por qué |
| --- | --- | --- |
| crear | O(f × c) | se inicializa cada celda |
| `consultar`, `asignar` | O(1) | cálculo directo de la posición |
| `dentro`, `filas`, `columnas` | O(1) | comparaciones y datos guardados |

Espacio: O(f × c).

## Alternativa descartada

**Matriz dispersa:** solo guarda celdas no vacías, pero cada consulta cuesta O(k) en una lista o exige una tabla hash. Con 400 celdas la memoria no importa y se consulta el mapa muchas veces por turno.

## Dónde se usa

`dominio/mapa.py` (terreno y objetos) y `estructuras/grafo.py` (predecesores del BFS).

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-30 | Versión inicial para la Entrega 2. |
