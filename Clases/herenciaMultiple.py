# Herencia multiple

# ¿ Que es la herencia mutiple ?
# La herencia multiple es cuando una clase hereda metodos de varias clases a la vez.

# ¿ Como hacemos para crear una herencia multiple ?
###
# Para qe una clase herede metodos de varias clases hacemos esto.
# EJEMPLO:
# class nombreClase(Herencia1, herencia2):
#   resto del codigo
###

# Problemas de la herencia multiple.
###
# Al utilizar las herencias muliples python las toma desde la derecha a la izquierda,
# si cambiamos ese orden se cambia toda la implementacion.
# Debemos utilizarr las herencias multiples solo cuando las clases sean pequeñas
# o con pocos metodos.
# Si utilizamos las herencias multiples en clases que tengan metodos duplicados
# debemos eliminar esos metodos.
###

class Animal:
    def comer(self):
        print('Es hora de comer!!')

class Perro:
    def pasear(self):
        print('Es hora de salir a pasear!!')

class PerroRaro( Animal, Perro ):
    def programar(self):
        print('¡Mi perro es programador!!')

primer_perro = PerroRaro()
segundo_perro = PerroRaro()
tercer_perro = PerroRaro()

primer_perro.programar()
segundo_perro.comer()
tercer_perro.pasear()
