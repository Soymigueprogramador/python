# Alcance de las funciones.

# Alcance de una variable dentro de una función:
# ---------------------------------------------
# Las variables que estén dentro de una función solo se pueden usar dentro de esa función.
# Si las quiero llamar desde afuera, me dará un error diciendo que esa variable no está definida.

## Alcance de variables globales:
# Las variables globales son las variables que estan fuera de las funciones.


# Ejemplo:

saludo = 'Hola desde Pyhton' # Esta es una variable global.
def saludos():
    saludo = 'Hola desde Pyhton'
    print(saludo)  # Esta variable solo existe dentro de esta función

def mensaje():
    saludo = 'Hola desde Pyhton'
    print(saludo) # También se imprime dentro de la función

# Llamado a las funciones
saludos()
mensaje()

# Llamado a la variable global.
print(saludo)
