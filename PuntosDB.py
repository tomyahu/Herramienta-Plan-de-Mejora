import numpy as np

puntos_asignados_por_semana = np.zeros((15,7))

def carga_baja(semana):
	puntos_asignados_por_semana[semana][0] = 6
	puntos_asignados_por_semana[semana][1] = 7
	puntos_asignados_por_semana[semana][2] = 8
	puntos_asignados_por_semana[semana][3] = 3
	puntos_asignados_por_semana[semana][4] = 10
	puntos_asignados_por_semana[semana][5] = 8
	puntos_asignados_por_semana[semana][6] = 8

def carga_media(semana):
	puntos_asignados_por_semana[semana][0] = 8
	puntos_asignados_por_semana[semana][1] = 8
	puntos_asignados_por_semana[semana][2] = 10
	puntos_asignados_por_semana[semana][3] = 5
	puntos_asignados_por_semana[semana][4] = 16
	puntos_asignados_por_semana[semana][5] = 10
	puntos_asignados_por_semana[semana][6] = 10

def carga_alta(semana):
	puntos_asignados_por_semana[semana][0] = 11
	puntos_asignados_por_semana[semana][1] = 11
	puntos_asignados_por_semana[semana][2] = 13
	puntos_asignados_por_semana[semana][3] = 8
	puntos_asignados_por_semana[semana][4] = 20
	puntos_asignados_por_semana[semana][5] = 15
	puntos_asignados_por_semana[semana][6] = 15

# Carga Media
for i in range(5,8):
	carga_media(i)

for i in range(8,12):
	carga_alta(i)

for i in range(12,13):
	carga_media(i)

for i in range(13,16):
	carga_alta(i)

def set_asigned_points_to_day(week, day, pts):
	array_week = week - 1
	array_day = day - 1
	puntos_asignados_por_semana[array_week][array_day] = pts

# Dias Libres
set_asigned_points_to_day(7,4,15)
set_asigned_points_to_day(8,3,15)

puntos_por_semana = np.zeros((15,7))

def add_points_to_day(week, day, pts):
	array_week = week - 1
	array_day = day - 1
	puntos_por_semana[array_week][array_day] += pts


# -------------------------------------------------------------------------------------------------------------------------------
# Semana 11
current_week = 11

#Lunes
current_day = 1

add_points_to_day(current_week, current_day, 5) # Hacer trabajo grupal evalua
add_points_to_day(current_week, current_day, 3) # Empezar programa tarea 2 mallas geométricas

#Martes
current_day = 2

add_points_to_day(current_week, current_day, 3) # Hacer 2 programas en base al programa del dia anterior mallas geométricas
add_points_to_day(current_week, current_day, 3) # Hacer quick fixes para seleccion cursos form ingenieria de software
add_points_to_day(current_week, current_day, 3) # Iniciar presentación mallas geométricas
add_points_to_day(current_week, current_day, 5) # Recolectar datos de mallas geométricas

#Miercoles
current_day = 3

add_points_to_day(current_week, current_day, 3) # Implementar busqueda de tareas ingeniería de software
add_points_to_day(current_week, current_day, 5) # Arreglar bugs ingeniería de software

#Jueves
current_day = 4

add_points_to_day(current_week, current_day, 3) # Empezar tarea 3 mallas geométricas
add_points_to_day(current_week, current_day, 3) # Ayudar a diseñar demo ingenieria de software

#Viernes:
current_day = 5

add_points_to_day(current_week, current_day, 1) # Preparar base de datos para demo
add_points_to_day(current_week, current_day, 3) # Implementar punto en triangulo mallas geometricas
add_points_to_day(current_week, current_day, 5) # Implementar punto en linea mallas geometricas
add_points_to_day(current_week, current_day, 3) # Demostrar existencia antitriángulos mallas geométricas y rantear sobre eso mallas geometricas
add_points_to_day(current_week, current_day, 3) # Leer Tarea 2 de criptografía y hacer P1
add_points_to_day(current_week, current_day, 5) # Hacer segundo protocolo introducción a la criptografía

