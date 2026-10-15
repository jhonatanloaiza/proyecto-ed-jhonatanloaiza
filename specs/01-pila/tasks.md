# Tasks · Componente 01: Pila e Historial de acciones

Cada tarea cierra uno o más criterios con su prueba. Orden: prueba primero, luego código.

| ID | Tarea | Criterios | Prueba | Estado |
| --- | --- | --- | --- | --- |
| T-01 | Crear `PilaVaciaError`, `Nodo` y `Pila` vacía con `esta_vacia` y `tamano` | CA-PIL-04 | `test_pila.py::test_pila_nueva_*` | Pendiente |
| T-02 | Implementar `apilar` y `cima` | CA-PIL-01 | `test_pila.py::test_apilar_*` | Pendiente |
| T-03 | Implementar `desapilar` (orden inverso y un solo elemento) | CA-PIL-02, CA-PIL-05 | `test_pila.py::test_desapilar_*` | Pendiente |
| T-04 | Errores sobre pila vacía en `desapilar` y `cima` | CA-PIL-03 | `test_pila.py::test_vacia_*` | Pendiente |
| T-05 | Implementar `vaciar` | CA-PIL-04 | `test_pila.py::test_vaciar_*` | Pendiente |
| T-06 | `Historial.registrar` y `puede_deshacer` / `puede_rehacer` | CA-HIS-03 | `test_historial.py::test_registrar_*` | Pendiente |
| T-07 | `Historial.deshacer` con acción de prueba | CA-HIS-01, CA-HIS-04 | `test_historial.py::test_deshacer_*` | Pendiente |
| T-08 | `Historial.rehacer` | CA-HIS-02, CA-HIS-04 | `test_historial.py::test_rehacer_*` | Pendiente |
| T-09 | Secuencia deshacer n / rehacer n | CA-HIS-05 | `test_historial.py::test_secuencia_*` | Pendiente |
| T-10 | Integrar acciones `Mover` y `Recoger` en la partida y comandos `z` / `y` en `main.py` | CA-13, CA-14, CA-16, CA-17 | `test_partida.py::test_deshacer_*` | Pendiente |
| T-11 | Registrar criterios ↔ pruebas en `specs/trazabilidad.md` | todos | — | Pendiente |

Mínimo 3 pruebas por operación pública: caso normal, pila vacía y un solo elemento.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-14 | Versión inicial para la Entrega 1. |
