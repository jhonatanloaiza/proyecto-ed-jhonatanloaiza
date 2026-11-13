"""Interfaz de consola de Escape Geométrico del Sistema Corrupto."""

import os
import sys

from dominio.entidades import CAZADOR, CENTINELA, ORBE
from dominio.mapa import COMPUERTA, PICO, PORTAL
from dominio.niveles import NIVELES
from dominio.partida import ABAJO, ARRIBA, DERECHA, DERROTA, EN_JUEGO, IZQUIERDA, VICTORIA, Partida
from dominio.puntajes import TablaPuntajes

TITULO = "ESCAPE GEOMÉTRICO DEL SISTEMA CORRUPTO"

OPCIONES = (
    ("1", "Nueva partida"),
    ("2", "Mejores puntajes"),
    ("s", "Salir"),
)

COMANDOS = (
    "w/a/s/d mover · e esperar · i inventario · u ID usar · x ID soltar · "
    "b ID buscar · c comparar BFS y A* · z deshacer · y rehacer · r reiniciar · q salir"
)

CUBO = "■"
RASTREADOR_SIMBOLO = "V"
CENTINELA_SIMBOLO = "S"
CAZADOR_SIMBOLO = "H"
ORBE_SIMBOLO = "o"
LLAVE_SIMBOLO = "k"

CIAN, ROJO, AMARILLO, MAGENTA, VERDE, GRIS, BLANCO = 96, 91, 93, 95, 92, 90, 97


def menu() -> str:
    """Devuelve el texto del menú principal. O(1)."""
    lineas = [TITULO, "=" * len(TITULO)]
    lineas += [f"[{tecla}] {texto}" for tecla, texto in OPCIONES]
    return "\n".join(lineas)


def procesar(opcion: str) -> str | None:
    """Devuelve la respuesta a una opción del menú que no abre otra pantalla, o None para salir. O(1)."""
    opcion = opcion.strip().lower()
    if opcion == "s":
        return None
    return "Opción no válida."


def texto_niveles() -> str:
    """Devuelve la lista de niveles para elegir. O(1)."""
    return "\n".join(f"[{numero}] {nombre}" for numero, (nombre, _) in enumerate(NIVELES, start=1))


def elegir_nivel(texto: str):
    """Devuelve (nombre, plano) del nivel elegido, o None si no existe. O(1)."""
    texto = texto.strip()
    if texto.isdigit() and 1 <= int(texto) <= len(NIVELES):
        return NIVELES[int(texto) - 1]
    return None


def texto_puntajes(puntajes) -> str:
    """Describe el ranking de mayor a menor puntaje. O(n)."""
    if puntajes.tamano() == 0:
        return "Todavía no hay partidas terminadas."
    lineas = ["MEJORES PUNTAJES"]
    for puesto, registro in enumerate(puntajes.ranking(), start=1):
        lineas.append(
            f"{puesto}. {registro.puntaje} pts · {registro.resultado} · "
            f"{registro.turnos} turnos · {registro.nivel}"
        )
    return "\n".join(lineas)


def _pintar(simbolo, codigo, color):
    return f"\033[{codigo}m{simbolo}\033[0m" if color else simbolo


def _simbolo_enemigo(partida, celda, color):
    for pajaro in partida.enemigos:
        if pajaro.celda == celda:
            if pajaro.tipo == CENTINELA:
                return _pintar(CENTINELA_SIMBOLO, ROJO, color)
            if pajaro.tipo == CAZADOR:
                return _pintar(CAZADOR_SIMBOLO, ROJO, color)
            return _pintar(RASTREADOR_SIMBOLO, ROJO, color)
    return None


def _simbolo_celda(partida, celda, color):
    if partida.cubo.celda == celda:
        return _pintar(CUBO, CIAN, color)
    enemigo = _simbolo_enemigo(partida, celda, color)
    if enemigo is not None:
        return enemigo
    objeto = partida.mapa.objeto_en(celda)
    if objeto is not None:
        if objeto.tipo == ORBE:
            return _pintar(ORBE_SIMBOLO, AMARILLO, color)
        return _pintar(LLAVE_SIMBOLO, MAGENTA, color)
    terreno = partida.mapa.terreno_en(celda)
    if terreno == COMPUERTA:
        return _pintar(terreno, BLANCO, color)
    if terreno == PORTAL:
        return _pintar(terreno, VERDE, color)
    return _pintar(terreno, GRIS, color)


