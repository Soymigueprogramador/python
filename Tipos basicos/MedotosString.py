# Metodos para los string.

animal = " perro gato marrano "

# Metodos = Es una funcion dentro de un objeto.
print(animal.upper()) #Toma el valor de la variable y lo transforma a mayusculas.
print(animal.lower()) #Toma el valor de la variable y lo transforma a minusculas.
print(animal.capitalize()) #Toma el valor de la variable y convierte el primer caracter en mayuscula
print(animal.title()) #Toma el valor de la variable y convierte la primer letra de cada palabra en mayuscula
print(animal.strip()) #Toma el valor de la variable y elimina los espacios en blanco a cada lado de la primer y ultima palabra
print(animal.lstrip()) #Toma el valor de la variable y elimina los espacios en blanco a izquierda del string
print(animal.rstrip()) #Toma el valor de la variable y elimina los espacios en blanco a derecha del string
print(animal.find("m")) #Toma el valor de la variable y nos devuelve el indice del string indicado,
#Dentro de los parentes y dentro de las "" escribimos el caracter buscado,
#Si encuentra un caracter devuelve un numero positivo, de lo contrario devuelve un numero negativo
print(animal.replace("marrano", "pato")) #Toma el valor de la variable y reemplaza el valor por lo indicado entre ""
#Para este metodo necesitamos pasarle 2 argumentos:
#El original que va a buscar y reemplazar y el el nuevo argumento que va a agregar
print("pa" in animal) #Toma el valor de la variable y devuelve un true o false si encuentra o no encuentra lo indicado
print("pa" in animal) #En este caso devuelve un false.
print("pe" in animal) #En este caso devuelve un true.
print("conejo" not in animal) #Toma el valor de la variable y comprueba si el string NO esta
