"""Pruebas de la Matriz (componente 02)."""

import pytest

from estructuras.matriz import FueraDeRangoError, Matriz


def test_crear_valor_inicial_en_esquinas():
    """CA-MAT-01: una matriz nueva tiene el valor inicial en sus esquinas."""
    matriz = Matriz(3, 4, ".")
    assert {matriz.consultar(f, c) for f, c in ((0, 0), (0, 3), (2, 0), (2, 3))} == {"."}


def test_crear_sin_valor_inicial():
    """CA-MAT-01: sin valor inicial, las celdas valen None."""
    assert Matriz(1, 1).consultar(0, 0) is None


@pytest.mark.parametrize("filas, columnas", [(0, 5), (5, 0), (-1, 5)])
def test_crear_tamano_invalido(filas, columnas):
    """CA-MAT-05: crear una matriz sin celdas lanza ValueError."""
    with pytest.raises(ValueError):
        Matriz(filas, columnas)


def test_consultar_devuelve_lo_asignado():
    """CA-MAT-02: consultar devuelve el valor asignado."""
    matriz = Matriz(2, 2)
    matriz.asignar(1, 0, "x")
    assert matriz.consultar(1, 0) == "x"


def test_consultar_ultima_celda():
    """CA-MAT-02: se puede consultar la última celda."""
    matriz = Matriz(2, 3)
    matriz.asignar(1, 2, "x")
    assert matriz.consultar(1, 2) == "x"


@pytest.mark.parametrize("fila, columna", [(-1, 0), (0, -1), (2, 0), (0, 3)])
def test_consultar_fuera_de_rango(fila, columna):
    """CA-MAT-03: consultar fuera de rango lanza FueraDeRangoError."""
    with pytest.raises(FueraDeRangoError):
        Matriz(2, 3).consultar(fila, columna)


def test_asignar_no_toca_otras_celdas():
    """CA-MAT-02: asignar no cambia las demás celdas."""
    matriz = Matriz(2, 2, 0)
    matriz.asignar(0, 1, 1)
    assert matriz.consultar(1, 0) == 0 and matriz.consultar(0, 0) == 0


def test_asignar_reemplaza():
    """CA-MAT-02: asignar dos veces deja el último valor."""
    matriz = Matriz(1, 1)
    matriz.asignar(0, 0, 1)
    matriz.asignar(0, 0, 2)
    assert matriz.consultar(0, 0) == 2


@pytest.mark.parametrize("fila, columna", [(-1, 0), (2, 2)])
def test_asignar_fuera_de_rango(fila, columna):
    """CA-MAT-03: asignar fuera de rango lanza FueraDeRangoError."""
    with pytest.raises(FueraDeRangoError):
        Matriz(2, 2).asignar(fila, columna, 1)


@pytest.mark.parametrize("fila, columna", [(0, 0), (0, 4), (2, 0), (2, 4)])
def test_dentro_esquinas(fila, columna):
    """CA-MAT-04: dentro es True en las cuatro esquinas."""
    assert Matriz(3, 5).dentro(fila, columna)


@pytest.mark.parametrize("fila, columna", [(-1, 0), (3, 0), (0, -1), (0, 5)])
def test_dentro_justo_afuera(fila, columna):
    """CA-MAT-04: dentro es False justo afuera de cada borde."""
    assert not Matriz(3, 5).dentro(fila, columna)


def test_dimensiones_no_cuadrada():
    """CA-MAT-06: filas y columnas funcionan en una matriz no cuadrada."""
    matriz = Matriz(2, 7)
    assert (matriz.filas(), matriz.columnas()) == (2, 7)


def test_dimensiones_uno_por_uno():
    """CA-MAT-06: filas y columnas funcionan en una matriz de 1 × 1."""
    matriz = Matriz(1, 1)
    assert (matriz.filas(), matriz.columnas()) == (1, 1)


def test_dimensiones_del_juego():
    """CA-MAT-06: la matriz del juego mide 20 × 20."""
    matriz = Matriz(20, 20)
    assert (matriz.filas(), matriz.columnas()) == (20, 20)
