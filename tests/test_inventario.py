"""Pruebas del Inventario (componente 03)."""

from dominio.entidades import LLAVE, ORBE, Entidad
from dominio.inventario import Inventario


def inventario_con(*identificadores):
    inventario = Inventario()
    for identificador in identificadores:
        inventario.agregar(Entidad(identificador, ORBE, None, 10))
    return inventario


def ids(inventario):
    return [objeto.id for objeto in inventario]


def test_agregar_en_orden_de_recogida():
    """CA-INV-01: el recorrido entrega los objetos en orden de recogida."""
    assert ids(inventario_con("O1", "K1", "O2")) == ["O1", "K1", "O2"]


def test_recorrido_vacio():
    """CA-INV-01: un inventario nuevo no tiene objetos."""
    assert ids(Inventario()) == []


def test_agregar_llave():
    """CA-INV-01: las llaves se guardan igual que los orbes."""
    inventario = Inventario()
    inventario.agregar(Entidad("K1", LLAVE, None))
    assert ids(inventario) == ["K1"]


def test_buscar_existente():
    """CA-INV-01: buscar encuentra un objeto recogido."""
    assert inventario_con("O1", "O2").buscar("O2").id == "O2"


def test_buscar_inexistente():
    """CA-INV-02: buscar un id inexistente devuelve None."""
    assert inventario_con("O1").buscar("O9") is None


def test_buscar_en_vacio():
    """CA-INV-02: buscar en un inventario vacío devuelve None."""
    assert Inventario().buscar("O1") is None


def test_quitar_devuelve_objeto_y_posicion():
    """CA-INV-03: quitar devuelve el objeto y su posición."""
    objeto, posicion = inventario_con("O1", "O2").quitar("O2")
    assert objeto.id == "O2" and posicion == 1


def test_quitar_inexistente():
    """CA-INV-02: quitar un id inexistente devuelve None y no cambia el inventario."""
    inventario = inventario_con("O1")
    assert inventario.quitar("O9") is None and ids(inventario) == ["O1"]


def test_quitar_en_vacio():
    """CA-INV-02: quitar de un inventario vacío devuelve None."""
    assert Inventario().quitar("O1") is None


def test_insertar_en_devuelve_a_su_posicion():
    """CA-INV-03: quitar y reinsertar deja el inventario como estaba."""
    inventario = inventario_con("O1", "O2", "O3")
    objeto, posicion = inventario.quitar("O2")
    inventario.insertar_en(posicion, objeto)
    assert ids(inventario) == ["O1", "O2", "O3"]


def test_insertar_en_primera_posicion():
    """CA-INV-03: se puede reinsertar en la primera posición."""
    inventario = inventario_con("O1", "O2")
    objeto, posicion = inventario.quitar("O1")
    inventario.insertar_en(posicion, objeto)
    assert ids(inventario) == ["O1", "O2"]


def test_insertar_en_inventario_vacio():
    """CA-INV-03: se puede reinsertar el único objeto."""
    inventario = inventario_con("O1")
    objeto, posicion = inventario.quitar("O1")
    inventario.insertar_en(posicion, objeto)
    assert ids(inventario) == ["O1"]


def test_tamano_vacio():
    """CA-INV-02: un inventario vacío tiene tamaño 0."""
    assert Inventario().tamano() == 0


def test_tamano_con_objetos():
    """CA-INV-01: el tamaño cuenta los objetos."""
    assert inventario_con("O1", "O2").tamano() == 2


def test_tamano_tras_quitar():
    """CA-INV-03: el tamaño baja al quitar."""
    inventario = inventario_con("O1")
    inventario.quitar("O1")
    assert inventario.tamano() == 0
