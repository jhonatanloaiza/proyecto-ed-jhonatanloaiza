"""Partida: coordina el mapa, los turnos, los enemigos, el inventario y el historial."""

from dominio.acciones import (
    AbrirCompuerta,
    Accion,
    AparecerEnemigo,
    CambiarEstado,
    ConsumirLlave,
    MoverEntidad,
    Recoger,
    Soltar,
    SumarPuntos,
    SumarTurno,
)
from dominio.entidades import CAZADOR, CENTINELA, CUBO, LLAVE, ORBE, RASTREADOR, Entidad
from dominio.eventos import APARICION, COLISION, RECOLECCION, Evento
from dominio.historial import Historial
from dominio.inventario import Inventario
from dominio.mapa import COMPUERTA, PICO, PORTAL, Mapa
from dominio.niveles import SECTOR_DE_ARRANQUE
from estructuras.cola import Cola
from estructuras.grafo import GrafoRejilla
from estructuras.lista_circular import ListaCircular
from estructuras.lista_enlazada import ListaEnlazada
from estructuras.tabla_hash import TablaHash

EN_JUEGO = "en juego"
VICTORIA = "victoria"
DERROTA = "derrota"

ARRIBA = (-1, 0)
ABAJO = (1, 0)
IZQUIERDA = (0, -1)
DERECHA = (0, 1)

PUNTOS_ORBE = 10
PARTIDA_TERMINADA = "La partida terminó: solo puedes deshacer, reiniciar o salir."


