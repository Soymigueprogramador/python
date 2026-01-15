# With

###
# Haciendo operaciones con SQLite sin:
# 1) Comprometer los cambios
# 2) Sin cerrar la conexion a la base de datos
# ###

import sqlite3

with sqlite3.connect("Bases-de-datos-SQLite/db/app.db")as conexion:
    cursor = conexion.cursor()
    cursor.execute(
        """
            CREATE TABLE if not exists usuarios
            (
                id INTEGER primary key,
                nombre VARCHAR(50)
            );
        """
    )

###
# Este nuevo codigo llama a __ exit __ el cual se encarga de:
# 1) Cerrar la conexion
# 2) Si no existe ningun error antes de cerrar la conexion llama a commit
# ###
