# Sets

# ¿Qué es un set?
###
# Los sets son un conjunto de datos que no se repiten y no están ordenados.
# Podemos trabajar con los sets de forma similar a las listas.
###

numeros_enteros = {1, 2, 3, 4, 5, 6, 7}

# Ejemplo de uso de métodos con sets:
numeros_enteros.add(8)      # Agrega un elemento
numeros_enteros.remove(2)   # Elimina un elemento

# Transformando una lista en un sets:
lista = [ 1, 2, 3 ] # Lista de numeros
setsTransformado = set(lista) # Lista de numeros transformada a sets.

# Operadores para los sets.
###
# Operador de union | Se utiliza para crear una union entre los sets que creamos.
# Operador de ^ & Se utiliza para devolver los elementos que esten dentro de ambos sets.
# Operador de diferencia - Se utiliza para calcular la diferencia entre ambos sets.
# Operador de diferencia simetrica ^ Se utiliza para devolver los elementos que no esten duplicados en los sets.
# ###

prueba = { 1, 2, 3 }
prueba2 = { 4, 5, 6 }

print(prueba | prueba2)
print(prueba & prueba2)
print(prueba - prueba2)
print(prueba ^ prueba2)

# Preguntando si un elemento existe dentro de un sets.
if 9 in lista:
    print('Elemento encontrado')
else:
    print('Elemento no encontrado')

#print(numeros_enteros)
#print(setsTransformado)
