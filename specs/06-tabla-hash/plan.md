# Plan · Componente 06: Tabla hash

## Estructura elegida

Tabla hash con encadenamiento: un arreglo de cubetas, cada una con una cadena de nodos. La función de dispersión es polinómica (base 31) sobre los caracteres de la clave. Cuando el factor de carga supera 0,75 se duplica la capacidad y se reubican las claves.

**Soporte interno declarado:** las cubetas son una `list` de Python usada como arreglo de tamaño fijo; crecer crea un arreglo nuevo.

## Complejidad

La longitud de la clave se trata como constante porque los identificadores son cortos.

| Operación | Promedio | Peor caso | Por qué |
| --- | --- | --- | --- |
| `insertar` | O(1) amortizado | O(n) | cadena corta; duplicar es O(n) pero poco frecuente |
| `buscar`, `contiene`, `eliminar` | O(1) | O(n) | todas las claves en una cubeta |
| `tamano` | O(1) | O(1) | contador |

Espacio: O(n + capacidad).

## Alternativa descartada

**BST:** búsqueda O(log n) y recorrido en orden que aquí nadie necesita. La operación dominante es buscar por identificador.

## Dónde se usa

`dominio/partida.py`: índice `id → entidad` para el comando buscar.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-30 | Versión inicial para la Entrega 2. |
