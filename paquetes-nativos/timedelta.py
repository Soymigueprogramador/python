# Timedelta

# Trabajando con las diferencias entre las fechas
from datetime import datetime, timedelta

fecha = datetime(1992, 7, 3) + timedelta(weeks=1)
fecha1 = datetime(2026, 1, 15)

# Restando las fechas
delta = fecha1 - fecha
print(delta)

# Propiedades del objeto delta
print(
    "Días:", delta.days,
    "Segundos:", delta.seconds,
    "Microsegundos:", delta.microseconds,
    "Total_seconds:", delta.total_seconds()
)

# timedelta
###
# timedelta nos permite sumarle o restarle tiempo a una fecha
# ###