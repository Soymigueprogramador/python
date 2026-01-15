# Insert many

# Insertando multiples valores con SQLite

import sqlite3

with sqlite3.connect("Bases-de-datos-SQLite/db/app.db") as conexion:
    cursor = conexion.cursor()
    usuarios = [ # Lista para guardar los usuarios nuevos
        (2, "Celeste"),
        (3, "Araceli"),
    ]
    cursor.executemany( # Cambiamos a este nuevo metodo
        "insert into usuarios values(?, ?)",
        usuarios, # Llamamos a la lista de usuarios
    )
