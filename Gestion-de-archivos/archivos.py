# Gestion de archivos

from pathlib import Path
from time import ctime

archivos = Path("Gestion-de-archivos/archivos-prueba.txt")

print(archivos)
print(archivos.stat())

# Metodos
# archivos.exists()                           # Para ver si es archivo existe
# archivos.rename("nuevo_nombre.extencion") # Cambia el nombre del archivo
# archivos.unlink()                         # Para eliminar el archivo

print(archivos)
print(archivos.stat()) # Nos muestra las estadisticas del archivo

# Accediendo a las metadatas

print("Acceso", archivos.stat().st_atime)        # Muestra la fecha del acceso
print("Creacion", ctime(archivos.stat().st_atime)) # Muestra una fecha en formato mas accesible
print("Modificacion", ctime(archivos.stat().st_atime)) # Muestra la fecha de la ultima modificacion
