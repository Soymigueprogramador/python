# Metodos pagicos

# ¿Que son los metodos magicos?
###
# Los metodos magicos son metodos que se van a ejecutar cuando nosotros no loe estemos llamando directamente.
# El constructor es un metodo magico.
# ###

# Creamos una clase llamada Perro.
class Perro:
    # Constructor.
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar():
        print(f"Mi perro {self.nombre} de {self.edad} años de edad se la pasa ladrando!!")

    def __str__(self):
        return f"Mi perro {self.nombre} de {self.edad} años de edad se la pasa ladrando!!"

    # Metodo magico destructor.
    def __delattr__(self, nombre):
        return f" Juira {self.nombre} "

nombre_perro = Perro('Proser', 3) # Metodo magico imbocado de forma indirecta.
print(nombre_perro)
#nombre_perro.__  Muestra todas los metodos disponibles para nuestra instancia.

# Metodos magicos mas importantes
print(nombre_perro) # Imprime el contedio del metodo __str__
perro = str(nombre_perro) # Imprime lo que queremos convertir a string.

# Documentacion de metodos magicos en python:
# https://www.geeksforgeeks.org/python/dunder-magic-methods-python/

# ¿ Como funciona el metodo magico destructor ?
###
# El metodo magico destructor se ejecuta cuando eliminamos un objeto.
# ###

# Ejemplo:
nombre_perro2 = Perro('Guau guau', 3)
del nombre_perro2  # Esto ejecuta automáticamente __del__
