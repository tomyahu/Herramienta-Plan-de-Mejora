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
	
for i in range(8,15):
	carga_alta(i)

# Dias Libres
set_asigned_points_to_day(7,4,15)
set_asigned_points_to_day(8,3,15)

puntos_por_semana = np.zeros((15,7))

def add_points_to_day(week, day, pts):
	array_week = week - 1
	array_day = day - 1
	puntos_por_semana[array_week][array_day] += pts

def set_asigned_points_to_day(week, day, pts):
	array_week = week - 1
	array_day = day - 1
	puntos_asignados_por_semana[array_week][array_day] = pts


# -------------------------------------------------------------------------------------------------------------------------------
# Semana 9
current_week = 9

#Lunes
current_day = 1

add_points_to_day(current_week, current_day, 3) # Agregar vistas ingenier�a de software a presentaci�n
add_points_to_day(current_week, current_day, 1) # Actualizar puntos
add_points_to_day(current_week, current_day, 3) # Ponerse al d�a con clase 12 de criptograf�a
add_points_to_day(current_week, current_day, 3) # Ponerse al d�a con primera mitad clase 13 de criptograf�a

#Martes
current_day = 2

add_points_to_day(current_week, current_day, 5) # Resumir primeras 2 diapos ingenier�a de software
add_points_to_day(current_week, current_day, 3) # Resumir primeras 2 diapos ingenier�a de software
add_points_to_day(current_week, current_day, 1) # Avanzar en sistema ingenier�a de software
add_points_to_day(current_week, current_day, 5) # Hacer 3 auxiliares de criptograf�a

#Miercoles
current_day = 3
set_asigned_points_to_day(current_week, current_day, 6) #Reducci�n tiempo por reuni�n con Jeremy


# -------------------------------------------------------------------------------------------------------------------------------
# Semana 8
current_week = 8

#Lunes
current_day = 1

add_points_to_day(current_week, current_day, 3) # Hacer vista LP Usuario no registrado + login Software 2
add_points_to_day(current_week, current_day, 5) # Hacer vista Curso para todos los usuarios + login Software 2

#Martes
current_day = 2

add_points_to_day(current_week, current_day, 5) # Rehacer programa ingenier�a de software
add_points_to_day(current_week, current_day, 10) # Rehacer programa mallas geom�tricas

#Miercoles
current_day = 3

add_points_to_day(current_week, current_day, 5) # Rehacer programa ingenier�a de software
add_points_to_day(current_week, current_day, 5) # Rehacer programa mallas geom�tricas
add_points_to_day(current_week, current_day, 3) # Probar usuario nobody ingenier�a de software

#Jueves
current_day = 4

add_points_to_day(current_week, current_day, 5) # Implementar scheduler ingenieria de software
add_points_to_day(current_week, current_day, 5) # Implementar ingenieria de software

#Viernes
current_day = 5

add_points_to_day(current_week, current_day, 1) # Pasar lo que llevo de ingenier�a de software a bit bucket
add_points_to_day(current_week, current_day, 5) # Escribir arquitectura l�gica documento dise�o 
add_points_to_day(current_week, current_day, 3) # Escribir arquitectura f�sica y modelo de datos ingenieria de software 

#Sabado
current_day = 6

add_points_to_day(current_week, current_day, 10) # Responder control de lectura mallas geom�tricas
add_points_to_day(current_week, current_day, 1) # Enviar encuesta trabajo en equipo

#Domingo
current_day = 7

add_points_to_day(current_week, current_day, 1) # Aprender a hacer DFD's
add_points_to_day(current_week, current_day, 5) # Hacer DFD's ingenier�a de software
add_points_to_day(current_week, current_day, 1) # Reemplazar imagenes modelo de datos presentaci�n
add_points_to_day(current_week, current_day, 3) # Escribir secci�n de m�dulos detallados documento de dise�o ingenier�a de software
add_points_to_day(current_week, current_day, 1) # Actualiza varias interfaces ingenieria de software

# -------------------------------------------------------------------------------------------------------------------------------
# Semana 7
current_week = 7

#Lunes
current_day = 1

