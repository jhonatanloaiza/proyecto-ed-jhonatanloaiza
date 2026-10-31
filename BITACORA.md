# Bitácora

## Entrega 1 · 14 oct 2026

- **Qué hice:** registro del proyecto, constitución, historias de usuario, priorización MoSCoW, decisión de estructuras, spec/plan/tasks del componente Pila e Historial, spec inicial del sistema y esqueleto del repositorio (`main.py` arranca, `pytest` corre).
- **Qué se dificultó:** separar en la spec el *qué* del *cómo* (no nombrar la estructura en los criterios), escribir criterios verificables para deshacer y rehacer con todos sus efectos, y decidir entre lista circular y cola para el orden de turnos.
- **Uso de IA:** usé un asistente de IA (Claude) para organizar el documento de registro, proponer la redacción inicial de historias, criterios y specs, y revisar las complejidades de la tabla de estructuras. Revisé cada decisión contra el enunciado y la ajusté a mi juego; el código de las estructuras lo escribiré y probaré yo, y no integraré nada que no pueda explicar línea por línea.

## Entrega 2 · 30 oct 2026

- **Qué hice:** implementé 7 de las 9 estructuras de la tabla de decisión (pila, cola, lista enlazada, lista circular, matriz, tabla hash y grafo con BFS) con sus specs, integradas al juego y accesibles desde `main.py`. El juego ya se puede jugar completo por consola: mover, recoger, usar, soltar, deshacer, rehacer, buscar, eventos, victoria y derrota. Hay 226 pruebas, cada una con su criterio en el docstring.
- **Qué se dificultó:** rehacer un turno debía repetir también lo que hicieron los Pájaros. El diseño de acciones separadas (`Mover`, `Recoger`) no lo resolvía, así que un turno pasó a ser una `Accion` compuesta de cambios reversibles (plan 1.1). También faltaba definir si usar y soltar gastan turno y qué pasa con los puntos de un orbe soltado (CA-41 a CA-43). El nivel debía poder ganarse: los Pájaros tienen la misma velocidad que el Cubo y un mapa mal armado los deja interceptarlo.
- **Uso de IA:** un asistente de IA (Claude) escribió una propuesta de specs, código y pruebas de esta entrega, a partir de la especificación del proyecto. **Esto corrige lo declarado en la Entrega 1**, donde dije que yo escribiría el código de las estructuras. Las pruebas y el código deben pasar por mi revisión línea por línea antes de la sustentación.
- **Entrega tardía:** la entrega se subió después del 28 de octubre.
