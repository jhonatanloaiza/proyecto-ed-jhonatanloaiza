"""Pruebas de integración de la Partida contra los criterios de las historias Must."""

from dominio.entidades import RASTREADOR
from dominio.mapa import COMPUERTA, LIBRE, PICO, PORTAL
from dominio.niveles import SECTOR_DE_ARRANQUE
from dominio.partida import ABAJO, ARRIBA, DERECHA, DERROTA, EN_JUEGO, IZQUIERDA, PARTIDA_TERMINADA, VICTORIA, Partida

# El Rastreador queda encerrado detrás de picos: no interfiere con el Cubo.
ABIERTO = (
    "Co.k.",
    ".....",
    ".#...",
    ".....",
    "....@",
    "^^^^^",
    "R....",
)


def posicion(partida, identificador):
    return partida.indice.buscar(identificador).celda


def estado(partida):
    """Foto de todo lo que un turno puede cambiar."""
    pajaros = [p.celda for p in partida.enemigos]
    objetos = [o.id for o in partida.inventario]
    return partida.cubo.celda, pajaros, objetos, partida.turno, partida.puntaje, partida.estado


def test_inicio_mapa_y_picos():
    """CA-01: el mapa tiene al menos 20 × 20 celdas y máximo 25 % de picos."""
    partida = Partida()
    assert partida.mapa.filas() >= 20 and partida.mapa.columnas() >= 20
    assert partida.mapa.proporcion_picos() <= 0.25


def test_inicio_entidades():
    """CA-02: hay un Cubo, al menos 2 Rastreadores, al menos 1 orbe y un portal."""
    partida = Partida()
    assert partida.cubo is not None and partida.enemigos.tamano() >= 2
    assert partida.indice.buscar("O1") is not None
    assert partida.mapa.terreno_en((19, 19)) == PORTAL


def test_inicio_contadores():
    """CA-03: turno en 0, inventario vacío y sin acciones para deshacer ni rehacer."""
    partida = Partida()
    assert partida.turno == 0 and partida.inventario.tamano() == 0
    assert not partida.historial.puede_deshacer() and not partida.historial.puede_rehacer()


def test_mover_a_celda_libre():
    """CA-04: en una celda transitable el Cubo queda en ella y el turno avanza."""
    partida = Partida(ABIERTO)
    partida.mover(ABAJO)
    assert partida.cubo.celda == (1, 0) and partida.turno == 1


def test_mover_fuera_del_mapa():
    """CA-05: fuera del mapa el Cubo no se mueve y el turno no avanza."""
    partida = Partida(ABIERTO)
    mensaje = partida.mover(ARRIBA)
    assert partida.cubo.celda == (0, 0) and partida.turno == 0 and "matriz" in mensaje


def test_mover_a_un_pico():
    """CA-05: contra un pico el Cubo no se mueve y se informa el motivo."""
    partida = Partida(("C^", "R."))
    mensaje = partida.mover(DERECHA)
    assert partida.cubo.celda == (0, 0) and partida.turno == 0 and "pico" in mensaje


def test_mover_a_compuerta_cerrada():
    """CA-05: la compuerta cerrada bloquea al Cubo."""
    partida = Partida(("C#", "^^", "R."))
    mensaje = partida.mover(DERECHA)
    assert partida.cubo.celda == (0, 0) and "compuerta" in mensaje


def test_esperar_avanza_el_turno():
    """CA-06: esperar no mueve el Cubo y el turno avanza en 1."""
    partida = Partida(ABIERTO)
    partida.esperar()
    assert partida.cubo.celda == (0, 0) and partida.turno == 1


def test_esperar_mueve_a_los_pajaros():
    """CA-19: esperar también activa a los Pájaros."""
    partida = Partida(("C...R",))
    partida.esperar()
    assert posicion(partida, "R1") == (0, 3)


def test_esperar_con_partida_terminada():
    """CA-28: terminada la partida no se puede esperar."""
    partida = Partida(("CR",))
    partida.esperar()
    assert partida.esperar() == PARTIDA_TERMINADA


