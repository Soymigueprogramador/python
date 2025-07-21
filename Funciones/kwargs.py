# kwargs.
# keyword arguments

###
# En Python cuando estamos usando los kwargs y hacemos el llamado a la funcion tenemos que pasarle el nombre del argumento
# ###

def getProduct(**datos): # A estos datos se los conoce como diccionarios.
    print(datos ['name'], datos['profesion']) # De esta forma podemos acceder a cada uno de los diccionarios.

getProduct(id = 'id', name = 'Miguel', profesion = 'Programador') # Asi como se ve aca.
# Al llamado de la funcion le podemos pasar todos los argumentos que queramos.
