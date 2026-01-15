# Operadores lógicos en Python

# Operadores: and, or, not

# Operador and:
# Se utiliza cuando queremos que dos condiciones sean verdaderas al mismo tiempo.
# Ejemplo: Si el usuario y la contraseña son correctos.

# Operador or:
# Se utiliza cuando basta con que una de las condiciones sea verdadera.
# Ejemplo: Si el usuario o el correo es correcto.

# Operador not:
# Se utiliza para negar una condición.
# Ejemplo: Si NO está registrado.

# Código con operador and: Ambos deben ser True para que la operación completa dé True.
gas = True
prendido = True

if gas and prendido:
    print("Aprobado")
else:
    print("No aprobado")

# Código con operador or: Solo uno debe ser True para que la operación completa dé True.
gas = False
prendido = True

if gas or prendido:
    print("Aprobado")
else:
    print("No aprobado")

# Código con operador not: Invierte el valor de la condición.
gas = False
prendido = True

if not gas or prendido:
    print("Aprobado")
else:
    print("No aprobado")

# Operadores combinados

gas = True
prendido = False
edad = 18

if gas and prendido and edad > 19:
    print("Aprobado, podés manejar")
else:
    print("No aprobado, no podés manejar")

gas = True
prendido = True
edad = 18

if gas and (prendido and edad > 19):
    print("Aprobado, podés manejar")
else:
    print("No aprobado, no podés manejar")

gas = True
prendido = True
edad = 18

if not gas and prendido and edad > 19:
    print("Aprobado, podés manejar")
else:
    print("No aprobado, no podés manejar")
