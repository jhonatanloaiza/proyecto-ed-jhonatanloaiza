"""Acciones reversibles: un turno es una Accion compuesta de cambios pequeños."""

from dominio.mapa import COMPUERTA, LIBRE
from estructuras.lista_enlazada import ListaEnlazada
from estructuras.pila import Pila


class MoverEntidad:
    def __init__(self, entidad, desde, hasta):
        self._entidad = entidad
        self._desde = desde
        self._hasta = hasta

    def hacer(self, partida):
        self._entidad.celda = self._hasta

    def revertir(self, partida):
        self._entidad.celda = self._desde


class SumarTurno:
    def hacer(self, partida):
        partida.turno += 1

    def revertir(self, partida):
        partida.turno -= 1


class SumarPuntos:
    def __init__(self, puntos):
        self._puntos = puntos

    def hacer(self, partida):
        partida.puntaje += self._puntos

    def revertir(self, partida):
        partida.puntaje -= self._puntos


class CambiarEstado:
    def __init__(self, antes, despues):
        self._antes = antes
        self._despues = despues

    def hacer(self, partida):
        partida.estado = self._despues

    def revertir(self, partida):
        partida.estado = self._antes


class Recoger:
    def __init__(self, objeto, celda):
        self._objeto = objeto
        self._celda = celda

    def hacer(self, partida):
        partida.mapa.quitar_objeto(self._celda)
        self._objeto.celda = None
        partida.inventario.agregar(self._objeto)

    def revertir(self, partida):
        partida.inventario.quitar(self._objeto.id)
        self._objeto.celda = self._celda
        partida.mapa.poner_objeto(self._celda, self._objeto)


class Soltar:
    def __init__(self, objeto, celda):
        self._objeto = objeto
        self._celda = celda
        self._posicion = None

    def hacer(self, partida):
        _, self._posicion = partida.inventario.quitar(self._objeto.id)
        self._objeto.celda = self._celda
        partida.mapa.poner_objeto(self._celda, self._objeto)

    def revertir(self, partida):
        partida.mapa.quitar_objeto(self._celda)
        self._objeto.celda = None
        partida.inventario.insertar_en(self._posicion, self._objeto)


class ConsumirLlave:
    def __init__(self, llave):
        self._llave = llave
        self._posicion = None

    def hacer(self, partida):
        _, self._posicion = partida.inventario.quitar(self._llave.id)

    def revertir(self, partida):
        partida.inventario.insertar_en(self._posicion, self._llave)


class AbrirCompuerta:
    def __init__(self, celda):
        self._celda = celda

    def hacer(self, partida):
        partida.mapa.poner_terreno(self._celda, LIBRE)

    def revertir(self, partida):
        partida.mapa.poner_terreno(self._celda, COMPUERTA)


class Accion:
    """Todos los cambios de un turno, en el orden en que ocurrieron."""

    def __init__(self):
        self._cambios = ListaEnlazada()

    def ejecutar(self, cambio, partida):
        """Aplica un cambio y lo guarda. O(1) más el costo del cambio."""
        cambio.hacer(partida)
        self._cambios.agregar(cambio)

    def hacer(self, partida):
        """Aplica de nuevo todos los cambios en orden. O(k) para k cambios."""
        for cambio in self._cambios:
            cambio.hacer(partida)

    def revertir(self, partida):
        """Revierte los cambios del último al primero. O(k) para k cambios."""
        pendientes = Pila()
        for cambio in self._cambios:
            pendientes.apilar(cambio)
        while not pendientes.esta_vacia():
            pendientes.desapilar().revertir(partida)
