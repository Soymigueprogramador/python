# Contenedores

# ¿Qué son y para qué se usan los contenedores?
# Son estructuras que almacenan y organizan múltiples objetos, como listas o diccionarios.

class Productos:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: ${self.precio}"

class Categorias:
    def __init__(self, nombre):  # Solo pedimos el nombre
        self.nombre = nombre
        self.productos = []  # Lista vacía para guardar productos

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def mostrarProductos(self):
        print(f"Categoría: {self.nombre}")
        for producto in self.productos:
            print(producto)

# Creamos productos
producto1 = Productos('Pepsi',     900)
producto2 = Productos('Manaos',    950)
producto3 = Productos('Coca Cola', 1000)
producto4 = Productos('Chocolates',2000)
producto5 = Productos('Caramelos', 200)

# Creamos la categoría y agregamos productos
bebidas = Categorias('Bebidas')
bebidas.agregarProducto(producto1)
bebidas.agregarProducto(producto2)
bebidas.agregarProducto(producto3)

golosinas = Categorias('Golosinas')
golosinas.agregarProducto(producto4)
golosinas.agregarProducto(producto5)

# Mostramos los productos
bebidas.mostrarProductos()
golosinas.mostrarProductos()
