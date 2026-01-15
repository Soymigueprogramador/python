# Syb-paquetes

# ¿Que son los sub-paquetes?
###
# Los sub-paquetes son paquetes dentro de otros paquetes, es lo mismo que carpetas dentro de carpetas
# ###

# ¿Como crear los sub-paquetes?
###
# 1) Volvemos a crear una carpeta dentro de otra carpeta
# 2( Volvemos a crear un archivo " __init__ "
# ###

# Importando un sub-paquete
###
# Para importar un sub-paquete hacemos esto:
# 1) Usamos la palabra reservada from
# Escribimos el nombre de la carpeta.nombreSub-carpeta.archivo
# 3) Usamos la palabra reservada import
# 4) Escribimos el nombre del bloque de codigo que vamos a usar
# ###

from paquete.util.utilidades import sumar

sumar(5, 21)