#Sabado:
current_day = 6

add_points_to_day(current_week, current_day, 5) # Hacer que el proceso servidor sea mas robusto ingeniería de software 2

#Domingo:
current_day = 7

add_points_to_day(current_week, current_day, 5) # Hacer que el proceso servdor sea mas robusto ingeniería de software 2
add_points_to_day(current_week, current_day, 3) # Hacer overleaf con tarea 2 de criptografía
add_points_to_day(current_week, current_day, 3) # Resolver P3 tarea 2 criptografía
add_points_to_day(current_week, current_day, 1) # Pasar P3 criptografía a overleaf
add_points_to_day(current_week, current_day, 1) # Planificar resto de la semana
add_points_to_day(current_week, current_day, 3) # Resumir una clase ingeniería de software
# -------------------------------------------------------------------------------------------------------------------------------
# Semana 10
current_week = 10

#Lunes
current_day = 1

add_points_to_day(current_week, current_day, 5) # Preparar presentación mallas geometricas
add_points_to_day(current_week, current_day, 3) # Implementar librería json ingenieria de software

#Martes
current_day = 2

add_points_to_day(current_week, current_day, 5) # Implementar links busqueda cursos y problemas
add_points_to_day(current_week, current_day, 5) # Implementar base formulario curso
add_points_to_day(current_week, current_day, 3) # Resumir primeras 2 diapos ingeniería de software

#Miercoles
current_day = 3
set_asigned_points_to_day(current_week, current_day, 10) #Reducción tiempo por reunión con Jeremy

add_points_to_day(current_week, current_day, 3) # Implementar vistas tarea ingenieria de software
add_points_to_day(current_week, current_day, 5) # Desarrollar protocolo comprador vendedor criptografía

#Jueves
current_day = 4
set_asigned_points_to_day(current_week, current_day, 11) # Paro

add_points_to_day(current_week, current_day, 1) # Resolver problema plan de mejora 2
add_points_to_day(current_week, current_day, 3) # Ponerse al día con primera mitad de clase de criptografía
add_points_to_day(current_week, current_day, 3) # Ponerse al día con segunda mitad de clase de criptografía
add_points_to_day(current_week, current_day, 3) # Repasar resumen criptografía
add_points_to_day(current_week, current_day, 3) # Hacer ejercicios de evalua

#Viernes
current_day = 5
set_asigned_points_to_day(current_week, current_day, 9) # Descanso

add_points_to_day(current_week, current_day, 1) # Pedir sala comdibujo
add_points_to_day(current_week, current_day, 1) # Enviar mail profe para estudiar evalua
add_points_to_day(current_week, current_day, 1) # Ordenar tiempo plan de mejora
# -------------------------------------------------------------------------------------------------------------------------------
# Semana 9
current_week = 9

#Lunes
current_day = 1

add_points_to_day(current_week, current_day, 3) # Agregar vistas ingeniería de software a presentación
add_points_to_day(current_week, current_day, 1) # Actualizar puntos
add_points_to_day(current_week, current_day, 3) # Ponerse al día con clase 12 de criptografía
add_points_to_day(current_week, current_day, 3) # Ponerse al día con primera mitad clase 13 de criptografía

#Martes
current_day = 2

add_points_to_day(current_week, current_day, 5) # Resumir primeras 2 diapos ingeniería de software
add_points_to_day(current_week, current_day, 3) # Resumir primeras 2 diapos ingeniería de software
add_points_to_day(current_week, current_day, 1) # Avanzar en sistema ingeniería de software
add_points_to_day(current_week, current_day, 5) # Hacer 3 auxiliares de criptografía

#Miercoles
current_day = 3
set_asigned_points_to_day(current_week, current_day, 15) #Reducción tiempo por reunión con Jeremy pero Paro

