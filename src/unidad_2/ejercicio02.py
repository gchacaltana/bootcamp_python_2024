"""
El área de inversión de una entidad bancaria desea analizar la información de tres categorías de clientes 
según el importe de sus cuentas de ahorros. Las categorías son:

* Categoría A: Son aquellos clientes que tienen ahorros de hasta S/. 10,000.00
* Categoría B: Son aquellos clientes que tienen ahorros de hasta S/. 30,000.00
* Categoría C: Son aquellos clientes que tienen ahorros mayores a S/. 30,000.00

Se necesita un programa que les permita saber:
1. Cuántos clientes tienen por cada categoría.
2. Total de dinero que disponen por cada categoría.
3. Promedio del dinero ahorrado por cada categoría.
4. Cuál es el monto más alto de dinero ahorrado
5. Cuál es el monto más bajo de dinero ahorrado.

Los montos de las cuentas de ahorro se deben ingresar por el usuario.
Se debe validar que el monto ingresado sea un número positivo.

Se debe ingresar montos hasta que el usuario decida terminar (ingresando la tecla Q), es decir, 
no se debe tener un número fijo de montos a ingresar.
"""
from statistics import median


def is_float(string: str):
    """
    Validar si un string es un número flotante
    """
    try:
        # Return true if float
        float(string)
        return True
    except ValueError:
        # Return False if Error
        return False


if __name__ == '__main__':
    lista_categoria_a = []
    lista_categoria_b = []
    lista_categoria_c = []

    # Declaración e inicialización de variable
    data_input: str = ""

    while data_input != "Q":
        data_input: str = str(input(
            "Ingrese el importe de ahorro [o ingresa Q para terminar]: ")).upper()

        if is_float(data_input):
            monto = float(data_input)
            if monto >= 0:
                if monto < 10000:
                    lista_categoria_a.append(monto)
                elif monto < 30000:
                    lista_categoria_b.append(monto)
                else:
                    lista_categoria_c.append(monto)

    print(
        f"Cantidad de elementos - Categoría A: {str(len(lista_categoria_a))}")
    print(
        f"Cantidad de elementos - Categoría B: {str(len(lista_categoria_b))}")
    print(
        f"Cantidad de elementos - Categoría C: {str(len(lista_categoria_c))}")

    print(f"Total ahorrado - Categoría A: {str(sum(lista_categoria_a))}")
    print(f"Total ahorrado - Categoría B: {str(sum(lista_categoria_b))}")
    print(f"Total ahorrado - Categoría C: {str(sum(lista_categoria_c))}")

    if len(lista_categoria_a) > 0:
        print(
            f"Promedio ahorrado - Categoría A: {str(median(lista_categoria_a))}")
        
    if len(lista_categoria_b) > 0:
        print(
            f"Promedio ahorrado - Categoría B: {str(median(lista_categoria_b))}")
        
    if len(lista_categoria_c) > 0:
        print(
            f"Promedio ahorrado - Categoría C: {str(median(lista_categoria_c))}")

    lista_general = lista_categoria_a + lista_categoria_b + lista_categoria_c
    valor_maximo: float = 0
    valor_minimo: float = 0
    if len(lista_general) > 0:
        valor_maximo = max(lista_general)
        valor_minimo = min(lista_general)

    print(f"Mayor valor ahorrado: {str(valor_maximo)}")
    print(f"Mínimo valor ahorrado: {str(valor_minimo)}")

    print("Categoría A")
    print(lista_categoria_a)

    print("Categoría B")
    print(lista_categoria_b)
    
    print("Categoría C")
    print(lista_categoria_c)
