"""Mapa del juego: terreno y objetos sobre dos matrices del mismo tamaño."""

from estructuras.grafo import DIRECCIONES
from estructuras.matriz import Matriz

LIBRE = "."
PICO = "^"
COMPUERTA = "#"
PORTAL = "@"


class Mapa:
    def __init__(self, filas, columnas):
        self._terreno = Matriz(filas, columnas, LIBRE)
        self._objetos = Matriz(filas, columnas)

    def filas(self):
        """Devuelve la cantidad de filas. O(1)."""
        return self._terreno.filas()

    def columnas(self):
        """Devuelve la cantidad de columnas. O(1)."""
        return self._terreno.columnas()

    def dentro(self, celda):
        """Indica si la celda existe. O(1)."""
        return self._terreno.dentro(*celda)

    def terreno_en(self, celda):
        """Devuelve el terreno de una celda. O(1)."""
        return self._terreno.consultar(*celda)

    def poner_terreno(self, celda, terreno):
        """Cambia el terreno de una celda. O(1)."""
        self._terreno.asignar(*celda, terreno)

    def es_transitable(self, fila, columna):
        """Indica si se puede pasar: los picos y las compuertas cerradas bloquean. O(1)."""
        return self._terreno.consultar(fila, columna) not in (PICO, COMPUERTA)

    def objeto_en(self, celda):
        """Devuelve el objeto de una celda, o None. O(1)."""
        return self._objetos.consultar(*celda)

    def poner_objeto(self, celda, objeto):
        """Coloca un objeto en una celda. O(1)."""
        self._objetos.asignar(*celda, objeto)

    def quitar_objeto(self, celda):
        """Deja la celda sin objeto. O(1)."""
        self._objetos.asignar(*celda, None)

    def compuerta_vecina(self, celda):
        """Devuelve una compuerta cerrada contigua a la celda, o None. O(1)."""
        for delta_fila, delta_columna in DIRECCIONES:
            vecina = (celda[0] + delta_fila, celda[1] + delta_columna)
            if self.dentro(vecina) and self.terreno_en(vecina) == COMPUERTA:
                return vecina
        return None

    def proporcion_picos(self):
        """Devuelve la fracción de celdas con picos. O(filas × columnas)."""
        picos = 0
        for fila in range(self.filas()):
            for columna in range(self.columnas()):
                if self._terreno.consultar(fila, columna) == PICO:
                    picos += 1
        return picos / (self.filas() * self.columnas())
