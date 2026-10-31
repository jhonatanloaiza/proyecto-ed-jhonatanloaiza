"""Pruebas del Historial (componente 01), con una acción de prueba que suma a un contador."""

from dominio.historial import Historial


class Contador:
    valor = 0


class Sumar:
    def __init__(self, partida, n):
        self.n = n
        self.hacer(partida)

    def hacer(self, partida):
        partida.valor += self.n

    def revertir(self, partida):
        partida.valor -= self.n


def historial_con(partida, *numeros):
    historial = Historial()
    for n in numeros:
        historial.registrar(Sumar(partida, n))
    return historial


def test_registrar_permite_deshacer():
    """CA-HIS-03: registrar deja la acción disponible para deshacer."""
    assert historial_con(Contador(), 1).puede_deshacer()


def test_registrar_no_habilita_rehacer():
    """CA-HIS-03: registrar no deja nada para rehacer."""
    assert not historial_con(Contador(), 1).puede_rehacer()


def test_registrar_tras_deshacer_borra_rehacer():
    """CA-HIS-03: registrar después de deshacer hace que puede_rehacer sea False."""
    partida = Contador()
    historial = historial_con(partida, 1)
    historial.deshacer(partida)
    historial.registrar(Sumar(partida, 2))
    assert not historial.puede_rehacer()


def test_deshacer_revierte_la_mas_reciente():
    """CA-HIS-01: deshacer revierte solo la acción más reciente."""
    partida = Contador()
    historial_con(partida, 1, 10).deshacer(partida)
    assert partida.valor == 1


def test_deshacer_devuelve_la_accion():
    """CA-HIS-01: deshacer devuelve la acción revertida."""
    partida = Contador()
    historial = Historial()
    accion = Sumar(partida, 1)
    historial.registrar(accion)
    assert historial.deshacer(partida) is accion


def test_deshacer_sin_acciones():
    """CA-HIS-04: deshacer sin acciones devuelve None y no cambia el estado."""
    partida = Contador()
    assert Historial().deshacer(partida) is None and partida.valor == 0


def test_rehacer_restaura_el_estado():
    """CA-HIS-02: rehacer deja el estado igual al que había antes de deshacer."""
    partida = Contador()
    historial = historial_con(partida, 5)
    historial.deshacer(partida)
    historial.rehacer(partida)
    assert partida.valor == 5


def test_rehacer_devuelve_a_deshacer():
    """CA-HIS-02: lo rehecho se puede deshacer otra vez."""
    partida = Contador()
    historial = historial_con(partida, 5)
    historial.deshacer(partida)
    historial.rehacer(partida)
    historial.deshacer(partida)
    assert partida.valor == 0


def test_rehacer_sin_acciones():
    """CA-HIS-04: rehacer sin acciones devuelve None y no cambia el estado."""
    partida = Contador()
    assert historial_con(partida, 1).rehacer(partida) is None and partida.valor == 1


def test_secuencia_deshacer_y_rehacer_n():
    """CA-HIS-05: deshacer n y rehacer n devuelve el estado final original."""
    partida = Contador()
    historial = historial_con(partida, 1, 2, 3)
    for _ in range(3):
        historial.deshacer(partida)
    assert partida.valor == 0
    for _ in range(3):
        historial.rehacer(partida)
    assert partida.valor == 6


def test_puede_deshacer_nuevo():
    """CA-HIS-04: un historial nuevo no puede deshacer."""
    assert not Historial().puede_deshacer()


def test_puede_deshacer_tras_agotar():
    """CA-HIS-04: tras deshacer todo, puede_deshacer es False."""
    partida = Contador()
    historial = historial_con(partida, 1)
    historial.deshacer(partida)
    assert not historial.puede_deshacer()


def test_puede_rehacer_nuevo():
    """CA-HIS-04: un historial nuevo no puede rehacer."""
    assert not Historial().puede_rehacer()


def test_puede_rehacer_tras_deshacer():
    """CA-HIS-02: después de deshacer, puede_rehacer es True."""
    partida = Contador()
    historial = historial_con(partida, 1)
    historial.deshacer(partida)
    assert historial.puede_rehacer()
