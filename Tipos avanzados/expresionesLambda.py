# Lambda

# Lista de productos como diccionarios
productos = [
    {"nombre": "Auriculares", "precio": 3500},
    {"nombre": "Teclado", "precio": 5000},
    {"nombre": "Mouse", "precio": 3000},
    {"nombre": "Monitor", "precio": 25000},
    {"nombre": "Webcam", "precio": 7000}
]

# Ordenar por precio (de menor a mayor)
productos_ordenados_precio = sorted(productos, key=lambda producto: producto["precio"])

# Ordenar por nombre (alfabéticamente)
productos_ordenados_nombre = sorted(productos, key=lambda producto: producto["nombre"])

# Mostrar resultados
print("Productos ordenados por precio:")
for p in productos_ordenados_precio:
    print(f"{p['nombre']} - ${p['precio']}")

print("\nProductos ordenados por nombre:")
for p in productos_ordenados_nombre:
    print(f"{p['nombre']} - ${p['precio']}")

###
# EXPLICACIÓN DETALLADA:
# ¿Qué es una función lambda?
# Es una función anónima (sin nombre) que se usa cuando necesitás una función
# rápida y simple, especialmente para ordenar, filtrar o mapear listas.
###
