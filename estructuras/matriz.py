"""Matriz densa de tamaño fijo guardada en un solo arreglo."""


class FueraDeRangoError(IndexError):
    """Se lanza al acceder a una celda que no existe."""


class Matriz:
    def __init__(self, filas, columnas, inicial=None):
        """Crea la matriz con todas sus celdas en el valor inicial. O(filas × columnas)."""
        if filas <= 0 or columnas <= 0:
            raise ValueError("la matriz debe tener al menos una celda")
        self._filas = filas
        self._columnas = columnas
        self._celdas = [inicial] * (filas * columnas)  # arreglo de tamaño fijo

    def filas(self):
        """Devuelve la cantidad de filas. O(1)."""
        return self._filas

    def columnas(self):
        """Devuelve la cantidad de columnas. O(1)."""
        return self._columnas

    def dentro(self, fila, columna):
        """Indica si la celda existe. O(1)."""
        return 0 <= fila < self._filas and 0 <= columna < self._columnas

    def consultar(self, fila, columna):
        """Devuelve el valor de una celda. O(1)."""
        return self._celdas[self._posicion(fila, columna)]

    def asignar(self, fila, columna, valor):
        """Guarda un valor en una celda. O(1)."""
        self._celdas[self._posicion(fila, columna)] = valor

    def _posicion(self, fila, columna):
        if not self.dentro(fila, columna):
            raise FueraDeRangoError(f"celda ({fila}, {columna}) fuera de la matriz")
        return fila * self._columnas + columna
