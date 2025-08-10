# Constructor.

# ¿ Que es un constructor ?
# Un constructor es una funcion que se va a ejecutar siempre que creemos una instancia en nuestra clase.

# ¿ Como creamos un constructor ?
###
# Para crear un constructor hacemos esto:
# Def __init__(self, mas_argumentos):
###

# ¿ Que es y porque se usa self como primer argumento ?
###
# ¿Que es self ?
# Es una palabra reservada que se utiliza como primer argumento en todas las clases de python.
#
# ¿ Para que se usa self ?
# Se utiliza para referencias a las instancias de las clases.
# Si creo otra instancia dela clase tambien se genera otroconstructory otro self.
# ###

class Perro:
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre # Nuevo parametro.
        self.edad = edad # Nuevo parametro.

    def ladrar(self):
        print(f"{self.nombre} ¡Dice GUAU GUAU!")
        print(f"Tiene {self.edad} de edad" )

mostrar = Perro('Proser', 1) # Asile asignamos el valor a la variable de nombre.
mostrar.ladrar()             # Asi mostramos el valor del metodo de la clase. 
mostrar2 = Perro('Orco', 2)
mostrar2.ladrar()

print(mostrar.nombre)
print(mostrar2.nombre)
