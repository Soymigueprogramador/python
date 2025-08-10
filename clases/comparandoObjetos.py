# Comparando objetos.


class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # Metodo para saber si es igual.
    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon

    # Metodo para saber si no es igual.
    def __ne__(self, otro):
        return self.lat != otro.lat or self.lon != otro.lon

    # Metodo para saber si uno es mayor que el otro.
    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon

    # Metodo para saber si es menor o igual.
    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon


cors = Coordenadas(45, 27)
cors2 = Coordenadas(45, 27)

print( cors == cors2 ) # Pregunta si es el mismo objeto, pero se guarda en un espacio diferente en la memoria.
print( cors, cors2 ) # Muestra los distintos lugares de memoria donde esta guardado.
print( cors == cors2 )
print( cors != cors2 )
print( cors < cors2 )
print( cors > cors2 )
print( cors <= cors2 )
print( cors >= cors2 )
