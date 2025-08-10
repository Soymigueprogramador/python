# Herencia

# ¿Qué es y cómo funciona la herencia en las clases de Python?
# Cuando tenemos muchas clases que comparten varios métodos, modificar esos métodos
# en todas las clases sería tedioso. La herencia permite definir esos métodos en una clase
# base y hacer que las demás clases hereden de ella, evitando duplicación.
# Si cambiamos algo en los métodos de la clase base, el cambio se refleja en todas las clases que hereden de ella.

# ¿Cómo definimos una clase para que sirva de herencia?
# 1. Creamos una clase base con los métodos y atributos comunes.
# 2. Creamos las clases que heredan de la clase base colocando el nombre de la clase base
#    entre paréntesis después del nombre de la clase hija.
# Ejemplo:
# class ClaseBase:
#     metodos...
# class ClaseHija(ClaseBase):
#     resto del código...

class Animal:
    def comer(self):
        print('Es hora de comer!!')

class Perro(Animal):
    def pasear(self):
        print('Es hora de salir a pasear!!')

class PerroRaro(Perro):
    def programar(self):
        print('¡Mi perro es programador!!')

# Ejemplo de uso
er_perro = Perro()
er_perro.pasear()
er_perro.comer()

ro_perro = PerroRaro()
ro_perro.comer()
ro_perro.pasear()
ro_perro.programar()
