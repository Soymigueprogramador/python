# Propiedades y métodos privados en Python

# ¿Qué son las propiedades privadas?
# Una propiedad privada es una propiedad que no debería modificarse
# directamente desde fuera de la clase (aunque Python no lo impide del todo).

class Perro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Propiedad "privada" usando doble guión bajo
        self.edad = edad        # Propiedad pública

    # Metodo para acceder al nombre.
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre


    def __str__(self):
        return f"Perro(nombre={self.__nombre}, edad={self.edad})"

    def ladrar(self):
        print(f"{self.__nombre} ¡Dice GUAU GUAU!")

    @classmethod
    def factory(cls):
        return cls("Proser", 1)

# Creamos una instancia del perro usando el método de clase 'factory'
perro1 = Perro.factory()

# Usamos el método ladrar
perro1.ladrar()
print(perro1.__dict__) # Es un diccionario que contiene todas las propiedades de una instancia.
