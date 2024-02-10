"""
Ejercicio 01: 
Escribir un programa que imprima en pantalla la suma de los números pares del 1 al 20.
"""


def suma_elementos_con_while():
    """
    Alternativa 1:
    Sumar los elementos de una lista con un ciclo while
    """
    contador = 1
    suma = 0
    while contador <= 20:
        if contador % 2 == 0:
            suma += contador
        contador += 1
    return suma


def suma_elementos_con_for():
    """
    Alternativa 2:
    Sumar los elementos de una lista con un ciclo for
    """
    suma = 0
    for contador in range(1, 21):
        if contador % 2 == 0:
            suma += contador
    return suma


def suma_elementos_con_lista_compresiva():
    """
    Alternativa 3:
    Sumar los elementos de una lista con una lista compresiva
    """
    return sum([i for i in range(1, 21) if i % 2 == 0])


if __name__ == '__main__':
    print("Suma con WHILE")
    print(suma_elementos_con_while())

    print("Suma con FOR")
    print(suma_elementos_con_for())

    print("Suma con Lista Compresiva")
    print(suma_elementos_con_lista_compresiva())
