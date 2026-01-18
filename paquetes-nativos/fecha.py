# Fecha

# Trabajando con fechas en pythone

import time
from datetime import datetime

print(time.time()) # Devuelve un timestanp con los segundos desde el 01/01/1970

# Creando fechas
fecha = datetime( 2025, 1, 1 ) # Muestra esta fecha con la hora, los minutos y los segundos
fecha1 = datetime.now()        # Muestra la fecha actual con hora, los minutos y los segundos

# Creando fechas apartir de strings
fechas_str = datetime.strptime(
    "2026-01-01", # El primer argumento es la fecha como un string
    # Le pasamos el formato de como python mostrara la fecha
    "%Y-%m-%d"
    ###
    # %Y Para el año con 4 numeros
    # -  El separador
    # %m Para el mes con 2 numeros
    # %d Para el dia con 2 numeros
    # ###
)

# Propiedades del objeto fecha
print(
    fecha.year,     # Nos muestra el año
    fecha.month,    # Nos muestra el mes
    fecha.day,      # Nos muestra el dia
    fecha.hour,     # Nos muestra la hora
    fecha.minute,   # Nos muestra los minutos
)

# Comparando fechas
fecha_comparada = fecha > fecha1

print(
    fecha,
    fecha1,
    fechas_str,
    fechas_str.strftime("%Y-%m-%d"), # Creando un string apartir de una fecha
    fecha_comparada,
)

# Documentacion de las directivas en python = "https://docs.python.org/3/library/datetime.html"
