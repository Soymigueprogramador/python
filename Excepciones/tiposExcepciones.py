# Tipos de excepciones
# ¿Cuáles son los tipos de excepciones?

###
# Con la palabra reservada Exception capturamos todas las excepciones
# Con la palabra reservada ValueError manejamos una excepción determinada
# Con la palabra reservada NameError manejamos una excepción de forma independiente
###

try:
    n1 = int(input('Ingresa un número: '))
    KUKA  # Provoca un NameError
except ValueError as e:  # Convenciones más usadas (e o ex)
    print('Ingresa un valor que sea correcto')
except NameError as e:
    print('Che, algo salió mal')
