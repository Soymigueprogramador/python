# Browser

# Integrando el explorador web (Navegador) con python

# ¿Porque usar un explorador web en python?
###
# Podriamos crear un script el cual puede ser levantado por el explorador web.
# Podriamos crear un web straper para buscar ofertas.
# ###

# Integrando el explorador web
import webbrowser

print('Producto encontrado')

# Abre el navegador en esa URL (Link)
webbrowser.open("https://www.google.com/")

# Abre una nueva pestaña en esa URL (Link)
webbrowser.open_new("https://www.google.com/")

# Abre una nueva pestaña del navegador abierto en esa URL (Link)
webbrowser.open_new_tab("https://www.google.com/")
