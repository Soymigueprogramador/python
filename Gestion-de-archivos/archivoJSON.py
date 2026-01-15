# Archivo json

###
# Los archivos JSON nos ayudan a traer informacion desde una API (Programa de Aplicacion de Interfaz)
# y tambien nos ayudan a traer datos desde una base de datos.
# ###

import json
from pathlib import Path

# Escribiendo en JSON
productos = [
    {
        "id": 1,
        "nombre": "Notebook Lenovo ThinkPad",
        "precio": 1250000,
        "stock": 8,
        "categoria": "Informática"
    },
    {
        "id": 2,
        "nombre": "Mouse Logitech MX Master 3",
        "precio": 145000,
        "stock": 15,
        "categoria": "Accesorios"
    },
    {
        "id": 3,
        "nombre": "Teclado Mecánico Redragon Kumara",
        "precio": 185000,
        "stock": 12,
        "categoria": "Accesorios"
    },
    {
        "id": 4,
        "nombre": "Monitor Samsung 27\"",
        "precio": 980000,
        "stock": 5,
        "categoria": "Monitores"
    },
    {
        "id": 5,
        "nombre": "Auriculares HyperX Cloud II",
        "precio": 320000,
        "stock": 10,
        "categoria": "Audio"
    }
]

data = json.dumps(productos) # Asi convertimos el array a json

# Creamos el archivo JSON con los datos del array de productos
# Path("Gestion-de-archivos/productos.json").write_text(data)

# Leer un archivo JSON
# Creamos una referencia al variable data
#data = Path("Gestion-de-archivos/productos.json").read_text(encoding="utf-8")

# Transformamos a una lista de diccionarios
productos = json.loads(data)

# Modificar el archivo JSON
productos[0] ["nombre"] = "MARRANO" # Le cambiamos el nombre al primer producto
# Convertimos a JSON
Path("Gestion-de-archivos/productos.json").write_text(json.dumps(productos))

###
# JSON:
# JS = JavaScript
# O = Object
# N = Notetion
# Notacion de Objetos en JavaScript
# ###