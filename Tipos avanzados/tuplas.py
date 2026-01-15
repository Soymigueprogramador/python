# Tuplas

###
# Las tuplas son similares a las listas, pero no se pueden modificar.
# Se pueden crear nuevas tuplas, pero no modificar las que ya existen.
###

# Esto es una tupla:
# Para crear una tupla tenemos que usar paréntesis ()

numero = (1, 2, 3, 4, 5)

# ¿Qué podemos hacer con las tuplas?
# Concatenar tuplas:
numero1 = (1, 2, 3, 4, 5) + (6, 7, 8, 9, 10)  # Esto es una nueva tupla.

punto = tuple([1, 2, 3, 4, 5])  # Creamos una tupla a partir de una lista.

menosNumero = numero[:2]  # Accediendo a los elementos de una tupla.

primero, *otros = numero  # Desempaquetado de tupla.

for n in numero:
    print(n)

print(numero)
print(numero1)
print(punto)
print(menosNumero)
print(primero, *otros)

# Con las tuplas podemos realizar todas las operaciones que usamos con las listas,
# excepto aquellas que permiten modificarlas.
# Usamos tuplas cuando no queremos modificar accidentalmente un conjunto de datos.

# Para modificar una tupla, primero tenemos que transformarla en una lista.
listaNumeros = list(numero)
listaNumeros[1] = 'PERRO' # Ahora se modifico la lista.
print(listaNumeros)
