import numpy as np
import matplotlib.pyplot as plt

dias = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')


def graficar(semana, punto_adquiridos, puntos_correspondientes):
	fig = plt.figure()
	N = len(punto_adquiridos)
	
	ind = np.arange(N)    # the x locations for the groups
	width = 0.35       # the width of the bars: can also be len(x) sequence

	p1 = plt.bar(ind - width/2, punto_adquiridos, width)
	p2 = plt.bar(ind + width/2, puntos_correspondientes, width)

	plt.ylabel('Puntos')
	plt.title('Puntos Adquiridos vs Correspondientes Semana ' + str(semana))
	plt.xticks(ind, dias)
	plt.legend((p1[0], p2[0]), ('Puntos Adquiridos', 'Puntos Correspondientes'))

	plt.grid()
	plt.savefig('graficos/Semana' + str(semana) + '.png')