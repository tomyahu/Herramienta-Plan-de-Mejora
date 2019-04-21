import numpy as np

puntos_asignados_por_semana = np.zeros((15,7))

# Carga Media
for i in range(5,14):
	puntos_asignados_por_semana[i][0] = 8
	puntos_asignados_por_semana[i][1] = 8
	puntos_asignados_por_semana[i][2] = 10
	puntos_asignados_por_semana[i][3] = 5
	puntos_asignados_por_semana[i][4] = 16
	puntos_asignados_por_semana[i][5] = 10
	puntos_asignados_por_semana[i][6] = 10

puntos_por_semana = np.zeros((15,7))

def add_points_to_day(week, day, pts):
	array_week = week - 1
	array_day = day - 1
	puntos_por_semana[array_week][array_day] += pts

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