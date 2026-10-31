# Spec · Componente 04: Lista circular (orden de turnos)

- **Historias que soporta:** HU-07 (Must), HU-13 (Should)

## Propósito

Atender a los enemigos por turnos en un ciclo sin fin, permitiendo que entren y salgan a mitad de partida.

## Contrato

| Operación | Resultado | Errores |
| --- | --- | --- |
| `insertar(valor)` | entra al final del ciclo | — |
| `quitar(valor)` | `True` si estaba y salió; `False` si no estaba | — |
| `siguiente()` | devuelve al que le toca y avanza | lista vacía → `ListaVaciaError` |
| `tamano()` / `esta_vacia()` | cantidad / si no hay elementos | — |
| recorrido (`for`) | una vuelta desde el primero, sin mover el turno | — |

## Criterios de aceptación

- **CA-CIR-01** `siguiente` entrega los valores en orden de inserción y, tras el último, vuelve al primero.
- **CA-CIR-02** Con un solo elemento, `siguiente` lo devuelve siempre.
- **CA-CIR-03** `siguiente` en una lista vacía lanza `ListaVaciaError`.
- **CA-CIR-04** Un valor insertado a mitad de un ciclo entra al final, sin alterar el orden de los demás.
- **CA-CIR-05** `quitar` saca al valor sin romper el ciclo, aunque sea el primero, el último, el actual o el único.
- **CA-CIR-06** `quitar` un valor inexistente devuelve `False` y no cambia la lista.
- **CA-CIR-07** `tamano` y `esta_vacia` reflejan inserciones y salidas.
- **CA-CIR-08** El recorrido entrega cada valor una vez en orden de inserción y no cambia a quién le toca.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-30 | Versión inicial para la Entrega 2. |
