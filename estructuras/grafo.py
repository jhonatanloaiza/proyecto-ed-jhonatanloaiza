"""Grafo implícito sobre una rejilla, con búsqueda en anchura (BFS) y A*."""

from dataclasses import dataclass

from estructuras.cola import Cola
from estructuras.lista_enlazada import ListaEnlazada
from estructuras.matriz import Matriz
from estructuras.monticulo import MonticuloMinimo
from estructuras.pila import Pila

DIRECCIONES = ((-1, 0), (1, 0), (0, -1), (0, 1))  # arriba, abajo, izquierda, derecha


@dataclass
class Busqueda:
    """Resultado de una búsqueda: el camino y cuántas celdas se exploraron."""

    camino: ListaEnlazada
    explorados: int


def manhattan(a, b):
    """Distancia Manhattan entre dos celdas: heurística admisible para 4 direcciones. O(1)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class GrafoRejilla:
    def __init__(self, filas, columnas, transitable):
        self._filas = filas
        self._columnas = columnas
        self._transitable = transitable

    def vecinos(self, celda):
        """Devuelve las celdas transitables contiguas. O(1)."""
        fila, columna = celda
        resultado = ListaEnlazada()
        for delta_fila, delta_columna in DIRECCIONES:
            nueva_fila = fila + delta_fila
            nueva_columna = columna + delta_columna
            if (0 <= nueva_fila < self._filas and 0 <= nueva_columna < self._columnas
                    and self._transitable(nueva_fila, nueva_columna)):
                resultado.agregar((nueva_fila, nueva_columna))
        return resultado

    def bfs(self, origen, destino):
        """Busca el camino de menos pasos de origen a destino. O(V + E)."""
        previos = Matriz(self._filas, self._columnas)
        previos.asignar(*origen, origen)
        frontera = Cola()
        frontera.encolar(origen)
        explorados = 0
        while not frontera.esta_vacia():
            celda = frontera.desencolar()
            explorados += 1
            if celda == destino:
                return Busqueda(self._reconstruir(previos, origen, destino), explorados)
            for vecino in self.vecinos(celda):
                if previos.consultar(*vecino) is None:
                    previos.asignar(*vecino, celda)
                    frontera.encolar(vecino)
        return Busqueda(ListaEnlazada(), explorados)

    def a_estrella(self, origen, destino):
        """Busca el camino de menos pasos guiado por la distancia Manhattan. O(E log V)."""
        costos = Matriz(self._filas, self._columnas)
        previos = Matriz(self._filas, self._columnas)
        cerradas = Matriz(self._filas, self._columnas, False)
        costos.asignar(*origen, 0)
        previos.asignar(*origen, origen)
        abiertas = MonticuloMinimo()
        estimado = manhattan(origen, destino)
        abiertas.insertar((estimado, estimado), origen)
        explorados = 0
        while not abiertas.esta_vacia():
            celda = abiertas.extraer_minimo()
            if cerradas.consultar(*celda):
                continue  # entrada vieja: la celda ya se cerró con un costo menor
            cerradas.asignar(*celda, True)
            explorados += 1
            if celda == destino:
                return Busqueda(self._reconstruir(previos, origen, destino), explorados)
            costo_vecino = costos.consultar(*celda) + 1
            for vecino in self.vecinos(celda):
                anterior = costos.consultar(*vecino)
                if not cerradas.consultar(*vecino) and (anterior is None or costo_vecino < anterior):
                    costos.asignar(*vecino, costo_vecino)
                    previos.asignar(*vecino, celda)
                    restante = manhattan(vecino, destino)
                    abiertas.insertar((costo_vecino + restante, restante), vecino)
        return Busqueda(ListaEnlazada(), explorados)

    def siguiente_paso(self, origen, destino, guiado=False):
        """Devuelve la primera celda del camino (de A* si guiado), o None si no hay camino o ya llegó."""
        busqueda = self.a_estrella(origen, destino) if guiado else self.bfs(origen, destino)
        camino = busqueda.camino
        if camino.tamano() < 2:
            return None
        pasos = iter(camino)
        next(pasos)
        return next(pasos)

    def _reconstruir(self, previos, origen, destino):
        pila = Pila()
        celda = destino
        while celda != origen:
            pila.apilar(celda)
            celda = previos.consultar(*celda)
        camino = ListaEnlazada()
        camino.agregar(origen)
        while not pila.esta_vacia():
            camino.agregar(pila.desapilar())
        return camino
