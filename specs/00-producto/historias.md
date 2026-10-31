# Historias de usuario

Formato: *Como* <rol>, *quiero* <acción>, *para* <valor>. Cada criterio de aceptación (CA) es verificable con una prueba.

| HU | Funcionalidad | Título | Prioridad |
| --- | --- | --- | --- |
| HU-01 | F-01 | Iniciar una partida | Must |
| HU-02 | F-02 | Mover al Cubo | Must |
| HU-03 | F-03 | Recoger objetos | Must |
| HU-04 | F-03 | Gestionar el inventario | Must |
| HU-05 | F-04 | Deshacer una jugada | Must |
| HU-06 | F-04 | Rehacer una jugada | Must |
| HU-07 | F-05 | Persecución de los Pájaros Rastreadores | Must |
| HU-08 | F-06 | Ver los eventos del turno en orden | Must |
| HU-09 | F-07 | Saber si gané o perdí | Must |
| HU-10 | F-08 | Buscar una entidad | Must |
| HU-11 | F-01 a F-08 | Jugar desde la consola | Must |
| HU-12 | F-08 | Consultar los mejores puntajes | Should |
| HU-13 | F-05 | Aparición del Pájaro Centinela | Should |
| HU-14 | F-05 | Pájaro Cazador con búsqueda guiada | Could |
| HU-15 | F-01 | Elegir nivel | Could |

---

## HU-01 · Iniciar una partida (F-01)

**Como** jugador, **quiero** iniciar una partida con el mapa, el Cubo, los enemigos y los objetos ya ubicados, **para** empezar a jugar de inmediato.

- **CA-01** Al iniciar, el mapa tiene al menos 20 × 20 celdas y los picos ocupan como máximo el 25 % de ellas.
- **CA-02** Al iniciar, hay exactamente un Cubo, al menos 2 Pájaros Rastreadores, al menos 1 orbe y un portal de salida, cada uno en una celda transitable distinta.
- **CA-03** Al iniciar, el contador de turnos está en 0, el inventario está vacío y no hay acciones para deshacer ni rehacer.

## HU-02 · Mover al Cubo (F-02)

**Como** jugador, **quiero** mover el Cubo una casilla arriba, abajo, izquierda o derecha, o esperar, **para** acercarme al portal esquivando peligros.

- **CA-04** Si la celda destino es transitable, el Cubo queda en ella y el turno avanza en 1.
- **CA-05** Si la celda destino está fuera del mapa o es un pico, el Cubo no se mueve, se informa el motivo y el turno no avanza.
- **CA-06** Si el jugador elige esperar, el Cubo no cambia de celda y el turno avanza en 1.

## HU-03 · Recoger objetos (F-03)

**Como** jugador, **quiero** recoger un orbe o una llave al pisar su celda, **para** sumar puntos y abrir compuertas.

- **CA-07** Al entrar en una celda con objeto, el objeto desaparece del mapa y queda al final del inventario.
- **CA-08** Recoger un orbe suma sus puntos al puntaje de la partida.

## HU-04 · Gestionar el inventario (F-03)

**Como** jugador, **quiero** listar, usar y soltar los objetos de mi inventario, **para** decidir cuándo aprovecharlos.

- **CA-09** Listar muestra los objetos en el orden en que se recogieron; con el inventario vacío se informa que está vacío.
- **CA-10** Usar una llave junto a una compuerta la abre y elimina la llave del inventario.
- **CA-11** Soltar un objeto lo elimina del inventario y lo deja en la celda actual del Cubo.
- **CA-12** Usar o soltar un objeto que no está en el inventario no cambia nada y se informa el error.
- **CA-41** Usar o soltar un objeto gasta el turno: los Pájaros avanzan y la acción se puede deshacer.
- **CA-42** Soltar un orbe resta sus puntos, para que recogerlo otra vez no los duplique.
- **CA-43** Un orbe no se puede usar, ni una llave lejos de una compuerta, ni soltar en una celda con otro objeto: no cambia nada, se informa el motivo y no se gasta el turno.

## HU-05 · Deshacer una jugada (F-04)

**Como** jugador, **quiero** deshacer mi última acción, **para** salir de una situación sin salida.

- **CA-13** Deshacer un movimiento devuelve al Cubo y a los Pájaros a las celdas que tenían antes de esa acción y resta 1 al turno.
- **CA-14** Deshacer una recogida devuelve el objeto a su celda, lo saca del inventario y resta sus puntos.
- **CA-15** Deshacer sin acciones previas no cambia nada y se informa que no hay qué deshacer.

## HU-06 · Rehacer una jugada (F-04)

**Como** jugador, **quiero** rehacer una acción que deshice, **para** recuperar una jugada si me arrepiento.

