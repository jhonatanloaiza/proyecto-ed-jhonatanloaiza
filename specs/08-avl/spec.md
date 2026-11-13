# Spec · Componente 08: Árbol AVL y tabla de puntajes

- **Historias que soporta:** HU-12 Consultar los mejores puntajes (Should)

## Propósito

Guardar los puntajes de las partidas terminadas y mostrarlos ordenados de mayor a menor.

## Contrato: ArbolAVL

Claves comparables y únicas.

| Operación | Resultado | Errores |
| --- | --- | --- |
| `insertar(clave, valor)` | guarda el par; si la clave existe, reemplaza el valor | — |
| `maximo()` | valor de la clave mayor | árbol vacío → `ArbolVacioError` |
| `descendente()` | `ListaEnlazada` con los valores de mayor a menor clave | — |
| `altura()` | altura del árbol (0 si está vacío) | — |
| `tamano()` / `esta_vacia()` | cantidad de claves / si no hay claves | — |

### Criterios de aceptación

- **CA-AVL-01** `descendente` devuelve los valores ordenados de mayor a menor clave, sin importar el orden de inserción.
- **CA-AVL-02** Insertar claves en orden creciente o decreciente mantiene la altura en O(log n): como máximo 1,45 · log2(n + 2).
- **CA-AVL-03** Las cuatro rotaciones (izquierda-izquierda, derecha-derecha, izquierda-derecha y derecha-izquierda) dejan el árbol ordenado y balanceado.
- **CA-AVL-04** Insertar una clave existente reemplaza el valor sin aumentar el tamaño.
- **CA-AVL-05** `maximo` devuelve el valor de la clave mayor; con el árbol vacío lanza `ArbolVacioError`.
- **CA-AVL-06** Un árbol vacío tiene tamaño 0, altura 0 y `descendente` vacío.

## Contrato: TablaPuntajes

`registrar(puntaje, resultado, turnos)`, `ranking()` (de mayor a menor) y `tamano()`.

- **CA-PUN-01** (CA-33) Cada partida registrada aparece en el ranking.
- **CA-PUN-02** (CA-34) El ranking va de mayor a menor puntaje; con empate, primero la partida más antigua.
- **CA-PUN-03** (CA-34) Sin partidas, el ranking está vacío.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-11-13 | Versión inicial para la Entrega final. |
