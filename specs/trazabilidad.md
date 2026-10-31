# Trazabilidad criterio ↔ prueba ↔ código

Generada a partir de los docstrings de `tests/`. CA-33 a CA-40 (Should y Could) aún no tienen prueba: se implementan en la Entrega final.

## De criterio a prueba y código

| Criterio | Pruebas | Código |
| --- | --- | --- |
| CA-01 | `test_partida.py::test_inicio_mapa_y_picos` | `dominio/partida.py` |
| CA-02 | `test_partida.py::test_inicio_entidades` | `dominio/partida.py` |
| CA-03 | `test_partida.py::test_inicio_contadores` | `dominio/partida.py` |
| CA-04 | `test_partida.py::test_mover_a_celda_libre` | `dominio/partida.py` |
| CA-05 | `test_partida.py::test_mover_fuera_del_mapa`<br>`test_partida.py::test_mover_a_un_pico`<br>`test_partida.py::test_mover_a_compuerta_cerrada` | `dominio/partida.py` |
| CA-06 | `test_partida.py::test_esperar_avanza_el_turno` | `dominio/partida.py` |
| CA-07 | `test_partida.py::test_recoger_orbe` | `dominio/partida.py` |
| CA-08 | `test_partida.py::test_recoger_orbe_suma_puntos` | `dominio/partida.py` |
| CA-09 | `test_main.py::test_listar_inventario_vacio`<br>`test_main.py::test_listar_inventario_en_orden` | `main.py` |
| CA-10 | `test_partida.py::test_usar_llave_abre_la_compuerta` | `dominio/partida.py` |
| CA-11 | `test_partida.py::test_soltar_deja_el_objeto_en_la_celda` | `dominio/partida.py` |
| CA-12 | `test_partida.py::test_inventario_vacio_al_soltar`<br>`test_partida.py::test_usar_inexistente` | `dominio/partida.py` |
| CA-13 | `test_partida.py::test_deshacer_movimiento` | `dominio/partida.py` |
| CA-14 | `test_partida.py::test_deshacer_recogida` | `dominio/partida.py` |
| CA-15 | `test_partida.py::test_deshacer_sin_acciones` | `dominio/partida.py` |
| CA-16 | `test_partida.py::test_rehacer_repite_los_mismos_efectos` | `dominio/partida.py` |
| CA-17 | `test_partida.py::test_accion_nueva_borra_rehacer` | `dominio/partida.py` |
| CA-18 | `test_partida.py::test_rehacer_sin_acciones` | `dominio/partida.py` |
| CA-19 | `test_partida.py::test_esperar_mueve_a_los_pajaros`<br>`test_partida.py::test_pajaro_avanza_una_casilla_por_camino_corto` | `dominio/partida.py` |
| CA-20 | `test_partida.py::test_pajaro_no_entra_en_picos` | `dominio/partida.py` |
| CA-21 | `test_partida.py::test_pajaro_sin_camino_no_se_mueve` | `dominio/partida.py` |
| CA-22 | `test_partida.py::test_pajaros_no_ocupan_la_misma_celda`<br>`test_partida.py::test_pajaros_orden_fijo` | `dominio/partida.py` |
| CA-23 | `test_partida.py::test_eventos_de_recoleccion_con_turno_y_celda`<br>`test_partida.py::test_eventos_de_aparicion_y_colision` | `dominio/partida.py` |
| CA-24 | `test_partida.py::test_eventos_en_orden` | `dominio/partida.py` |
| CA-25 | `test_partida.py::test_turno_sin_eventos` | `dominio/partida.py` |
| CA-26 | `test_partida.py::test_victoria_en_el_portal`<br>`test_partida.py::test_nivel_se_puede_ganar_por_el_camino_corto` | `dominio/partida.py` |
| CA-27 | `test_partida.py::test_derrota_si_el_pajaro_llega`<br>`test_partida.py::test_derrota_si_el_cubo_entra_a_la_celda_del_pajaro`<br>`test_partida.py::test_nivel_esperar_lleva_a_la_derrota` | `dominio/partida.py` |
| CA-28 | `test_partida.py::test_esperar_con_partida_terminada`<br>`test_partida.py::test_partida_terminada_no_acepta_movimientos`<br>`test_partida.py::test_partida_terminada_permite_deshacer` | `dominio/partida.py` |
| CA-29 | `test_partida.py::test_buscar_entidad_existente`<br>`test_partida.py::test_buscar_objeto_en_inventario` | `dominio/partida.py` |
| CA-30 | `test_partida.py::test_buscar_inexistente` | `dominio/partida.py` |
| CA-31 | `test_main.py::test_dibujar_un_simbolo_por_elemento`<br>`test_main.py::test_dibujar_muestra_turno_puntaje_e_inventario`<br>`test_main.py::test_dibujar_con_color`<br>`test_main.py::test_comandos_ejercitan_el_juego` | `main.py` |
| CA-32 | `test_main.py::test_menu_muestra_opciones`<br>`test_main.py::test_salir_devuelve_none`<br>`test_main.py::test_opcion_invalida`<br>`test_main.py::test_comando_no_reconocido`<br>`test_main.py::test_comando_vacio`<br>`test_main.py::test_comando_sin_identificador` | `main.py` |
| CA-41 | `test_partida.py::test_soltar_gasta_turno_y_se_puede_deshacer`<br>`test_partida.py::test_deshacer_llave_cierra_la_compuerta` | `dominio/partida.py` |
| CA-42 | `test_partida.py::test_soltar_orbe_resta_puntos` | `dominio/partida.py` |
| CA-43 | `test_partida.py::test_soltar_en_celda_ocupada`<br>`test_partida.py::test_usar_orbe_no_cambia_nada`<br>`test_partida.py::test_usar_llave_lejos_de_compuerta` | `dominio/partida.py` |
| CA-CIR-01 | `test_lista_circular.py::test_siguiente_vuelve_al_primero` | `estructuras/lista_circular.py` |
| CA-CIR-02 | `test_lista_circular.py::test_siguiente_un_elemento` | `estructuras/lista_circular.py` |
| CA-CIR-03 | `test_lista_circular.py::test_siguiente_vacia_lanza_error` | `estructuras/lista_circular.py` |
| CA-CIR-04 | `test_lista_circular.py::test_insertar_en_lista_vacia`<br>`test_lista_circular.py::test_insertar_a_mitad_de_ciclo`<br>`test_lista_circular.py::test_insertar_conserva_el_orden` | `estructuras/lista_circular.py` |
| CA-CIR-05 | `test_lista_circular.py::test_quitar_el_primero`<br>`test_lista_circular.py::test_quitar_el_ultimo`<br>`test_lista_circular.py::test_quitar_el_actual`<br>`test_lista_circular.py::test_quitar_el_unico` | `estructuras/lista_circular.py` |
| CA-CIR-06 | `test_lista_circular.py::test_quitar_inexistente`<br>`test_lista_circular.py::test_quitar_de_lista_vacia` | `estructuras/lista_circular.py` |
| CA-CIR-07 | `test_lista_circular.py::test_tamano_vacia`<br>`test_lista_circular.py::test_tamano_refleja_cambios`<br>`test_lista_circular.py::test_tamano_no_cambia_con_siguiente`<br>`test_lista_circular.py::test_esta_vacia_nueva`<br>`test_lista_circular.py::test_esta_vacia_con_elemento`<br>`test_lista_circular.py::test_esta_vacia_tras_quitar` | `estructuras/lista_circular.py` |
| CA-CIR-08 | `test_lista_circular.py::test_recorrido_en_orden`<br>`test_lista_circular.py::test_recorrido_vacia`<br>`test_lista_circular.py::test_recorrido_no_mueve_el_turno` | `estructuras/lista_circular.py` |
| CA-COL-01 | `test_cola.py::test_encolar_uno`<br>`test_cola.py::test_encolar_varios_conserva_el_frente`<br>`test_cola.py::test_encolar_repetidos`<br>`test_cola.py::test_desencolar_en_orden_de_llegada`<br>`test_cola.py::test_desencolar_un_solo_elemento` | `estructuras/cola.py` |
| CA-COL-02 | `test_cola.py::test_frente_no_quita`<br>`test_cola.py::test_frente_con_un_elemento` | `estructuras/cola.py` |
| CA-COL-03 | `test_cola.py::test_desencolar_vacia_lanza_error`<br>`test_cola.py::test_frente_vacia_lanza_error` | `estructuras/cola.py` |
| CA-COL-04 | `test_cola.py::test_reutilizar_tras_vaciarse` | `estructuras/cola.py` |
| CA-COL-05 | `test_cola.py::test_esta_vacia_nueva`<br>`test_cola.py::test_esta_vacia_con_elemento`<br>`test_cola.py::test_esta_vacia_tras_desencolar`<br>`test_cola.py::test_tamano_vacia`<br>`test_cola.py::test_tamano_crece_y_baja`<br>`test_cola.py::test_tamano_un_elemento` | `estructuras/cola.py` |
| CA-GRA-01 | `test_grafo.py::test_vecinos_en_el_centro`<br>`test_grafo.py::test_vecinos_en_la_esquina`<br>`test_grafo.py::test_vecinos_evita_no_transitables` | `estructuras/grafo.py` |
| CA-GRA-02 | `test_grafo.py::test_bfs_camino_mas_corto_sin_obstaculos`<br>`test_grafo.py::test_bfs_rodea_obstaculos` | `estructuras/grafo.py` |
| CA-GRA-03 | `test_grafo.py::test_bfs_cada_paso_es_contiguo_y_transitable` | `estructuras/grafo.py` |
| CA-GRA-04 | `test_grafo.py::test_bfs_sin_camino` | `estructuras/grafo.py` |
| CA-GRA-05 | `test_grafo.py::test_bfs_origen_igual_a_destino` | `estructuras/grafo.py` |
| CA-GRA-06 | `test_grafo.py::test_explorados_origen_igual_a_destino`<br>`test_grafo.py::test_explorados_sin_camino_cuenta_la_region`<br>`test_grafo.py::test_explorados_no_repite_celdas` | `estructuras/grafo.py` |
| CA-GRA-07 | `test_grafo.py::test_siguiente_paso_primer_paso`<br>`test_grafo.py::test_siguiente_paso_ya_llego`<br>`test_grafo.py::test_siguiente_paso_sin_camino` | `estructuras/grafo.py` |
| CA-HAS-01 | `test_tabla_hash.py::test_insertar_y_buscar`<br>`test_tabla_hash.py::test_insertar_varias_claves` | `estructuras/tabla_hash.py` |
| CA-HAS-02 | `test_tabla_hash.py::test_insertar_clave_existente_reemplaza` | `estructuras/tabla_hash.py` |
| CA-HAS-03 | `test_tabla_hash.py::test_buscar_inexistente`<br>`test_tabla_hash.py::test_buscar_en_tabla_vacia`<br>`test_tabla_hash.py::test_eliminar_inexistente`<br>`test_tabla_hash.py::test_eliminar_en_tabla_vacia` | `estructuras/tabla_hash.py` |
| CA-HAS-04 | `test_tabla_hash.py::test_buscar_con_colision`<br>`test_tabla_hash.py::test_colisiones_se_eliminan_por_separado`<br>`test_tabla_hash.py::test_colisiones_eliminar_la_mas_antigua` | `estructuras/tabla_hash.py` |
| CA-HAS-05 | `test_tabla_hash.py::test_crecer_conserva_las_claves`<br>`test_tabla_hash.py::test_crecer_aumenta_las_cubetas` | `estructuras/tabla_hash.py` |
| CA-HAS-06 | `test_tabla_hash.py::test_eliminar_existente`<br>`test_tabla_hash.py::test_contiene_existente`<br>`test_tabla_hash.py::test_contiene_inexistente`<br>`test_tabla_hash.py::test_contiene_tras_eliminar`<br>`test_tabla_hash.py::test_tamano_vacia`<br>`test_tabla_hash.py::test_tamano_un_elemento`<br>`test_tabla_hash.py::test_tamano_tras_eliminar_todo` | `estructuras/tabla_hash.py` |
| CA-HIS-01 | `test_historial.py::test_deshacer_revierte_la_mas_reciente`<br>`test_historial.py::test_deshacer_devuelve_la_accion` | `dominio/historial.py` |
| CA-HIS-02 | `test_historial.py::test_rehacer_restaura_el_estado`<br>`test_historial.py::test_rehacer_devuelve_a_deshacer`<br>`test_historial.py::test_puede_rehacer_tras_deshacer` | `dominio/historial.py` |
| CA-HIS-03 | `test_historial.py::test_registrar_permite_deshacer`<br>`test_historial.py::test_registrar_no_habilita_rehacer`<br>`test_historial.py::test_registrar_tras_deshacer_borra_rehacer` | `dominio/historial.py` |
| CA-HIS-04 | `test_historial.py::test_deshacer_sin_acciones`<br>`test_historial.py::test_rehacer_sin_acciones`<br>`test_historial.py::test_puede_deshacer_nuevo`<br>`test_historial.py::test_puede_deshacer_tras_agotar`<br>`test_historial.py::test_puede_rehacer_nuevo` | `dominio/historial.py` |
| CA-HIS-05 | `test_historial.py::test_secuencia_deshacer_y_rehacer_n` | `dominio/historial.py` |
| CA-INV-01 | `test_inventario.py::test_agregar_en_orden_de_recogida`<br>`test_inventario.py::test_recorrido_vacio`<br>`test_inventario.py::test_agregar_llave`<br>`test_inventario.py::test_buscar_existente`<br>`test_inventario.py::test_tamano_con_objetos` | `dominio/inventario.py` |
| CA-INV-02 | `test_inventario.py::test_buscar_inexistente`<br>`test_inventario.py::test_buscar_en_vacio`<br>`test_inventario.py::test_quitar_inexistente`<br>`test_inventario.py::test_quitar_en_vacio`<br>`test_inventario.py::test_tamano_vacio` | `dominio/inventario.py` |
| CA-INV-03 | `test_inventario.py::test_quitar_devuelve_objeto_y_posicion`<br>`test_inventario.py::test_insertar_en_devuelve_a_su_posicion`<br>`test_inventario.py::test_insertar_en_primera_posicion`<br>`test_inventario.py::test_insertar_en_inventario_vacio`<br>`test_inventario.py::test_tamano_tras_quitar` | `dominio/inventario.py` |
| CA-LIS-01 | `test_lista_enlazada.py::test_agregar_conserva_el_orden`<br>`test_lista_enlazada.py::test_agregar_a_lista_vacia`<br>`test_lista_enlazada.py::test_agregar_repetidos`<br>`test_lista_enlazada.py::test_recorrer_lista_vacia` | `estructuras/lista_enlazada.py` |
| CA-LIS-02 | `test_lista_enlazada.py::test_insertar_al_inicio`<br>`test_lista_enlazada.py::test_insertar_en_el_medio`<br>`test_lista_enlazada.py::test_insertar_al_final_y_agregar`<br>`test_lista_enlazada.py::test_insertar_en_lista_vacia` | `estructuras/lista_enlazada.py` |
| CA-LIS-03 | `test_lista_enlazada.py::test_quitar_al_inicio`<br>`test_lista_enlazada.py::test_quitar_en_el_medio`<br>`test_lista_enlazada.py::test_quitar_el_ultimo_y_agregar`<br>`test_lista_enlazada.py::test_quitar_unico_y_agregar` | `estructuras/lista_enlazada.py` |
| CA-LIS-04 | `test_lista_enlazada.py::test_insertar_posicion_invalida`<br>`test_lista_enlazada.py::test_quitar_posicion_invalida`<br>`test_lista_enlazada.py::test_quitar_en_lista_vacia` | `estructuras/lista_enlazada.py` |
| CA-LIS-05 | `test_lista_enlazada.py::test_buscar_encuentra_el_primero`<br>`test_lista_enlazada.py::test_buscar_inexistente`<br>`test_lista_enlazada.py::test_buscar_en_lista_vacia` | `estructuras/lista_enlazada.py` |
| CA-LIS-06 | `test_lista_enlazada.py::test_tamano_vacia`<br>`test_lista_enlazada.py::test_tamano_un_elemento`<br>`test_lista_enlazada.py::test_tamano_tras_quitar`<br>`test_lista_enlazada.py::test_esta_vacia_nueva`<br>`test_lista_enlazada.py::test_esta_vacia_con_elemento`<br>`test_lista_enlazada.py::test_esta_vacia_tras_quitar` | `estructuras/lista_enlazada.py` |
| CA-MAT-01 | `test_matriz.py::test_crear_valor_inicial_en_esquinas`<br>`test_matriz.py::test_crear_sin_valor_inicial` | `estructuras/matriz.py` |
| CA-MAT-02 | `test_matriz.py::test_consultar_devuelve_lo_asignado`<br>`test_matriz.py::test_consultar_ultima_celda`<br>`test_matriz.py::test_asignar_no_toca_otras_celdas`<br>`test_matriz.py::test_asignar_reemplaza` | `estructuras/matriz.py` |
| CA-MAT-03 | `test_matriz.py::test_consultar_fuera_de_rango`<br>`test_matriz.py::test_asignar_fuera_de_rango` | `estructuras/matriz.py` |
| CA-MAT-04 | `test_matriz.py::test_dentro_esquinas`<br>`test_matriz.py::test_dentro_justo_afuera` | `estructuras/matriz.py` |
| CA-MAT-05 | `test_matriz.py::test_crear_tamano_invalido` | `estructuras/matriz.py` |
| CA-MAT-06 | `test_matriz.py::test_dimensiones_no_cuadrada`<br>`test_matriz.py::test_dimensiones_uno_por_uno`<br>`test_matriz.py::test_dimensiones_del_juego` | `estructuras/matriz.py` |
| CA-PIL-01 | `test_pila.py::test_pila_con_elemento_no_esta_vacia`<br>`test_pila.py::test_apilar_deja_el_valor_en_la_cima`<br>`test_pila.py::test_apilar_aumenta_el_tamano`<br>`test_pila.py::test_apilar_acepta_none_y_duplicados`<br>`test_pila.py::test_cima_no_quita_el_elemento` | `estructuras/pila.py` |
| CA-PIL-02 | `test_pila.py::test_desapilar_en_orden_inverso`<br>`test_pila.py::test_desapilar_reduce_el_tamano` | `estructuras/pila.py` |
| CA-PIL-03 | `test_pila.py::test_vacia_desapilar_lanza_error`<br>`test_pila.py::test_vacia_cima_lanza_error`<br>`test_pila.py::test_vacia_error_no_cambia_la_pila` | `estructuras/pila.py` |
| CA-PIL-04 | `test_pila.py::test_pila_nueva_esta_vacia`<br>`test_pila.py::test_pila_nueva_tamano_cero`<br>`test_pila.py::test_vaciar_con_elementos`<br>`test_pila.py::test_vaciar_pila_vacia`<br>`test_pila.py::test_vaciar_permite_reutilizar` | `estructuras/pila.py` |
| CA-PIL-05 | `test_pila.py::test_desapilar_un_solo_elemento` | `estructuras/pila.py` |