def test_recoger_orbe():
    """CA-07: al entrar en la celda, el objeto sale del mapa y va al inventario."""
    partida = Partida(ABIERTO)
    partida.mover(DERECHA)
    assert partida.mapa.objeto_en((0, 1)) is None and partida.inventario.buscar("O1") is not None


def test_recoger_orbe_suma_puntos():
    """CA-08: recoger un orbe suma sus puntos."""
    partida = Partida(ABIERTO)
    partida.mover(DERECHA)
    assert partida.puntaje == 10


def test_inventario_vacio_al_soltar():
    """CA-12: soltar un objeto que no se tiene no cambia nada."""
    partida = Partida(ABIERTO)
    antes = estado(partida)
    mensaje = partida.soltar("O1")
    assert estado(partida) == antes and "No tienes" in mensaje


def test_usar_inexistente():
    """CA-12: usar un objeto que no se tiene no cambia nada."""
    partida = Partida(ABIERTO)
    antes = estado(partida)
    partida.usar("K1")
    assert estado(partida) == antes


def test_soltar_deja_el_objeto_en_la_celda():
    """CA-11: soltar deja el objeto en la celda del Cubo y lo saca del inventario."""
    partida = Partida(ABIERTO)
    partida.mover(DERECHA)
    partida.soltar("O1")
    assert partida.mapa.objeto_en((0, 1)).id == "O1" and partida.inventario.tamano() == 0


def test_soltar_orbe_resta_puntos():
    """CA-42: soltar un orbe resta sus puntos."""
    partida = Partida(ABIERTO)
    partida.mover(DERECHA)
    partida.soltar("O1")
    assert partida.puntaje == 0


def test_soltar_gasta_turno_y_se_puede_deshacer():
    """CA-41: soltar gasta el turno y se puede deshacer."""
    partida = Partida(ABIERTO)
    partida.mover(DERECHA)
    partida.soltar("O1")
    assert partida.turno == 2
    partida.deshacer()
    assert partida.inventario.tamano() == 1 and partida.puntaje == 10


def test_soltar_en_celda_ocupada():
    """CA-43: no se puede soltar en una celda que ya tiene un objeto."""
    partida = Partida(ABIERTO)
    partida.mover(DERECHA)
    partida.mover(DERECHA)
    partida.mover(DERECHA)
    partida.soltar("K1")
    antes = estado(partida)
    assert "Ya hay" in partida.soltar("O1") and estado(partida) == antes


def test_usar_orbe_no_cambia_nada():
    """CA-43: un orbe no se puede usar y no gasta el turno."""
    partida = Partida(ABIERTO)
    partida.mover(DERECHA)
    antes = estado(partida)
    partida.usar("O1")
    assert estado(partida) == antes


def recoger_llave():
    partida = Partida(ABIERTO)
    partida.mover(DERECHA)
    partida.mover(DERECHA)
    partida.mover(DERECHA)
    return partida


def test_usar_llave_lejos_de_compuerta():
    """CA-43: una llave lejos de una compuerta no se puede usar."""
    partida = recoger_llave()
    antes = estado(partida)
    assert "compuerta" in partida.usar("K1") and estado(partida) == antes


def llegar_a_la_compuerta():
    partida = recoger_llave()
    partida.mover(ABAJO)
    partida.mover(IZQUIERDA)
    partida.mover(IZQUIERDA)
    return partida


def test_usar_llave_abre_la_compuerta():
    """CA-10: usar una llave junto a una compuerta la abre y elimina la llave."""
    partida = llegar_a_la_compuerta()
    partida.usar("K1")
    assert partida.mapa.terreno_en((2, 1)) == LIBRE and partida.inventario.buscar("K1") is None


