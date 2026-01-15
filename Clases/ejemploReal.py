# Ejemplo real.

class Model(): # Clase para el modelo de la tabla.
    tabla = False

    def __init__(self): # Constructor
        if not self.tabla: # Pregunta si la tabla definida
            print('Tabla no definida')
        else:
            print('Tabla definida')

    def guardarDatos(self): # Metodo para guardar los datos en la tabla.
        print(f'Los datos fueron guardados en {self.tabla} en la base de datos')

    @classmethod
    def buscar_por_id(self, _id): # Metodo para buscar usuarios por ID.
        print(f'Buscando usuarios por {_id} en la tabla de {self.tabla}')

class Usuario(Model): # Clase de usuario que hereda los metodos de la clase model.
    tabla = 'Usuario'

usuario = Usuario()
usuario.guardarDatos()
Usuario.buscar_por_id(123)
