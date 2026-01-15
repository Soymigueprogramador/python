# Ciclo while

# El ciclo while es un ciclo inexacto, lo usamos cuando necesitamos verificar si una condición se cumple o no.

# Sintaxis de un ciclo while:
# while condición:
#     # Código a ejecutar mientras la condición sea verdadera

# Ejemplo en código:
#numero = 1

#while numero < 10:
#    print(numero)
#    numero *= 2
#    #break  # Esto hace que el ciclo se detenga después de la primera iteración

comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)
