"""Pruebas del GrafoRejilla (componente 07)."""

import random

from estructuras.grafo import GrafoRejilla


def grafo_de(*plano):
    return GrafoRejilla(len(plano), len(plano[0]), lambda f, c: plano[f][c] != "^")


def test_vecinos_en_el_centro():
    """CA-GRA-01: una celda central tiene 4 vecinos en orden fijo."""
    assert list(grafo_de("...", "...", "...").vecinos((1, 1))) == [(0, 1), (2, 1), (1, 0), (1, 2)]


def test_vecinos_en_la_esquina():
    """CA-GRA-01: vecinos no incluye celdas fuera de la rejilla."""
    assert list(grafo_de("..", "..").vecinos((0, 0))) == [(1, 0), (0, 1)]


def test_vecinos_evita_no_transitables():
    """CA-GRA-01: vecinos no incluye celdas no transitables."""
    assert list(grafo_de(".^", "^.").vecinos((0, 0))) == []


def test_bfs_camino_mas_corto_sin_obstaculos():
    """CA-GRA-02: el camino tiene el menor número de pasos y va de origen a destino."""
    camino = list(grafo_de("...", "...", "...").bfs((0, 0), (2, 2)).camino)
    assert len(camino) == 5 and camino[0] == (0, 0) and camino[-1] == (2, 2)


def test_bfs_rodea_obstaculos():
    """CA-GRA-02: con una pared, el camino la rodea por la ruta más corta."""
    camino = list(grafo_de(".^.", ".^.", "...").bfs((0, 0), (0, 2)).camino)
    assert len(camino) == 7


def test_bfs_cada_paso_es_contiguo_y_transitable():
    """CA-GRA-03: cada paso va a una celda contigua y transitable."""
    plano = (".^...", ".^.^.", "...^.")
    camino = list(grafo_de(*plano).bfs((0, 0), (2, 4)).camino)
    pares = zip(camino, camino[1:])
    assert all(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1 for a, b in pares)
    assert all(plano[f][c] != "^" for f, c in camino)


def test_bfs_sin_camino():
    """CA-GRA-04: si no hay camino, camino queda vacío."""
    assert grafo_de(".^.", ".^.").bfs((0, 0), (0, 2)).camino.esta_vacia()


def test_bfs_origen_igual_a_destino():
    """CA-GRA-05: si origen y destino coinciden, el camino tiene solo esa celda."""
    assert list(grafo_de("..").bfs((0, 1), (0, 1)).camino) == [(0, 1)]


def test_explorados_origen_igual_a_destino():
    """CA-GRA-06: explorados es 1 si el origen ya es el destino."""
    assert grafo_de("..").bfs((0, 0), (0, 0)).explorados == 1


def test_explorados_sin_camino_cuenta_la_region():
    """CA-GRA-06: sin camino, explorados cuenta todas las celdas alcanzables."""
    assert grafo_de(".^.", ".^.").bfs((0, 0), (0, 2)).explorados == 2


def test_explorados_no_repite_celdas():
    """CA-GRA-06: explorados no supera las celdas de la rejilla."""
    assert grafo_de("...", "...", "...").bfs((0, 0), (2, 2)).explorados <= 9


def test_siguiente_paso_primer_paso():
    """CA-GRA-07: devuelve la primera celda del camino."""
    assert grafo_de("...").siguiente_paso((0, 0), (0, 2)) == (0, 1)


def test_siguiente_paso_ya_llego():
    """CA-GRA-07: devuelve None si ya está en el destino."""
    assert grafo_de("...").siguiente_paso((0, 1), (0, 1)) is None


def test_siguiente_paso_sin_camino():
    """CA-GRA-07: devuelve None si no hay camino."""
    assert grafo_de(".^.").siguiente_paso((0, 0), (0, 2)) is None


def test_a_estrella_misma_longitud_que_bfs():
    """CA-GRA-08: A* devuelve un camino de la misma longitud que BFS."""
    grafo = grafo_de(".....", ".^^^.", ".^...", ".^.^.", "...^.")
    assert grafo.a_estrella((0, 0), (4, 4)).camino.tamano() == grafo.bfs((0, 0), (4, 4)).camino.tamano()


