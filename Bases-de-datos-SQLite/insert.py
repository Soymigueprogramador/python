# Insert

import sqlite3

with sqlite3.connect("Bases-de-datos-SQLite/db/app.db")as conexion:
    # Insertando datos dentro de una tabla de SQLite
    ###
    # 1) Creamos el objeto cursor apartir de la conexion
    # 2) Llamamos al metodo de execute()
    # 3) Usamos las commillas dobles
    # 4) Le pasamos la consulta para insertar los datos como primer argumento
    # 5) Le pasamos una tupla con los datos que insertaremos como segundo argumento
    # ###

    cursor = conexion.cursor()
    cursor.execute(
    "insert into usuarios values(?, ?)",
    ( 1, "Miguel" ),
    )

###
# Esto se hace para evitar una (SQL injection) que es la forma en la que un hacker
# puede entrar a la base de datos
# ###