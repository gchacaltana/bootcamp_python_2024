"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el total a pagar. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Tabla:
Manzana -> S/. 4.85
Pera -> S/. 8.95
Sandía -> S/. 1.89
Naranja -> S/. 4.75
"""

if __name__ == "__main__":
    frutas = {
        "manzana": 4.85,
        "pera": 8.95,
        "sandia": 1.89,
        "naranja": 4.75
    }

    input_fruta: str = str(input("Ingrese la fruta: "))
    input_cantidad: float = float(input("Ingrese la cantidad (KG): "))

    if input_fruta not in frutas:
        print("Fruta no disponible")
    else:
        precio = frutas[input_fruta.lower()]
        print(f"El precio total es: {round(precio * input_cantidad, 2)}")