def dibujar(partida, color=False) -> str:
    """Devuelve el mapa y el estado de la partida como texto. O(filas × columnas × k)."""
    lineas = []
    for fila in range(partida.mapa.filas()):
        simbolos = [_simbolo_celda(partida, (fila, columna), color) for columna in range(partida.mapa.columnas())]
        lineas.append(" ".join(simbolos))
    objetos = ", ".join(objeto.id for objeto in partida.inventario) or "vacío"
    lineas.append(f"{partida.nombre} · Turno: {partida.turno} · Puntaje: {partida.puntaje} · Inventario: {objetos}")
    return "\n".join(lineas)


def listar_inventario(partida) -> str:
    """Describe el inventario en orden de recogida. O(n)."""
    if partida.inventario.tamano() == 0:
        return "El inventario está vacío."
    return "\n".join(f"{objeto.id}: {objeto.tipo}" for objeto in partida.inventario)


def texto_comparacion(partida) -> str:
    """Celdas exploradas por BFS y A* desde cada Pájaro hasta el Cubo. O(k × V log V)."""
    lineas = ["Pájaro · pasos · BFS explora · A* explora"]
    for pajaro, pasos, bfs, guiada in partida.comparar_busquedas():
        lineas.append(f"{pajaro} · {pasos} · {bfs} · {guiada}")
    return "\n".join(lineas)


def ejecutar_comando(partida, texto: str) -> str:
    """Aplica un comando del jugador y devuelve el mensaje de respuesta."""
    partes = texto.strip().lower().split()
    comando = partes[0] if partes else ""
    identificador = partes[1].upper() if len(partes) == 2 else None
    for tecla, direccion in (("w", ARRIBA), ("s", ABAJO), ("a", IZQUIERDA), ("d", DERECHA)):
        if comando == tecla and len(partes) == 1:
            return partida.mover(direccion)
    if comando == "e" and len(partes) == 1:
        return partida.esperar()
    if comando == "i" and len(partes) == 1:
        return listar_inventario(partida)
    if comando == "c" and len(partes) == 1:
        return texto_comparacion(partida)
    if comando == "z" and len(partes) == 1:
        return partida.deshacer()
    if comando == "y" and len(partes) == 1:
        return partida.rehacer()
    if comando == "u" and identificador:
        return partida.usar(identificador)
    if comando == "x" and identificador:
        return partida.soltar(identificador)
    if comando == "b" and identificador:
        return partida.buscar(identificador)
    return f"Comando no válido. {COMANDOS}"


def registrar_si_termino(partida, puntajes):
    """Guarda el puntaje de una partida terminada al salir de ella. O(log n)."""
    if partida.estado != EN_JUEGO:
        puntajes.registrar(partida.puntaje, partida.estado, partida.turno, partida.nombre)


def mostrar_eventos(partida):
    eventos = partida.drenar_eventos()
    if not eventos.esta_vacia():
        print("Eventos:")
        for texto in eventos:
            print(f"  {texto}")


def mostrar_fin(partida):
    if partida.estado == VICTORIA:
        print(f"\aSISTEMA RESTAURADO · Turnos: {partida.turno} · Puntaje: {partida.puntaje}")
        print("Usa q para volver al menú, r para jugar de nuevo o z para retroceder.")
    elif partida.estado == DERROTA:
        print("\aFRAGMENTO ELIMINADO · SISTEMA CORRUPTO · Usa z para retroceder, r para reiniciar o q para salir.")


def jugar(nombre, plano, puntajes):
    partida = Partida(plano, nombre)
    print(COMANDOS)
    while True:
        print(dibujar(partida, color=True))
        mostrar_eventos(partida)
        mostrar_fin(partida)
        texto = input("> ").strip().lower()
        if texto == "q":
            registrar_si_termino(partida, puntajes)
            return
        if texto == "r":
            registrar_si_termino(partida, puntajes)
            partida = Partida(plano, nombre)
            continue
        print(ejecutar_comando(partida, texto))


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    os.system("")  # activa los colores en la consola de Windows
    puntajes = TablaPuntajes()
    while True:
        print(menu())
        opcion = input("> ").strip().lower()
        if opcion == "1":
            print(texto_niveles())
            nivel = elegir_nivel(input("Nivel > "))
            if nivel is None:
                print("Ese nivel no existe.", end="\n\n")
                continue
            jugar(*nivel, puntajes)
            continue
        if opcion == "2":
            print(texto_puntajes(puntajes), end="\n\n")
            continue
        respuesta = procesar(opcion)
        if respuesta is None:
            print("Saliendo del sistema...")
            break
        print(respuesta, end="\n\n")


if __name__ == "__main__":
    main()
