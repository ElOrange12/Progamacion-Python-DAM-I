import os
import zipfile

origen = 'archivos'
destino = 'archivos'

archivo = zipfile.ZipFile(destino, 'w', zipfile.ZIP.DEFLATED)

for directorio, carpetas, archivo in os.walk(carpeta):
	for archivo in archivos:
		rutaarchivo = os.path.join(directorio, archivo)
		rutarelativa = os.path.relpath(rutaarchivo, origen)
		archivozip.write(rutaarchivo, rutarelativa)
		
archivozip.close()
