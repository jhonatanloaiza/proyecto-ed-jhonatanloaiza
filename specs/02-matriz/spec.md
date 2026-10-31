# Spec · Componente 02: Matriz

- **Historias que soporta:** HU-01, HU-02, HU-11 (Must)

## Propósito

Guardar un valor por cada celda de una rejilla de tamaño fijo y consultarlo por fila y columna.

## Contrato

| Operación | Resultado | Errores |
| --- | --- | --- |
| `Matriz(filas, columnas, inicial=None)` | todas las celdas valen `inicial` | tamaño no positivo → `ValueError` |
| `consultar(fila, columna)` | valor de la celda | fuera de rango → `FueraDeRangoError` |
| `asignar(fila, columna, valor)` | la celda guarda `valor` | fuera de rango → `FueraDeRangoError` |
| `dentro(fila, columna)` | `True` si la celda existe | — |
| `filas()` / `columnas()` | dimensiones | — |

## Criterios de aceptación

- **CA-MAT-01** Una matriz nueva tiene el valor inicial en todas sus celdas, incluidas las esquinas.
- **CA-MAT-02** Después de `asignar`, `consultar` devuelve ese valor y las demás celdas no cambian.
- **CA-MAT-03** Consultar o asignar fuera de rango lanza `FueraDeRangoError`, incluidos índices negativos.
- **CA-MAT-04** `dentro` es `True` en las cuatro esquinas y `False` justo afuera de cada borde.
- **CA-MAT-05** Crear una matriz con 0 filas o columnas lanza `ValueError`.
- **CA-MAT-06** `filas()` y `columnas()` devuelven las dimensiones, también si la matriz no es cuadrada o es de 1 × 1.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-30 | Versión inicial para la Entrega 2. |
