# Diccionarios.

###
# ¿Qué son los diccionarios?
# Los diccionarios son un tipo de dato que están agrupados por llave y valor.
# Llave = "nombre" → Tiene que ser sí o sí un string, como "nombre":
# Valor = "Miguel" → Puede ser cualquier tipo de dato.
# Ejemplo: nombre_diccionario = { "Llave": valor }
###

# Ejemplo en código:
personas = {
    1: {"nombre": "Ana", "apellido": "Gómez", "edad": 25, "email": "ana.gomez@example.com"},
    2: {"nombre": "Luis", "apellido": "Martínez", "edad": 32, "email": "luis.martinez@example.com"},
    3: {"nombre": "Carla", "apellido": "Ramírez", "edad": 27, "email": "carla.ramirez@example.com"},
    4: {"nombre": "Miguel", "apellido": "Salazar", "edad": 30, "email": "miguel.salazar@example.com"},
    5: {"nombre": "Sofía", "apellido": "Fernández", "edad": 22, "email": "sofia.fernandez@example.com"},
    6: {"nombre": "Pedro", "apellido": "López", "edad": 28, "email": "pedro.lopez@example.com"},
    7: {"nombre": "Lucía", "apellido": "Díaz", "edad": 24, "email": "lucia.diaz@example.com"},
    8: {"nombre": "Diego", "apellido": "Ruiz", "edad": 35, "email": "diego.ruiz@example.com"},
    9: {"nombre": "Valentina", "apellido": "Sosa", "edad": 21, "email": "valentina.sosa@example.com"},
    10: {"nombre": "Julián", "apellido": "Torres", "edad": 33, "email": "julian.torres@example.com"},
    11: {"nombre": "Micaela", "apellido": "Paz", "edad": 29, "email": "micaela.paz@example.com"},
    12: {"nombre": "Facundo", "apellido": "Vega", "edad": 26, "email": "facundo.vega@example.com"},
    13: {"nombre": "Florencia", "apellido": "Morales", "edad": 31, "email": "florencia.morales@example.com"},
    14: {"nombre": "Tomás", "apellido": "Castro", "edad": 23, "email": "tomas.castro@example.com"},
    15: {"nombre": "Camila", "apellido": "Silva", "edad": 30, "email": "camila.silva@example.com"},
    16: {"nombre": "Nicolás", "apellido": "Ortega", "edad": 34, "email": "nicolas.ortega@example.com"},
    17: {"nombre": "Agustina", "apellido": "Herrera", "edad": 20, "email": "agustina.herrera@example.com"},
    18: {"nombre": "Juan", "apellido": "Rojas", "edad": 36, "email": "juan.rojas@example.com"},
    19: {"nombre": "Martina", "apellido": "Arias", "edad": 28, "email": "martina.arias@example.com"},
    20: {"nombre": "Ezequiel", "apellido": "Navarro", "edad": 27, "email": "ezequiel.navarro@example.com"}
}

# Accediendo al valor de una llave.
print(personas[20]["nombre"])  # Muestra "Ezequiel"

# Agregando un nuevo ítem al diccionario
personas[21] = {
    "nombre": "Lucas",
    "apellido": "Perro",
    "edad": 20,
    "email": "lucasperro@gmail.com"
}

# Verificamos si una clave existe (en este caso, "boca")
if "boca" in personas:
    print("BOCA FUE ENCONTRADO")
else:
    print("BOCA NO FUE ENCONTRADO")

# Intentamos acceder a una clave que no existe, usando .get()
#print(personas.get("nombre"))  # None, porque no hay clave "nombre" en el nivel superior
#print(personas.get("nombre", "No encontrado"))  # Devuelve "No encontrado"

# Eliminar una persona cuyo nombre sea "Lucas"
for clave in list(personas):  # convertimos a lista para evitar error al modificar el dict mientras lo recorremos
    if personas[clave]["nombre"] == "Lucas":
        del personas[clave]
        break  # eliminamos solo la primera coincidencia

# Iterando los valores del diccionario.
for valor in personas:
    print(valor, personas[valor])

# Convirtiendo un diccionario en una tupla.
for valor in personas.items():
    print(valor)

# Descempaquetando una tupla para volver al diccionario.
for llave, valor in personas.items():
    print(llave, valor)

# Mostramos el diccionario actualizado
print(personas)

nombres = [
    {"id": 1, "nombre": "Miguel"},
    {"id": 2, "nombre": "Celeste"},
    {"id": 3, "nombre": "Araceli"},
    {"id": 4, "nombre": "Micaela"}
]

for nombre in nombres:
    print(nombres[1]["nombre"])
