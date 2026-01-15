# Iterar listas

mascotas = [
    {"nombre": "Firulais", "especie": "Perro", "edad": 5, "dueño": "Juan"},
    {"nombre": "Mishi", "especie": "Gato", "edad": 3, "dueño": "Lucía"},
    {"nombre": "Bunny", "especie": "Conejo", "edad": 2, "dueño": "Martín"},
    {"nombre": "Coco", "especie": "Loro", "edad": 4, "dueño": "Sofía"},
    {"nombre": "Rocky", "especie": "Hamster", "edad": 1, "dueño": "Pedro"},
    {"nombre": "Nala", "especie": "Gata", "edad": 2, "dueño": "Valeria"},
    {"nombre": "Toby", "especie": "Perro", "edad": 6, "dueño": "Carla"},
    {"nombre": "Kiwi", "especie": "Tortuga", "edad": 10, "dueño": "Diego"},
    {"nombre": "Luna", "especie": "Gata", "edad": 3, "dueño": "María"},
    {"nombre": "Max", "especie": "Perro", "edad": 4, "dueño": "José"}
]

# Desempaquetar los primeros elementos
primero, segundo, *otros = mascotas

print("Primero:", primero)
print("Segundo:", segundo)
print("Otros:", otros)

print("\n--- Iterando la lista completa ---\n")

# Iterar la lista con índice
for indice, mascota in enumerate(mascotas):
    print(f"{indice}: {mascota['nombre']} ({mascota['especie']}) - {mascota['edad']} años, dueño: {mascota['dueño']}")
