# Creando tabla

import sqlite3
conexion = sqlite3.connect(
    "Bases-de-datos-SQLite/db/app.db"
)
#conexion.close()

# Realizando consultas a la base de datos
###
# 1) Creamos un objeto cursor apartir del objeto de conexion
# 2) ###
cursor = conexion.cursor() # Es un intermediario entre la base de datos y nosotros

# Ejecutando las consultas
###
# 1) Llamamos al objeto cursor
# 2) Llamamos al metodo execute()
# 3) Entre los () tenemos que usar 3 comillas dobles """ consulta """
# ###
cursor.execute(
    # Aca van las consultas
    """
        CREATE TABLE if not exists usuarios
        (
            id INTEGER primary key,
            nombre VARCHAR(50)
        );
    """
)

# Comprometemos el codigo anterior contra la base de datos
###
# Para eso llamamos al metodo de commit()
# ###
conexion.commit() # Sin esto la consulta no se ejecuta.

conexion.close()
