# Select all

import sqlite3

with sqlite3.connect("Bases-de-datos-SQLite/db/app.db") as conexion:
    cursor = conexion.cursor()
    cursor.execute(
    """
        SELECT * FROM usuarios
    """
    )
    print(cursor.fetchall()) # Esto devuelve todos los registros
