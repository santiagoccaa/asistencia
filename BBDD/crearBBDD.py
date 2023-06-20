import pymysql
from tkinter import messagebox

def crearDB():

	try:
		conexion = pymysql.connect(
			host='localhost',
			user= 'root', 
			passwd=''
			)

		cursor = conexion.cursor()

		cursor.execute("CREATE DATABASE IF NOT EXISTS call_center")

		messagebox.showinfo('Aviso', 'Creacion de DB Exitosa')

		conexion.close()
		cursor.close()

	except Exception as er:
		print(er)

	return creartabla()

def creartabla():

	try:
		conexion = pymysql.connect(
			host='localhost',
			user= 'root', 
			passwd='',
			db='call_center'
			)

		cursor = conexion.cursor()

		#----ELIMINAR TABLA ASISTENCIA--------------

		#cursor.execute("DROP TABLE asistencia")

		#-------ASISTENCIA--------------------
		
		cursor.execute("""CREATE TABLE IF NOT EXISTS asistencia 
			(id INT AUTO_INCREMENT PRIMARY KEY, 
				nombre VARCHAR(50),
				cedula VARCHAR(20) UNIQUE, 
				cuenta VARCHAR(20), 
				fecha_Ingreso DATE, 
				hora_ingreso TIME, 
				hora_salida TIME, 
				tiempo_laborado TIME)""")

		#-------EMPLEADOS----------------------

		cursor.execute("""CREATE TABLE IF NOT EXISTS empleados 
			(id INT AUTO_INCREMENT PRIMARY KEY, 
				nombre VARCHAR(50),
				apellidos VARCHAR(90),
				telefono VARCHAR(40),
				cedula VARCHAR(50) UNIQUE,
				cuenta VARCHAR(50),
				departamento VARCHAR(20), 
				correo VARCHAR(50) UNIQUE,
				fecha_Ingreso DATE, 
				hora_ingreso TIME)""")

		#-------ADMINISTRADORES

		cursor.execute("""CREATE TABLE IF NOT EXISTS administradores 
			(id INT AUTO_INCREMENT PRIMARY KEY, 
				nombre VARCHAR(50),
				password VARCHAR(20))""")

		#-------DEPARTAMENTOS

		cursor.execute("""CREATE TABLE IF NOT EXISTS departamentos 
			(id INT AUTO_INCREMENT PRIMARY KEY, 
				nombre VARCHAR(20) UNIQUE)""")

		messagebox.showinfo('Aviso', 'Creacion de Tablas Exitosa')

		conexion.close()
		cursor.close()

	except Exception as er:
		print(er)


