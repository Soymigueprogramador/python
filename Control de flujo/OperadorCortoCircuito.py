# Operador de corto circuito

# Los operadores de corto circuito en Python (como `and` y `or`) evalúan las condiciones de izquierda a derecha.
# En una expresión con `and`, si una condición es False, se detiene y no evalúa las siguientes.
# En una expresión con `or`, si una condición es True, se detiene y no evalúa las siguientes.

gas = True
prendido = True
edad = 18

if not gas and prendido and edad > 19:
    print("Aprobado, podés manejar")
else:
    print("No aprobado, no podés manejar")
