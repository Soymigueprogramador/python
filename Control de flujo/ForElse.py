# Ciclo for con condicionales.

# Al ciclo for le agregamos un condicional.

# Ejemplo en codigo.
buscar = 33

for numero in range(6):
    print(numero)
    if numero == buscar:
        print("Número encontrado:", numero)
        break
else:
    print(" Numero no encontrado ")
