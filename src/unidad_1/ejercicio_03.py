"""
Implementar una función que reciba como parámetro una cantidad de segundos y 
que devuelva la cantidad de horas, minutos y segundos equivalente.

1 hora = 3600 segundos
1 minuto = 60 segundos

Usuario ingresa: 3800 segundos
Resultado: 2 horas, 12 minutos y 40 segundos
"""

# Declaración de variables
segundos: int = int(input("Ingrese la cantidad de segundos: "))

# Proceso

# Obtenemos el valor numérico entero de una división.
horas: int = segundos // 3600

# Obtenemos la cantidad de minutos
minutos: int = (segundos % 3600) // 60

# Obtenemos la cantidad de segundos
segundos: int = (segundos % 3600) % 60

print(f"{horas} horas, {minutos} minutos y {segundos} segundos")
