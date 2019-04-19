from PuntosDB import puntos_asignados_por_semana, puntos_por_semana
from graficar import graficar

def actualizar_graficos():
	for i in range(len(puntos_por_semana)):
		graficar(i+1, puntos_por_semana[i], puntos_asignados_por_semana[i])
	

actualizar_graficos()