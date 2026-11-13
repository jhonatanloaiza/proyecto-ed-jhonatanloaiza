"""Montículo binario mínimo sobre un arreglo."""


class MonticuloVacioError(Exception):
    """Se lanza al pedir el mínimo de un montículo vacío."""


class MonticuloMinimo:
    def __init__(self):
        self._datos = []  # arreglo de soporte: (prioridad, llegada, valor)
        self._llegadas = 0

    def insertar(self, prioridad, valor):
        """Agrega un valor con su prioridad. O(log n)."""
        self._datos.append((prioridad, self._llegadas, valor))
        self._llegadas += 1
        self._subir(len(self._datos) - 1)

    def extraer_minimo(self):
        """Quita y devuelve el valor de menor prioridad. O(log n)."""
        if not self._datos:
            raise MonticuloVacioError("el montículo está vacío")
        ultimo = len(self._datos) - 1
        self._intercambiar(0, ultimo)
        _, _, valor = self._datos.pop()
        self._bajar(0)
        return valor

    def minimo(self):
        """Devuelve el valor de menor prioridad sin quitarlo. O(1)."""
        if not self._datos:
            raise MonticuloVacioError("el montículo está vacío")
        return self._datos[0][2]

    def tamano(self):
        """Devuelve la cantidad de elementos. O(1)."""
        return len(self._datos)

    def esta_vacia(self):
        """Indica si el montículo no tiene elementos. O(1)."""
        return not self._datos

    def _menor(self, i, j):
        return self._datos[i][:2] < self._datos[j][:2]

    def _intercambiar(self, i, j):
        self._datos[i], self._datos[j] = self._datos[j], self._datos[i]

    def _subir(self, i):
        while i > 0:
            padre = (i - 1) // 2
            if not self._menor(i, padre):
                return
            self._intercambiar(i, padre)
            i = padre

    def _bajar(self, i):
        n = len(self._datos)
        while True:
            menor = i
            for hijo in (2 * i + 1, 2 * i + 2):
                if hijo < n and self._menor(hijo, menor):
                    menor = hijo
            if menor == i:
                return
            self._intercambiar(i, menor)
            i = menor