add_points_to_day(current_week, current_day, 5) # Resumir clase 6 ingeniería de software
add_points_to_day(current_week, current_day, 3) # Resumir clase 7 ingenieria de software
add_points_to_day(current_week, current_day, 3) # Modificar documento de requisitos
add_points_to_day(current_week, current_day, 8) # Estudiar de auxiliares criptografía
add_points_to_day(current_week, current_day, 3) # Resumir clase 13 criptografía
add_points_to_day(current_week, current_day, 1) # Repasar resumen ingenieria de software

#Jueves
current_day = 4
add_points_to_day(current_week, current_day, 1) # Actualizar puntos ayer
add_points_to_day(current_week, current_day, 5) # Hacer mitad resumen criptografía
add_points_to_day(current_week, current_day, 3) # Hacer 2 planas mas resumen criptografía

#Viernes
current_day = 5
add_points_to_day(current_week, current_day, 5) # Terminar resumen criptografía
add_points_to_day(current_week, current_day, 3) # Agregar Fibonacci Heaps a mallas geometricas
add_points_to_day(current_week, current_day, 5) # Implementar el módulo comunicación del sistema ingeniería de software
add_points_to_day(current_week, current_day, 3) # Cambiar archivos sistema ingeniería de software a json

#Sabado
current_day = 6
add_points_to_day(current_week, current_day, 3) # Hacer resumen evaluación de proyectos
add_points_to_day(current_week, current_day, 3) # Probar módulo de comunicación

#Domingo
current_day = 7
add_points_to_day(current_week, current_day, 5) # Hacer entrega 2 plan de mejora trabajo en equipo
add_points_to_day(current_week, current_day, 1) # Pedir sala comdibujo
add_points_to_day(current_week, current_day, 3) # Crear clase para guardar tests en json ingenieria de software
add_points_to_day(current_week, current_day, 3) # Recolectar datos mallas geométricas

# -------------------------------------------------------------------------------------------------------------------------------
# Semana 8
current_week = 8

#Lunes
current_day = 1

add_points_to_day(current_week, current_day, 3) # Hacer vista LP Usuario no registrado + login Software 2
add_points_to_day(current_week, current_day, 5) # Hacer vista Curso para todos los usuarios + login Software 2

#Martes
current_day = 2

add_points_to_day(current_week, current_day, 5) # Rehacer programa ingeniería de software
add_points_to_day(current_week, current_day, 10) # Rehacer programa mallas geométricas

#Miercoles
current_day = 3

add_points_to_day(current_week, current_day, 5) # Rehacer programa ingeniería de software
add_points_to_day(current_week, current_day, 5) # Rehacer programa mallas geométricas
add_points_to_day(current_week, current_day, 3) # Probar usuario nobody ingeniería de software

#Jueves
current_day = 4

add_points_to_day(current_week, current_day, 5) # Implementar scheduler ingenieria de software
add_points_to_day(current_week, current_day, 5) # Implementar ingenieria de software

#Viernes
current_day = 5

add_points_to_day(current_week, current_day, 1) # Pasar lo que llevo de ingeniería de software a bit bucket
add_points_to_day(current_week, current_day, 5) # Escribir arquitectura lógica documento diseño 
add_points_to_day(current_week, current_day, 3) # Escribir arquitectura física y modelo de datos ingenieria de software 

#Sabado
current_day = 6

add_points_to_day(current_week, current_day, 10) # Responder control de lectura mallas geométricas
add_points_to_day(current_week, current_day, 1) # Enviar encuesta trabajo en equipo

#Domingo
current_day = 7

add_points_to_day(current_week, current_day, 1) # Aprender a hacer DFD's
add_points_to_day(current_week, current_day, 5) # Hacer DFD's ingeniería de software
add_points_to_day(current_week, current_day, 1) # Reemplazar imagenes modelo de datos presentación
add_points_to_day(current_week, current_day, 3) # Escribir sección de módulos detallados documento de diseño ingeniería de software
add_points_to_day(current_week, current_day, 1) # Actualiza varias interfaces ingenieria de software

# -------------------------------------------------------------------------------------------------------------------------------
# Semana 7
current_week = 7

