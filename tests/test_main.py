"""Pruebas de la interfaz de consola (HU-11)."""

from dominio.partida import Partida
from dominio.puntajes import TablaPuntajes
from main import (
    COMANDOS,
    dibujar,
    ejecutar_comando,
    elegir_nivel,
    listar_inventario,
    menu,
    procesar,
    registrar_si_termino,
    texto_comparacion,
    texto_niveles,
    texto_puntajes,
)

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


# --- Entrega final: niveles, puntajes y comparación ---


def test_elegir_nivel_valido():
    """CA-39: elegir un nivel existente devuelve su nombre y su plano."""
    nombre, plano = elegir_nivel("2")
    assert nombre == "Memoria Fragmentada" and len(plano) == 20


def test_elegir_nivel_lista_los_tres():
    """CA-39: el menú de niveles muestra los tres niveles."""
    assert texto_niveles().count("\n") == 2 and "[3] Núcleo Corrupto" in texto_niveles()


def test_partida_usa_el_nivel_elegido():
    """CA-39: la partida inicia con los elementos del nivel elegido."""
    nombre, plano = elegir_nivel("3")
    partida = Partida(plano, nombre)
    assert partida.indice.contiene("H1") and dibujar(partida).splitlines()[-1].startswith("Núcleo Corrupto")


def test_elegir_nivel_inexistente():
    """CA-40: un nivel inexistente devuelve None."""
    assert elegir_nivel("4") is None and elegir_nivel("0") is None


def test_elegir_nivel_texto():
    """CA-40: un texto que no es número devuelve None."""
    assert elegir_nivel("dos") is None


def test_elegir_nivel_vacio():
    """CA-40: una línea vacía devuelve None."""
    assert elegir_nivel("") is None


def test_puntajes_sin_partidas():
    """CA-34: sin partidas registradas se informa que la tabla está vacía."""
    assert texto_puntajes(TablaPuntajes()) == "Todavía no hay partidas terminadas."


def test_puntajes_de_mayor_a_menor():
    """CA-34: la tabla muestra los puntajes de mayor a menor."""
    tabla = TablaPuntajes()
    tabla.registrar(10, "derrota", 3, "Sector de Arranque")
    tabla.registrar(40, "victoria", 30, "Sector de Arranque")
    lineas = texto_puntajes(tabla).splitlines()
    assert lineas[1].startswith("1. 40 pts") and lineas[2].startswith("2. 10 pts")


def test_registrar_partida_terminada():
    """CA-33: al salir de una partida terminada su puntaje se registra."""
    tabla = TablaPuntajes()
    partida = Partida(("Co@", "^^^", "R.."))
    ejecutar_comando(partida, "d")
    ejecutar_comando(partida, "d")
    registrar_si_termino(partida, tabla)
    registro = next(iter(tabla.ranking()))
    assert (registro.puntaje, registro.resultado, registro.turnos) == (10, "victoria", 2)


def test_no_registrar_partida_en_juego():
    """CA-33: una partida sin terminar no se registra."""
    tabla = TablaPuntajes()
    registrar_si_termino(Partida(PLANO), tabla)
    assert tabla.tamano() == 0


def test_comando_comparar():
    """CA-38: el comando c muestra las celdas exploradas por BFS y A* de cada Pájaro."""
    partida = Partida(PLANO)
    assert ejecutar_comando(partida, "c") == texto_comparacion(partida)
    assert texto_comparacion(partida).splitlines()[1].startswith("R1 · 3 · ")


def test_dibujar_centinela_y_cazador():
    """CA-31: el Cazador se dibuja con H y el Centinela con S cuando aparece."""
    partida = Partida(("CkS", "^^^", "H.@"))
    ejecutar_comando(partida, "d")
    lineas = dibujar(partida).splitlines()
    assert lineas[0] == ". ■ S" and lineas[2].startswith("H")
