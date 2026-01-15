# Agregar y eliminar elementos de una lista.

mascotas = [
    'conan',
    'milton',
    'murray',
    'robert',
    'lucas'
]

# Mostrando la lista original.
print(mascotas)

# Agregar elemento a la lista.
###
# Para agregar un elemento a la lista hacemos esto:
# Nombre de la lista
# Usamos el metodo .insert()
# Dentro de los parentesis escribimos el indice que va a ocupar, el valor del mismo
# Ejemplo: nombreLista.insert(indice, valor)
###

# Ejemplo en codigo:
mascotas.insert(6, 'Proser') # Agrego un elemento a la lista.
mascotas.append('Malevo') # Agrego un elemento al final de la lista.
print(mascotas) # Va despues del codigo que agrega un elemento a la lista.

# Eliminar elementos de la lista.
###
# Para eliminar un elemento de la lista hacemos esto:
# Nombre de la lista
# Usamos el metodo .remove()
# Entre los parentesis escribimos el elemento a eliminar
# Ejemplo: nombreLista.remove(elemento)
###

# Ejemplo en codigo:
mascotas.remove('Proser') # Elimina un elemento de la lista
# Si la lista tiene elementos repetidos solo se eliminara el primer elemento con ese nombre.
mascotas.pop() # Elimina un elemento el ultimo elemento de la lista
# Para eliminar un elemento espesifico solo le pasamos el indice.

# Otros metodos para eliminar elementos de una lista.
del mascotas[3] # Elimina el elemento que esta en ese indice
mascotas.clear() # Elimina todos los elementos de la lista.
print(mascotas) # Va despues del codigo que elimina un elemento a la lista.
