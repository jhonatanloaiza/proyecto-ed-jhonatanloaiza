# Plan · Componente 08: Árbol AVL

## Estructura elegida

**Árbol AVL**: árbol binario de búsqueda donde cada nodo guarda su altura. Después de cada inserción se recalcula la altura en el camino de vuelta y, si un nodo queda con factor de balance mayor que 1 en valor absoluto, se rota (simple o doble).

La tabla de puntajes usa como clave `(puntaje, -número de partida)`: así las claves son únicas y, a igual puntaje, la partida más antigua queda primero al recorrer de mayor a menor. El recorrido descendente es un inorden invertido iterativo con la `Pila` del componente 01.

## Complejidad

| Operación | Tiempo | Por qué |
| --- | --- | --- |
| `insertar` | O(log n) | la altura está acotada por ~1,44 log2 n; cada rotación es O(1) |
| `maximo` | O(log n) | se baja siempre a la derecha |
| `descendente` | O(n) | cada nodo se apila y desapila una vez |
| `altura`, `tamano`, `esta_vacia` | O(1) | datos guardados |

Espacio: O(n); la recursión de `insertar` usa O(log n).

## Alternativas descartadas

- **Montículo máximo:** obtiene el mejor puntaje en O(1), pero listar todo el ranking ordenado cuesta O(n log n) y vacía el montículo. La comparación medida está en `ANALISIS.md`.
- **BST sin balancear:** si los puntajes llegan ordenados degenera en una lista con O(n) por inserción.

## Dónde se usa

`dominio/puntajes.py` (`TablaPuntajes`) y la opción 2 del menú principal de `main.py`.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-11-13 | Versión inicial para la Entrega final. |
