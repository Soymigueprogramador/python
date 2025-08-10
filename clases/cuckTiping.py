# Duck typing
# Un objeto es válido si tiene los métodos requeridos, sin importar su clase.

class Usuario:
    def guardar(self):
        print('Guardando en la base de datos!!')

class Sesion:
    def guardar(self):
        print('Guardando en archivo!!')

# Función que usa polimorfismo vía Duck Typing
def guardar_entidad(entidades):
    # Si es una lista o tupla, recorremos cada objeto
    if isinstance(entidades, (list, tuple)):
        for e in entidades:
            e.guardar()
    else:
        # Si es un solo objeto, lo usamos directamente
        entidades.guardar()

# =====================
# Ejemplo de uso
# =====================

usuario = Usuario()
sesion = Sesion()

print("Ejecutando con lista:")
guardar_entidad([usuario, sesion])  # Lista de objetos

print("\nEjecutando con un solo objeto:")
guardar_entidad(usuario)            # Un solo objeto
guardar_entidad(sesion)             # Un solo objeto
