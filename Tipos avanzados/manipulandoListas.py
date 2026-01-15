# Manipulando listas

mascotas = ['Proser', 'orco', 'guauguau', 'fatiga']

# Manipulando las listas.
print(mascotas)  # Lista original
print(mascotas[0])  # Esto imprimirá el primer elemento de la lista.
mascotas[1] = 'cachilo' # Esto midifica el elemento
print(mascotas[0:2])  # Muestra una parte de la lista, desde el 0 hasta una parte determinada.
# El indice izquierdo es desde donde arranca y el indice derecho es hasta donde va a llegar
print(mascotas[1::2]) # Esto muestra los elementos pares de la lista
print(mascotas[0::2]) # Esto muestra los elementos impares de la lista
print(mascotas)  # Lista modificada

# Manipulando una lista de numeros.
numeros = list(range(21))
print(numeros[::2])  # Numeros pares
print(numeros[1::2]) # Numeros impares
