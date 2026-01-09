# Directorios

from pathlib import Path

# Creamos un objeto Path que representa un directorio
path = Path("Rutas y directorios")

# -----------------------------------
# Métodos para trabajar con directorios
# -----------------------------------

# path.exists()   # Verifica si existe el directorio
# path.mkdir()    # Crea el directorio
# path.rmdir()    # Elimina el directorio (debe estar vacío)
# path.rename("Directorio-de-carpetas")  # Renombra el directorio

# -----------------------------------
# Iterar el contenido del directorio
# -----------------------------------

# Devuelve un generador con archivos y carpetas
# print(path.iterdir())

# -----------------------------------
# Listas por comprensión
# -----------------------------------

# Archivos que NO son directorios
# archivos = [p for p in path.iterdir() if not p.is_dir()]

# Archivos .py SOLO en este directorio
# archivos = [p for p in path.glob("*.py")]

# Archivos .py en este directorio y en todos los subdirectorios
archivos = [p for p in path.rglob("*.py")]

print(archivos)
