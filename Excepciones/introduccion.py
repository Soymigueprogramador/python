# Introducción a las excepciones
# Las excepciones son tipos de errores que ocurren durante la ejecución de un programa.
# Podemos "capturarlas" para evitar que el programa se detenga.

# Ejemplo:
try:
    n1 = int(input('Ingresa un número: '))
    print(f'Número ingresado: {n1}')
except ValueError:
    print('Error: Debes ingresar un número entero.')
