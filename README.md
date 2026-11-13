# Escape Geométrico del Sistema Corrupto

Proyecto integrador · Estructuras de Datos (ID 706132) · Universidad Cooperativa de Colombia · II-2026

- **Temática:** A · Motor de juego 2D con pathfinding
- **Modalidad:** individual
- **Lenguaje:** Python 3.11 o superior (juego por consola)

## Contexto narrativo

Un Cubo Geométrico atrapado en una matriz de seguridad de 20 × 20 celdas debe llegar al portal de salida, turno a turno, mientras Pájaros Rastreadores calculan la ruta más corta para atraparlo.

## Estado

Entrega final: 9 estructuras implementadas e integradas, 3 niveles y 15 historias de usuario terminadas. Ver `ANALISIS.md` y `specs/trazabilidad.md`.

## Cómo ejecutar

Requisitos: Python 3.11 o superior. Para las pruebas, `pytest` (`python -m pip install pytest`). El juego no usa otras librerías.

1. Clonar el repositorio y entrar a la carpeta:

   ```bash
   git clone https://github.com/jhonatanloaiza/proyecto-ed-jhonatanloaiza.git
   cd proyecto-ed-jhonatanloaiza
   ```

2. Jugar:

   ```bash
   python main.py
   ```

3. Correr las pruebas:

   ```bash
   python -m pytest
   ```

4. Repetir las mediciones de `ANALISIS.md` (opcional):

   ```bash
   python docs/evidencias/medicion.py
   ```

En Windows conviene usar **Windows Terminal** o la terminal de VS Code para ver los colores y el símbolo `■` del Cubo. Si `python` no se reconoce, prueba con `py`.

## Cómo jugar

En el menú, `1` inicia una partida (luego eliges el nivel 1, 2 o 3), `2` muestra los mejores puntajes y `s` sale.

Llega al portal `@` sin que te atrape un Pájaro. Cada comando se escribe y se confirma con Enter.

| Símbolo | Elemento |
| --- | --- |
| `■` | Cubo Geométrico (tú) |
| `V` | Pájaro Rastreador: te persigue por el camino más corto (BFS) |
| `S` | Pájaro Centinela: aparece cuando recoges una llave |
| `H` | Pájaro Cazador: te persigue con A* |
| `o` / `k` | Orbe (10 puntos) / llave |
| `^` / `#` / `@` | Pico / compuerta cerrada / portal de salida |

| Nivel | Reto |
| --- | --- |
| 1 · Sector de Arranque | 2 Rastreadores; el portal está abierto |
| 2 · Memoria Fragmentada | el portal está tras una compuerta; la llave despierta al Centinela |
| 3 · Núcleo Corrupto | 2 compuertas, 2 llaves, Centinela y Cazador |

| Comando | Acción |
| --- | --- |
| `w` `a` `s` `d` | mover arriba, izquierda, abajo, derecha |
| `e` | esperar |
| `i` | ver el inventario |
| `u ID` | usar un objeto (por ejemplo `u k1`) |
| `x ID` | soltar un objeto |
| `b ID` | buscar una entidad (por ejemplo `b r1`) |
| `c` | comparar cuántas celdas exploran BFS y A* para cada Pájaro |
| `z` / `y` | deshacer / rehacer |
| `r` / `q` | reiniciar / volver al menú (si la partida terminó, su puntaje se registra) |

## Estructura

- `specs/`: artefactos SDD (constitución, historias, MoSCoW, estructuras, specs por componente).
- `estructuras/`: un módulo por estructura de datos.
- `dominio/`: lógica del juego.
- `tests/`: pruebas con pytest.
- `docs/`: documentos y evidencias.
