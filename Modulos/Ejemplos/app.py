# Importando archivos
###
# Usamos la palabra reservado from
# Le indicamos el nombre del archivo
# Usamos la palabra reservada import
# Le indicamos el bloque de codigo que vamos a usar
# Luego podemos llamar a dicho bloque de codigo
# ###
from Usuarios import guardar, pagar_impuestos

guardar() # Llamamos a esta funcion desde el archivo de Usuarios
pagar_impuestos('Los impuestos son un robo!!') # Asi le pasamos argumentos a la funcion
