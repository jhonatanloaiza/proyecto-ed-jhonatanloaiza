"""Pruebas del MonticuloMinimo (componente 09)."""

import pytest

from estructuras.monticulo import MonticuloMinimo, MonticuloVacioError


def monticulo_con(*prioridades):
    monticulo = MonticuloMinimo()
    for prioridad in prioridades:
        monticulo.insertar(prioridad, f"v{prioridad}")
    return monticulo


def vaciar(monticulo):
    return [monticulo.extraer_minimo() for _ in range(monticulo.tamano())]


def test_insertar_desordenado():
    """CA-MON-01: extraer_minimo entrega en orden creciente sin importar el orden de inserción."""
    assert vaciar(monticulo_con(5, 1, 4, 2, 3)) == ["v1", "v2", "v3", "v4", "v5"]


def test_insertar_en_orden_decreciente():
    """CA-MON-01: insertar de mayor a menor también sale en orden creciente."""
    assert vaciar(monticulo_con(*range(20, 0, -1))) == [f"v{i}" for i in range(1, 21)]


def test_insertar_un_elemento():
    """CA-MON-01: con un elemento, extraer_minimo lo devuelve."""
    assert vaciar(monticulo_con(7)) == ["v7"]


def test_empates_en_orden_de_llegada():
    """CA-MON-02: con prioridades iguales, salen en el orden en que entraron."""
    monticulo = MonticuloMinimo()
    for valor in "abcd":
        monticulo.insertar(1, valor)
    assert vaciar(monticulo) == ["a", "b", "c", "d"]


def test_empates_mezclados():
    """CA-MON-02: los empates se respetan aunque haya otras prioridades."""
    monticulo = MonticuloMinimo()
    for prioridad, valor in ((2, "a"), (1, "b"), (2, "c"), (1, "d")):
        monticulo.insertar(prioridad, valor)
    assert vaciar(monticulo) == ["b", "d", "a", "c"]


def test_prioridades_compuestas():
    """CA-MON-01: las prioridades (f, h) de A* se comparan por ambos valores."""
    monticulo = MonticuloMinimo()
    monticulo.insertar((5, 3), "lejos")
    monticulo.insertar((5, 1), "cerca")
    assert monticulo.extraer_minimo() == "cerca"


def test_extraer_vacio_lanza_error():
    """CA-MON-04: extraer_minimo en un montículo vacío lanza MonticuloVacioError."""
    with pytest.raises(MonticuloVacioError):
        MonticuloMinimo().extraer_minimo()


def test_extraer_hasta_vaciar_y_reutilizar():
    """CA-MON-05: tras vaciarse, el montículo se puede volver a usar."""
    monticulo = monticulo_con(1)
    monticulo.extraer_minimo()
    monticulo.insertar(2, "x")
    assert monticulo.extraer_minimo() == "x"


def test_minimo_no_quita():
    """CA-MON-03: minimo devuelve el menor sin quitarlo."""
    monticulo = monticulo_con(3, 1, 2)
    assert monticulo.minimo() == "v1" and monticulo.tamano() == 3


def test_minimo_un_elemento():
    """CA-MON-03: minimo funciona con un elemento."""
    assert monticulo_con(9).minimo() == "v9"


def test_minimo_vacio_lanza_error():
    """CA-MON-04: minimo en un montículo vacío lanza MonticuloVacioError."""
    with pytest.raises(MonticuloVacioError):
        MonticuloMinimo().minimo()


def test_tamano_vacio():
    """CA-MON-05: un montículo vacío tiene tamaño 0."""
    assert MonticuloMinimo().tamano() == 0


def test_tamano_tras_extraer():
    """CA-MON-05: el tamaño baja al extraer."""
    monticulo = monticulo_con(1, 2)
    monticulo.extraer_minimo()
    assert monticulo.tamano() == 1


def test_tamano_con_repetidos():
    """CA-MON-05: los repetidos cuentan por separado."""
    assert monticulo_con(1, 1, 1).tamano() == 3


def test_esta_vacia_nuevo():
    """CA-MON-05: un montículo nuevo está vacío."""
    assert MonticuloMinimo().esta_vacia()


def test_esta_vacia_con_elemento():
    """CA-MON-05: con un elemento no está vacío."""
    assert not monticulo_con(1).esta_vacia()


def test_esta_vacia_tras_extraer():
    """CA-MON-05: extraer el único elemento lo deja vacío."""
    monticulo = monticulo_con(1)
    monticulo.extraer_minimo()
    assert monticulo.esta_vacia()
