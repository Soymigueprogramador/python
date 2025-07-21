# Ejercicio con funciones.

# Consigna:
# Se debe crear una función para comprobar si una palabra es un palíndromo.
# Esta deberá eliminar los espacios entre las palabras ingresadas y deberá dar vuelta la palabra.
# Las palabras serán pasadas por argumento a la función.

# Mi resolucion del ejersicio.
def es_palindromo(texto):
    palabra_sin_espacios = texto.replace(" ", "").lower()
    palabra_invertida = palabra_sin_espacios[::-1]
    if palabra_sin_espacios == palabra_invertida:
        return True
    else:
        return False

print('mama:', es_palindromo('mama'))
print('neuquen:', es_palindromo('neuquen'))
print('anita lava la tina:', es_palindromo('anita lava la tina'))
print('python:', es_palindromo('python'))

# Respuesta del udemy al ejersicio.
def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

def al_rebes(texto):
    texto_invertido = ""
    for char in texto:
        texto_invertido = char + texto_invertido
    return texto_invertido

def palindromo(texto):
    texto = no_space(texto).lower()
    texto_invertido = al_rebes(texto)
    #return texto == texto_invertido
    print(texto.lower())
    print(texto_invertido.lower())


# Pruebas
print('Amo la paloma:', es_palindromo('Amo la paloma'))  
print('Hola mundo:', es_palindromo('Hola mundo'))              # True
