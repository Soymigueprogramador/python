# Buscando elementos

mascotas = [ 'conan', 'milton', 'murray', 'murray', 'robert', 'licas' ]

# Buscando un elemento.
###
# Para buscar un elemento debemos utilizar el metodo .index() de esta forma:
# nombre de la lista
# Llamamos al metodo .index()
# Dentro de los parentesis indicamos el elemento buscado (elemento)
# Ejemplo: nombreLista.index(elemento a buscar)
###

# Ejemplo en codigo
print(mascotas.index("conan"))

# Buscando un elemento que no existe dentro de la lista.
if 'proser' in mascotas:
    print(mascotas.index("proser"))
else:
    print('Perro no encontrado')

# Metodo count para buscar cuantas veces aparece un mismo elemento en la lista.
print(mascotas.count("murray")) # Muestra la cantidad de veces que aparece el elemento en la lista.
