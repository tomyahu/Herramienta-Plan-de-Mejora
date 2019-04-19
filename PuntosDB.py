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