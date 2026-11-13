"""Tabla de mejores puntajes sobre un árbol AVL."""

from dataclasses import dataclass

from estructuras.avl import ArbolAVL


@dataclass
class Registro:
    numero: int
    puntaje: int
    resultado: str
    turnos: int
    nivel: str


class TablaPuntajes:
    def __init__(self):
        self._arbol = ArbolAVL()
        self._partidas = 0

    def registrar(self, puntaje, resultado, turnos, nivel=""):
        """Guarda el puntaje de una partida terminada. O(log n)."""
        self._partidas += 1
        registro = Registro(self._partidas, puntaje, resultado, turnos, nivel)
        # A igual puntaje, la partida más antigua (número menor) queda primero en el ranking.
        self._arbol.insertar((puntaje, -self._partidas), registro)

    def ranking(self):
        """Devuelve los registros de mayor a menor puntaje. O(n)."""
        return self._arbol.descendente()

    def tamano(self):
        """Devuelve la cantidad de partidas registradas. O(1)."""
        return self._arbol.tamano()
