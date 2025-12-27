# Excepciones
# Para crear excepciones personalizadas hacemos esto:
###
# Creamos una clase para los errores
# Le podemos agregar un string de documentacion
# Podemos crear un constructor para pasarle codigos de error
# ###

# Ejemplo en codigo
class MiError(Exception):
# En caso de heredar excepciones de otra parte del codigo se lo agregamos dentro de los parentesis
    "Aca podemos dejar un mensaje de explicacion de la clase"

    # Codigos de error
    def __init__(self, mensaje, codigo):
        ## Asignando el mensaje de error con el codigo
        self.mensaje = mensaje
        self.codigo = codigo

    # Le pasamos el mensaje con el codigo de error
    def __str__(self):
        return f"mensaje: {self.mensaje} -codigo: {self.codigo}"

def dividir(n=0):
    if n == 0:
        raise MiError('No se puede dividir por cero', 805)
    return 5 / n

try:
    dividir()
except MiError as e:
    print(e)
