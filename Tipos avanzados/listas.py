# Listas

###
# En una lista de python podemos:
# Listas de numeros,
# Listas de caracteres,
# Meter una lista dentro de otra,
# Podemos juntas varias listas.
# Entre otras.
###

# Syntaxis de listas en python
###
# Nombre de la lista
# Usamos el singno =
# Abrimos corchetes []
# Dentro de los corchetes ingresamos el valor de esa lista [Valor de la lista]
####

# Codigo de ejemplo:
numeros = [ 1, 2, 3, 4, 5 ]                       # Lista de numeros
palabras = [ 'mama', 'papa', 'perro' ]            # Lista de palabras
caracteres = [ 'A', 'B', 'C' ]                    # Lista de caracteres
listaCombinadas = [ 'A', 1, True, 'mama', False ] # Lista de combinada
booleanos = [ True, False ]                       # Lista de booleanos
listasAnidadas = [ ['mama'], [1, 2, 3]]           # Listas anidadas
ceros = [ 0 ] * 10                                # Listado con valor multiplicado
alfanumerico = numeros + caracteres               # Listas unidas
rango = list(range(10))                           # Lista con un rango
rango2 = list(range(10 + 1))                      # Lista con un rango y que agrega 1 a la lista
char = list('Hola mundo desde python')            # Lista con caracteres separados

print(numeros)
print(palabras)
print(caracteres)
print(listaCombinadas)
print(booleanos)
print(listasAnidadas)
print(ceros)
print(alfanumerico)
print(rango)
print(rango2)
print(char)

# Las listas en Python se escriben igual que:
###
# Vector en C++
# Arrays en JavaScript
###
