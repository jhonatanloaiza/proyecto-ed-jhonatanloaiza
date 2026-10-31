"""Lista enlazada simple con referencias al primer y al último nodo."""


class Nodo:
    """Elemento de la lista con una referencia al que sigue."""

    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self._primero = None
        self._ultimo = None
        self._tamano = 0

    def agregar(self, valor):
        """Agrega un valor al final. O(1)."""
        nodo = Nodo(valor)
        if self._ultimo is None:
            self._primero = nodo
        else:
            self._ultimo.siguiente = nodo
        self._ultimo = nodo
        self._tamano += 1

    def insertar_en(self, posicion, valor):
        """Inserta un valor en una posición de 0 a tamano. O(n); O(1) al inicio o al final."""
        if posicion < 0 or posicion > self._tamano:
            raise IndexError("posición fuera de la lista")
        if posicion == self._tamano:
            self.agregar(valor)
        elif posicion == 0:
            self._primero = Nodo(valor, self._primero)
            self._tamano += 1
        else:
            anterior = self._nodo_en(posicion - 1)
            anterior.siguiente = Nodo(valor, anterior.siguiente)
            self._tamano += 1

    def quitar_en(self, posicion):
        """Quita y devuelve el valor de una posición. O(n); O(1) al inicio."""
        if posicion < 0 or posicion >= self._tamano:
            raise IndexError("posición fuera de la lista")
        if posicion == 0:
            nodo = self._primero
            self._primero = nodo.siguiente
            if self._primero is None:
                self._ultimo = None
        else:
            anterior = self._nodo_en(posicion - 1)
            nodo = anterior.siguiente
            anterior.siguiente = nodo.siguiente
            if nodo is self._ultimo:
                self._ultimo = anterior
        self._tamano -= 1
        return nodo.valor

    def buscar(self, condicion):
        """Devuelve (posicion, valor) del primero que cumple la condición, o None. O(n)."""
        posicion = 0
        for valor in self:
            if condicion(valor):
                return posicion, valor
            posicion += 1
        return None

    def esta_vacia(self):
        """Indica si la lista no tiene elementos. O(1)."""
        return self._tamano == 0

    def tamano(self):
        """Devuelve la cantidad de elementos. O(1)."""
        return self._tamano

    def __iter__(self):
        """Recorre los valores en orden. O(n)."""
        nodo = self._primero
        while nodo is not None:
            yield nodo.valor
            nodo = nodo.siguiente

    def _nodo_en(self, posicion):
        nodo = self._primero
        for _ in range(posicion):
            nodo = nodo.siguiente
        return nodo
