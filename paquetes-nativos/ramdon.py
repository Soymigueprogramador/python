# Random
# Trabajando con números random

import random

numeros = [1, 2, 3, 4, 5]
numero = [1, 2, 3, 4, 5]
random.shuffle(numeros)

print(
    random.random(),        # Genera un número aleatorio entre 0 y 1
    random.randint(1, 10),  # Genera un número aleatorio entre dos números distintos
    numeros,                # Lista ya desordenada
    random.choice(numero),   # Obtenemos un numero aleatorio del nuevo listado
    random.choices(          # Obtenemos mas de un numero aleatorio del nuevo listado
        numero, # Le pasamos la lista
        k=3     # Le pasamos la cantidad de elementos que vamos a necesitar
    )
    # Esos metodos tambien funcionan con strings.
)

###
# Con esto podemos generar contraseñas aleatorias
# Con esto podemos generar ID aleatorios
# ###

# Generando una contraseña aleatoria
import string

# Creamos variables de letras y digitos
letras = string.ascii_letters
digitos = string.digits

seleccion = random.choices(
    letras + digitos, # Le indicamos que debe concatenar ambas variables
    k=16,             # Le indicamos la cantidad de caracteres que debe tener
)

clave = "".join(seleccion) # Genera una clave alfanumerica aleatoria
print(clave)
