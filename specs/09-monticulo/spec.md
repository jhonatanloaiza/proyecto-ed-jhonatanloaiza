# Spec · Componente 09: Montículo mínimo

- **Historias que soporta:** HU-14 Pájaro Cazador con búsqueda guiada (Could)

## Propósito

Entregar siempre el elemento de menor prioridad, como necesita la frontera de A*.

## Contrato

| Operación | Resultado | Errores |
| --- | --- | --- |
| `insertar(prioridad, valor)` | agrega el valor con esa prioridad | — |
| `extraer_minimo()` | quita y devuelve el valor de menor prioridad | vacío → `MonticuloVacioError` |
| `minimo()` | devuelve el valor de menor prioridad sin quitarlo | vacío → `MonticuloVacioError` |
| `tamano()` / `esta_vacia()` | cantidad / si no hay elementos | — |

## Criterios de aceptación

- **CA-MON-01** `extraer_minimo` entrega los valores en orden creciente de prioridad, sin importar el orden de inserción.
- **CA-MON-02** Con prioridades iguales, los valores salen en el orden en que entraron.
- **CA-MON-03** `minimo` devuelve el de menor prioridad sin quitarlo.
- **CA-MON-04** `extraer_minimo` o `minimo` en un montículo vacío lanzan `MonticuloVacioError`.
- **CA-MON-05** `tamano` y `esta_vacia` reflejan inserciones y extracciones.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-11-13 | Versión inicial para la Entrega final. |
