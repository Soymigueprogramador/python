# Open
# Trabajando con la funcion Open

from io import open


# Escribiendo en un archivo.
#texto1 = "Hola mundo desde python"
texto2 = "HOLA"

archivo = open("Gestion-de-archivos/hola.txt", "w") # Asi le indicamos al python que vamos a escribir
# archivo = open("Gestion-de-archivos/saludo.txt", "w") # Asi hacemos que python genere un nuevo archivo automaticamente


#archivo.write( texto2) # Asi le agregamos el texto al archivo
#archivo.close() # Asi cerramos el archivo para que no ocupe memoria

# Leyendo en un archivo (Forma 1)
# archivo = open("Gestion-de-archivos/hola.txt", "r") # Asi le indicamos que vamos a entrar en modo lectura

# archivo.read() # Asi leemos el archivo
# archivo.close() # Asi cerramos el archivo

# Leyendo el archivo en forma de lista (Forma 2)
# archivo = open("Gestion-de-archivos/hola.txt", "r") # Asi le indicamos que vamos a entrar en modo lectura

# archivo.readline() # Asi leemos el archivo en forma de lista
# archivo.close() # Asi cerramos el archivo

#print(texto2)

# Metodos de la funcion Open

#with open("Gestion-de-archivos/archivos-prueba.txt", "r") as archivo: # Cierra nuestros archivos sin que se lo indiquemos
    # El metodo enter se ejecuta cuando abrimos el archivo
    # print(archivo.readline()) # Carga todo el archivo
    #archivo.seek(0) # Asi le indicamos que a un caracter espesifico
    #for linea in archivo: # Carga una linea a la vez
        #print(linea)

    # El metodo exit se ejecuta cuando terminemos de ejecutar todo el bloque de codigo dentro de with

# Agregamdp cosas añ archivo
archivo = open("Gestion-de-archivos/saludo.txt", "a+")

# archivo.write("Estoy aprendiendo python") # Asi le agregamos este texto al archivo
# archivo.close()

# Lectura y escritura simultaneamente
with open("Gestion-de-archivos/saludo.txt", "r+", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    lineas[0] = "Estoy aprendiendo python desde cero\n"

    archivo.seek(0)
    archivo.writelines(lineas)
    archivo.truncate()
