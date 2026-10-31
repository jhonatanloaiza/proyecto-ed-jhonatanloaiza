"""Eventos que ocurren durante un turno."""

from dataclasses import dataclass

APARICION = "aparición"
RECOLECCION = "recolección"
COLISION = "colisión"


@dataclass
class Evento:
    tipo: str
    turno: int
    celda: tuple
    detalle: str

    def texto(self):
        """Devuelve la línea que se muestra en la consola. O(1)."""
        return f"[T{self.turno}] {self.detalle} en {self.celda}"
