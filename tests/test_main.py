"""Pruebas de humo de la interfaz de consola."""

from main import menu, procesar


def test_menu_muestra_opciones():
    """Verifica que el menú principal lista la opción de salir."""
    assert "[s] Salir" in menu()


def test_salir_devuelve_none():
    """Verifica que la opción 's' termina el programa, sin importar mayúsculas."""
    assert procesar("S") is None


def test_opcion_invalida():
    """Verifica que una opción desconocida no termina el programa."""
    assert procesar("x") == "Opción no válida."
