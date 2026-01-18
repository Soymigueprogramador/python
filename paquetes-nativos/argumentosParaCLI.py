# Argumentos para cli

import sys
import os
from pathlib import Path

# Creando una aplicacion que toma un archivo y le cambia el nombre.
def cli(args):
    # Validando que se le allan pasado argumentos a la funcion
    if len(args) == 1:
        print(" No se le pasaron argumentos ")
        return

    # Verificamos que tenga mas de 3 argumentos
    if len(args) != 3:
        print(" Se necesitan como minimo 2 argumentos ")
        return

    # Preguntamos por el archivo de origen
    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print(" Origen desconocido ")
        return

    # Preguntamos por el archivo de destino
    destino = args[2]
    d = Path(destino)
    if d.exists():
        print(" Destino desconocido ")
        return

    # Renombrando el archivo
    os.rename(str(origen), str(destino))
    print(" Archivo renombrado con exito!! ")

cli(sys.argv)

# ¿Como lo ejecutamos?
###
# 1) Abrimos la terminal integrada (git bash en este caso, vos usa la que quieras)
# 2) Escribimos python (Si estas en windows) o python3 (si estas en macOS)
# 3) Escribimos la ruta dende esta el archivo de la aplicacion que creamos
# 4) Escribimos la ruta del archivo de origen al que le queremos cambiar el nombre (Debe ser creado primero)
# 5) Escribimos la ruta donde queremos guardar el archivo con el nuevo nombre
#    La ruta debe ser (nombre_carpeta/nombre_archivo-destino.extencion)
# ###

