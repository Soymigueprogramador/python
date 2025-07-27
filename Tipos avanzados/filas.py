# Importando un modulo.
from collections import deque

# Filas

# ¿ Que son las filas en python ?
###
# Las filas con una lista de orden, la misma se compene de elementos que se ordenan segun su llegada.
###

# Ejemplo en codigo:
fila = deque([ 1, 2, 3 ]) # Asi creamos una fila.
fila.append(4) # Asi le agregamos elementos a la ffila.


fila.popleft() # Asi eliminamos elementos que esten a la izquierda de la fila.


# Comprobando si la fila esta vacia.
if not fila:
    print("Esta fila esta vacia perro!!")
else:
    print("Esta fila esta no vacia perro!!")

print(fila)
