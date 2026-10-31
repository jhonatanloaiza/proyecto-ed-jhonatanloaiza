"""Historial de acciones del jugador con deshacer y rehacer."""

from estructuras.pila import Pila


class Historial:
    def __init__(self):
        self._hechas = Pila()
        self._deshechas = Pila()

    def registrar(self, accion):
        """Guarda una acción ya aplicada y descarta lo que se podía rehacer. O(1)."""
        self._hechas.apilar(accion)
        self._deshechas.vaciar()

    def deshacer(self, partida):
        """Revierte la acción más reciente y la devuelve, o None si no hay. O(1) + costo de la acción."""
        if self._hechas.esta_vacia():
            return None
        accion = self._hechas.desapilar()
        accion.revertir(partida)
        self._deshechas.apilar(accion)
        return accion

    def rehacer(self, partida):
        """Aplica de nuevo la última acción deshecha y la devuelve, o None si no hay. O(1) + costo de la acción."""
        if self._deshechas.esta_vacia():
            return None
        accion = self._deshechas.desapilar()
        accion.hacer(partida)
        self._hechas.apilar(accion)
        return accion

    def puede_deshacer(self):
        """Indica si hay acciones para deshacer. O(1)."""
        return not self._hechas.esta_vacia()

    def puede_rehacer(self):
        """Indica si hay acciones para rehacer. O(1)."""
        return not self._deshechas.esta_vacia()
