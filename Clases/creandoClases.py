# Creando clases en Python

# ¿Cómo crear una clase?
# Para crear una clase hacemos lo siguiente:
###
# Usamos la palabra reservada `class`.
# Le asignamos un nombre: (El nombre debe empezar con mayúscula,
#                          si el nombre tiene dos palabras, ambas deben empezar con mayúscula).
# EJEMPLO: class Perro:
# EJEMPLO: class MiPerro:
#   resto del código
# Cuando creamos una función dentro de una clase, esta se llama "método".
# Dentro de los paréntesis de los métodos debemos agregar "self".
# EJEMPLO: def nombreMetodo(self):
###

# Ejemplo en código.
class Perro:                      # Definición y nombre de la clase
    def ladrar(self):             # Definición y nombre del método
        print("¡GUAU GUAU!")      # Valor del método

mostrar = Perro()                 # Instanciación de la clase asignada a una variable
mostrar.ladrar()                  # Accediendo al método de la clase
print(isinstance(mostrar, Perro)) # Verifica si mostrar es una instancia de Perro

print(mostrar)
print(type(mostrar))
