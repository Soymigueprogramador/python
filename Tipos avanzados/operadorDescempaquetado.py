# Operador desempaquetado

lista = [1, 2, 3]

# Combinación de listas con el operador de desempaquetado
numero = [1, 2, 3]
numero2 = [4, 5, 6]

lista_combinada = [*numero, *numero2]  # Combino ambas listas

# Utilizando el operador de desempaquetado también para los diccionarios.
# Su sintaxis es similar, pero para los diccionarios se usa **.

# Ejemplo en código:
punto = { "x": 20}
punto2 = {"y": 20}
nuevoPunto = { **punto, **punto2 }

print(lista)
print(*lista)
print(lista_combinada)
print(nuevoPunto) # Asi podemos unir dos diccionarios con el operador de descempaquetado.