- **CA-16** Rehacer aplica de nuevo la última acción deshecha, con los mismos efectos que tuvo.
- **CA-17** Hacer una acción nueva después de deshacer elimina las acciones que se podían rehacer.
- **CA-18** Rehacer sin acciones deshechas no cambia nada y se informa que no hay qué rehacer.

## HU-07 · Persecución de los Pájaros Rastreadores (F-05)

**Como** jugador, **quiero** que cada Pájaro avance hacia mí por el camino más corto después de mi turno, **para** sentir la presión de una persecución real.

- **CA-19** Después de cada acción válida del jugador, cada Pájaro avanza exactamente una casilla por un camino de menos pasos hacia el Cubo.
- **CA-20** Ningún Pájaro entra en un pico ni sale del mapa.
- **CA-21** Si no existe camino hacia el Cubo, el Pájaro se queda en su celda.
- **CA-22** Los Pájaros se mueven en un orden fijo; si dos quieren la misma celda, el segundo espera.

## HU-08 · Ver los eventos del turno en orden (F-06)

**Como** jugador, **quiero** ver los eventos de cada turno en el orden en que ocurrieron, **para** entender qué pasó.

- **CA-23** Cada aparición, recolección y colisión genera un evento con el turno y la celda donde ocurrió.
- **CA-24** Al final del turno, los eventos se muestran y se procesan en el mismo orden en que se generaron.
- **CA-25** Un turno sin eventos no muestra la sección de eventos.

## HU-09 · Saber si gané o perdí (F-07)

**Como** jugador, **quiero** que el juego detecte la victoria o la derrota, **para** saber cuándo termina la partida.

- **CA-26** Si el Cubo llega a la celda del portal abierto, la partida termina con victoria y se muestra el resumen.
- **CA-27** Si un Pájaro ocupa la celda del Cubo, la partida termina con derrota.
- **CA-28** Terminada la partida, no se aceptan movimientos; solo deshacer, reiniciar o salir.

## HU-10 · Buscar una entidad (F-08)

**Como** jugador, **quiero** buscar una entidad por su identificador, **para** saber dónde está un enemigo u objeto.

- **CA-29** Buscar un identificador existente (por ejemplo `R1` u `O3`) muestra su tipo y su celda actual.
- **CA-30** Buscar un identificador inexistente informa que no existe.

## HU-11 · Jugar desde la consola (F-01 a F-08)

**Como** jugador, **quiero** ver el mapa dibujado en la consola y un menú de comandos, **para** usar todas las funciones del juego.

- **CA-31** Después de cada turno se dibuja el mapa con un símbolo por tipo de elemento, el turno, el puntaje y el inventario.
- **CA-32** Un comando no reconocido no cambia el estado y muestra la lista de comandos válidos.

## HU-12 · Consultar los mejores puntajes (F-08) · Should

**Como** jugador, **quiero** ver la tabla de mejores puntajes, **para** comparar mis partidas.

- **CA-33** Al terminar una partida, su puntaje se registra.
- **CA-34** La tabla muestra los puntajes de mayor a menor; sin partidas registradas informa que está vacía.

## HU-13 · Aparición del Pájaro Centinela (F-05) · Should

**Como** jugador, **quiero** que recoger una llave despierte a un Pájaro Centinela, **para** que avanzar tenga un costo.

- **CA-35** Al recoger una llave se genera un evento de aparición y el Centinela entra al orden de turnos a partir del turno siguiente.
- **CA-36** Si se deshace la recogida de la llave, el Centinela desaparece del mapa y del orden de turnos.

## HU-14 · Pájaro Cazador con búsqueda guiada (F-05) · Could

**Como** jugador, **quiero** enfrentar a un Pájaro que use una búsqueda guiada, **para** tener un reto mayor en el último nivel.

- **CA-37** El Cazador encuentra un camino de la misma longitud que el de menos pasos.
- **CA-38** En el mismo mapa, se muestra cuántas celdas exploró el Cazador frente a la búsqueda en anchura.

## HU-15 · Elegir nivel (F-01) · Could

**Como** jugador, **quiero** elegir entre los niveles 1, 2 y 3, **para** jugar con distinta dificultad.

- **CA-39** Al elegir un nivel, la partida inicia con los picos, enemigos y objetos de ese nivel.
- **CA-40** Elegir un nivel inexistente informa el error y vuelve al menú.

## Historial de cambios

| Versión | Fecha | Cambio |
| --- | --- | --- |
| 1.0 | 2026-10-14 | Versión inicial para la Entrega 1. |
| 1.1 | 2026-10-30 | Se agregan CA-41 a CA-43: al implementar, HU-04 no decía si usar y soltar gastan turno, qué pasa con los puntos de un orbe soltado ni qué hacen los usos inválidos. |
