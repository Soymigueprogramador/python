# Propiedades de las clases.

# Cuando hablamos de propiedades o atributos nos referimos a lo mismo.

class Perro:
    patas = 4 # Propiedad o argumento
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} ¡Dice GUAU GUAU!")
        print(f"Tiene {self.edad} años de edad")

mostrar = Perro('Proser', 1)
mostrar2 = Perro('Orco', 2)

Perro.patas = 2    # Asi se cambia el valor de una propiedad.
                   # Lo cambia para todas las instancias de la clase.

mostrar.patas = 9  # Solo cambia el valor para la instancia pero no para la clase.
print(Perro.patas) # Accedemos a la propiedad.

mostrar.ladrar()
mostrar2.ladrar()
