"""Lista circular simple: el último nodo apunta al primero."""


class ListaVaciaError(Exception):
    """Se lanza al pedir el siguiente de una lista vacía."""


class Nodo:
    """Elemento del ciclo con una referencia al que sigue."""

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = self


class ListaCircular:
    def __init__(self):
        self._ultimo = None
        self._actual = None
        self._tamano = 0

    def insertar(self, valor):
        """Agrega un valor al final del ciclo. O(1)."""
        nodo = Nodo(valor)
        if self._ultimo is None:
            self._actual = nodo
        else:
            nodo.siguiente = self._ultimo.siguiente
            self._ultimo.siguiente = nodo
        self._ultimo = nodo
        self._tamano += 1

    def siguiente(self):
        """Devuelve el valor al que le toca el turno y avanza el ciclo. O(1)."""
        if self._actual is None:
            raise ListaVaciaError("la lista está vacía")
        valor = self._actual.valor
        self._actual = self._actual.siguiente
        return valor

    def quitar(self, valor):
        """Saca un valor del ciclo; devuelve True si estaba. O(n)."""
        if self._ultimo is None:
            return False
        anterior = self._ultimo
        for _ in range(self._tamano):
            nodo = anterior.siguiente
            if nodo.valor == valor:
                self._desenlazar(anterior, nodo)
                return True
            anterior = nodo
        return False

    def esta_vacia(self):
        """Indica si la lista no tiene elementos. O(1)."""
        return self._tamano == 0

    def tamano(self):
        """Devuelve la cantidad de elementos. O(1)."""
        return self._tamano

    def __iter__(self):
        """Recorre el ciclo una vuelta desde el primero, sin mover el turno. O(n)."""
        if self._ultimo is None:
            return
        nodo = self._ultimo.siguiente
        for _ in range(self._tamano):
            yield nodo.valor
            nodo = nodo.siguiente

    def _desenlazar(self, anterior, nodo):
        self._tamano -= 1
        if self._tamano == 0:
            self._ultimo = None
            self._actual = None
            return
        anterior.siguiente = nodo.siguiente
        if nodo is self._ultimo:
            self._ultimo = anterior
        if nodo is self._actual:
            self._actual = nodo.siguiente
