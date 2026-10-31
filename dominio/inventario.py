"""Inventario del Cubo: objetos en orden de recogida."""

from estructuras.lista_enlazada import ListaEnlazada


class Inventario:
    def __init__(self):
        self._objetos = ListaEnlazada()

    def agregar(self, objeto):
        """Agrega un objeto al final. O(1)."""
        self._objetos.agregar(objeto)

    def buscar(self, identificador):
        """Devuelve el objeto con ese id, o None. O(n)."""
        encontrado = self._objetos.buscar(lambda objeto: objeto.id == identificador)
        return None if encontrado is None else encontrado[1]

    def quitar(self, identificador):
        """Quita un objeto y devuelve (objeto, posicion), o None si no está. O(n)."""
        encontrado = self._objetos.buscar(lambda objeto: objeto.id == identificador)
        if encontrado is None:
            return None
        posicion, objeto = encontrado
        self._objetos.quitar_en(posicion)
        return objeto, posicion

    def insertar_en(self, posicion, objeto):
        """Devuelve un objeto a su posición. O(n)."""
        self._objetos.insertar_en(posicion, objeto)

    def tamano(self):
        """Devuelve la cantidad de objetos. O(1)."""
        return self._objetos.tamano()

    def __iter__(self):
        """Recorre los objetos en orden de recogida. O(n)."""
        return iter(self._objetos)
