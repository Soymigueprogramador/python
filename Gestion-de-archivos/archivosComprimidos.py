# Archivos comprimidos

# Trabajando con archivos comprimidos como los ZIP

# Importaciones necesarias.
from pathlib import Path  # Para hacer la referencia a los archivos a comprimit
from zipfile import ZipFile  # Modulo para comprimir los archivos

# Debemos asegurarnos de no comprimir este archivo
with ZipFile("Gestion-de-archivos/comprimido.zip", "w") as zip:
    # Debemos recordar en que carpeta estamos
    for path in Path().rglob("*.*"):  # Le indicamos todos los archivos
        ###
        # El primer * es para indicar el nombre del archivo
        # El .* es para indicar la extension de los archivos
        # ###
        print(path)
        # Validamos que no estemos incluyendo este archivo
        if str(path) != "Gestion-de-archivos/comprimido.zip":
            zip.write(path)

# Leer un archivo comprimido
with ZipFile("Gestion-de-archivos/comprimido.zip", "r") as zipf:
    archivos = zipf.namelist()
    print(archivos)

    # Obtener info de un archivo REAL dentro del ZIP
    info = zipf.getinfo(archivos[0])

    print(
        info.file_size,
        info.compress_size,
    )

    # Extraer todo el contenido
    zipf.extractall("Gestion-de-archivos/descomprimidos")
