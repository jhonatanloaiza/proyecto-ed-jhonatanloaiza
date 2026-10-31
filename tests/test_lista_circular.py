"""Pruebas de la ListaCircular (componente 04)."""

import pytest

from estructuras.lista_circular import ListaCircular, ListaVaciaError


def lista_con(*valores):
    lista = ListaCircular()
    for valor in valores:
        lista.insertar(valor)
    return lista


def turnos(lista, n):
    return [lista.siguiente() for _ in range(n)]


def test_siguiente_vuelve_al_primero():
    """CA-CIR-01: tras el último, siguiente vuelve al primero."""
    assert turnos(lista_con(1, 2, 3), 5) == [1, 2, 3, 1, 2]


def test_siguiente_un_elemento():
    """CA-CIR-02: con un elemento, siguiente lo devuelve siempre."""
    assert turnos(lista_con(7), 3) == [7, 7, 7]


def test_siguiente_vacia_lanza_error():
    """CA-CIR-03: siguiente en una lista vacía lanza ListaVaciaError."""
    with pytest.raises(ListaVaciaError):
        ListaCircular().siguiente()


def test_insertar_en_lista_vacia():
    """CA-CIR-04: insertar en una lista vacía deja a ese valor con el turno."""
    assert lista_con(1).siguiente() == 1


def test_insertar_a_mitad_de_ciclo():
    """CA-CIR-04: un valor insertado a mitad de ciclo entra al final."""
    lista = lista_con(1, 2, 3)
    lista.siguiente()
    lista.insertar(4)
    assert turnos(lista, 4) == [2, 3, 4, 1]


def test_insertar_conserva_el_orden():
    """CA-CIR-04: insertar no altera el orden de los demás."""
    lista = lista_con(1, 2)
    lista.insertar(3)
    assert list(lista) == [1, 2, 3]


def test_quitar_el_primero():
    """CA-CIR-05: quitar al primero no rompe el ciclo."""
    lista = lista_con(1, 2, 3)
    assert lista.quitar(1) and turnos(lista, 3) == [2, 3, 2]


def test_quitar_el_ultimo():
    """CA-CIR-05: quitar al último cierra el ciclo y deja correcto el siguiente insertar."""
    lista = lista_con(1, 2, 3)
    lista.quitar(3)
    lista.insertar(4)
    assert list(lista) == [1, 2, 4]


def test_quitar_el_actual():
    """CA-CIR-05: quitar al que le toca pasa el turno al siguiente."""
    lista = lista_con(1, 2, 3)
    lista.siguiente()
    lista.quitar(2)
    assert turnos(lista, 3) == [3, 1, 3]


def test_quitar_el_unico():
    """CA-CIR-05: quitar al único deja la lista vacía y reutilizable."""
    lista = lista_con(1)
    assert lista.quitar(1) and lista.esta_vacia()
    lista.insertar(2)
    assert lista.siguiente() == 2


def test_quitar_inexistente():
    """CA-CIR-06: quitar un valor que no está devuelve False y no cambia la lista."""
    lista = lista_con(1, 2)
    assert not lista.quitar(9) and list(lista) == [1, 2]


def test_quitar_de_lista_vacia():
    """CA-CIR-06: quitar de una lista vacía devuelve False."""
    assert not ListaCircular().quitar(1)


def test_tamano_vacia():
    """CA-CIR-07: una lista vacía tiene tamaño 0."""
    assert ListaCircular().tamano() == 0


def test_tamano_refleja_cambios():
    """CA-CIR-07: el tamaño refleja inserciones y salidas."""
    lista = lista_con(1, 2, 3)
    lista.quitar(2)
    assert lista.tamano() == 2


def test_tamano_no_cambia_con_siguiente():
    """CA-CIR-07: avanzar el turno no cambia el tamaño."""
    lista = lista_con(1)
    lista.siguiente()
    assert lista.tamano() == 1


def test_esta_vacia_nueva():
    """CA-CIR-07: una lista nueva está vacía."""
    assert ListaCircular().esta_vacia()


def test_esta_vacia_con_elemento():
    """CA-CIR-07: con un elemento no está vacía."""
    assert not lista_con(1).esta_vacia()


def test_esta_vacia_tras_quitar():
    """CA-CIR-07: quitar el último valor la deja vacía."""
    lista = lista_con(1)
    lista.quitar(1)
    assert lista.esta_vacia()


def test_recorrido_en_orden():
    """CA-CIR-08: el recorrido entrega cada valor una vez en orden de inserción."""
    assert list(lista_con(1, 2, 3)) == [1, 2, 3]


def test_recorrido_vacia():
    """CA-CIR-08: recorrer una lista vacía no entrega nada."""
    assert list(ListaCircular()) == []


def test_recorrido_no_mueve_el_turno():
    """CA-CIR-08: recorrer no cambia a quién le toca."""
    lista = lista_con(1, 2, 3)
    lista.siguiente()
    list(lista)
    assert lista.siguiente() == 2