add_points_to_day(current_week, current_day, 5) # Resumir flujo de caja evalua
add_points_to_day(current_week, current_day, 3) # P1 tarea criptograf�a hecha

#Martes
current_day = 2

add_points_to_day(current_week, current_day, 5) # Resolver P2 tarea criptograf�a
add_points_to_day(current_week, current_day, 5) # Estudiar lectura mallas geometricas

#Miercoles
current_day = 3

add_points_to_day(current_week, current_day, 1) # Redactar preguntas diggo
add_points_to_day(current_week, current_day, 5) # Investigar sobre proyecto criptograf�a
add_points_to_day(current_week, current_day, 5) # Hacer P3 a

#Jueves
current_day = 4

add_points_to_day(current_week, current_day, 3) # Hacer software testeo ingenier�a de software 2
add_points_to_day(current_week, current_day, 1) # Planearse pr�ximos d�as
add_points_to_day(current_week, current_day, 5) # P3 criptograf�a hecha
add_points_to_day(current_week, current_day, 5) # Encontrar y leer lectura P3 mallas geom�tricas.

#Viernes
current_day = 5

add_points_to_day(current_week, current_day, 5) # Creaci�n programa basico para mostrar la aproxiacion de imagenes
add_points_to_day(current_week, current_day, 5) # Se comenzo un programa para aproximar la grilla en cada momento.
add_points_to_day(current_week, current_day, 5) # Se termin� la P3 del control de mallas geometricas

#Sabado
current_day = 6

add_points_to_day(current_week, current_day, 15) # Entrega 1 Evalua

#Domingo
current_day = 7

add_points_to_day(current_week, current_day, 15) # Tarea 1 Criptograf�a


# -------------------------------------------------------------------------------------------------------------------------------
# Semana 6
current_week = 6

#Miercoles
current_day = 3

add_points_to_day(current_week, current_day, 5) # Trabajo grupal evalua
add_points_to_day(current_week, current_day, 1) # Ponerse al d�a con ingenier�a de software
add_points_to_day(current_week, current_day, 3) # Ponerse al d�a con clase 10 e inicio clase 9 + 2 criptograf�a

#Jueves
current_day = 4

add_points_to_day(current_week, current_day, 3) # Hacer mini API para zips y csv
add_points_to_day(current_week, current_day, 3) # Hacer vista administrador curso ingenieria de software 2
add_points_to_day(current_week, current_day, 3) # Programar script para graficar puntos

#Viernes
current_day = 5

add_points_to_day(current_week, current_day, 1) # Mover trabajo de trabajo en equipo a github
add_points_to_day(current_week, current_day, 1) # Subir mockup ingenieria de software 2
add_points_to_day(current_week, current_day, 1) # Se pidi� la sala comdibujo para la proxima semana
add_points_to_day(current_week, current_day, 1) # Molestar gente ingenieria de software 2 para empezar a programar stuff

#S�bado
current_day = 6

add_points_to_day(current_week, current_day, 5) # Se investig� sobre protocolos de encriptaci�n homom�rfica
add_points_to_day(current_week, current_day, 3) # Se puso al d�a con primera mitad de clase criptograf�a.
add_points_to_day(current_week, current_day, 1) # Imprimir resto de lectura mallas geometricas
add_points_to_day(current_week, current_day, 3) # Se ley� la parte de lectura mallas geometricas asociada al algoritmo 3, triangulacion dependiente de los datos y algortimo 4
add_points_to_day(current_week, current_day, 1) # Se respondi� la P2 b del control de lectura de mallas geometricas

#Domingo
current_day = 7

add_points_to_day(current_week, current_day, 5) # Se resolvio el control de lectura mallas geometricas
add_points_to_day(current_week, current_day, 3) # Se puso al d�a con criptograf�a
add_points_to_day(current_week, current_day, 1) # Se movio el proyecto de ingenier�a de software a github
add_points_to_day(current_week, current_day, 3) # Se agregaron im�genes a las respuestas del control de lectura
add_points_to_day(current_week, current_day, 1) # Se firmo un contrato de confidencialidad criptograf�a




