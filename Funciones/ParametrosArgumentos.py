# Parametros y argumentos.

# Parametros.
###
# Entre los parentesis le podemos pasar parametros a una funcion.
# Estos parametros solo se pueden usar dentro del bloque de codigo de la funcion.
# Cuando hacemos el llamado debemos pasarle el valor de los parametros
# ###

# Ejemplo en codigo:
def saludar(nombre, apellido):
    print(f'Hola mi nombre es {nombre} y mi apellido es {apellido}')

saludar('Miguel', 'Salazar') # Llamado a la funcion con los argumentos de los parametros.

# Argumentos:
###
# Los argumentos son los valores que le pasamos al llamado de la funcion
# ###

# Agumento opcional.
###
# Un argumento opcional es un tipo de parametros al que le podemos agregar un valor por defecto.
# Este valor se asignara en caso de no indicarle un parametro espesifico.
###

def novia(nombre = 'Aru'):
    print(f'el nombre de mi novia es {nombre}')

novia('Celeste')

# Argumentos nombrados.
###
# Los argumentos nombrados los usamos cuando no sabemos en que orden se los vamos a pasar.
###

# Ejemplo:
def chica(apellido= 'Romero', nombre = 'Araceli'):
    print(f'Hola soy {nombre, apellido}')

chica('Marina', 'chavez')
