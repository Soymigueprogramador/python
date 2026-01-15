# Select one

import sqlite3

with sqlite3.connect("Bases-de-datos-SQLite/db/app.db") as conexion:
    cursor = conexion.cursor()
    cursor.execute(
    """
        SELECT * FROM usuarios
    """
    )
    print(cursor.fetchone()) # Esto devuelve el primer registro
