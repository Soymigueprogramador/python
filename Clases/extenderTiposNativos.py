# Externder tipos nativos

# Forma antigua o tradicional.
lista_de_numeros = list([ 1, 2, 3 ])
lista_de_letras = list([ 'a', 'b', 'c' ])

lista_de_numeros.append(4)
lista_de_numeros.insert(0, 0)
lista_de_numeros.insert(6, 5)

lista_de_letras.append('d')
lista_de_letras.insert(0, 0)
lista_de_letras.insert(5, 'e')


print(lista_de_numeros)
print(lista_de_letras)

# Utilizando clases para hacer lo mismo que lo anterior.
class Lista(list):
    def prepend(self, item): # Agrega el contenido al principio de la lista.
        self.insert(0, item) # Le indicamos la posicion donde se guarda y lo que vamos a guardar alli.

lista = Lista([ 4, 5, 6 ])
lista.append(7)
lista.prepend(3)

print(lista)
