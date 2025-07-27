# Desempaquetar listas.

numeros = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# Obteniendo los números de la lista.
primero, segundo, tercero, cuarto, quinto, sexto, septimo, obtavo, noveno, decimo = numeros
primero, *otros = numeros

print(primero, numeros)
print(segundo)
print(tercero)
print(decimo)
print(sexto)
print(*otros)
