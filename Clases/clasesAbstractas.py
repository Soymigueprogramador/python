# Clases abstractas
# ¿Qué son las clases abstractas?
# Son clases que no se pueden instanciar directamente y sirven como base para otras clases.
# Se usan para definir métodos que las subclases deben implementar.

from abc import ABC, abstractclassmethod

class Model(ABC):  # Clase base abstracta para el modelo de la tabla
    def __init__(self):  # Constructor
        if not self.tabla:
            print('Tabla no definida')
        else:
            print(f'Tabla definida: {self.tabla}')

    @property
    @abstractclassmethod
    def tabla(self):
        pass

    def guardarDatos(self):  # Método para guardar datos en la tabla
        print(f'Los datos fueron guardados en {self.tabla} en la base de datos')

    @classmethod
    def buscar_por_id(cls, _id):  # Método para buscar usuarios por ID
        print(f'Buscando usuarios por {_id} en la tabla de {cls.tabla}')


class Usuario(Model):  # Clase de usuario que hereda de Model
    tabla = 'Usuario'


# Ejemplo de uso
usuario = Usuario()
usuario.guardarDatos()
Usuario.buscar_por_id(5)
