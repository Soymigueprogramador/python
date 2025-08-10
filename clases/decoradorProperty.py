# Decorador @property

# ¿Qué es el decorador @property?
# Es una forma de definir métodos "getter" y "setter" como si fueran atributos.
# Permite acceder y modificar propiedades privadas de forma controlada.

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre  # Esto llama al setter (gracias a @property)

    @property  # Convierte al método en una propiedad.
    def nombre(self):
        # Getter: devuelve el valor de la propiedad privada
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        # Setter: valida y asigna un nuevo valor a la propiedad privada
        if nombre.strip():
            print('Pasando por setter')
            self.__nombre = nombre
        else:
            raise ValueError("El nombre no puede estar vacío")

# Creamos una instancia
persona1 = Persona('Miguel')

# Accedemos al nombre usando la sintaxis de atributo, aunque internamente usa el getter
print(persona1.nombre)

# También podemos modificar el nombre así (esto llama al setter)
persona1.nombre = "Celeste"
print(persona1.nombre)
