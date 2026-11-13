"""Mediciones empíricas para ANALISIS.md.

Uso, desde la raíz del repositorio:  python docs/evidencias/medicion.py
Escribe docs/evidencias/mediciones.md.
"""

import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ))

from dominio.niveles import NIVELES  # noqa: E402
from dominio.partida import Partida  # noqa: E402
from estructuras.avl import ArbolAVL  # noqa: E402
from estructuras.grafo import GrafoRejilla  # noqa: E402
from estructuras.monticulo import MonticuloMinimo  # noqa: E402

REPETICIONES = 5


def cronometrar(funcion):
    """Mejor tiempo de varias repeticiones, en milisegundos."""
    mejor = float("inf")
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        funcion()
        mejor = min(mejor, time.perf_counter() - inicio)
    return mejor * 1000


def bfs_contra_a_estrella():
    lineas = ["## 1. Rutas: BFS (elegido para el Rastreador) contra A* (Cazador)", "",
              "Rejilla abierta de n × n, de la esquina superior izquierda a la inferior derecha.", "",
              "| n | celdas | pasos | BFS explora | A* explora | BFS (ms) | A* (ms) |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for n in (20, 40, 80, 160):
        grafo = GrafoRejilla(n, n, lambda f, c: True)
        origen, destino = (0, 0), (n - 1, n - 1)
        bfs, guiada = grafo.bfs(origen, destino), grafo.a_estrella(origen, destino)
        t_bfs = cronometrar(lambda: grafo.bfs(origen, destino))
        t_a = cronometrar(lambda: grafo.a_estrella(origen, destino))
        lineas.append(f"| {n} | {n * n} | {bfs.camino.tamano() - 1} | {bfs.explorados} | {guiada.explorados} | {t_bfs:.2f} | {t_a:.2f} |")
    lineas += ["", "Niveles del juego: cada Pájaro hacia la posición inicial del Cubo.", "",
               "| Nivel | Pájaro | pasos | BFS explora | A* explora |", "| --- | --- | --- | --- | --- |"]
    for nombre, plano in NIVELES:
        for pajaro, pasos, bfs, guiada in Partida(plano, nombre).comparar_busquedas():
            lineas.append(f"| {nombre} | {pajaro} | {pasos} | {bfs} | {guiada} |")
    return lineas


def avl_contra_monticulo():
    lineas = ["", "## 2. Puntajes: AVL (elegido) contra montículo (descartado)", "",
              "Se insertan n puntajes y luego se obtiene el ranking completo ordenado de mayor a menor.", "",
              "| n | AVL insertar (ms) | AVL ranking (ms) | Montículo insertar (ms) | Montículo ranking (ms) |",
              "| --- | --- | --- | --- | --- |"]
    for n in (1000, 2000, 4000, 8000):
        puntajes = [(i * 7919) % 10007 for i in range(n)]

        def llenar_avl():
            arbol = ArbolAVL()
            for numero, puntaje in enumerate(puntajes):
                arbol.insertar((puntaje, -numero), puntaje)
            return arbol

        def llenar_monticulo():
            monticulo = MonticuloMinimo()
            for puntaje in puntajes:
                monticulo.insertar(-puntaje, puntaje)  # prioridad negativa: sale primero el mayor
            return monticulo

        def ranking_monticulo():
            monticulo = llenar_monticulo()
            while not monticulo.esta_vacia():
                monticulo.extraer_minimo()

        arbol = llenar_avl()
        t_avl_ins = cronometrar(llenar_avl)
        t_avl_rank = cronometrar(arbol.descendente)
        t_mon_ins = cronometrar(llenar_monticulo)
        t_mon_rank = cronometrar(ranking_monticulo) - t_mon_ins
        lineas.append(f"| {n} | {t_avl_ins:.1f} | {t_avl_rank:.1f} | {t_mon_ins:.1f} | {t_mon_rank:.1f} |")
    lineas += ["", "El ranking del montículo lo vacía: para volver a mostrarlo habría que reconstruirlo."]
    return lineas


def main():
    lineas = ["# Mediciones", "", f"Generado con `python docs/evidencias/medicion.py` (mejor de {REPETICIONES} repeticiones).", ""]
    lineas += bfs_contra_a_estrella()
    lineas += avl_contra_monticulo()
    salida = RAIZ / "docs" / "evidencias" / "mediciones.md"
    salida.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print(salida.read_text(encoding="utf-8"))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
