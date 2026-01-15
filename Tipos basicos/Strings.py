# Para crear una variable que contenga un string relativamente corto hacemos esto:

nombre_variable = "Miguel"
apellido_variable = 'Salazar'

# Para crear una variable que contenga un string mucho más largo usamos las triples comillas dobles así:

nombre_descripcion = """ 
Estoy aprendiendo Python porque siempre lo quise aprender.
"""

# En una variable con un string corto podemos usar comillas dobles o simples.

print(nombre_variable, apellido_variable, nombre_descripcion)

# Función len
###
# La función len es una función integrada en Python que nos permite saber cuál es
# la longitud (cantidad de caracteres) de un string.
###

# ¿Cómo llamamos a la función len?
###
# Para llamar a dicha función hacemos lo siguiente:
# - Usamos la palabra reservada len
# - Abrimos paréntesis e indicamos dentro la variable o string
# Ejemplo de código: len(nombre_de_la_variable)
###

print(len(nombre_descripcion))

# Para poder acceder a un carácter específico del string hacemos esto:
###
# - Imprimimos la variable
# - Usamos corchetes y dentro indicamos el índice del carácter que queremos acceder
###

print(nombre_descripcion[15])

# Para cortar (hacer slicing) un string hacemos esto:
###
# - Imprimimos la variable
# - Entre corchetes indicamos desde dónde : hasta dónde queremos cortar
###

print(nombre_variable[0:5])

# Costa una parte del string y completa la parte restante.
print(nombre_variable[0:])
print(nombre_variable[:5])

# Muestra todo el string ya que python asume automaticamente la referencia completa. 
print(nombre_variable[:])
