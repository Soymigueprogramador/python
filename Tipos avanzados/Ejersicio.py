# Ejercicio

# 1
# Crear una función que elimine los espacios de un string y retorne los caracteres restantes.
# Se debe utilizar comprensión de listas.

# 2
# Contar cuántas veces se repite cada carácter en un string.

# 3
# Ordenar las llaves de un diccionario según sus valores y devolver una lista que contenga tuplas.

# 4
# Dado un listado de tuplas, devolver aquella que tenga el mayor valor.

# 5
# Crear un programa que devuelva un mensaje que diga: "Los caracteres que más se repiten son".
# Se debe devolver una lista con los caracteres que más se repiten, y estos deben estar en mayúsculas.

# 6
# Combinar la solución de los ejercicios anteriores para encontrar los caracteres que más se repiten en un string.

# EJERCICIO 1: Eliminar espacios de un string usando comprensión de listas
def eliminar_espacios(mensaje):
    return ''.join([char for char in mensaje if char != ' '])

# EJERCICIO 2: Contar cuántas veces se repite cada carácter en un string
def contar_caracteres(mensaje):
    contador = {}
    for char in mensaje:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1
    return contador

# EJERCICIO 3: Ordenar las llaves de un diccionario por su valor y devolver lista de tuplas
def ordenar_por_valor(diccionario):
    return sorted(diccionario.items(), key=lambda item: item[1])

# EJERCICIO 4: De una lista de tuplas, devolver la que tenga mayor valor
def tupla_mayor(lista_tuplas):
    return max(lista_tuplas, key=lambda tupla: tupla[1])

# EJERCICIO 5: Mostrar los caracteres más repetidos (en mayúsculas)
def caracteres_mas_repetidos(mensaje):
    mensaje = eliminar_espacios(mensaje.lower())
    contador = contar_caracteres(mensaje)
    max_repeticiones = max(contador.values())
    mas_repetidos = [char.upper() for char, cant in contador.items() if cant == max_repeticiones]
    print("Los caracteres que más se repiten son:", mas_repetidos)

# EJERCICIO 6: Combinar todo
def ejercicio_completo(mensaje):
    mensaje_sin_espacios = eliminar_espacios(mensaje.lower())
    contador = contar_caracteres(mensaje_sin_espacios)
    max_repeticiones = max(contador.values())
    mas_repetidos = [char.upper() for char, cant in contador.items() if cant == max_repeticiones]
    print("Los caracteres que más se repiten son:", mas_repetidos)

# EJEMPLOS DE USO:

# Ejercicio 1
mensaje = ' Hola a todos desde los ejercicios en python '
print("Sin espacios:", eliminar_espacios(mensaje))

# Ejercicio 2
print("Conteo de caracteres:", contar_caracteres(mensaje))

# Ejercicio 3
datos = {'a': 3, 'b': 1, 'c': 2}
print("Ordenados por valor:", ordenar_por_valor(datos))

# Ejercicio 4
lista_tuplas = [('m', 3), ('s', 1), ('t', 5)]
print("Tupla con mayor valor:", tupla_mayor(lista_tuplas))

# Ejercicio 5
caracteres_mas_repetidos("Hola hola desde Python")

# Ejercicio 6
mensaje_final = """
El Día del Programador se celebra cada año el día número 256 del calendario (el 13 de septiembre en años normales y el 12 de septiembre en años bisiestos).

¿Por qué el 256?
Porque 256 es un número muy especial en informática: es la cantidad de valores distintos que puede representar un byte (desde 0 hasta 255). Además, es 2 elevado a la 8ª potencia (2⁸).

¿Quién lo propuso?
Fue propuesto por programadores rusos en 2002 y en 2009 se convirtió en una fecha oficial en Rusia. Desde entonces, muchos países lo celebran informalmente.

¿Qué se celebra?
Se celebra el trabajo, el ingenio y el impacto de los programadores en la tecnología moderna: desde sitios web y videojuegos hasta inteligencia artificial y sistemas críticos.

¡Feliz Día del Programador a quienes escriben código que cambia el mundo línea a línea!
"""

ejercicio_completo(mensaje_final)
