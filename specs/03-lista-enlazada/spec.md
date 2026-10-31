# Spec · Componente 03: Lista enlazada e Inventario

- **Historias que soporta:** HU-03, HU-04 (Must)

## Propósito

Guardar elementos en orden de llegada, agregarlos al final y quitarlos o reinsertarlos en cualquier posición.

## Contrato: ListaEnlazada

| Operación | Resultado | Errores |
| --- | --- | --- |
| `agregar(valor)` | queda al final | — |
| `insertar_en(posicion, valor)` | queda en esa posición | fuera de `0..tamano` → `IndexError` |
| `quitar_en(posicion)` | devuelve y quita el valor | fuera de rango → `IndexError` |
| `buscar(condicion)` | `(posicion, valor)` del primero que cumple, o `None` | — |
| `tamano()` / `esta_vacia()` | cantidad / si no hay elementos | — |
| recorrido (`for`) | valores en orden | — |

## Criterios de aceptación

- **CA-LIS-01** `agregar` conserva el orden de llegada al recorrer.
- **CA-LIS-02** `insertar_en` funciona al inicio, en el medio y al final; luego `agregar` sigue yendo al final.
- **CA-LIS-03** `quitar_en` funciona al inicio, en el medio y al final; quitar el último deja correcto el siguiente `agregar`.
- **CA-LIS-04** Una posición inválida lanza `IndexError` y la lista no cambia.
- **CA-LIS-05** `buscar` devuelve la posición y el valor del primero que cumple, o `None` si no hay ninguno o la lista está vacía.
- **CA-LIS-06** `tamano` y `esta_vacia` reflejan el contenido en lista vacía, con un elemento y tras quitarlo.

## Contrato: Inventario

`agregar(objeto)`, `buscar(id)`, `quitar(id)` (devuelve `(objeto, posicion)` o `None`), `insertar_en(posicion, objeto)`, `tamano()` y recorrido.

- **CA-INV-01** (CA-07, CA-09) El recorrido entrega los objetos en orden de recogida.
- **CA-INV-02** (CA-12) Buscar o quitar un id inexistente devuelve `None` y no cambia el inventario.
- **CA-INV-03** Quitar un objeto y reinsertarlo en su posición deja el inventario como estaba.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-30 | Versión inicial para la Entrega 2. |
