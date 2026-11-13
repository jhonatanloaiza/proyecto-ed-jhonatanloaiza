"""Árbol AVL: árbol binario de búsqueda que se mantiene balanceado con rotaciones."""

from estructuras.lista_enlazada import ListaEnlazada
from estructuras.pila import Pila


class ArbolVacioError(Exception):
    """Se lanza al pedir el máximo de un árbol vacío."""


class Nodo:
    """Clave, valor, hijos y altura del subárbol que empieza en este nodo."""

    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1


def _altura(nodo):
    return 0 if nodo is None else nodo.altura


def _actualizar(nodo):
    nodo.altura = 1 + max(_altura(nodo.izquierdo), _altura(nodo.derecho))


def _rotar_derecha(nodo):
    nueva_raiz = nodo.izquierdo
    nodo.izquierdo = nueva_raiz.derecho
    nueva_raiz.derecho = nodo
    _actualizar(nodo)
    _actualizar(nueva_raiz)
    return nueva_raiz


def _rotar_izquierda(nodo):
    nueva_raiz = nodo.derecho
    nodo.derecho = nueva_raiz.izquierdo
    nueva_raiz.izquierdo = nodo
    _actualizar(nodo)
    _actualizar(nueva_raiz)
    return nueva_raiz


def _balancear(nodo):
    _actualizar(nodo)
    balance = _altura(nodo.izquierdo) - _altura(nodo.derecho)
    if balance > 1:
        if _altura(nodo.izquierdo.izquierdo) < _altura(nodo.izquierdo.derecho):
            nodo.izquierdo = _rotar_izquierda(nodo.izquierdo)  # caso izquierda-derecha
        return _rotar_derecha(nodo)
    if balance < -1:
        if _altura(nodo.derecho.derecho) < _altura(nodo.derecho.izquierdo):
            nodo.derecho = _rotar_derecha(nodo.derecho)  # caso derecha-izquierda
        return _rotar_izquierda(nodo)
    return nodo


class ArbolAVL:
    def __init__(self):
        self._raiz = None
        self._tamano = 0

    def insertar(self, clave, valor):
        """Guarda un par o reemplaza el valor si la clave existe. O(log n)."""
        self._raiz = self._insertar(self._raiz, clave, valor)

    def maximo(self):
        """Devuelve el valor de la clave mayor. O(log n)."""
        if self._raiz is None:
            raise ArbolVacioError("el árbol está vacío")
        nodo = self._raiz
        while nodo.derecho is not None:
            nodo = nodo.derecho
        return nodo.valor

    def descendente(self):
        """Devuelve los valores de mayor a menor clave. O(n)."""
        resultado = ListaEnlazada()
        pendientes = Pila()
        nodo = self._raiz
        while nodo is not None or not pendientes.esta_vacia():
            while nodo is not None:
                pendientes.apilar(nodo)
                nodo = nodo.derecho
            nodo = pendientes.desapilar()
            resultado.agregar(nodo.valor)
            nodo = nodo.izquierdo
        return resultado

    def altura(self):
        """Devuelve la altura del árbol; 0 si está vacío. O(1)."""
        return _altura(self._raiz)

    def tamano(self):
        """Devuelve la cantidad de claves. O(1)."""
        return self._tamano

    def esta_vacia(self):
        """Indica si el árbol no tiene claves. O(1)."""
        return self._raiz is None

    def _insertar(self, nodo, clave, valor):
        if nodo is None:
            self._tamano += 1
            return Nodo(clave, valor)
        if clave < nodo.clave:
            nodo.izquierdo = self._insertar(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self._insertar(nodo.derecho, clave, valor)
        else:
            nodo.valor = valor
            return nodo
        return _balancear(nodo)
