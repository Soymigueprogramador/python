# Lectura y escritura

from pathlib import Path

# Creamos una referencia a ese archivo
archivo = Path("Gestion-de-archivos/archivos-prueba.txt")

# Leyendo un archivo
texto = archivo.read_text("utf-8").split("/n") # Metodo para separar los string por salto de linea

# Modificando el texto
texto.insert(0, " Conejo blanco ") # Agrega el texto al principio del archivo
archivo.write_text("/n".join(texto), "utf-8") # Le agregamos el texto que creamo como un string

print(texto)
