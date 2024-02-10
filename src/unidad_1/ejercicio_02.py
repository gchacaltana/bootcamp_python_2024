"""
Escribir un programa que pregunte al usuario la capacidad de su disco duro en Gigabytes 
para calcular la cantidad de bloques de almacenamiento que tiene el disco duro, 
si sabemos que un bloque de almacenamiento tiene un tamaño de 512 bytes. 
Considerar que: 
1 Kilobyte es equivalente a 1024 bytes; 
1 Megabyte es equivalente a 1024 Kilobytes; y un 
1 Gigabyte es equivalente a 1024 Megabytes.
"""

# Declaración de variables
capacidad_disco: float = float(
    input("Ingrese la capacidad de su disco duro en Gigabytes: "))

# Proceso

# Convertimos la capacidad de disco a bytes
# Alternativa 1
# capacidad_disco_bytes: float = capacidad_disco * 1024 * 1024 * 1024

# Alternativa 2
capacidad_disco_bytes: float = capacidad_disco * 1024 ** 3

# Calculamos la cantidad de bloques de almacenamiento
bloques_almacenamiento: float = capacidad_disco_bytes / 512

# Salida
print(f"La cantidad de bloques de almacenamiento que tiene el disco duro es: {bloques_almacenamiento:.2f}")
