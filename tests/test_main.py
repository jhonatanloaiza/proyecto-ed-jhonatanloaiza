"""Pruebas de la interfaz de consola (HU-11)."""

from dominio.partida import Partida
from main import COMANDOS, dibujar, ejecutar_comando, listar_inventario, menu, procesar

PLANO = (
    "Co.R",
    "^^^^",
    "...@",
)


def test_menu_muestra_opciones():
    """CA-32: el menú principal lista las opciones."""
    assert "[s] Salir" in menu()


def test_salir_devuelve_none():
    """CA-32: la opción 's' termina el programa, sin importar mayúsculas."""
    assert procesar("S") is None


def test_opcion_invalida():
    """CA-32: una opción desconocida no termina el programa."""
    assert procesar("x") == "Opción no válida."


def test_dibujar_un_simbolo_por_elemento():
    """CA-31: el mapa usa un símbolo por tipo de elemento."""
    lineas = dibujar(Partida(PLANO)).splitlines()
    assert lineas[0] == "■ o . V" and lineas[1] == "^ ^ ^ ^" and lineas[2] == ". . . @"


def test_dibujar_muestra_turno_puntaje_e_inventario():
    """CA-31: bajo el mapa se muestran el turno, el puntaje y el inventario."""
    partida = Partida(PLANO)
    ejecutar_comando(partida, "d")
    assert "Turno: 1 · Puntaje: 10 · Inventario: O1" in dibujar(partida)


def test_dibujar_con_color():
    """CA-31: con color, los símbolos llevan códigos de la terminal."""
    assert "\033[96m■" in dibujar(Partida(PLANO), color=True)


def test_comando_no_reconocido():
    """CA-32: un comando no reconocido no cambia el estado y muestra los comandos."""
    partida = Partida(PLANO)
    assert COMANDOS in ejecutar_comando(partida, "volar") and partida.turno == 0


def test_comando_vacio():
    """CA-32: una línea vacía se trata como comando no reconocido."""
    assert COMANDOS in ejecutar_comando(Partida(PLANO), "")


def test_comando_sin_identificador():
    """CA-32: usar sin identificador es un comando no reconocido."""
    assert COMANDOS in ejecutar_comando(Partida(PLANO), "u")


def test_comandos_ejercitan_el_juego():
    """CA-31: los comandos llegan a mover, buscar, deshacer y rehacer."""
    partida = Partida(PLANO)
    ejecutar_comando(partida, "d")
    assert "O1" in ejecutar_comando(partida, "b o1")
    ejecutar_comando(partida, "z")
    assert partida.turno == 0
    ejecutar_comando(partida, "y")
    assert partida.turno == 1


def test_listar_inventario_vacio():
    """CA-09: con el inventario vacío se informa que está vacío."""
    assert listar_inventario(Partida(PLANO)) == "El inventario está vacío."


def test_listar_inventario_en_orden():
    """CA-09: listar muestra los objetos con su tipo."""
    partida = Partida(PLANO)
    ejecutar_comando(partida, "d")
    assert ejecutar_comando(partida, "i").startswith("O1: Orbe")
