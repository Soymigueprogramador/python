# Inyección de dependencias

# ===============================
# Inyección de dependencias con clases
# ===============================

class Correa:
    def usar(self):
        print("Usando la correa")


class Perro:
    def __init__(self, correa):
        # Se inyecta la dependencia (una instancia, no la clase)
        self.correa = correa

    def pasear(self):
        self.correa.usar()


# Uso
correa = Correa()
perro = Perro(correa)
perro.pasear()


# ===============================
# Inyección de dependencias con funciones
# ===============================

# Ejemplo SIN inyección de dependencias
# (acoplamiento fuerte)
import usuarios

def guardar_sin_inyeccion():
    usuarios.guardar()


# Ejemplo CON inyección de dependencias
# (acoplamiento débil)
def guardar_con_inyeccion(entidad):
    entidad.guardar()


# Ejemplo de entidad
class Usuario:
    def guardar(self):
        print("Usuario guardado")


# Uso
usuario = Usuario()
guardar_con_inyeccion(usuario)
