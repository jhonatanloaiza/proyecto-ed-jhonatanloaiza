# Plan · Componente 05: Cola

## Estructura elegida

Cola enlazada con referencias al frente y al final, más un contador. Sin soporte interno de `list`.

## Complejidad

| Operación | Tiempo | Por qué |
| --- | --- | --- |
| `encolar` | O(1) | se enlaza detrás del final |
| `desencolar`, `frente` | O(1) | se opera sobre el frente |
| `tamano`, `esta_vacia` | O(1) | contador |

Espacio: O(n).

## Alternativa descartada

**Cola de prioridad:** aquí ningún evento es más urgente que otro; costaría O(log n) y podría alterar el orden de llegada, que es lo que exige la temática.

## Dónde se usa

`dominio/partida.py` encola cada `Evento`; `estructuras/grafo.py` la usa como frontera del BFS.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-30 | Versión inicial para la Entrega 2. |