class Partida:
    def __init__(self, plano=SECTOR_DE_ARRANQUE, nombre="Sector de Arranque"):
        self.nombre = nombre
        self.turno = 0
        self.puntaje = 0
        self.estado = EN_JUEGO
        self.mapa = Mapa(len(plano), len(plano[0]))
        self.inventario = Inventario()
        self.enemigos = ListaCircular()
        self.eventos = Cola()
        self.indice = TablaHash()
        self.historial = Historial()
        self.cubo = None
        self._centinelas = ListaEnlazada()  # esperan a que el Cubo recoja una llave
        self._cargar(plano)
        self.grafo = GrafoRejilla(self.mapa.filas(), self.mapa.columnas(), self.mapa.es_transitable)

    def mover(self, direccion):
        """Mueve el Cubo una casilla y resuelve el turno. O(k × V log V) para k enemigos."""
        if self.estado != EN_JUEGO:
            return PARTIDA_TERMINADA
        destino = (self.cubo.celda[0] + direccion[0], self.cubo.celda[1] + direccion[1])
        if not self.mapa.dentro(destino):
            return "No puedes salir de la matriz."
        terreno = self.mapa.terreno_en(destino)
        if terreno == PICO:
            return "Ahí hay un pico: el Cubo no puede entrar."
        if terreno == COMPUERTA:
            return "La compuerta está cerrada: usa una llave."
        accion = self._nueva_accion()
        accion.ejecutar(MoverEntidad(self.cubo, self.cubo.celda, destino), self)
        objeto = self.mapa.objeto_en(destino)
        if objeto is not None:
            self._recoger(accion, objeto, destino)
        self._cerrar_turno(accion)
        return "Movimiento realizado."

    def esperar(self):
        """Pasa el turno sin mover el Cubo. O(k × V log V) para k enemigos."""
        if self.estado != EN_JUEGO:
            return PARTIDA_TERMINADA
        self._cerrar_turno(self._nueva_accion())
        return "El Cubo espera."

    def usar(self, identificador):
        """Usa una llave junto a una compuerta. O(n + k × V log V)."""
        if self.estado != EN_JUEGO:
            return PARTIDA_TERMINADA
        objeto = self.inventario.buscar(identificador)
        if objeto is None:
            return f"No tienes {identificador} en el inventario."
        if objeto.tipo != LLAVE:
            return "Ese objeto no se puede usar: los orbes ya sumaron sus puntos."
        compuerta = self.mapa.compuerta_vecina(self.cubo.celda)
        if compuerta is None:
            return "No hay una compuerta junto al Cubo."
        accion = self._nueva_accion()
        accion.ejecutar(ConsumirLlave(objeto), self)
        accion.ejecutar(AbrirCompuerta(compuerta), self)
        self._cerrar_turno(accion)
        return "Compuerta abierta."

    def soltar(self, identificador):
        """Deja un objeto en la celda del Cubo. O(n + k × V log V)."""
        if self.estado != EN_JUEGO:
            return PARTIDA_TERMINADA
        objeto = self.inventario.buscar(identificador)
        if objeto is None:
            return f"No tienes {identificador} en el inventario."
        if self.mapa.objeto_en(self.cubo.celda) is not None:
            return "Ya hay un objeto en esta celda."
        accion = self._nueva_accion()
        accion.ejecutar(Soltar(objeto, self.cubo.celda), self)
        if objeto.puntos:
            accion.ejecutar(SumarPuntos(-objeto.puntos), self)
        self._cerrar_turno(accion)
        return f"Soltaste {identificador}."

    def deshacer(self):
        """Revierte la última acción con todos sus efectos. O(k) para k cambios."""
        if self.historial.deshacer(self) is None:
            return "No hay qué deshacer."
        return "Retrocediste en el tiempo."

    def rehacer(self):
        """Repite la última acción deshecha. O(k) para k cambios."""
        if self.historial.rehacer(self) is None:
            return "No hay qué rehacer."
        return "Avanzaste en el tiempo."

    def buscar(self, identificador):
        """Describe una entidad por su id. O(1) promedio."""
        entidad = self.indice.buscar(identificador)
        if entidad is None:
            return f"No existe {identificador}."
        if entidad.celda is None:
            return f"{identificador}: {entidad.tipo}, en el inventario."
        return f"{identificador}: {entidad.tipo}, en {entidad.celda}."

    def comparar_busquedas(self):
        """Para cada Pájaro, celdas exploradas por BFS y por A* hacia el Cubo. O(k × V log V)."""
        filas = ListaEnlazada()
        for pajaro in self.enemigos:
            bfs = self.grafo.bfs(pajaro.celda, self.cubo.celda)
            guiada = self.grafo.a_estrella(pajaro.celda, self.cubo.celda)
            pasos = max(bfs.camino.tamano() - 1, 0)
            filas.agregar((pajaro.id, pasos, bfs.explorados, guiada.explorados))
        return filas

    def hay_pajaro_en(self, celda):
        """Indica si algún enemigo activo está en la celda. O(k)."""
        for pajaro in self.enemigos:
            if pajaro.celda == celda:
                return True
        return False

    def drenar_eventos(self):
        """Saca los eventos pendientes en orden y devuelve sus textos. O(e) para e eventos."""
        textos = ListaEnlazada()
        while not self.eventos.esta_vacia():
            textos.agregar(self.eventos.desencolar().texto())
        return textos

    def _cargar(self, plano):
        contadores = TablaHash()
        for fila, linea in enumerate(plano):
            for columna, simbolo in enumerate(linea):
                celda = (fila, columna)
                if simbolo == "C":
                    self.cubo = Entidad("C", CUBO, celda)
                    self._registrar(self.cubo)
                elif simbolo in ("R", "H"):
                    tipo = RASTREADOR if simbolo == "R" else CAZADOR
                    pajaro = Entidad(self._nuevo_id(contadores, simbolo), tipo, celda)
                    self.enemigos.insertar(pajaro)
                    self._registrar(pajaro)
                elif simbolo == "S":
                    self._centinelas.agregar(Entidad(self._nuevo_id(contadores, "S"), CENTINELA, celda))
                elif simbolo == "o":
                    self._colocar(Entidad(self._nuevo_id(contadores, "O"), ORBE, celda, PUNTOS_ORBE))
                elif simbolo == "k":
                    self._colocar(Entidad(self._nuevo_id(contadores, "K"), LLAVE, celda))
                elif simbolo in (PICO, COMPUERTA, PORTAL):
                    self.mapa.poner_terreno(celda, simbolo)

    @staticmethod
    def _nuevo_id(contadores, letra):
        numero = (contadores.buscar(letra) or 0) + 1
        contadores.insertar(letra, numero)
        return f"{letra}{numero}"

    def _registrar(self, entidad):
        self.indice.insertar(entidad.id, entidad)
        self._anunciar(entidad)

    def _anunciar(self, entidad):
        self.eventos.encolar(Evento(APARICION, self.turno, entidad.celda, f"Aparece {entidad.id}"))

    def _colocar(self, objeto):
        self.mapa.poner_objeto(objeto.celda, objeto)
        self._registrar(objeto)

    def _nueva_accion(self):
        accion = Accion()
        accion.ejecutar(SumarTurno(), self)
        return accion

    def _recoger(self, accion, objeto, celda):
        accion.ejecutar(Recoger(objeto, celda), self)
        if objeto.puntos:
            accion.ejecutar(SumarPuntos(objeto.puntos), self)
        self.eventos.encolar(Evento(RECOLECCION, self.turno, celda, f"Recogiste {objeto.id}"))
        if objeto.tipo == LLAVE:
            self._despertar_centinela(accion)

    def _despertar_centinela(self, accion):
        for centinela in self._centinelas:
            dormido = not self.indice.contiene(centinela.id)
            libre = centinela.celda != self.cubo.celda and not self.hay_pajaro_en(centinela.celda)
            if dormido and libre:
                accion.ejecutar(AparecerEnemigo(centinela), self)
                self._anunciar(centinela)
                return

    def _cerrar_turno(self, accion):
        self._revisar_fin(accion)
        if self.estado == EN_JUEGO:
            self._mover_enemigos(accion)
            self._revisar_fin(accion)
        self.historial.registrar(accion)

    def _mover_enemigos(self, accion):
        for _ in range(self.enemigos.tamano()):
            pajaro = self.enemigos.siguiente()
            if pajaro.desde_turno > self.turno:
                continue  # el Centinela recién aparecido espera un turno
            guiado = pajaro.tipo == CAZADOR
            paso = self.grafo.siguiente_paso(pajaro.celda, self.cubo.celda, guiado)
            if paso is not None and not self.hay_pajaro_en(paso):
                accion.ejecutar(MoverEntidad(pajaro, pajaro.celda, paso), self)

    def _revisar_fin(self, accion):
        celda = self.cubo.celda
        if self.hay_pajaro_en(celda):
            self.eventos.encolar(Evento(COLISION, self.turno, celda, "Un Pájaro atrapó al Cubo"))
            accion.ejecutar(CambiarEstado(EN_JUEGO, DERROTA), self)
        elif self.mapa.terreno_en(celda) == PORTAL:
            accion.ejecutar(CambiarEstado(EN_JUEGO, VICTORIA), self)
