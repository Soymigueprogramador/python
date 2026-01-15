# Comprensión de listas.

usuarios = [
    [1, "Ana Torres", "ana.torres@gmail.com", 24, True],
    [2, "Carlos Ruiz", "carlos.ruiz@hotmail.com", 31, False],
    [3, "María López", "maria.lopez@yahoo.com", 28, True],
    [4, "Juan Pérez", "juan.perez@gmail.com", 22, True],
    [5, "Lucía Fernández", "lucia.fernandez@gmail.com", 35, False],
    [6, "Diego Giménez", "diego.gimenez@gmail.com", 29, True],
    [7, "Camila Sánchez", "camila.sanchez@outlook.com", 26, False],
    [8, "Mateo Romero", "mateo.romero@gmail.com", 30, True],
    [9, "Sofía Castro", "sofia.castro@gmail.com", 27, True],
    [10, "Gabriel Díaz", "gabriel.diaz@gmail.com", 33, False]
]

# Vamos a convertir la lista de usuarios en una lista de solo nombres.
###
# Para ello hacemos esto:
# Creamos una variable y la igualamos a una lista por comprensión.
# Dentro de los corchetes escribimos [expresion for nombreVariable in lista]
# Ejemplo: variable = [expresion for usuario in usuarios]
###

# Ejemplo en código:

# Transformando la lista a solo nombres.
nombres = [ usuario[0] for usuario in usuarios ]

# Filtrando usuarios
nombres = [ usuario[1] for usuario in usuarios if usuario[3] > 2 ]

# Transformando y filtrando la lista de usuarios.
nombres = [usuario[1] for usuario in usuarios if usuario[3] > 25]

print(nombres)
