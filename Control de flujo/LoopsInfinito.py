# Loops infinitos.

# Los loops infinitos son bloque de codigo que no terminan nunca de ejecutarse,
# Esto ocurre cuando no le indicamos un condicion de salida como un brack.

comando = ""

while True: # Esto hace que el programa se ejecute indefinidamente al no tener una condicion de salida.
    comando = input("$ ")
    print(comando)
