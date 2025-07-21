# Depuracion.

def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
        return resultado

print('PERRO')
l = largo('Hola a todos')
print(l)

# Pasos para usar el depurador:
###
# Damos click en el icono del depurador (Barra lateral izquierda en el icono de un incecto con el boton de play)
# Seleccionamos en "create a launch.json" (En el explorador se creara una carpeta llama "vscode" alli adentro estara el archivo .json que fue creado)
# Volvemos abrir el depurador y creamos un punto de quiebre donde el depurador se detendra
# ###