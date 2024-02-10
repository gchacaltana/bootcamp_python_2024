"""
Programa para calcular el interes moratorio.

Retos:
1. Sintaxis básica
2. Entendimiento de las estructura de datos
3. Entendimiento de las Funciones nativas (cómo y cuando utilizarlas)
4. Conocer POO
5. Pensamiento Algoritmico (Interpretación del enunciado)

--

Escribir un programa que calcule el importe del interés moratorio de una cuota de deuda vencida. 
El usuario debe poder ingresar (ingreso de datos):
 - El importe de la deuda (cuota vencida), -> float
 - La tasa de interés mensual (valor porcentual) -> float
 - Y la cantidad de días transcurridos. -> int

Después debe mostrar por pantalla el monto total que debe pagar, detallando el importe de mora.

Fórmula para calcular el importe del interés moratorio mensual.

X = cuota deuda vencida * tasa de interés * (días vencido / 360)

"""

# comentario de una linea

# Declaración de variables

# conversión de variables
cuota_vencida: float = float(
    input("Ingrese el importe de la deuda (cuota vencida): "))
tasa_interes: float = float(
    input("Ingrese la tasa de interés mensual (Ejem: 15): "))
dias_transcurridos: int = int(
    input("Ingrese la cantidad de días transcurridos: "))

# Proceso
importe_mora: float = cuota_vencida * \
    tasa_interes/100 * (dias_transcurridos / 360)

# Salida
total_pagar: float = cuota_vencida + importe_mora
print(
    f"El monto total a pagar es: {total_pagar:.2f} \nImporte de mora: {importe_mora:.2f}")
