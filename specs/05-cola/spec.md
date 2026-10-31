# Spec · Componente 05: Cola y eventos

- **Historias que soporta:** HU-08 (Must)

## Propósito

Atender los eventos de cada turno en el mismo orden en que ocurrieron.

## Contrato

| Operación | Resultado | Errores |
| --- | --- | --- |
| `encolar(valor)` | queda al final | — |
| `desencolar()` | devuelve y quita el del frente | vacía → `ColaVaciaError` |
| `frente()` | devuelve el del frente sin quitarlo | vacía → `ColaVaciaError` |
| `tamano()` / `esta_vacia()` | cantidad / si no hay elementos | — |

## Criterios de aceptación

- **CA-COL-01** `desencolar` entrega los valores en el orden en que se encolaron.
- **CA-COL-02** `frente` devuelve el primero sin quitarlo.
- **CA-COL-03** `desencolar` o `frente` en una cola vacía lanzan `ColaVaciaError`.
- **CA-COL-04** La cola se puede volver a usar después de vaciarse.
- **CA-COL-05** `tamano` y `esta_vacia` reflejan el contenido.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-30 | Versión inicial para la Entrega 2. |
