# Creando conexion a la base de datos

# Trabajando con SQLite

# Importando SQLite 3
import sqlite3

###
# Para conectarnos hacemos esto:
# 1) Creamos una variable de conexion
# Llamamos al module de sqlite.connect()
# Le indicamos de donde esta almacenada nuestra base de datos
# 3###

# Codigo de conexion a la base de datos
conexion = sqlite3.connect(
    ###
    # Ruta de almacenamiento de la base de datos
    # ###
    "Bases-de-datos-SQLite/db/app.db"
)

# Debemos siempre cerrar la conexion o de lo contrario no podemos escribir en la base de datos.

# Cerrando la conexion
conexion.close()
