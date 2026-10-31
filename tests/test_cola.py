"""Pruebas de la Cola (componente 05)."""

import pytest

from estructuras.cola import Cola, ColaVaciaError


def cola_con(*valores):
    cola = Cola()
    for valor in valores:
        cola.encolar(valor)
    return cola


def test_encolar_uno():
    """CA-COL-01: un valor encolado queda al frente de una cola vacía."""
    assert cola_con(1).frente() == 1


def test_encolar_varios_conserva_el_frente():
    """CA-COL-01: encolar no cambia quién está al frente."""
    assert cola_con(1, 2, 3).frente() == 1


def test_encolar_repetidos():
    """CA-COL-01: se aceptan valores repetidos y cuentan por separado."""
    assert cola_con(5, 5).tamano() == 2


def test_desencolar_en_orden_de_llegada():
    """CA-COL-01: desencolar entrega los valores en el orden en que entraron."""
    cola = cola_con(1, 2, 3)
    assert [cola.desencolar(), cola.desencolar(), cola.desencolar()] == [1, 2, 3]


def test_desencolar_un_solo_elemento():
    """CA-COL-01: con un elemento, desencolar lo devuelve y la cola queda vacía."""
    cola = cola_con(9)
    assert cola.desencolar() == 9 and cola.esta_vacia()


def test_desencolar_vacia_lanza_error():
    """CA-COL-03: desencolar en una cola vacía lanza ColaVaciaError."""
    with pytest.raises(ColaVaciaError):
        Cola().desencolar()


def test_frente_no_quita():
    """CA-COL-02: frente devuelve el primero sin quitarlo."""
    cola = cola_con(1, 2)
    cola.frente()
    assert cola.tamano() == 2


def test_frente_con_un_elemento():
    """CA-COL-02: frente funciona con un solo elemento."""
    assert cola_con(4).frente() == 4


def test_frente_vacia_lanza_error():
    """CA-COL-03: frente en una cola vacía lanza ColaVaciaError."""
    with pytest.raises(ColaVaciaError):
        Cola().frente()


def test_reutilizar_tras_vaciarse():
    """CA-COL-04: la cola se puede usar de nuevo después de vaciarse."""
    cola = cola_con(1)
    cola.desencolar()
    cola.encolar(2)
    assert cola.frente() == 2 and cola.desencolar() == 2 and cola.esta_vacia()


def test_esta_vacia_nueva():
    """CA-COL-05: una cola nueva está vacía."""
    assert Cola().esta_vacia()


def test_esta_vacia_con_elemento():
    """CA-COL-05: una cola con elementos no está vacía."""
    assert not cola_con(1).esta_vacia()


def test_esta_vacia_tras_desencolar():
    """CA-COL-05: desencolar el último deja la cola vacía."""
    cola = cola_con(1)
    cola.desencolar()
    assert cola.esta_vacia()


def test_tamano_vacia():
    """CA-COL-05: una cola vacía tiene tamaño 0."""
    assert Cola().tamano() == 0


def test_tamano_crece_y_baja():
    """CA-COL-05: el tamaño refleja encolar y desencolar."""
    cola = cola_con(1, 2, 3)
    cola.desencolar()
    assert cola.tamano() == 2


def test_tamano_un_elemento():
    """CA-COL-05: con un elemento el tamaño es 1."""
    assert cola_con(1).tamano() == 1
