"""Pila enlazada: el último elemento que entra es el primero que sale."""


class PilaVaciaError(Exception):
    """Se lanza al pedir un elemento de una pila vacía."""


class Nodo:
    """Elemento de la pila con una referencia al nodo de abajo."""

    def __init__(self, valor, abajo=None):
        self.valor = valor
        self.abajo = abajo


class Pila:
    def __init__(self):
        self._cima = None
        self._tamano = 0

    def apilar(self, valor):
        """Pone un valor en la cima. O(1)."""
        self._cima = Nodo(valor, self._cima)
        self._tamano += 1

    def desapilar(self):
        """Quita y devuelve el valor de la cima. O(1)."""
        if self._cima is None:
            raise PilaVaciaError("la pila está vacía")
        valor = self._cima.valor
        self._cima = self._cima.abajo
        self._tamano -= 1
        return valor

    def cima(self):
        """Devuelve el valor de la cima sin quitarlo. O(1)."""
        if self._cima is None:
            raise PilaVaciaError("la pila está vacía")
        return self._cima.valor

    def esta_vacia(self):
        """Indica si la pila no tiene elementos. O(1)."""
        return self._cima is None

    def tamano(self):
        """Devuelve la cantidad de elementos. O(1)."""
        return self._tamano

    def vaciar(self):
        """Quita todos los elementos. O(1)."""
        self._cima = None
        self._tamano = 0
