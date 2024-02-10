"""
Escribir un programa que pregunte al usuario por una fruta, el número de kilos a comprar y muestre 
por pantalla el total a pagar. Aplicar la programación orientada a objetos para instanciar las 
frutas y sus características (nombre y precio). Si la fruta ingresada por el usuario no forma parte
del catálogo de frutas debe mostrar un mensaje informando de ello.

Tabla:
Manzana -> S/. 4.85
Pera -> S/. 8.95
Sandía -> S/. 1.89
Naranja -> S/. 4.75
"""

from typing import List


class Fruta:
    """
    Clase Fruta
    """

    def __init__(self, nombre: str, precio: float):
        """
        Constructor de la clase Fruta
        """
        self.nombre: str = nombre
        self.precio: str = precio

    def __str__(self):
        """
        Método mágico __str__
        """
        return self.nombre


class CatalogoFruta:
    """
    Clase Catalogo Fruta
    """

    def __init__(self):
        """
        Constructor de la clase CatalogoFruta
        """
        self.catalogo: List = []

    def agregar_item(self, fruta: Fruta):
        """
        Agrega una fruta al catálogo
        """
        self.catalogo.append(fruta)

    def imprimir_catalogo(self):
        """
        Imprime el catálogo de frutas
        """
        print("Catálogo de frutas")
        for fruta in self.catalogo:
            print(fruta)

    def buscar_fruta(self, nombre) -> Fruta | None:
        """
        Busca una fruta en el catálogo.
        Retorna:
            Objeto Fruta si la fruta se encuentra en el catálogo, 
            None en caso contrario
        """

        for fruta in self.catalogo:
            if fruta.nombre == nombre:
                return fruta
        return None


def crear_catalogo_frutas():
    """
    Crea un catálogo de frutas
    """
    catalogo = CatalogoFruta()
    catalogo.agregar_item(Fruta("Manzana", 4.85))
    catalogo.agregar_item(Fruta("Pera", 8.95))
    catalogo.agregar_item(Fruta("Sandía", 1.89))
    catalogo.agregar_item(Fruta("Naranja", 4.75))
    return catalogo


if __name__ == "__main__":
    catalogo_frutas = crear_catalogo_frutas()
    catalogo_frutas.imprimir_catalogo()

    input_fruta: str = str(
        input("Ingrese el nombre de la fruta que desea comprar: "))

    input_cantidad: float = float(
        input("Ingrese la cantidad de frutas (Kg) que desea comprar: "))

    fruta = catalogo_frutas.buscar_fruta(input_fruta)
    if fruta is None:
        print(f"La fruta {input_fruta} no se encuentra en el catálogo")
    else:
        total = round(fruta.precio * input_cantidad, 2)
        print(f"Fruta: {fruta.nombre}")
        print(f"Precio: {fruta.precio}")
        print(f"Total: {total}")
