import sqlite3
from random import choice
from tkinter import LabelFrame, Tk, Entry, Label, Button


class App:
	def __init__(self, ventana):
		self.ventana = ventana
		ventana.title("Elección")
		ventana.geometry('200x200')
		self.interfaz_grafica()

	def interfaz_grafica(self):

		self.frame = LabelFrame(self.ventana, text="Elección aleatoria")
		self.frame.config(font=('Arial',12,'bold'))
		self.frame.pack(ipadx=20)

		self.ci = Label(self.frame, text="CI")
		self.ci.pack()
		self.cedula = Entry(self.frame)
		self.cedula.pack()

		self.name = Label(self.frame, text="Nombre")
		self.name.pack()
		self.nombre_elegido = Entry(self.frame)
		self.nombre_elegido.pack()

		self.last_name = Label(self.frame, text="Apellido")
		self.last_name.pack()
		self.apellido_elegido = Entry(self.frame)
		self.apellido_elegido.pack()

		self.boton = Button(self.frame, text="Elegir", command=self.eleccion_alumno)
		self.boton.config(font=('Arial', 10, 'bold'), fg='white', bg='red')
		self.boton.pack(ipadx=10, pady=10)

	def consulta(self):
		with sqlite3.connect('seccion_D2.db') as conn:
			cursor = conn.cursor()
			try:
				consulta = '''SELECT * FROM seccion'''
				cursor.execute(consulta)
				conn.commit()
				listado = cursor.fetchall()
				cursor.close()
			except:
				print("No se ha podido realizar la consulta.")
				return
			return listado

	def eleccion_alumno(self):
		eleccion = self.consulta()
		elegido = choice(eleccion)
		self.cedula_identidad, self.nombre, self.apellido = elegido
		self.cedula.delete(0, 'end')
		self.cedula.insert(0, self.cedula_identidad)
		self.nombre_elegido.delete(0,'end')
		self.nombre_elegido.insert(0,self.nombre)
		self.apellido_elegido.delete(0,'end')
		self.apellido_elegido.insert(0,self.apellido)

if __name__ == '__main__':
	ventana = Tk()
	app = App(ventana)
	ventana.mainloop()