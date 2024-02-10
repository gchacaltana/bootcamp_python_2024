"""
Dado un arreglo de números (por ejemplo [1, 2, 6, 19, 12, 3, 1]),  

crear la función wave_sort que ordene los elementos del arreglo "como serrucho". 

Esto es, el arreglo retornado debe cumplir con el siguiente criterio

arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= ...

Una posible solución, para el caso del ejemplo es:

wave_sort([1, 2, 6, 19, 12, 3, 1])
=> [19, 1, 12, 1, 6, 2, 3]

"""
# importamos la libreria typing
from typing import List


def wave_sort(lista_entrada: List):
    """
    Función que ordena los elementos del arreglo "como serrucho"
    """
    wave_list: List = []

    # 1. Ordenar la lista de entrada de mayor a menor (manera descendente)
    # lista input: 19,12,6,3,2,1,1
    # 19,6,12,
    lista_entrada.sort(reverse=True)

    # Obtener cantidad de elementos
    total_elementos = len(lista_entrada)

    # aagregar primer elemento
    wave_list.append(lista_entrada[0])

    # Recorrer lista devuelve por la función range
    # Range: Devuelve una secuencia de números, comienza desde 1 hasta total_elementos
    for index in range(1, total_elementos):
        if index % 2 == 0:
            # Si el indice es par
            # Agregamos el elemento anterior
            wave_list.append(lista_entrada[index-1])
        else:
            # Si el indice es impar
            # Agregamos el elemento siguiente o actual
            if index+1 < total_elementos:
                wave_list.append(lista_entrada[index+1])
            else:
                wave_list.append(lista_entrada[index])
    return wave_list


# Ejecución
# El bloque __main__ es el punto de entrada del programa
if __name__ == "__main__":
    lista = [1, 2, 6, 19, 12, 3, 1]
    print("Lista Entrada")
    print(lista)
    print("Resultado")
    print(wave_sort(lista))
