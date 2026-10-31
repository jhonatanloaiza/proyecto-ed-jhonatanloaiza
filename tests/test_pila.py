"""Pruebas de la Pila (componente 01)."""

import pytest

from estructuras.pila import Pila, PilaVaciaError


def pila_con(*valores):
    pila = Pila()
    for valor in valores:
        pila.apilar(valor)
    return pila


def test_pila_nueva_esta_vacia():
    """CA-PIL-04: una pila nueva está vacía."""
    assert Pila().esta_vacia()


def test_pila_nueva_tamano_cero():
    """CA-PIL-04: una pila nueva tiene tamaño 0."""
    assert Pila().tamano() == 0


def test_pila_con_elemento_no_esta_vacia():
    """CA-PIL-01: después de apilar la pila deja de estar vacía."""
    assert not pila_con(1).esta_vacia()


def test_apilar_deja_el_valor_en_la_cima():
    """CA-PIL-01: después de apilar(x), cima() devuelve x."""
    assert pila_con(1, 2).cima() == 2


def test_apilar_aumenta_el_tamano():
    """CA-PIL-01: apilar aumenta el tamaño en 1."""
    assert pila_con(1, 2, 3).tamano() == 3


def test_apilar_acepta_none_y_duplicados():
    """CA-PIL-01: se puede apilar cualquier elemento, incluidos None y repetidos."""
    pila = pila_con(None, None)
    assert pila.tamano() == 2 and pila.cima() is None


def test_cima_no_quita_el_elemento():
    """CA-PIL-01: cima() no cambia el tamaño."""
    pila = pila_con(1)
    pila.cima()
    assert pila.tamano() == 1


def test_desapilar_en_orden_inverso():
    """CA-PIL-02: desapilar entrega los valores en orden inverso."""
    pila = pila_con(1, 2, 3)
    assert [pila.desapilar(), pila.desapilar(), pila.desapilar()] == [3, 2, 1]


def test_desapilar_un_solo_elemento():
    """CA-PIL-05: con un elemento, desapilar lo devuelve y la pila queda vacía."""
    pila = pila_con(7)
    assert pila.desapilar() == 7 and pila.esta_vacia()


def test_desapilar_reduce_el_tamano():
    """CA-PIL-02: desapilar reduce el tamaño en 1."""
    pila = pila_con(1, 2)
    pila.desapilar()
    assert pila.tamano() == 1


def test_vacia_desapilar_lanza_error():
    """CA-PIL-03: desapilar en una pila vacía lanza PilaVaciaError."""
    with pytest.raises(PilaVaciaError):
        Pila().desapilar()


def test_vacia_cima_lanza_error():
    """CA-PIL-03: cima en una pila vacía lanza PilaVaciaError."""
    with pytest.raises(PilaVaciaError):
        Pila().cima()


def test_vacia_error_no_cambia_la_pila():
    """CA-PIL-03: el error deja la pila vacía y utilizable."""
    pila = Pila()
    with pytest.raises(PilaVaciaError):
        pila.desapilar()
    pila.apilar(1)
    assert pila.cima() == 1 and pila.tamano() == 1


def test_vaciar_con_elementos():
    """CA-PIL-04: una pila recién vaciada está vacía y su tamaño es 0."""
    pila = pila_con(1, 2)
    pila.vaciar()
    assert pila.esta_vacia() and pila.tamano() == 0


def test_vaciar_pila_vacia():
    """CA-PIL-04: vaciar una pila vacía no falla."""
    pila = Pila()
    pila.vaciar()
    assert pila.esta_vacia()


def test_vaciar_permite_reutilizar():
    """CA-PIL-04: una pila vaciada se puede volver a usar."""
    pila = pila_con(1)
    pila.vaciar()
    pila.apilar(2)
    assert pila.cima() == 2 and pila.tamano() == 1
