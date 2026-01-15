# Invocando excepciones

# Definimos una función que recibe un número como parámetro
# Si no se pasa ningún valor, n toma 0 por defecto

def dividir(n=0):

    # Validamos si el valor es 0 para evitar una división inválida
    if n == 0:
        # Lanzamos manualmente una excepción indicando el error
        raise ZeroDivisionError('No se puede dividir por cero')

    # Si el valor es válido, realizamos la división
    return 5 / n

try:
    # Llamamos a la función sin pasar argumentos
    dividir()
except ZeroDivisionError as e:
    # Capturamos la excepción y mostramos un mensaje de error
    print('No se puede dividir por cero')
