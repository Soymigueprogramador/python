# Polimorfismo
# ¿Qué es el polimorfismo?
# Es la capacidad de que diferentes clases respondan al mismo método de distintas maneras.

from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass

class Usuario(Model):
    def guardar(self):
        print('Guardando en la base de datos!!')

class Sesion(Model):
    def guardar(self):
        print('Guardando en archivo!!')

# Función que usa polimorfismo
def guardar_entidad(entidad: Model):
    entidad.guardar()

# Ejemplo de uso
usuario = Usuario()
sesion = Sesion()

guardar_entidad(usuario)
guardar_entidad(sesion) 
