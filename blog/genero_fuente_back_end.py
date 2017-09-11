
class Entrada:
	kanji = None
	pronunciacion = None
	descripcion = None
	
	def __init__(self, kanji, pronunciacion, descripcion):
		self.kanji = kanji
		self.pronunciacion = pronunciacion
		self.descripcion = descripcion
	
	def __str__(self):
		return ":".join([self.pronunciacion, self.kanji, self.descripcion])

def generar_salida(entradas, ruta_salida):
	archivo = open(ruta_salida, 'w')
	for entrada in entradas:
		archivo.write(str(entrada) + "\n")
	archivo.close()
