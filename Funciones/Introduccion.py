# Introduccion a funciones.

###
# Una funcion es un bloque de codigo que se utiliza con un unico proposito.
# Este proposito es:
# 1- REUTILIZAR CODIGO.
# 2- CREAR UN CODIGO MAS LEGIBLE.
# EVITAR LA REPETICION DEL CODIGO
# ###

# Funciones conocidas.
###
# print('') = muestra un mensaje por consola.
###

# Creando una funcion propia.
###
# Sintaxis:
# Palabra reservada = def
# Le asignamos un nombre a la funcion = nombreFuncion
# Usamos los parentesis = () alli van los argumentos.
# Usamos los dos puntos = :
# Para llamar a una funcion hacemos esto:
# nombreFuncion()
# ##
# Ejemplo: def nombreFuncion():

def saludo(): # Definicion y nombre de la funcion.
    # Cuerpo de la funcion.
    print('Hola a todos!!')
    print('Estoy aprendiendo funciones en Python')

saludo() # Llamado a la funcion.

# Recordemos que:
# Si hacemos mas de un llamado a una misma funcion esta se ejecutara todas las veces que es llamada.
