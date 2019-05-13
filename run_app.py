from PuntosDB import puntos_asignados_por_semana, puntos_por_semana
from graficar import graficar
import tkinter as tk
import os


def actualizar_graficos():
	print("Actualizando Gráficos...")
	try:
		os.mkdir("graficos")
	except:
		pass
	for i in range(len(puntos_por_semana)):
		graficar(i+1, puntos_por_semana[i], puntos_asignados_por_semana[i])
	
	print("Gráficos Actualizados")

#actualizar_graficos()


canvas_width = 680
canvas_height = 520

master = tk.Tk()

num_semana = 6

title_var = tk.StringVar()
title_var.set("Semana " + str(num_semana))

titulo = tk.Label(master, textvariable=title_var, font=("Helvetica", 16))
titulo.grid(row=0,column=0, columnspan=3)

canvas = tk.Canvas(master, 
           width=canvas_width, 
           height=canvas_height)

imgs = []
for i in range(15):
	imgs.append(tk.PhotoImage(file="graficos/Semana"+ str(i+1) + ".png"))
canvas_img = canvas.create_image(20,20, anchor=tk.NW, image=imgs[num_semana - 1])
canvas.grid(row=1,column=0, columnspan=2)


def adelantar_semana():
	global num_semana
	if num_semana < 15:
		num_semana += 1
		canvas.itemconfig(canvas_img, image=imgs[num_semana - 1])
		title_var.set("Semana " + str(num_semana))

def atrasar_semana():
	global num_semana
	if num_semana > 1:
		num_semana -= 1
		canvas.itemconfig(canvas_img, image=imgs[num_semana - 1])
		title_var.set("Semana " + str(num_semana))

atras = tk.Button(master, text="<<", command=atrasar_semana)
atras.grid(row=2,column=0)

adelante = tk.Button(master, text=">>", command=adelantar_semana)
adelante.grid(row=2,column=1)

master.mainloop()