## De prueba a criterio

| Prueba | Criterios |
| --- | --- |
| `test_cola.py::test_encolar_uno` | CA-COL-01 |
| `test_cola.py::test_encolar_varios_conserva_el_frente` | CA-COL-01 |
| `test_cola.py::test_encolar_repetidos` | CA-COL-01 |
| `test_cola.py::test_desencolar_en_orden_de_llegada` | CA-COL-01 |
| `test_cola.py::test_desencolar_un_solo_elemento` | CA-COL-01 |
| `test_cola.py::test_desencolar_vacia_lanza_error` | CA-COL-03 |
| `test_cola.py::test_frente_no_quita` | CA-COL-02 |
| `test_cola.py::test_frente_con_un_elemento` | CA-COL-02 |
| `test_cola.py::test_frente_vacia_lanza_error` | CA-COL-03 |
| `test_cola.py::test_reutilizar_tras_vaciarse` | CA-COL-04 |
| `test_cola.py::test_esta_vacia_nueva` | CA-COL-05 |
| `test_cola.py::test_esta_vacia_con_elemento` | CA-COL-05 |
| `test_cola.py::test_esta_vacia_tras_desencolar` | CA-COL-05 |
| `test_cola.py::test_tamano_vacia` | CA-COL-05 |
| `test_cola.py::test_tamano_crece_y_baja` | CA-COL-05 |
| `test_cola.py::test_tamano_un_elemento` | CA-COL-05 |
| `test_grafo.py::test_vecinos_en_el_centro` | CA-GRA-01 |
| `test_grafo.py::test_vecinos_en_la_esquina` | CA-GRA-01 |
| `test_grafo.py::test_vecinos_evita_no_transitables` | CA-GRA-01 |
| `test_grafo.py::test_bfs_camino_mas_corto_sin_obstaculos` | CA-GRA-02 |
| `test_grafo.py::test_bfs_rodea_obstaculos` | CA-GRA-02 |
| `test_grafo.py::test_bfs_cada_paso_es_contiguo_y_transitable` | CA-GRA-03 |
| `test_grafo.py::test_bfs_sin_camino` | CA-GRA-04 |
| `test_grafo.py::test_bfs_origen_igual_a_destino` | CA-GRA-05 |
| `test_grafo.py::test_explorados_origen_igual_a_destino` | CA-GRA-06 |
| `test_grafo.py::test_explorados_sin_camino_cuenta_la_region` | CA-GRA-06 |
| `test_grafo.py::test_explorados_no_repite_celdas` | CA-GRA-06 |
| `test_grafo.py::test_siguiente_paso_primer_paso` | CA-GRA-07 |
| `test_grafo.py::test_siguiente_paso_ya_llego` | CA-GRA-07 |
| `test_grafo.py::test_siguiente_paso_sin_camino` | CA-GRA-07 |
| `test_historial.py::test_registrar_permite_deshacer` | CA-HIS-03 |
| `test_historial.py::test_registrar_no_habilita_rehacer` | CA-HIS-03 |
| `test_historial.py::test_registrar_tras_deshacer_borra_rehacer` | CA-HIS-03 |
| `test_historial.py::test_deshacer_revierte_la_mas_reciente` | CA-HIS-01 |
| `test_historial.py::test_deshacer_devuelve_la_accion` | CA-HIS-01 |
| `test_historial.py::test_deshacer_sin_acciones` | CA-HIS-04 |
| `test_historial.py::test_rehacer_restaura_el_estado` | CA-HIS-02 |
| `test_historial.py::test_rehacer_devuelve_a_deshacer` | CA-HIS-02 |
| `test_historial.py::test_rehacer_sin_acciones` | CA-HIS-04 |
| `test_historial.py::test_secuencia_deshacer_y_rehacer_n` | CA-HIS-05 |
| `test_historial.py::test_puede_deshacer_nuevo` | CA-HIS-04 |
| `test_historial.py::test_puede_deshacer_tras_agotar` | CA-HIS-04 |
| `test_historial.py::test_puede_rehacer_nuevo` | CA-HIS-04 |
| `test_historial.py::test_puede_rehacer_tras_deshacer` | CA-HIS-02 |
| `test_inventario.py::test_agregar_en_orden_de_recogida` | CA-INV-01 |
| `test_inventario.py::test_recorrido_vacio` | CA-INV-01 |
| `test_inventario.py::test_agregar_llave` | CA-INV-01 |
| `test_inventario.py::test_buscar_existente` | CA-INV-01 |
| `test_inventario.py::test_buscar_inexistente` | CA-INV-02 |
| `test_inventario.py::test_buscar_en_vacio` | CA-INV-02 |
| `test_inventario.py::test_quitar_devuelve_objeto_y_posicion` | CA-INV-03 |
| `test_inventario.py::test_quitar_inexistente` | CA-INV-02 |
| `test_inventario.py::test_quitar_en_vacio` | CA-INV-02 |
| `test_inventario.py::test_insertar_en_devuelve_a_su_posicion` | CA-INV-03 |
| `test_inventario.py::test_insertar_en_primera_posicion` | CA-INV-03 |
| `test_inventario.py::test_insertar_en_inventario_vacio` | CA-INV-03 |
| `test_inventario.py::test_tamano_vacio` | CA-INV-02 |
| `test_inventario.py::test_tamano_con_objetos` | CA-INV-01 |
| `test_inventario.py::test_tamano_tras_quitar` | CA-INV-03 |
| `test_lista_circular.py::test_siguiente_vuelve_al_primero` | CA-CIR-01 |
| `test_lista_circular.py::test_siguiente_un_elemento` | CA-CIR-02 |
| `test_lista_circular.py::test_siguiente_vacia_lanza_error` | CA-CIR-03 |
| `test_lista_circular.py::test_insertar_en_lista_vacia` | CA-CIR-04 |
| `test_lista_circular.py::test_insertar_a_mitad_de_ciclo` | CA-CIR-04 |
| `test_lista_circular.py::test_insertar_conserva_el_orden` | CA-CIR-04 |
| `test_lista_circular.py::test_quitar_el_primero` | CA-CIR-05 |
| `test_lista_circular.py::test_quitar_el_ultimo` | CA-CIR-05 |
| `test_lista_circular.py::test_quitar_el_actual` | CA-CIR-05 |
| `test_lista_circular.py::test_quitar_el_unico` | CA-CIR-05 |
| `test_lista_circular.py::test_quitar_inexistente` | CA-CIR-06 |
| `test_lista_circular.py::test_quitar_de_lista_vacia` | CA-CIR-06 |
| `test_lista_circular.py::test_tamano_vacia` | CA-CIR-07 |
| `test_lista_circular.py::test_tamano_refleja_cambios` | CA-CIR-07 |
| `test_lista_circular.py::test_tamano_no_cambia_con_siguiente` | CA-CIR-07 |
| `test_lista_circular.py::test_esta_vacia_nueva` | CA-CIR-07 |
| `test_lista_circular.py::test_esta_vacia_con_elemento` | CA-CIR-07 |
| `test_lista_circular.py::test_esta_vacia_tras_quitar` | CA-CIR-07 |
| `test_lista_circular.py::test_recorrido_en_orden` | CA-CIR-08 |
| `test_lista_circular.py::test_recorrido_vacia` | CA-CIR-08 |
| `test_lista_circular.py::test_recorrido_no_mueve_el_turno` | CA-CIR-08 |
| `test_lista_enlazada.py::test_agregar_conserva_el_orden` | CA-LIS-01 |
| `test_lista_enlazada.py::test_agregar_a_lista_vacia` | CA-LIS-01 |
| `test_lista_enlazada.py::test_agregar_repetidos` | CA-LIS-01 |
| `test_lista_enlazada.py::test_recorrer_lista_vacia` | CA-LIS-01 |
| `test_lista_enlazada.py::test_insertar_al_inicio` | CA-LIS-02 |
| `test_lista_enlazada.py::test_insertar_en_el_medio` | CA-LIS-02 |
| `test_lista_enlazada.py::test_insertar_al_final_y_agregar` | CA-LIS-02 |
| `test_lista_enlazada.py::test_insertar_en_lista_vacia` | CA-LIS-02 |
| `test_lista_enlazada.py::test_insertar_posicion_invalida` | CA-LIS-04 |
| `test_lista_enlazada.py::test_quitar_al_inicio` | CA-LIS-03 |
| `test_lista_enlazada.py::test_quitar_en_el_medio` | CA-LIS-03 |
| `test_lista_enlazada.py::test_quitar_el_ultimo_y_agregar` | CA-LIS-03 |
| `test_lista_enlazada.py::test_quitar_unico_y_agregar` | CA-LIS-03 |
| `test_lista_enlazada.py::test_quitar_posicion_invalida` | CA-LIS-04 |
| `test_lista_enlazada.py::test_quitar_en_lista_vacia` | CA-LIS-04 |
| `test_lista_enlazada.py::test_buscar_encuentra_el_primero` | CA-LIS-05 |
| `test_lista_enlazada.py::test_buscar_inexistente` | CA-LIS-05 |
| `test_lista_enlazada.py::test_buscar_en_lista_vacia` | CA-LIS-05 |
| `test_lista_enlazada.py::test_tamano_vacia` | CA-LIS-06 |
| `test_lista_enlazada.py::test_tamano_un_elemento` | CA-LIS-06 |
| `test_lista_enlazada.py::test_tamano_tras_quitar` | CA-LIS-06 |
| `test_lista_enlazada.py::test_esta_vacia_nueva` | CA-LIS-06 |
| `test_lista_enlazada.py::test_esta_vacia_con_elemento` | CA-LIS-06 |
| `test_lista_enlazada.py::test_esta_vacia_tras_quitar` | CA-LIS-06 |
| `test_main.py::test_menu_muestra_opciones` | CA-32 |
| `test_main.py::test_salir_devuelve_none` | CA-32 |
| `test_main.py::test_opcion_invalida` | CA-32 |
| `test_main.py::test_dibujar_un_simbolo_por_elemento` | CA-31 |
| `test_main.py::test_dibujar_muestra_turno_puntaje_e_inventario` | CA-31 |
| `test_main.py::test_dibujar_con_color` | CA-31 |
| `test_main.py::test_comando_no_reconocido` | CA-32 |
| `test_main.py::test_comando_vacio` | CA-32 |
| `test_main.py::test_comando_sin_identificador` | CA-32 |
| `test_main.py::test_comandos_ejercitan_el_juego` | CA-31 |
| `test_main.py::test_listar_inventario_vacio` | CA-09 |
| `test_main.py::test_listar_inventario_en_orden` | CA-09 |
| `test_matriz.py::test_crear_valor_inicial_en_esquinas` | CA-MAT-01 |
| `test_matriz.py::test_crear_sin_valor_inicial` | CA-MAT-01 |
| `test_matriz.py::test_crear_tamano_invalido` | CA-MAT-05 |
| `test_matriz.py::test_consultar_devuelve_lo_asignado` | CA-MAT-02 |
| `test_matriz.py::test_consultar_ultima_celda` | CA-MAT-02 |
| `test_matriz.py::test_consultar_fuera_de_rango` | CA-MAT-03 |
| `test_matriz.py::test_asignar_no_toca_otras_celdas` | CA-MAT-02 |
| `test_matriz.py::test_asignar_reemplaza` | CA-MAT-02 |
| `test_matriz.py::test_asignar_fuera_de_rango` | CA-MAT-03 |
| `test_matriz.py::test_dentro_esquinas` | CA-MAT-04 |
| `test_matriz.py::test_dentro_justo_afuera` | CA-MAT-04 |
| `test_matriz.py::test_dimensiones_no_cuadrada` | CA-MAT-06 |
| `test_matriz.py::test_dimensiones_uno_por_uno` | CA-MAT-06 |
| `test_matriz.py::test_dimensiones_del_juego` | CA-MAT-06 |
| `test_partida.py::test_inicio_mapa_y_picos` | CA-01 |
| `test_partida.py::test_inicio_entidades` | CA-02 |
| `test_partida.py::test_inicio_contadores` | CA-03 |
| `test_partida.py::test_mover_a_celda_libre` | CA-04 |
| `test_partida.py::test_mover_fuera_del_mapa` | CA-05 |
| `test_partida.py::test_mover_a_un_pico` | CA-05 |
| `test_partida.py::test_mover_a_compuerta_cerrada` | CA-05 |
| `test_partida.py::test_esperar_avanza_el_turno` | CA-06 |
| `test_partida.py::test_esperar_mueve_a_los_pajaros` | CA-19 |
| `test_partida.py::test_esperar_con_partida_terminada` | CA-28 |
| `test_partida.py::test_recoger_orbe` | CA-07 |
| `test_partida.py::test_recoger_orbe_suma_puntos` | CA-08 |
| `test_partida.py::test_inventario_vacio_al_soltar` | CA-12 |
| `test_partida.py::test_usar_inexistente` | CA-12 |
| `test_partida.py::test_soltar_deja_el_objeto_en_la_celda` | CA-11 |
| `test_partida.py::test_soltar_orbe_resta_puntos` | CA-42 |
| `test_partida.py::test_soltar_gasta_turno_y_se_puede_deshacer` | CA-41 |
| `test_partida.py::test_soltar_en_celda_ocupada` | CA-43 |
| `test_partida.py::test_usar_orbe_no_cambia_nada` | CA-43 |
| `test_partida.py::test_usar_llave_lejos_de_compuerta` | CA-43 |
| `test_partida.py::test_usar_llave_abre_la_compuerta` | CA-10 |
| `test_partida.py::test_deshacer_llave_cierra_la_compuerta` | CA-41 |
| `test_partida.py::test_deshacer_movimiento` | CA-13 |
| `test_partida.py::test_deshacer_recogida` | CA-14 |
| `test_partida.py::test_deshacer_sin_acciones` | CA-15 |
| `test_partida.py::test_rehacer_repite_los_mismos_efectos` | CA-16 |
| `test_partida.py::test_accion_nueva_borra_rehacer` | CA-17 |
| `test_partida.py::test_rehacer_sin_acciones` | CA-18 |
| `test_partida.py::test_pajaro_avanza_una_casilla_por_camino_corto` | CA-19 |
| `test_partida.py::test_pajaro_no_entra_en_picos` | CA-20 |
| `test_partida.py::test_pajaro_sin_camino_no_se_mueve` | CA-21 |
| `test_partida.py::test_pajaros_no_ocupan_la_misma_celda` | CA-22 |
| `test_partida.py::test_pajaros_orden_fijo` | CA-22 |
| `test_partida.py::test_eventos_de_recoleccion_con_turno_y_celda` | CA-23 |
| `test_partida.py::test_eventos_de_aparicion_y_colision` | CA-23 |
| `test_partida.py::test_eventos_en_orden` | CA-24 |
| `test_partida.py::test_turno_sin_eventos` | CA-25 |
| `test_partida.py::test_victoria_en_el_portal` | CA-26 |
| `test_partida.py::test_derrota_si_el_pajaro_llega` | CA-27 |
| `test_partida.py::test_derrota_si_el_cubo_entra_a_la_celda_del_pajaro` | CA-27 |
| `test_partida.py::test_partida_terminada_no_acepta_movimientos` | CA-28 |
| `test_partida.py::test_partida_terminada_permite_deshacer` | CA-28 |
| `test_partida.py::test_buscar_entidad_existente` | CA-29 |
| `test_partida.py::test_buscar_objeto_en_inventario` | CA-29 |
| `test_partida.py::test_buscar_inexistente` | CA-30 |
| `test_partida.py::test_nivel_se_puede_ganar_por_el_camino_corto` | CA-26 |
| `test_partida.py::test_nivel_esperar_lleva_a_la_derrota` | CA-27 |
| `test_pila.py::test_pila_nueva_esta_vacia` | CA-PIL-04 |
| `test_pila.py::test_pila_nueva_tamano_cero` | CA-PIL-04 |
| `test_pila.py::test_pila_con_elemento_no_esta_vacia` | CA-PIL-01 |
| `test_pila.py::test_apilar_deja_el_valor_en_la_cima` | CA-PIL-01 |
| `test_pila.py::test_apilar_aumenta_el_tamano` | CA-PIL-01 |
| `test_pila.py::test_apilar_acepta_none_y_duplicados` | CA-PIL-01 |
| `test_pila.py::test_cima_no_quita_el_elemento` | CA-PIL-01 |
| `test_pila.py::test_desapilar_en_orden_inverso` | CA-PIL-02 |
| `test_pila.py::test_desapilar_un_solo_elemento` | CA-PIL-05 |
| `test_pila.py::test_desapilar_reduce_el_tamano` | CA-PIL-02 |
| `test_pila.py::test_vacia_desapilar_lanza_error` | CA-PIL-03 |
| `test_pila.py::test_vacia_cima_lanza_error` | CA-PIL-03 |
| `test_pila.py::test_vacia_error_no_cambia_la_pila` | CA-PIL-03 |
| `test_pila.py::test_vaciar_con_elementos` | CA-PIL-04 |
| `test_pila.py::test_vaciar_pila_vacia` | CA-PIL-04 |
| `test_pila.py::test_vaciar_permite_reutilizar` | CA-PIL-04 |
| `test_tabla_hash.py::test_insertar_y_buscar` | CA-HAS-01 |
| `test_tabla_hash.py::test_insertar_varias_claves` | CA-HAS-01 |
| `test_tabla_hash.py::test_insertar_clave_existente_reemplaza` | CA-HAS-02 |
| `test_tabla_hash.py::test_buscar_inexistente` | CA-HAS-03 |
| `test_tabla_hash.py::test_buscar_en_tabla_vacia` | CA-HAS-03 |
| `test_tabla_hash.py::test_buscar_con_colision` | CA-HAS-04 |
| `test_tabla_hash.py::test_eliminar_existente` | CA-HAS-06 |
| `test_tabla_hash.py::test_eliminar_inexistente` | CA-HAS-03 |
| `test_tabla_hash.py::test_eliminar_en_tabla_vacia` | CA-HAS-03 |
| `test_tabla_hash.py::test_colisiones_se_eliminan_por_separado` | CA-HAS-04 |
| `test_tabla_hash.py::test_colisiones_eliminar_la_mas_antigua` | CA-HAS-04 |
| `test_tabla_hash.py::test_crecer_conserva_las_claves` | CA-HAS-05 |
| `test_tabla_hash.py::test_crecer_aumenta_las_cubetas` | CA-HAS-05 |
| `test_tabla_hash.py::test_contiene_existente` | CA-HAS-06 |
| `test_tabla_hash.py::test_contiene_inexistente` | CA-HAS-06 |
| `test_tabla_hash.py::test_contiene_tras_eliminar` | CA-HAS-06 |
| `test_tabla_hash.py::test_tamano_vacia` | CA-HAS-06 |
| `test_tabla_hash.py::test_tamano_un_elemento` | CA-HAS-06 |
| `test_tabla_hash.py::test_tamano_tras_eliminar_todo` | CA-HAS-06 |
