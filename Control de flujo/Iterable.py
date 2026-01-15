# Iterables en un ciclo for.

#  Nosotros podemos iterar (es como buscar) por un dato espesifico.

# Ejemplo en codigo.
buscar = 33

for numero in range(6): # range(6) es un iterable.
    print(numero)
    if numero == buscar:
        print("Número encontrado:", numero)
        break
else:
    print(" Numero no encontrado ")

# Ejemplo de iterable con string.
for char in " Hola mundo ":
    print(char)
