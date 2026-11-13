"""Pruebas de la TablaPuntajes (componente 08)."""

from dominio.puntajes import TablaPuntajes


def puntajes_de(tabla):
    return [registro.puntaje for registro in tabla.ranking()]


def test_registrar_aparece_en_el_ranking():
    """CA-PUN-01: una partida registrada aparece en el ranking."""
    tabla = TablaPuntajes()
    tabla.registrar(30, "victoria", 25, "Sector de Arranque")
    assert puntajes_de(tabla) == [30]


def test_registrar_varias():
    """CA-PUN-01: cada partida registrada cuenta por separado."""
    tabla = TablaPuntajes()
    for puntaje in (10, 20, 10):
        tabla.registrar(puntaje, "derrota", 5)
    assert tabla.tamano() == 3


def test_registrar_guarda_los_datos():
    """CA-PUN-01: el registro conserva resultado, turnos y nivel."""
    tabla = TablaPuntajes()
    tabla.registrar(40, "victoria", 31, "Memoria Fragmentada")
    registro = next(iter(tabla.ranking()))
    assert (registro.resultado, registro.turnos, registro.nivel) == ("victoria", 31, "Memoria Fragmentada")


def test_ranking_de_mayor_a_menor():
    """CA-PUN-02: el ranking va de mayor a menor puntaje."""
    tabla = TablaPuntajes()
    for puntaje in (20, 50, 10, 40):
        tabla.registrar(puntaje, "victoria", 1)
    assert puntajes_de(tabla) == [50, 40, 20, 10]


def test_ranking_empate_primero_la_mas_antigua():
    """CA-PUN-02: con empate, primero la partida más antigua."""
    tabla = TablaPuntajes()
    tabla.registrar(30, "victoria", 1, "primera")
    tabla.registrar(30, "derrota", 2, "segunda")
    assert [registro.nivel for registro in tabla.ranking()] == ["primera", "segunda"]


def test_ranking_vacio():
    """CA-PUN-03: sin partidas, el ranking está vacío."""
    tabla = TablaPuntajes()
    assert tabla.ranking().esta_vacia() and tabla.tamano() == 0