def test_deshacer_llave_cierra_la_compuerta():
    """CA-41: deshacer el uso devuelve la llave a su posición y cierra la compuerta."""
    partida = llegar_a_la_compuerta()
    partida.usar("K1")
    partida.deshacer()
    assert partida.mapa.terreno_en((2, 1)) == COMPUERTA
    assert [objeto.id for objeto in partida.inventario] == ["O1", "K1"]


def test_deshacer_movimiento():
    """CA-13: deshacer devuelve al Cubo y a los Pájaros a sus celdas y resta 1 al turno."""
    partida = Partida(("C.....R",))
    partida.mover(DERECHA)
    assert posicion(partida, "R1") == (0, 5)
    partida.deshacer()
    assert partida.cubo.celda == (0, 0) and posicion(partida, "R1") == (0, 6) and partida.turno == 0


def test_deshacer_recogida():
    """CA-14: deshacer una recogida devuelve el objeto a su celda y resta sus puntos."""
    partida = Partida(ABIERTO)
    partida.mover(DERECHA)
    partida.deshacer()
    assert partida.mapa.objeto_en((0, 1)).id == "O1"
    assert partida.inventario.tamano() == 0 and partida.puntaje == 0
    assert posicion(partida, "O1") == (0, 1)


def test_deshacer_sin_acciones():
    """CA-15: deshacer sin acciones no cambia nada y lo informa."""
    partida = Partida(ABIERTO)
    antes = estado(partida)
    assert partida.deshacer() == "No hay qué deshacer." and estado(partida) == antes


def test_rehacer_repite_los_mismos_efectos():
    """CA-16: rehacer aplica de nuevo la acción con los mismos efectos, también en los Pájaros."""
    partida = Partida(ABIERTO)
    partida.mover(DERECHA)
    despues = estado(partida)
    partida.deshacer()
    partida.rehacer()
    assert estado(partida) == despues


def test_accion_nueva_borra_rehacer():
    """CA-17: una acción nueva después de deshacer elimina lo que se podía rehacer."""
    partida = Partida(ABIERTO)
    partida.mover(DERECHA)
    partida.deshacer()
    partida.mover(ABAJO)
    assert partida.rehacer() == "No hay qué rehacer."


def test_rehacer_sin_acciones():
    """CA-18: rehacer sin acciones no cambia nada y lo informa."""
    partida = Partida(ABIERTO)
    antes = estado(partida)
    assert partida.rehacer() == "No hay qué rehacer." and estado(partida) == antes


def test_pajaro_avanza_una_casilla_por_camino_corto():
    """CA-19: el Pájaro avanza exactamente una casilla hacia el Cubo."""
    partida = Partida(("C....",  ".....", "....R"))
    partida.esperar()
    celda = posicion(partida, "R1")
    assert abs(celda[0] - 2) + abs(celda[1] - 4) == 1
    assert celda[0] + celda[1] == 5


def test_pajaro_no_entra_en_picos():
    """CA-20: el Pájaro rodea los picos."""
    partida = Partida(("C.^.R", "....."))
    for _ in range(2):
        partida.esperar()
        assert partida.mapa.terreno_en(posicion(partida, "R1")) != PICO


def test_pajaro_sin_camino_no_se_mueve():
    """CA-21: si no existe camino, el Pájaro se queda en su celda."""
    partida = Partida(ABIERTO)
    partida.esperar()
    assert posicion(partida, "R1") == (6, 0)


def test_pajaros_no_ocupan_la_misma_celda():
    """CA-22: si dos Pájaros quieren la misma celda, el segundo espera."""
    partida = Partida(("C...RR",))
    partida.esperar()
    assert posicion(partida, "R1") == (0, 3) and posicion(partida, "R2") == (0, 4)


def test_pajaros_orden_fijo():
    """CA-22: los Pájaros se mueven en orden fijo, turno tras turno."""
    partida = Partida(("R.........C",))
    partida.esperar()
    primero = partida.enemigos.siguiente()
    assert primero.id == "R1"