#Lunes
current_day = 1

add_points_to_day(current_week, current_day, 5) # Resumir flujo de caja evalua
add_points_to_day(current_week, current_day, 3) # P1 tarea criptografía hecha

#Martes
current_day = 2

add_points_to_day(current_week, current_day, 5) # Resolver P2 tarea criptografía
add_points_to_day(current_week, current_day, 5) # Estudiar lectura mallas geometricas

#Miercoles
current_day = 3

add_points_to_day(current_week, current_day, 1) # Redactar preguntas diggo
add_points_to_day(current_week, current_day, 5) # Investigar sobre proyecto criptografía
add_points_to_day(current_week, current_day, 5) # Hacer P3 a

#Jueves
current_day = 4

add_points_to_day(current_week, current_day, 3) # Hacer software testeo ingeniería de software 2
add_points_to_day(current_week, current_day, 1) # Planearse próximos días
add_points_to_day(current_week, current_day, 5) # P3 criptografía hecha
add_points_to_day(current_week, current_day, 5) # Encontrar y leer lectura P3 mallas geométricas.

#Viernes
current_day = 5

add_points_to_day(current_week, current_day, 5) # Creación programa basico para mostrar la aproxiacion de imagenes
add_points_to_day(current_week, current_day, 5) # Se comenzo un programa para aproximar la grilla en cada momento.
add_points_to_day(current_week, current_day, 5) # Se terminó la P3 del control de mallas geometricas

#Sabado
current_day = 6

add_points_to_day(current_week, current_day, 15) # Entrega 1 Evalua

#Domingo
current_day = 7

add_points_to_day(current_week, current_day, 15) # Tarea 1 Criptografía


# -------------------------------------------------------------------------------------------------------------------------------
# Semana 6
current_week = 6

#Miercoles
current_day = 3

add_points_to_day(current_week, current_day, 5) # Trabajo grupal evalua
add_points_to_day(current_week, current_day, 1) # Ponerse al día con ingeniería de software
add_points_to_day(current_week, current_day, 3) # Ponerse al día con clase 10 e inicio clase 9 + 2 criptografía

#Jueves
current_day = 4

add_points_to_day(current_week, current_day, 3) # Hacer mini API para zips y csv
add_points_to_day(current_week, current_day, 3) # Hacer vista administrador curso ingenieria de software 2
add_points_to_day(current_week, current_day, 3) # Programar script para graficar puntos

#Viernes
current_day = 5

add_points_to_day(current_week, current_day, 1) # Mover trabajo de trabajo en equipo a github
add_points_to_day(current_week, current_day, 1) # Subir mockup ingenieria de software 2
add_points_to_day(current_week, current_day, 1) # Se pidió la sala comdibujo para la proxima semana
add_points_to_day(current_week, current_day, 1) # Molestar gente ingenieria de software 2 para empezar a programar stuff

#Sábado
current_day = 6

add_points_to_day(current_week, current_day, 5) # Se investigó sobre protocolos de encriptación homomórfica
add_points_to_day(current_week, current_day, 3) # Se puso al día con primera mitad de clase criptografía.
add_points_to_day(current_week, current_day, 1) # Imprimir resto de lectura mallas geometricas
add_points_to_day(current_week, current_day, 3) # Se leyó la parte de lectura mallas geometricas asociada al algoritmo 3, triangulacion dependiente de los datos y algortimo 4
add_points_to_day(current_week, current_day, 1) # Se respondió la P2 b del control de lectura de mallas geometricas

#Domingo
current_day = 7

add_points_to_day(current_week, current_day, 5) # Se resolvio el control de lectura mallas geometricas
add_points_to_day(current_week, current_day, 3) # Se puso al día con criptografía
add_points_to_day(current_week, current_day, 1) # Se movio el proyecto de ingeniería de software a github
add_points_to_day(current_week, current_day, 3) # Se agregaron imágenes a las respuestas del control de lectura
add_points_to_day(current_week, current_day, 1) # Se firmo un contrato de confidencialidad criptografía




