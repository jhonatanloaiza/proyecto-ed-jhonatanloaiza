# Spec · Componente 06: Tabla hash (índice de entidades)

- **Historias que soporta:** HU-10 (Must)

## Propósito

Encontrar una entidad a partir de su identificador de texto (`R1`, `O3`).

## Contrato

| Operación | Resultado |
| --- | --- |
| `insertar(clave, valor)` | guarda el par; si la clave existe, reemplaza el valor |
| `buscar(clave)` | el valor, o `None` si no existe |
| `eliminar(clave)` | `True` si existía y salió; `False` si no |
| `contiene(clave)` | `True` si la clave existe |
| `tamano()` | cantidad de claves |

## Criterios de aceptación

- **CA-HAS-01** Después de `insertar`, `buscar` devuelve el valor.
- **CA-HAS-02** Insertar una clave existente reemplaza el valor sin aumentar el tamaño.
- **CA-HAS-03** Buscar o eliminar una clave inexistente no falla y no cambia la tabla, también con la tabla vacía.
- **CA-HAS-04** Las claves que chocan en la misma cubeta se conservan y se pueden eliminar por separado.
- **CA-HAS-05** Al crecer más allá de su capacidad inicial, todas las claves siguen encontrándose.
- **CA-HAS-06** `contiene` y `tamano` reflejan inserciones y eliminaciones.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-30 | Versión inicial para la Entrega 2. |
