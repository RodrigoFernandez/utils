
import tkinter
from genero_fuente_back_end import Entrada
from genero_fuente_back_end import generar_salida

campos = {}

def get_campo(ventana, caption):
	lbl = tkinter.Label(ventana, text=caption)
	entry = tkinter.Entry(ventana)
	return (lbl, entry)

def get_boton(ventana, caption, comando):
	btn = tkinter.Button(ventana, text=caption, command=comando)
	return btn

def get_fila_campos(ventana, comando):
	campo_kanji = get_campo(ventana, "Kanji")
	campo_pronunciacion = get_campo(ventana, "Pronunciacion")
	campo_descripcion = get_campo(ventana, "Descripcion")
	btn_agregar = get_boton(ventana, "+", comando)
	
	return (campo_kanji, campo_pronunciacion, campo_descripcion, btn_agregar)

def agregar():
	aux = Entrada(campos['pronunciacion'].get(), campos['kanji'].get(), campos['descripcion'].get())
	campos['entradas'].append(aux)
	rta = str(aux)
	
	campos['estado']['text'] = rta
	campos['pronunciacion'].delete(0, tkinter.END)
	campos['pronunciacion'].insert(0, '')
	campos['kanji'].delete(0, tkinter.END)
	campos['kanji'].insert(0, '')
	campos['descripcion'].delete(0, tkinter.END)
	campos['descripcion'].insert(0, '')
	campos['kanji'].focus()

def generar():
	generar_salida(campos['entradas'], campos['ruta_salida'])
	campos['estado']['text'] = "Se creo el archivo: " + campos['ruta_salida']

def salir():
	campos['ventana'].destroy()

def agrego_ampersan(event):
	campos['kanji'].insert(tkinter.INSERT, '^')

def principal():
	campos['ruta_salida'] = "./fuente.txt"
	
	ventana = tkinter.Tk()
	ventana.title("Fuentes")
	
	contenido = tkinter.Frame(ventana)
	marco = tkinter.Frame(contenido, borderwidth=5, relief="sunken")
	
	contenido.grid(column=0, row=0)
	marco.grid(column=0, row=0)
	
	campo_kanji, campo_pronunciacion, campo_descripcion, btn_agregar = get_fila_campos(contenido, agregar)
	
	campo_kanji[0].grid(column=0, row=0)
	campo_kanji[1].grid(column=0, row=1)
	campos['kanji'] = campo_kanji[1]
	campo_kanji[1].bind('<Alt-a>', agrego_ampersan)
	campo_kanji[1].focus()
	
	campo_pronunciacion[0].grid(column=1, row=0)
	campo_pronunciacion[1].grid(column=1, row=1)
	campos['pronunciacion'] = campo_pronunciacion[1]
	
	campo_descripcion[0].grid(column=2, row=0)
	campo_descripcion[1].grid(column=2, row=1)
	campos['descripcion'] = campo_descripcion[1]
	
	btn_agregar.grid(column=3, row=1)
	
	btn_generar = get_boton(contenido, "Generar", generar)
	btn_generar.grid(column=2, row=2)
	
	btn_salir = get_boton(contenido, "Salir", salir)
	btn_salir.grid(column=3, row=2)
	
	estado = tkinter.Label(contenido, text="")
	estado.grid(column=0, row=3, columnspan=3)
	campos['estado'] = estado
	
	campos['entradas'] = []
	
	campos['ventana'] = ventana
	ventana.mainloop()

if __name__ == '__main__':
	principal()
