# Metodos de clases.

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Perro(nombre={self.nombre}, edad={self.edad})"

    @classmethod
    def ladrar(cls):
        print("¡Dice GUAU GUAU!")

    @classmethod
    def factory(cls):
        return cls("Proser", 1)

Perro.ladrar()
nombre_perro = Perro.factory()
print(nombre_perro)
