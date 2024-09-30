import os

def renombrar_archivos(ruta):
	for archivo in os.listdir(ruta):
		os.rename(os.path.join(ruta, archivo), os.path.join(ruta, archivo.lower()))

if __name__ == '__main__':
	# Aca va al lista de cadenas con las rutas de los directorios a renombrar su contenido.
	directorios = []
	for directorio in directorios:
		renombrar_archivos(directorio)
