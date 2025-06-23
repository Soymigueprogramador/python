x = input("")

# Conversiones de tipos.
###
# int() Toma un dato y lo transforma a un numero entero (Ejemplo: 2).
# str() Toma cualquier dato y los transforma a un string.
# float() Toma un dato y lo transforma a un numero flotante (Ejemplo: 1.5).
# bool() Toma un dato y lo transforma a un booleano (Ejemplo: true o false)
###

# bool() Tomo absolutamente cualquier dato y lo transforma a booleano.
###
# En python existe un concepto llamado "TRYTLY y Falsy".
# Quiere decir que van a existir siertos tipos de datos que van a ser evaluados como true o false.
# Estos datos son:
# " " string vacios
# 0 el numero cero
# Un objeto llamado none
###

# Probando los ejemplos de bool() en codigo. 
print(bool(""))
print(bool(" "))
print(bool("0"))
print(bool(None))
print(bool(0))
