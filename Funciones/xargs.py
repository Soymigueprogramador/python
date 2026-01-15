# xargs
###
# Usamos xargs cuando queremos pasarle múltiples parámetros a una función pero no sabemos cuántos serán.
# Para ello tenemos que escribir un * (asterisco) antes del parámetro de la función.
###
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2, 3, 5)
