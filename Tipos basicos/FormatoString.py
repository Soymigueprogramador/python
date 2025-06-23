nombre = 'Miguel'
apellido = 'Salazar'

# Para concatenar variables usamos el signo + (Esta no es la mejor opcion)
#nombreCompleto = nombre + " " + apellido

# Usamos la letra f como operador de formateo de estring (Esta es la forma correcta)
nombreCompleto = f" {nombre} {apellido} "

# Siempre que escribamos dentro de las " " podremos escribir la instruccion que sea
nombreCompleto = f" {nombre[0]} { 8 + 2 } "

print(nombreCompleto)