def test_a_estrella_camino_contiguo_y_transitable():
    """CA-GRA-08: cada paso de A* va a una celda contigua y transitable, de origen a destino."""
    plano = (".^...", ".^.^.", "...^.")
    camino = list(grafo_de(*plano).a_estrella((0, 0), (2, 4)).camino)
    assert camino[0] == (0, 0) and camino[-1] == (2, 4)
    assert all(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1 for a, b in zip(camino, camino[1:]))
    assert all(plano[f][c] != "^" for f, c in camino)


def plano_al_azar(azar, lado, proporcion):
    return ["".join("^" if azar.random() < proporcion else "." for _ in range(lado)) for _ in range(lado)]


def test_a_estrella_igual_que_bfs_en_mapas_aleatorios():
    """CA-GRA-08: en 100 mapas aleatorios A* y BFS encuentran caminos de igual longitud."""
    azar = random.Random(7)
    for _ in range(100):
        plano = plano_al_azar(azar, 12, 0.3)
        plano[0] = "." + plano[0][1:]
        plano[11] = plano[11][:11] + "."
        grafo = grafo_de(*plano)
        assert grafo.a_estrella((0, 0), (11, 11)).camino.tamano() == grafo.bfs((0, 0), (11, 11)).camino.tamano()


def test_a_estrella_explora_menos_en_campo_abierto():
    """CA-GRA-09: sin obstáculos A* explora mucho menos que BFS."""
    grafo = grafo_de(*["." * 20] * 20)
    assert grafo.a_estrella((0, 0), (19, 19)).explorados < grafo.bfs((0, 0), (19, 19)).explorados


def test_a_estrella_nunca_explora_mas_que_bfs():
    """CA-GRA-09: en el mismo mapa A* explora como máximo tantas celdas como BFS."""
    azar = random.Random(3)
    for _ in range(100):
        grafo = grafo_de(*plano_al_azar(azar, 15, 0.25))
        assert grafo.a_estrella((7, 7), (0, 14)).explorados <= grafo.bfs((7, 7), (0, 14)).explorados


def test_a_estrella_sin_camino_explora_igual():
    """CA-GRA-09: sin camino, ambas búsquedas recorren la misma región."""
    grafo = grafo_de(".^.", ".^.")
    assert grafo.a_estrella((0, 0), (0, 2)).explorados == grafo.bfs((0, 0), (0, 2)).explorados == 2


def test_a_estrella_sin_camino():
    """CA-GRA-10: si no hay camino, A* devuelve el camino vacío."""
    assert grafo_de(".^.", ".^.").a_estrella((0, 0), (0, 2)).camino.esta_vacia()


def test_a_estrella_origen_igual_a_destino():
    """CA-GRA-10: si origen y destino coinciden, el camino tiene solo esa celda."""
    assert list(grafo_de("..").a_estrella((0, 1), (0, 1)).camino) == [(0, 1)]


def test_a_estrella_destino_encerrado():
    """CA-GRA-10: un destino rodeado de picos no tiene camino."""
    assert grafo_de("...", ".^.", "^.^").a_estrella((0, 0), (2, 1)).camino.esta_vacia()


def test_siguiente_paso_guiado():
    """CA-GRA-11: con guiado=True devuelve la primera celda del camino de A*."""
    assert grafo_de("...").siguiente_paso((0, 0), (0, 2), guiado=True) == (0, 1)


def test_siguiente_paso_guiado_sin_camino():
    """CA-GRA-11: con guiado=True devuelve None si no hay camino."""
    assert grafo_de(".^.").siguiente_paso((0, 0), (0, 2), guiado=True) is None


def test_siguiente_paso_guiado_ya_llego():
    """CA-GRA-11: con guiado=True devuelve None si ya está en el destino."""
    assert grafo_de("..").siguiente_paso((0, 0), (0, 0), guiado=True) is None
