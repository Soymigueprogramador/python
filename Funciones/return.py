# return.

# El return nos permite tomar el valor de una función y pasársela a otra función, entre otras cosas.

def suma(a, b):
    resultado = a + b  # En la variable resultado guardamos el valor de la suma.
    return resultado   # Retornamos el valor de esa variable.

# Formas para pasar el valor de la función a otra variable o función.
c = suma(5, 5)
d = suma(c, 20)

print(c)
print(d)
