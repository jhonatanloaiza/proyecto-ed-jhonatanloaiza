"""Pruebas de la ListaEnlazada (componente 03)."""

import pytest

from estructuras.lista_enlazada import ListaEnlazada


def lista_con(*valores):
    lista = ListaEnlazada()
    for valor in valores:
        lista.agregar(valor)
    return lista


def test_agregar_conserva_el_orden():
    """CA-LIS-01: agregar conserva el orden de llegada."""
    assert list(lista_con(1, 2, 3)) == [1, 2, 3]


def test_agregar_a_lista_vacia():
    """CA-LIS-01: agregar a una lista vacía deja un elemento."""
    assert list(lista_con(1)) == [1]


def test_agregar_repetidos():
    """CA-LIS-01: se aceptan valores repetidos."""
    assert list(lista_con(1, 1)) == [1, 1]


def test_recorrer_lista_vacia():
    """CA-LIS-01: recorrer una lista vacía no entrega nada."""
    assert list(ListaEnlazada()) == []


def test_insertar_al_inicio():
    """CA-LIS-02: insertar_en funciona al inicio."""
    lista = lista_con(2, 3)
    lista.insertar_en(0, 1)
    assert list(lista) == [1, 2, 3]


def test_insertar_en_el_medio():
    """CA-LIS-02: insertar_en funciona en el medio."""
    lista = lista_con(1, 3)
    lista.insertar_en(1, 2)
    assert list(lista) == [1, 2, 3]


def test_insertar_al_final_y_agregar():
    """CA-LIS-02: tras insertar al final, agregar sigue yendo al final."""
    lista = lista_con(1)
    lista.insertar_en(1, 2)
    lista.agregar(3)
    assert list(lista) == [1, 2, 3]


def test_insertar_en_lista_vacia():
    """CA-LIS-02: insertar en la posición 0 de una lista vacía funciona."""
    lista = ListaEnlazada()
    lista.insertar_en(0, 1)
    assert list(lista) == [1]


@pytest.mark.parametrize("posicion", [-1, 3])
def test_insertar_posicion_invalida(posicion):
    """CA-LIS-04: insertar en una posición inválida lanza IndexError y no cambia la lista."""
    lista = lista_con(1, 2)
    with pytest.raises(IndexError):
        lista.insertar_en(posicion, 9)
    assert list(lista) == [1, 2]


def test_quitar_al_inicio():
    """CA-LIS-03: quitar_en funciona al inicio."""
    lista = lista_con(1, 2, 3)
    assert lista.quitar_en(0) == 1 and list(lista) == [2, 3]


def test_quitar_en_el_medio():
    """CA-LIS-03: quitar_en funciona en el medio."""
    lista = lista_con(1, 2, 3)
    assert lista.quitar_en(1) == 2 and list(lista) == [1, 3]


def test_quitar_el_ultimo_y_agregar():
    """CA-LIS-03: quitar el último deja correcto el siguiente agregar."""
    lista = lista_con(1, 2)
    lista.quitar_en(1)
    lista.agregar(3)
    assert list(lista) == [1, 3]


def test_quitar_unico_y_agregar():
    """CA-LIS-03: quitar el único elemento deja la lista lista para agregar."""
    lista = lista_con(1)
    lista.quitar_en(0)
    lista.agregar(2)
    assert list(lista) == [2]


@pytest.mark.parametrize("posicion", [-1, 2])
def test_quitar_posicion_invalida(posicion):
    """CA-LIS-04: quitar una posición inválida lanza IndexError y no cambia la lista."""
    lista = lista_con(1, 2)
    with pytest.raises(IndexError):
        lista.quitar_en(posicion)
    assert list(lista) == [1, 2]


def test_quitar_en_lista_vacia():
    """CA-LIS-04: quitar de una lista vacía lanza IndexError."""
    with pytest.raises(IndexError):
        ListaEnlazada().quitar_en(0)


def test_buscar_encuentra_el_primero():
    """CA-LIS-05: buscar devuelve la posición y el valor del primero que cumple."""
    assert lista_con(1, 2, 4).buscar(lambda x: x % 2 == 0) == (1, 2)


def test_buscar_inexistente():
    """CA-LIS-05: buscar devuelve None si ninguno cumple."""
    assert lista_con(1, 3).buscar(lambda x: x == 2) is None


def test_buscar_en_lista_vacia():
    """CA-LIS-05: buscar en una lista vacía devuelve None."""
    assert ListaEnlazada().buscar(lambda x: True) is None


def test_tamano_vacia():
    """CA-LIS-06: una lista vacía tiene tamaño 0."""
    assert ListaEnlazada().tamano() == 0


def test_tamano_un_elemento():
    """CA-LIS-06: con un elemento el tamaño es 1."""
    assert lista_con(1).tamano() == 1


def test_tamano_tras_quitar():
    """CA-LIS-06: el tamaño baja al quitar."""
    lista = lista_con(1, 2)
    lista.quitar_en(0)
    assert lista.tamano() == 1


def test_esta_vacia_nueva():
    """CA-LIS-06: una lista nueva está vacía."""
    assert ListaEnlazada().esta_vacia()


def test_esta_vacia_con_elemento():
    """CA-LIS-06: una lista con un elemento no está vacía."""
    assert not lista_con(1).esta_vacia()


def test_esta_vacia_tras_quitar():
    """CA-LIS-06: quitar el único elemento deja la lista vacía."""
    lista = lista_con(1)
    lista.quitar_en(0)
    assert lista.esta_vacia()
