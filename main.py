"""Interfaz de consola de Escape Geométrico del Sistema Corrupto."""

TITULO = "ESCAPE GEOMÉTRICO DEL SISTEMA CORRUPTO"

OPCIONES = (
    ("1", "Nueva partida"),
    ("2", "Mejores puntajes"),
    ("s", "Salir"),
)


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
    if opcion in ("1", "2"):
        return "Función en construcción (Entrega 2)."
    return "Opción no válida."


def main() -> None:
    while True:
        print(menu())
        respuesta = procesar(input("> "))
        if respuesta is None:
            print("Saliendo del sistema...")
            break
        print(respuesta, end="\n\n")


if __name__ == "__main__":
    main()
