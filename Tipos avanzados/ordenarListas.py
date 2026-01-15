# Ordenar listas.

numeros = [3, 7, 1, 9, 12, 4, 8, 2, 10, 5]

# Ordenando una lista
# -------------------
# Para ordenar una lista usamos el método .sort()
# Ejemplo: nombre_lista.sort()

#numeros.sort()  # Ordena de menor a mayor
numeros.sort(reverse=True)  # Ordena de mayor a menor
#print("Lista ordenada descendente:", numeros)

# También podemos usar la función sorted(lista), que NO modifica la lista original,
# sino que devuelve una nueva lista ordenada.
numeros2 = sorted(numeros, reverse=True)
#print("Lista original ordenada con sorted:", numeros2)

# ---------------------------------------------
# Trabajando con listas que contienen otras listas
# ---------------------------------------------

usuarios = [
    ['Miguel', 2],
    ['Araceli', 1],
    ['Celeste', 3]
]

# ❗ Si el ID estuviera al principio (posición 0), podríamos hacer:
# usuarios.sort()  ← ordenaría por ID sin problema.

# Pero como el ID está al final (posición 1), debemos decirle a sort cómo comparar.

# Definimos una función que retorne el valor por el cual queremos ordenar
def acomodar(elemento):
    return elemento[1]  # posición del ID

# Ordenamos usando esa función como "key"
usuarios.sort(key=acomodar) # Prdemado normal
usuarios.sort(key=acomodar, reverse=True) # Ordenado al reves

# También se puede hacer con una función anónima (lambda), por ejemplo:
# usuarios.sort(key=lambda x: x[1])

# Mostramos el resultado
print("Usuarios ordenados por ID:", usuarios)
print("Usuarios ordenados por ID (descendente):", usuarios)
