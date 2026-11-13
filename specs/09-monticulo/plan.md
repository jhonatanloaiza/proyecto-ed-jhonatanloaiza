# Plan · Componente 09: Montículo mínimo

## Estructura elegida

**Montículo binario mínimo** sobre un arreglo: el hijo izquierdo de la posición i está en 2i + 1 y el derecho en 2i + 2. Cada elemento se guarda como `(prioridad, llegada, valor)`. El número de llegada desempata y hace que los iguales salgan en orden de llegada.

**Soporte interno declarado:** el arreglo es una `list` de Python. El enunciado lo permite expresamente para el montículo, y solo se usan acceso por índice, agregar al final y quitar del final.

## Complejidad

| Operación | Tiempo | Por qué |
| --- | --- | --- |
| `insertar` | O(log n) | se agrega al final y sube por su rama |
| `extraer_minimo` | O(log n) | el último pasa a la raíz y baja por su rama |
| `minimo`, `tamano`, `esta_vacia` | O(1) | raíz y longitud del arreglo |

Espacio: O(n).

## Alternativa descartada

**Lista ordenada:** extraer el mínimo es O(1), pero insertar en orden cuesta O(n). A* inserta una vez por vecino mejorado, así que domina la inserción.

## Dónde se usa

`estructuras/grafo.py`: frontera de `a_estrella`, ordenada por `(g + h, h)`.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-11-13 | Versión inicial para la Entrega final. |
