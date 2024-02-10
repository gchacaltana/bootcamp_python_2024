"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al género y 
el nombre del alumno. El grupo A está formado por las mujeres con un nombre anterior a la M y 
los hombres con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla 
el grupo que le corresponde.
"""

# Declaración y entrada de variables
genero: str = str(input("Ingrese su género (M/F): ")).upper() # Mayúscula
nombre: str = str(input("Ingrese su nombre: ")).lower() # Minúscula

# Proceso
# Condición para determinar el grupo
if (nombre[0] < 'm' and genero == 'F') or (nombre[0] > 'n' and genero == 'M'):
    print("Usted pertence al Grupo A")
else:
    print("Usted pertence al Grupo B")
