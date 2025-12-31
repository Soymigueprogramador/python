# Paquetes

###
# Paquetes:
# Los paquetes apuntan a carpetas
# Modulos:
# Los modulos apuntan a archivos
# ###

# ¿Como crear un paquete?
###
# Para crear un paquete en python hacemos esto:
# 1) Creamos una carpeta para guardar los archivos
# 2) Dentro de la carpeta creamos un archivo llamado " __init__ "
# Con este paquete podemos repartir todo el codigo en distintos archivos
# ###

# Importando un paquete
###
# Para importar un paquete hacemos esto:
# 1) Usamos la palabra reservada de from
# 2) Escribimos el nombre del paquete.nombreDelArchivo
# 3) Usamos la palabra reservada de import
# 4) Escribimos el nombre del bloque de codigo que vamos a usar
# ###

from paquete.acciones import saludar

saludar('Miguel')
