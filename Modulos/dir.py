# Dir

import paquete.util

# print(dir(paquete.util))

# dir
###
# dir() es una función que nos permite listar todos los métodos y atributos
# que están definidos dentro de un módulo o paquete.
# Es especialmente útil cuando trabajamos con frameworks,
# ya que nos permite inspeccionar qué funcionalidades expone cada módulo.
###

# Atributos especiales de módulos y paquetes en Python

# __name__
print(paquete.util.__name__)
# Muestra el nombre del módulo

# __package__
print(paquete.util.__package__)
# Muestra el nombre del paquete al que pertenece el módulo

# __path__
print(paquete.util.__path__)
# Muestra la ruta del paquete (solo existe en paquetes, no en módulos)

# __file__
print(paquete.util.__file__)
# Muestra la ruta completa del archivo del módulo
