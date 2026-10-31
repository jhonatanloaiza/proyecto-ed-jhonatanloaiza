"""Pruebas de la TablaHash (componente 06)."""

from estructuras.tabla_hash import TablaHash


def tabla_con(*claves, capacidad=16):
    tabla = TablaHash(capacidad)
    for clave in claves:
        tabla.insertar(clave, clave.lower())
    return tabla


def test_insertar_y_buscar():
    """CA-HAS-01: después de insertar, buscar devuelve el valor."""
    assert tabla_con("R1").buscar("R1") == "r1"


def test_insertar_varias_claves():
    """CA-HAS-01: cada clave conserva su propio valor."""
    tabla = tabla_con("R1", "R2", "O1")
    assert tabla.buscar("R2") == "r2" and tabla.buscar("O1") == "o1"


def test_insertar_clave_existente_reemplaza():
    """CA-HAS-02: insertar una clave existente reemplaza el valor sin aumentar el tamaño."""
    tabla = tabla_con("R1")
    tabla.insertar("R1", "nuevo")
    assert tabla.buscar("R1") == "nuevo" and tabla.tamano() == 1


def test_buscar_inexistente():
    """CA-HAS-03: buscar una clave inexistente devuelve None."""
    assert tabla_con("R1").buscar("R9") is None


def test_buscar_en_tabla_vacia():
    """CA-HAS-03: buscar en una tabla vacía devuelve None."""
    assert TablaHash().buscar("R1") is None


def test_buscar_con_colision():
    """CA-HAS-04: las claves que chocan en la misma cubeta se encuentran."""
    tabla = tabla_con("A", "Q", capacidad=16)
    assert tabla.buscar("A") == "a" and tabla.buscar("Q") == "q"


def test_eliminar_existente():
    """CA-HAS-06: eliminar una clave existente devuelve True y baja el tamaño."""
    tabla = tabla_con("R1", "R2")
    assert tabla.eliminar("R1") and tabla.tamano() == 1


def test_eliminar_inexistente():
    """CA-HAS-03: eliminar una clave inexistente devuelve False y no cambia la tabla."""
    tabla = tabla_con("R1")
    assert not tabla.eliminar("R9") and tabla.tamano() == 1


def test_eliminar_en_tabla_vacia():
    """CA-HAS-03: eliminar en una tabla vacía devuelve False."""
    assert not TablaHash().eliminar("R1")


def test_colisiones_se_eliminan_por_separado():
    """CA-HAS-04: en una cadena, eliminar una clave conserva las demás."""
    tabla = tabla_con("A", "Q", capacidad=16)  # ord("A") y ord("Q") chocan en 16 cubetas
    assert tabla._indice("A") == tabla._indice("Q")
    assert tabla.eliminar("A") and tabla.buscar("Q") == "q" and tabla.buscar("A") is None


def test_colisiones_eliminar_la_mas_antigua():
    """CA-HAS-04: se puede eliminar el nodo que no está al inicio de la cadena."""
    tabla = tabla_con("A", "Q", capacidad=16)
    assert tabla.eliminar("Q") and tabla.buscar("A") == "a"


def test_crecer_conserva_las_claves():
    """CA-HAS-05: al superar la capacidad inicial, todas las claves se encuentran."""
    claves = [f"E{i}" for i in range(50)]
    tabla = tabla_con(*claves, capacidad=2)
    assert all(tabla.buscar(clave) == clave.lower() for clave in claves)


def test_crecer_aumenta_las_cubetas():
    """CA-HAS-05: la capacidad crece cuando la carga supera 0,75."""
    tabla = tabla_con("A", "B", "C", "D", capacidad=2)
    assert len(tabla._cubetas) > 2 and tabla.tamano() == 4


def test_contiene_existente():
    """CA-HAS-06: contiene es True para una clave insertada."""
    assert tabla_con("R1").contiene("R1")


def test_contiene_inexistente():
    """CA-HAS-06: contiene es False para una clave que no está."""
    assert not tabla_con("R1").contiene("R2")


def test_contiene_tras_eliminar():
    """CA-HAS-06: contiene es False después de eliminar la clave."""
    tabla = tabla_con("R1")
    tabla.eliminar("R1")
    assert not tabla.contiene("R1")


def test_tamano_vacia():
    """CA-HAS-06: una tabla vacía tiene tamaño 0."""
    assert TablaHash().tamano() == 0


def test_tamano_un_elemento():
    """CA-HAS-06: con una clave el tamaño es 1."""
    assert tabla_con("R1").tamano() == 1


def test_tamano_tras_eliminar_todo():
    """CA-HAS-06: eliminar todas las claves deja el tamaño en 0."""
    tabla = tabla_con("R1")
    tabla.eliminar("R1")
    assert tabla.tamano() == 0
