"""Tabla hash con encadenamiento para claves de texto."""

CARGA_MAXIMA = 0.75


class Nodo:
    """Par clave-valor dentro de la cadena de una cubeta."""

    def __init__(self, clave, valor, siguiente=None):
        self.clave = clave
        self.valor = valor
        self.siguiente = siguiente


class TablaHash:
    def __init__(self, capacidad=16):
        self._cubetas = [None] * capacidad  # arreglo de tamaño fijo
        self._tamano = 0

    def insertar(self, clave, valor):
        """Guarda un par o reemplaza el valor si la clave existe. O(1) amortizado; peor caso O(n)."""
        nodo = self._nodo(clave)
        if nodo is not None:
            nodo.valor = valor
            return
        if (self._tamano + 1) / len(self._cubetas) > CARGA_MAXIMA:
            self._crecer()
        indice = self._indice(clave)
        self._cubetas[indice] = Nodo(clave, valor, self._cubetas[indice])
        self._tamano += 1

    def buscar(self, clave):
        """Devuelve el valor de una clave, o None si no existe. O(1) promedio; peor caso O(n)."""
        nodo = self._nodo(clave)
        return None if nodo is None else nodo.valor

    def contiene(self, clave):
        """Indica si la clave existe. O(1) promedio; peor caso O(n)."""
        return self._nodo(clave) is not None

    def eliminar(self, clave):
        """Quita una clave; devuelve True si existía. O(1) promedio; peor caso O(n)."""
        indice = self._indice(clave)
        anterior = None
        nodo = self._cubetas[indice]
        while nodo is not None:
            if nodo.clave == clave:
                if anterior is None:
                    self._cubetas[indice] = nodo.siguiente
                else:
                    anterior.siguiente = nodo.siguiente
                self._tamano -= 1
                return True
            anterior = nodo
            nodo = nodo.siguiente
        return False

    def tamano(self):
        """Devuelve la cantidad de claves. O(1)."""
        return self._tamano

    def _indice(self, clave):
        dispersion = 0
        for caracter in clave:
            dispersion = dispersion * 31 + ord(caracter)
        return dispersion % len(self._cubetas)

    def _nodo(self, clave):
        nodo = self._cubetas[self._indice(clave)]
        while nodo is not None and nodo.clave != clave:
            nodo = nodo.siguiente
        return nodo

    def _crecer(self):
        anteriores = self._cubetas
        self._cubetas = [None] * (len(anteriores) * 2)
        for nodo in anteriores:
            while nodo is not None:
                siguiente = nodo.siguiente
                indice = self._indice(nodo.clave)
                nodo.siguiente = self._cubetas[indice]
                self._cubetas[indice] = nodo
                nodo = siguiente
