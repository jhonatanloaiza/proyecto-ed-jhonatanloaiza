"""Entidades del juego: el Cubo, los enemigos y los objetos."""

from dataclasses import dataclass

CUBO = "Cubo Geométrico"
RASTREADOR = "Pájaro Rastreador"
CENTINELA = "Pájaro Centinela"
CAZADOR = "Pájaro Cazador"
ORBE = "Orbe de energía"
LLAVE = "Llave geométrica"


@dataclass(eq=False)
class Entidad:
    """Algo que ocupa una celda. Un objeto en el inventario tiene celda None."""

    id: str
    tipo: str
    celda: tuple | None
    puntos: int = 0
    desde_turno: int = 0  # un enemigo se mueve solo a partir de este turno
