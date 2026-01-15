# Else y finally

###
# El else solo se ejecuta cuando no se encuentran excepciones
# El finally se ejecuta siempre sin importar las excepciones
# ###

try:
    n1 = int(input('Ingresa un número: '))
except Exception as e:
    print('Ingresa un valor que sea correcto')
else:
    print('Todo esta bien')
finally:
    print('Termino la ejecucion de la app')
