# Map y Filter.

# Lista de usuarios: [id, nombre, email, edad, activo]
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

# Obtener solo los nombres (posición 1) con map
nombres = list(map(lambda usuario: usuario[1], usuarios))

# Filtrar usuarios con ID mayor a 2
usuarios_filtrados = list(filter(lambda usuario: usuario[0] > 2, usuarios))

# Mostrar resultados
print("Nombres de todos los usuarios:")
print(nombres)

print("\nUsuarios con ID mayor a 2:")
print(usuarios_filtrados)
