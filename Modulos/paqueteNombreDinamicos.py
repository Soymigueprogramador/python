# Paquetes con nombres dinámicos

import paquete.util

print(paquete.util.__name__)

###
# En Python, los módulos y paquetes son dinámicos.
# Esto significa que su nombre puede variar según
# la forma en que el programa sea ejecutado o importado.
#
# Por ejemplo:
# - Si el archivo se ejecuta directamente, __name__ vale "__main__".
# - Si se importa desde otro módulo, __name__ toma el nombre real del módulo.
###
