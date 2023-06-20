from tkinter import messagebox
import tkinter as tk

import datetime
import time 

from datetime import date
from Styles import styles 
from BBDD.tomar_asistencia import insertar_asistencia, insertar_salida

class Asistencia():

	def __init__(self):

		self.root=tk.Tk()

		self.ancho_ventana = 1366
		self.alto_ventana = 768

		self.x_ventana = self.root.winfo_screenwidth() // 2 - self.ancho_ventana // 2
		self.y_ventana = self.root.winfo_screenheight() // 2 - self.alto_ventana // 2

		self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
		self.root.geometry(self.posicion)

		self.root.iconbitmap('img/icono.ico')
		self.root.resizable(0,0)
		self.root.title("Asistencia")
		self.root.config(bg="#FFFFFF")

		self.img=tk.PhotoImage(file="img/img.png")
		self.lb_img=tk.Label(self.root, image = self.img, bg='#FFFFFF').place(x=80,y=50)

		self.lado=tk.PhotoImage(file="img/prueba4.png")
		self.lb_img=tk.Label(self.root, image = self.lado, bg='#FFFFFF').place(x=1050,y=170)

#----------------FRAMES----------------------------

		#self.frame_padre=tk.Frame(self.root,
		 #width=800, height=767, bg='#FFFFFF').place(x=499, y=0)


#-----------FECHA Y HORA-------------------

		self.tiempoActual=tk.Label(text="", **styles.STYLE_LABEL, pady=10, padx=10)
		self.diaActual=tk.Label(text="", **styles.STYLE_LABEL, pady=10, padx=10)

		self.tiempoActual.configure(font=('Poppins 25 italic'), bg='#FFFFFF', fg='#239CF4')
		self.tiempoActual.place(x=100, y=545)
		self.diaActual.configure(font=('Poppins 25 italic'), bg='#FFFFFF', fg='#239CF4')
		self.diaActual.place(x=80, y=500)
		self.update_clock()
		self.get_date()

		#-----NOMBRE EMPRESA------------

		self.ide=tk.Label(self.root, 
			text='READY TO ANSWER',
			 font=('Poppins 30 italic bold'),
			 bg='#FFFFFF', fg='#149CFA').place(x=690, y=60)

		self.ide=tk.Label(self.root, 
			text='CONTACT CENTER',
			 font=('Poppins 15 italic bold'),
			 bg='#FFFFFF', fg='#767676').place(x=790, y=110)

		#---------TITULO-------------------------

		self.ide=tk.Label(self.root, 
			text='Ingrese su ID de Empleado',
			 font=('Poppins 27 italic'),
			 bg='#FFFFFF', fg='#202020').place(x=680, y=210)

		self.cedula=tk.StringVar()

		#----------CAJA DE TEXTO-------------------

		self.dig_ID=tk.Entry(
			self.root,
			**styles.STYLE_Entry, 
			justify=tk.CENTER,
			width=27,
			textvar=self.cedula).place(x=650, y=280)

#-----------BOTON---------------------

		self.boton=tk.Button(self.root,text='Marcar Entrada',**styles.STYLE_Boton ,bd=1, 
			command=lambda:insertar_asistencia(self.cedula.get()),width=25).place(x=750, y=400)

		self.boton=tk.Button(self.root,text='Marcar Salida',**styles.STYLE_Boton ,bd=1, 
			command=lambda:insertar_salida(self.cedula.get()),width=25).place(x=750, y=490)

		self.root.mainloop()

	def update_clock(self):
		now=time.strftime("%I:%M:%S %p")
		self.tiempoActual.configure(text=now)
		self.root.after(1000, self.update_clock)

	def get_date(self):

		fecha=datetime.datetime.now()
		diaSemana=fecha.strftime("%A")

		dia =date.today()
		d1=dia.strftime("%d-%m-%y")
		self.diaActual.configure(text=d1 +  ' | ' + diaSemana)

main=Asistencia()