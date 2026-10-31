"""Cola enlazada: el primer elemento que entra es el primero que sale."""


class ColaVaciaError(Exception):
    """Se lanza al pedir un elemento de una cola vacía."""


class Nodo:
    """Elemento de la cola con una referencia al que sigue."""

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class Cola:
    def __init__(self):
        self._frente = None
        self._final = None
        self._tamano = 0

    def encolar(self, valor):
        """Agrega un valor al final. O(1)."""
        nodo = Nodo(valor)
        if self._final is None:
            self._frente = nodo
        else:
            self._final.siguiente = nodo
        self._final = nodo
        self._tamano += 1

    def desencolar(self):
        """Quita y devuelve el valor del frente. O(1)."""
        if self._frente is None:
            raise ColaVaciaError("la cola está vacía")
        valor = self._frente.valor
        self._frente = self._frente.siguiente
        if self._frente is None:
            self._final = None
        self._tamano -= 1
        return valor

    def frente(self):
        """Devuelve el valor del frente sin quitarlo. O(1)."""
        if self._frente is None:
            raise ColaVaciaError("la cola está vacía")
        return self._frente.valor

    def esta_vacia(self):
        """Indica si la cola no tiene elementos. O(1)."""
        return self._frente is None

    def tamano(self):
        """Devuelve la cantidad de elementos. O(1)."""
        return self._tamano
