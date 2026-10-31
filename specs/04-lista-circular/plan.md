# Plan · Componente 04: Lista circular

## Estructura elegida

Lista circular simple: el último nodo apunta al primero. Se guardan el último nodo, el nodo actual y un contador.

## Complejidad

| Operación | Tiempo | Por qué |
| --- | --- | --- |
| `insertar` | O(1) | se enlaza después del último |
| `siguiente` | O(1) | se lee el actual y se avanza |
| `quitar` | O(n) | hay que encontrar el nodo y su anterior |
| `tamano`, `esta_vacia` | O(1) | contador |
| recorrido | O(n) | una vuelta completa |

Espacio: O(n).

## Alternativa descartada

**Cola:** también O(1), pero cada turno exige desencolar y volver a encolar, y el ciclo queda implícito. La lista circular lo expresa de forma directa.

## Dónde se usa

`dominio/partida.py`: cada ronda llama `siguiente()` tantas veces como enemigos haya.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-30 | Versión inicial para la Entrega 2. |