def test_eventos_de_recoleccion_con_turno_y_celda():
    """CA-23: una recolección genera un evento con el turno y la celda."""
    partida = Partida(ABIERTO)
    partida.drenar_eventos()
    partida.mover(DERECHA)
    assert list(partida.drenar_eventos()) == ["[T1] Recogiste O1 en (0, 1)"]


def test_eventos_de_aparicion_y_colision():
    """CA-23: las apariciones y las colisiones generan eventos."""
    partida = Partida(("CR",))
    assert "Aparece R1" in " ".join(partida.drenar_eventos())
    partida.esperar()
    assert "atrapó" in " ".join(partida.drenar_eventos())


def test_eventos_en_orden():
    """CA-24: los eventos salen en el mismo orden en que se generaron."""
    textos = list(Partida(("Co.R",)).drenar_eventos())
    assert textos[0].startswith("[T0] Aparece C") and textos[1].startswith("[T0] Aparece O1")


def test_turno_sin_eventos():
    """CA-25: un turno sin eventos no deja eventos para mostrar."""
    partida = Partida(ABIERTO)
    partida.drenar_eventos()
    partida.mover(ABAJO)
    assert partida.drenar_eventos().esta_vacia()


def test_victoria_en_el_portal():
    """CA-26: si el Cubo llega al portal, la partida termina con victoria."""
    partida = Partida(("C@", "^^", "R."))
    partida.mover(DERECHA)
    assert partida.estado == VICTORIA


def test_derrota_si_el_pajaro_llega():
    """CA-27: si un Pájaro ocupa la celda del Cubo, la partida termina con derrota."""
    partida = Partida(("C.R",))
    partida.esperar()
    partida.esperar()
    assert partida.estado == DERROTA


def test_derrota_si_el_cubo_entra_a_la_celda_del_pajaro():
    """CA-27: entrar en la celda de un Pájaro también es derrota."""
    partida = Partida(("CR",))
    partida.mover(DERECHA)
    assert partida.estado == DERROTA


def test_partida_terminada_no_acepta_movimientos():
    """CA-28: terminada la partida no se aceptan movimientos."""
    partida = Partida(("C@", "^^", "R."))
    partida.mover(DERECHA)
    assert partida.mover(IZQUIERDA) == PARTIDA_TERMINADA and partida.cubo.celda == (0, 1)


def test_partida_terminada_permite_deshacer():
    """CA-28: terminada la partida se puede deshacer y seguir jugando."""
    partida = Partida(("CR",))
    partida.esperar()
    partida.deshacer()
    assert partida.estado == EN_JUEGO and partida.turno == 0


def test_buscar_entidad_existente():
    """CA-29: buscar un id existente muestra su tipo y su celda."""
    assert Partida(ABIERTO).buscar("R1") == f"R1: {RASTREADOR}, en (6, 0)."


def test_buscar_objeto_en_inventario():
    """CA-29: un objeto recogido aparece en el inventario."""
    partida = Partida(ABIERTO)
    partida.mover(DERECHA)
    assert "en el inventario" in partida.buscar("O1")


def test_buscar_inexistente():
    """CA-30: buscar un id inexistente informa que no existe."""
    assert Partida(ABIERTO).buscar("X9") == "No existe X9."


def test_nivel_se_puede_ganar_por_el_camino_corto():
    """CA-26: el nivel del juego se gana yendo directo al portal sin ser atrapado."""
    partida = Partida(SECTOR_DE_ARRANQUE)
    camino = list(partida._grafo.bfs(partida.cubo.celda, (19, 19)).camino)
    for desde, hasta in zip(camino, camino[1:]):
        partida.mover((hasta[0] - desde[0], hasta[1] - desde[1]))
    assert partida.estado == VICTORIA


def test_nivel_esperar_lleva_a_la_derrota():
    """CA-27: si el jugador no se mueve, los Pájaros lo atrapan."""
    partida = Partida(SECTOR_DE_ARRANQUE)
    for _ in range(40):
        partida.esperar()
    assert partida.estado == DERROTA
