# Anulación de métodos

# ¿Qué es la anulación de métodos?
# La anulación de métodos es cuando tomamos un método heredado
# y lo reemplazamos por otro con diferente funcionalidad.

class Ave:
    def __init__(self):
        self.volare = True

    def volar(self):
        print('Ave voladora')

class Pato(Ave):
    def __init__(self):
        super().__init__()  # Llama al constructor de la superclase (Ave)
        self.volareando = True

    def volar(self):
        super().volar()  # Llama al método volar() de la superclase (Ave)
        print('Pato volador')

# Ejemplo de uso
mi_pato = Pato()
mi_pato.volar()  # Usará el método anulado

mi_ave = Ave()
mi_ave.volar()

# Mostrar atributos
print("¿Ave puede volar?:", mi_ave.volare)
print("¿Pato puede volar?:", mi_pato.volare)
print("¿Pato está volareando?:", mi_pato.volareando)
