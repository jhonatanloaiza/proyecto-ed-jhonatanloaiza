# Bitácora

## Entrega 1 · 14 oct 2026

- **Qué hice:** registro del proyecto, constitución, historias de usuario, priorización MoSCoW, decisión de estructuras, spec/plan/tasks del componente Pila e Historial, spec inicial del sistema y esqueleto del repositorio (`main.py` arranca, `pytest` corre).
- **Qué se dificultó:** separar en la spec el *qué* del *cómo* (no nombrar la estructura en los criterios), escribir criterios verificables para deshacer y rehacer con todos sus efectos, y decidir entre lista circular y cola para el orden de turnos.
- **Uso de IA:** usé un asistente de IA (Claude) para organizar el documento de registro, proponer la redacción inicial de historias, criterios y specs, y revisar las complejidades de la tabla de estructuras. Revisé cada decisión contra el enunciado y la ajusté a mi juego; el código de las estructuras lo escribiré y probaré yo, y no integraré nada que no pueda explicar línea por línea.

## Entrega 2 · 30 oct 2026

- **Qué hice:** quedaron implementadas 7 de las 9 estructuras de la tabla de decisión (pila, cola, lista enlazada, lista circular, matriz, tabla hash y grafo con BFS) con sus specs, integradas al juego y accesibles desde `main.py`. El juego ya se puede jugar completo por consola: mover, recoger, usar, soltar, deshacer, rehacer, buscar, eventos, victoria y derrota. Hay 226 pruebas, cada una con su criterio en el docstring.
- **Qué se dificultó:** rehacer un turno debía repetir también lo que hicieron los Pájaros. El diseño de acciones separadas (`Mover`, `Recoger`) no lo resolvía, así que un turno pasó a ser una `Accion` compuesta de cambios reversibles (plan 1.1). También faltaba definir si usar y soltar gastan turno y qué pasa con los puntos de un orbe soltado (CA-41 a CA-43). El nivel debía poder ganarse: los Pájaros tienen la misma velocidad que el Cubo y un mapa mal armado los deja interceptarlo.
- **Uso de IA:** un asistente de IA (Claude) escribió una propuesta de specs, código y pruebas de esta entrega, a partir de la especificación del proyecto. **Esto corrige lo declarado en la Entrega 1**, donde dije que yo escribiría el código de las estructuras. Las pruebas y el código deben pasar por mi revisión línea por línea antes de la sustentación.
- **Entrega tardía:** la entrega se subió después del 28 de octubre.

## Entrega final · 13 nov 2026

- **Qué hice:** quedaron implementadas las 2 estructuras que faltaban (árbol AVL y montículo mínimo) y A* sobre el montículo, con sus specs. Se agregaron el Pájaro Centinela, el Pájaro Cazador, la tabla de mejores puntajes y la elección entre 3 niveles. Las 15 historias de usuario están terminadas y hay 310 pruebas con trazabilidad completa. `ANALISIS.md` incluye mediciones de BFS contra A* y de AVL contra montículo.
- **Qué se dificultó:** que el Centinela entrara a la lista circular a mitad de partida sin alterar el orden de los demás y que deshacer lo sacara del todo. Se resolvió con un cambio reversible (`AparecerEnemigo`) y un turno de espera (`desde_turno`). En el nivel 3, la pared que divide el mapa no llegaba hasta abajo y permitía rodear la primera compuerta. Los niveles 2 y 3 se validaron con una simulación: se ganan con una ruta directa y se pierden si el jugador solo espera.
- **Uso de IA:** como en la Entrega 2, un asistente de IA (Claude) escribió la propuesta de specs, código, pruebas y mediciones de esta entrega. Debo revisar cada módulo línea por línea antes de la sustentación.
- **Entrega tardía:** la entrega se subió después del 11 de noviembre.
