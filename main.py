"""Interfaz de consola de Escape Geométrico del Sistema Corrupto."""

import os
import sys

from dominio.entidades import ORBE
from dominio.mapa import COMPUERTA, PICO, PORTAL
from dominio.partida import ABAJO, ARRIBA, DERECHA, DERROTA, EN_JUEGO, IZQUIERDA, VICTORIA, Partida

TITULO = "ESCAPE GEOMÉTRICO DEL SISTEMA CORRUPTO"

OPCIONES = (
    ("1", "Nueva partida"),
    ("2", "Mejores puntajes"),
    ("s", "Salir"),
)

COMANDOS = (
    "w/a/s/d mover · e esperar · i inventario · u ID usar · x ID soltar · "
    "b ID buscar · z deshacer · y rehacer · r reiniciar · q salir"
)

CUBO = "■"
PAJARO = "V"
ORBE_SIMBOLO = "o"
LLAVE_SIMBOLO = "k"

CIAN, ROJO, AMARILLO, MAGENTA, VERDE, GRIS, BLANCO = 96, 91, 93, 95, 92, 90, 97


def menu() -> str:
    """Devuelve el texto del menú principal. O(1)."""
    lineas = [TITULO, "=" * len(TITULO)]
    lineas += [f"[{tecla}] {texto}" for tecla, texto in OPCIONES]
    return "\n".join(lineas)


def procesar(opcion: str) -> str | None:
    """Devuelve la respuesta a una opción del menú, o None para salir. O(1)."""
    opcion = opcion.strip().lower()
    if opcion == "s":
        return None
    if opcion == "2":
        return "Mejores puntajes: llega en la Entrega final."
    return "Opción no válida."


def _pintar(simbolo, codigo, color):
    return f"\033[{codigo}m{simbolo}\033[0m" if color else simbolo


def _simbolo_celda(partida, celda, color):
    if partida.cubo.celda == celda:
        return _pintar(CUBO, CIAN, color)
    if partida.hay_pajaro_en(celda):
        return _pintar(PAJARO, ROJO, color)
    objeto = partida.mapa.objeto_en(celda)
    if objeto is not None:
        if objeto.tipo == ORBE:
            return _pintar(ORBE_SIMBOLO, AMARILLO, color)
        return _pintar(LLAVE_SIMBOLO, MAGENTA, color)
    terreno = partida.mapa.terreno_en(celda)
    if terreno == PICO:
        return _pintar(terreno, GRIS, color)
    if terreno == COMPUERTA:
        return _pintar(terreno, BLANCO, color)
    if terreno == PORTAL:
        return _pintar(terreno, VERDE, color)
    return _pintar(terreno, GRIS, color)


def dibujar(partida, color=False) -> str:
    """Devuelve el mapa y el estado de la partida como texto. O(filas × columnas)."""
    lineas = []
    for fila in range(partida.mapa.filas()):
        simbolos = [_simbolo_celda(partida, (fila, columna), color) for columna in range(partida.mapa.columnas())]
        lineas.append(" ".join(simbolos))
    objetos = ", ".join(objeto.id for objeto in partida.inventario) or "vacío"
    lineas.append(f"Turno: {partida.turno} · Puntaje: {partida.puntaje} · Inventario: {objetos}")
    return "\n".join(lineas)


def listar_inventario(partida) -> str:
    """Describe el inventario en orden de recogida. O(n)."""
    if partida.inventario.tamano() == 0:
        return "El inventario está vacío."
    return "\n".join(f"{objeto.id}: {objeto.tipo}" for objeto in partida.inventario)


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


def mostrar_eventos(partida):
    eventos = partida.drenar_eventos()
    if not eventos.esta_vacia():
        print("Eventos:")
        for texto in eventos:
            print(f"  {texto}")


def mostrar_fin(partida):
    if partida.estado == VICTORIA:
        print(f"SISTEMA RESTAURADO · Turnos: {partida.turno} · Puntaje: {partida.puntaje}")
    elif partida.estado == DERROTA:
        print("FRAGMENTO ELIMINADO · SISTEMA CORRUPTO · Usa z para retroceder, r para reiniciar o q para salir.")


def jugar():
    partida = Partida()
    print(COMANDOS)
    while True:
        print(dibujar(partida, color=True))
        mostrar_eventos(partida)
        mostrar_fin(partida)
        texto = input("> ").strip().lower()
        if texto == "q":
            return
        if texto == "r":
            partida = Partida()
            continue
        print(ejecutar_comando(partida, texto))


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    os.system("")  # activa los colores en la consola de Windows
    while True:
        print(menu())
        opcion = input("> ").strip().lower()
        if opcion == "1":
            jugar()
            continue
        respuesta = procesar(opcion)
        if respuesta is None:
            print("Saliendo del sistema...")
            break
        print(respuesta, end="\n\n")


if __name__ == "__main__":
    main()
