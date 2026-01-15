# ===============================
# IMPORTS CONDICIONALES EN PYTHON
# ===============================

# En Python, un import condicional ocurre cuando un módulo
# se importa solo si se cumple una condición determinada.
#
# A diferencia de otros lenguajes, Python permite colocar
# imports en cualquier parte del archivo: dentro de if,
# funciones, bucles o bloques try/except.


# -------------------------------------------------------
# EJEMPLO 1: Import condicional con if
# -------------------------------------------------------

usar_matematica = True

if usar_matematica:
    import math
    print("Raíz cuadrada de 16:", math.sqrt(16))

# El módulo math solo se importa si la condición es True.


# -------------------------------------------------------
# EJEMPLO 2: Import condicional según el sistema operativo
# -------------------------------------------------------

import os

if os.name == 'nt':
    import msvcrt
    print("Sistema Windows: módulo msvcrt importado")
else:
    import tty
    print("Sistema Unix/Linux: módulo tty importado")

# Esto se usa mucho cuando el código debe funcionar
# en distintos sistemas operativos.


# -------------------------------------------------------
# EJEMPLO 3: Import condicional con try / except
# -------------------------------------------------------

# Se utiliza para compatibilidad entre versiones
# o cuando un módulo puede no estar instalado.

try:
    import importlib.resources as resources
    print("Usando importlib.resources (Python moderno)")
except ImportError:
    import importlib_resources as resources
    print("Usando importlib_resources (versión alternativa)")

# Si el primer import falla, se ejecuta el segundo.


# -------------------------------------------------------
# EJEMPLO 4: Import condicional dentro de una función
# -------------------------------------------------------

def calcular():
    import random
    return random.randint(1, 10)

print("Número aleatorio:", calcular())

# El módulo random solo se importa cuando la función se ejecuta.
# Esto puede mejorar el rendimiento en programas grandes.


# -------------------------------------------------------
# ACLARACIÓN IMPORTANTE
# -------------------------------------------------------

# Un comentario como:
#   # Import condicionales
# no hace nada por sí mismo.
#
# Solo describe la intención del código que sigue.
# Para que sea correcto, el código DEBE incluir imports
# dentro de condiciones, como en los ejemplos anteriores.
