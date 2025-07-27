# Pilas

# ¿Qué son las pilas en Python?
###
# Una pila es como una torre de monedas, donde vamos poniendo una sobre otra.
# Si queremos sacar una, la primera en salir será la última que llegó (LIFO: Last In, First Out).
###

# Ejemplo en código:
pila = []

pila.append(1)  # Así agregamos elementos a la pila.
pila.append(2)  # Así agregamos elementos a la pila.
pila.append(3)  # Así agregamos elementos a la pila.

ultimo_elemento = pila.pop()  # Eliminamos y obtenemos el último elemento agregado.

# Comprobando si la pila esta vacia.
if not pila:
    print('Esta pila esta vacia')
else:
    print('Esta pila aun no esta vacia')

print(pila)             # Muestra el contenido actual de la pila
print(pila[-1])         # Muestra el ultimo contenido actual de la pila
print(ultimo_elemento)  # Muestra el elemento que se extrajo
