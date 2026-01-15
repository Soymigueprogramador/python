# Archivo CSV

# Importamos CSV y os para trabajar con archivos separados por coma (,)
import csv
import os

# Escribiendo en un archivo CSV
# with open("Gestion-de-archivos/a.csv", "w") as archivo:
# with open("Gestion-de-archivos/b.csv", "w") as archivo: # Si el archivo no existe, esto lo crea automaticamente
# Creamos un objeto writer
# writer = csv.writer(archivo)
###
# Le pasamos el ID de los twit
# Le pasamos el ID del usuario
# Le pasamos el contenido del twit
# ###
# writer.writerow(["twit_id", "user_id", "text"]) # Le pasamos listas que contienen listas
# writer.writerow([10, 1, "Hola"])
# writer.writerow([11, 2, "Otro gato!!"])

# Lectura
# with open("Gestion-de-archivos/a.csv") as archivo:
#  Creamos un reader
# reader = csv.reader(archivo)
# print(list(reader)) # Convertimos todo en una lista
# archivo.seek(0)
# for linea in reader:
# print(linea)

# Actualizando el CSV
###
# Para actualizar un archivo CSV hacemos esto:
# Tenemos que indicar el archivo original
# Tenemos que indicar que vamos a crear un archivo temporal
# ###
with open("Gestion-de-archivos/a.csv", newline="", encoding="utf-8") as r, \
     open("Gestion-de-archivos/temporal.csv", "w", newline="", encoding="utf-8") as w:

    # Creamos los objetos reader y writer
    reader = csv.reader(r)
    writer = csv.writer(w)

    for linea in reader:
        # Evitamos filas vacías
        if not linea:
            continue

        if linea[0] == "10":  # Pedimos la línea del ID
            # Reemplazamos la fila completa
            writer.writerow(["10", "1", "Linea modificada"])
        else:
            # Copiamos la fila sin cambios
            writer.writerow(linea)

# Eliminamos el archivo original
os.remove("Gestion-de-archivos/a.csv")

# Renombramos el temporal con el nombre original
os.rename("Gestion-de-archivos/temporal.csv", "Gestion-de-archivos/a.csv")
