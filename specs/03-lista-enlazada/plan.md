# Plan · Componente 03: Lista enlazada e Inventario

## Estructura elegida

Lista enlazada simple con referencias al primer y al último nodo, más un contador. Sin soporte interno de `list`.

## Complejidad

| Operación | Tiempo | Por qué |
| --- | --- | --- |
| `agregar` | O(1) | se enlaza detrás del último nodo |
| `insertar_en`, `quitar_en` | O(n) | hay que caminar hasta la posición; O(1) al inicio |
| `buscar` | O(n) | recorrido secuencial |
| `tamano`, `esta_vacia` | O(1) | contador |
| recorrido | O(n) | un paso por nodo |

Espacio: O(n).

## Alternativas descartadas

- **Lista doble:** el puntero hacia atrás ocupa memoria y nunca se recorre al revés.
- **Arreglo dinámico:** quitar del medio desplaza elementos, también O(n), sin ventaja, y se usaría `list` como sustituto.

## Dónde se usa

`dominio/inventario.py`, los cambios de cada `Accion` y el camino que devuelve el BFS.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-30 | Versión inicial para la Entrega 2. |
