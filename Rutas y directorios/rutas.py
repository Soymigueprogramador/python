# Rutas
# Importando la clase Path desde pathlib
from pathlib import Path

# -----------------------------------
# La clase Path nos permite trabajar
# con rutas de archivos y carpetas
# de forma independiente del sistema operativo
# -----------------------------------

# Ruta absoluta en Windows
ruta_windows = Path(r"C:\ruta\para\windows")

# Ruta absoluta en Linux / macOS
ruta_linux = Path("/ruta/para/linux")

# Ruta absoluta al directorio HOME del usuario
ruta_home = Path.home()

# Ruta absoluta construida a partir del HOME
ruta_absoluta = ruta_home / "programa" / "mi_app"

# Ruta relativa (dentro del proyecto)
ruta_relativa = Path("one/__inicio__.py")

# Mostramos las rutas
print(ruta_windows)
print(ruta_linux)
print(ruta_home)
print(ruta_absoluta)
print(ruta_relativa)

# -----------------------------------
# Creando un objeto Path para un archivo
# (la ruta puede existir o no)
# -----------------------------------

path = Path("python") / "Rutas y directorios" / "hola-mundo.py"

# Métodos de este objeto
print("¿Es archivo?:", path.is_file())
print("¿Es directorio?:", path.is_dir())
print("¿Existe?:", path.exists())

# -----------------------------------
# Propiedades del objeto Path
# -----------------------------------

print(
    path.name,        # Nombre del archivo con su extensión
    path.stem,        # Nombre del archivo sin extensión
    path.suffix,      # Extensión del archivo
    path.parent,      # Directorio padre
    path.absolute(),  # Ruta absoluta completa
)

# Metodo para cambiarle el nombre al archivo con si extencion
p = path.with_name('Hola.js') # Cambia el nombre y la extencion del archivo
print(p)
a = path.with_suffix('.cpp') # Cambia la extencion del archivo
print(a)
a = path.with_stem('chau') # Cambia el nombre del archivo sin su extencion
print(a)
