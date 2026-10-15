# Spec · Componente 01: Pila e Historial de acciones

- **Historias que soporta:** HU-05 Deshacer una jugada (Must), HU-06 Rehacer una jugada (Must)
- **Versión:** 1.0

## Propósito

Guardar las acciones del jugador para poder deshacerlas y rehacerlas en orden inverso a como ocurrieron, con todos sus efectos.

## Contrato: Pila

Colección de elementos donde el último que entra es el primero que sale.

| Operación | Entrada | Resultado | Errores |
| --- | --- | --- | --- |
| `apilar(elemento)` | cualquier elemento | el elemento queda en la cima; el tamaño aumenta en 1 | — |
| `desapilar()` | — | devuelve y quita el elemento de la cima; el tamaño baja en 1 | pila vacía → `PilaVaciaError` |
| `cima()` | — | devuelve el elemento de la cima sin quitarlo | pila vacía → `PilaVaciaError` |
| `esta_vacia()` | — | `True` si no hay elementos | — |
| `tamano()` | — | cantidad de elementos | — |
| `vaciar()` | — | la pila queda sin elementos | — |

### Criterios de aceptación de la Pila

- **CA-PIL-01** Después de `apilar(x)`, `cima()` devuelve `x` y `tamano()` aumenta en 1.
- **CA-PIL-02** `desapilar()` devuelve los elementos en orden inverso al que se apilaron.
- **CA-PIL-03** `desapilar()` o `cima()` sobre una pila vacía lanzan `PilaVaciaError` y la pila no cambia.
- **CA-PIL-04** Una pila nueva o recién vaciada está vacía y su tamaño es 0.
- **CA-PIL-05** Con un solo elemento, `desapilar()` lo devuelve y la pila queda vacía.

## Contrato: Historial

Registra acciones del jugador. Cada acción sabe aplicarse (`hacer`) y revertirse (`revertir`) sobre el estado de la partida.

| Operación | Resultado | Caso sin acciones |
| --- | --- | --- |
| `registrar(accion)` | guarda la acción ya aplicada como la más reciente y descarta todo lo que se podía rehacer | — |
| `deshacer(partida)` | revierte la acción más reciente y la deja disponible para rehacer; devuelve la acción | devuelve `None`, el estado no cambia |
| `rehacer(partida)` | aplica de nuevo la última acción deshecha; devuelve la acción | devuelve `None`, el estado no cambia |
| `puede_deshacer()` / `puede_rehacer()` | indica si hay acciones disponibles | `False` |

### Criterios de aceptación del Historial

- **CA-HIS-01** (CA-13, CA-14) Deshacer revierte todos los efectos de la acción más reciente: posiciones, objetos, inventario, puntaje y turno.
- **CA-HIS-02** (CA-16) Rehacer después de deshacer deja el estado igual al que había antes de deshacer.
- **CA-HIS-03** (CA-17) Registrar una acción nueva después de deshacer hace que `puede_rehacer()` sea `False`.
- **CA-HIS-04** (CA-15, CA-18) Deshacer o rehacer sin acciones disponibles devuelve `None` y no cambia el estado.
- **CA-HIS-05** Deshacer n veces y rehacer n veces devuelve el estado final original.

## Fuera de alcance

- Límite de acciones guardadas (no lo pide ninguna historia).
- Deshacer acciones de los enemigos por separado: sus movimientos forman parte de la acción del turno del jugador.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-14 | Versión inicial para la Entrega 1. |
