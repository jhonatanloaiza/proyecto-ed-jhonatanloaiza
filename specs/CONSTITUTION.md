# Constitución del proyecto

Escape Geométrico del Sistema Corrupto · Temática A · Estructuras de Datos (ID 706132)

Estas reglas no se negocian durante el proyecto. Si una cambia, se registra en el historial de cambios con su motivo.

## 1. Principios

1. **La especificación va primero.** Ningún componente se implementa sin su `spec.md`, `plan.md` y `tasks.md` en el repositorio. El historial de Git debe mostrar la spec antes que el código.
2. **La spec dice qué, el plan dice cómo.** `spec.md` describe operaciones y criterios de aceptación sin mencionar la estructura; `plan.md` elige la estructura y la justifica con complejidad.
3. **Estructuras propias.** Cada capacidad del dominio se resuelve con una estructura implementada desde cero en `estructuras/`.
4. **Cada decisión se justifica.** Toda estructura declara su operación dominante y su complejidad, la alternativa descartada y por qué, y dónde se usa.
5. **Trazabilidad total.** Cada criterio tiene un identificador (`CA-01`, `CA-PIL-01`…) y cada prueba nombra en su docstring el criterio que verifica.

## 2. Restricciones técnicas

- Python 3.11 o superior. Sin dependencias externas salvo `pytest` (y `matplotlib` opcional para mediciones).
- Prohibido usar `list`, `dict`, `set`, `collections.deque` o `heapq` como sustituto de una estructura declarada. Se permiten como soporte interno solo si el `plan.md` lo justifica.
- Un módulo por estructura. Nada de archivos monolíticos.
- Cada operación pública lleva un docstring con su complejidad temporal.
- El juego se juega por consola; no se evalúan gráficos.

## 3. Calidad

- Mínimo 3 pruebas por operación pública, incluidos los extremos: vacío, un elemento, elemento inexistente.
- `pytest` debe pasar al 100 % en cada etiqueta de entrega.
- `main.py` debe arrancar en una máquina limpia siguiendo el `README.md`.

## 4. Forma de trabajo

- Flujo: historia de usuario → prioridad MoSCoW → `spec.md` → `plan.md` → `tasks.md` → prueba → código.
- Commits pequeños, uno por tarea de `tasks.md` cuando sea posible, con prefijos `spec`, `plan`, `test`, `feat`, `fix`, `docs`.
- Un cambio de decisión después de una entrega se hace con commit en la spec o el plan y una línea en su historial de cambios.
- El uso de asistentes de IA se declara en `BITACORA.md`. No se integra código que no se pueda explicar línea por línea.

## 5. Definición de terminado

Una historia está terminada cuando todos sus criterios tienen prueba que pasa, el código está integrado al dominio y es accesible desde `main.py`, y `trazabilidad.md` enlaza criterio ↔ prueba.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-14 | Versión inicial para la Entrega 1. |
