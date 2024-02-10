"""
Escribir un programa que pregunte al usuario una cantidad a invertir y el número de años, y 
muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión. 
La tasa de interés dependerá del importe de la inversión. 

Si el importe es menor a S/. 5,000, su tasa será de 5%; 
Si el importe es menor a S/. 10,000, su tasa será de 7.5%;
Si el importe es mayor a S/. 10,000, su tasa será del 8.5%

"""

# Declaración de variables
cantidad_invertir: float = float(input("Ingrese la cantidad a invertir: "))
anios: int = int(input("Ingrese el número de años: "))
tasa_interes: float = 0.0

# Proceso

# Condición para determinar la tasa de interés
if cantidad_invertir < 5000:
    tasa_interes: float = 5
elif cantidad_invertir < 10000:
    tasa_interes: float = 7.5
else:
    tasa_interes: float = 8.5

# Calculamos el capital obtenido en la inversión cada año
for i in range(anios):
    cantidad_invertir += cantidad_invertir * tasa_interes / 100
    print(f"Capital obtenido en el año {i+1}: {cantidad_invertir:.2f}")
