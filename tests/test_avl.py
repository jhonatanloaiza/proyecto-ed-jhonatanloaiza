"""Pruebas del ArbolAVL (componente 08)."""

import math

import pytest

from estructuras.avl import ArbolAVL, ArbolVacioError


def arbol_con(*claves):
    arbol = ArbolAVL()
    for clave in claves:
        arbol.insertar(clave, f"v{clave}")
    return arbol


def claves(arbol):
    return [int(valor[1:]) for valor in arbol.descendente()]


def esta_balanceado(nodo):
    """Devuelve la altura si el subárbol es AVL y ordenado; -1 si no."""
    if nodo is None:
        return 0
    izquierda, derecha = esta_balanceado(nodo.izquierdo), esta_balanceado(nodo.derecho)
    if izquierda < 0 or derecha < 0 or abs(izquierda - derecha) > 1:
        return -1
    if nodo.izquierdo and nodo.izquierdo.clave >= nodo.clave:
        return -1
    if nodo.derecho and nodo.derecho.clave <= nodo.clave:
        return -1
    return 1 + max(izquierda, derecha)


def test_insertar_desordenado_queda_ordenado():
    """CA-AVL-01: descendente ordena de mayor a menor sin importar el orden de inserción."""
    assert claves(arbol_con(5, 1, 9, 3, 7)) == [9, 7, 5, 3, 1]


def test_insertar_un_elemento():
    """CA-AVL-01: con una clave, descendente devuelve solo su valor."""
    assert list(arbol_con(4).descendente()) == ["v4"]


@pytest.mark.parametrize("orden", [range(1, 512), range(511, 0, -1)])
def test_insertar_ordenado_mantiene_altura_logaritmica(orden):
    """CA-AVL-02: insertar en orden creciente o decreciente mantiene la altura en O(log n)."""
    arbol = arbol_con(*orden)
    assert arbol.altura() <= 1.45 * math.log2(arbol.tamano() + 2)


@pytest.mark.parametrize("secuencia", [(3, 2, 1), (1, 2, 3), (3, 1, 2), (1, 3, 2)])
def test_rotaciones_dejan_el_arbol_balanceado(secuencia):
    """CA-AVL-03: los casos izquierda-izquierda, derecha-derecha, izquierda-derecha y derecha-izquierda quedan balanceados."""
    arbol = arbol_con(*secuencia)
    assert arbol.altura() == 2 and arbol._raiz.clave == 2
    assert esta_balanceado(arbol._raiz) == 2


def test_rotaciones_en_arbol_grande():
    """CA-AVL-03: tras muchas inserciones el árbol sigue ordenado y balanceado."""
    arbol = arbol_con(*[(i * 37) % 101 for i in range(101)])
    assert esta_balanceado(arbol._raiz) == arbol.altura()


def test_insertar_clave_existente_reemplaza():
    """CA-AVL-04: insertar una clave existente reemplaza el valor sin aumentar el tamaño."""
    arbol = arbol_con(1, 2)
    arbol.insertar(2, "nuevo")
    assert arbol.tamano() == 2 and list(arbol.descendente()) == ["nuevo", "v1"]


def test_insertar_clave_existente_en_arbol_de_uno():
    """CA-AVL-04: reemplazar en un árbol de una clave mantiene el tamaño en 1."""
    arbol = arbol_con(1)
    arbol.insertar(1, "otro")
    assert arbol.tamano() == 1 and arbol.maximo() == "otro"


def test_insertar_claves_compuestas():
    """CA-AVL-04: claves como (puntaje, -partida) se ordenan por ambos valores."""
    arbol = ArbolAVL()
    arbol.insertar((10, -1), "a")
    arbol.insertar((10, -2), "b")
    arbol.insertar((20, -3), "c")
    assert list(arbol.descendente()) == ["c", "a", "b"]


def test_maximo():
    """CA-AVL-05: maximo devuelve el valor de la clave mayor."""
    assert arbol_con(3, 8, 1).maximo() == "v8"


def test_maximo_un_elemento():
    """CA-AVL-05: con una clave, maximo devuelve su valor."""
    assert arbol_con(5).maximo() == "v5"


def test_maximo_vacio_lanza_error():
    """CA-AVL-05: maximo en un árbol vacío lanza ArbolVacioError."""
    with pytest.raises(ArbolVacioError):
        ArbolAVL().maximo()


def test_descendente_vacio():
    """CA-AVL-06: descendente de un árbol vacío está vacío."""
    assert ArbolAVL().descendente().esta_vacia()


def test_altura_vacio():
    """CA-AVL-06: un árbol vacío tiene altura 0."""
    assert ArbolAVL().altura() == 0


def test_altura_un_elemento():
    """CA-AVL-06: un árbol de una clave tiene altura 1."""
    assert arbol_con(1).altura() == 1


def test_altura_tres_elementos():
    """CA-AVL-03: tres claves balanceadas dan altura 2."""
    assert arbol_con(2, 1, 3).altura() == 2


def test_tamano_vacio():
    """CA-AVL-06: un árbol vacío tiene tamaño 0."""
    assert ArbolAVL().tamano() == 0


def test_tamano_varios():
    """CA-AVL-04: el tamaño cuenta las claves distintas."""
    assert arbol_con(1, 2, 2, 3).tamano() == 3


def test_tamano_un_elemento():
    """CA-AVL-06: con una clave el tamaño es 1."""
    assert arbol_con(1).tamano() == 1


def test_esta_vacia_nuevo():
    """CA-AVL-06: un árbol nuevo está vacío."""
    assert ArbolAVL().esta_vacia()


def test_esta_vacia_con_elemento():
    """CA-AVL-06: un árbol con una clave no está vacío."""
    assert not arbol_con(1).esta_vacia()


def test_esta_vacia_tras_reemplazar():
    """CA-AVL-04: reemplazar un valor no vacía el árbol."""
    arbol = arbol_con(1)
    arbol.insertar(1, "x")
    assert not arbol.esta_vacia()
