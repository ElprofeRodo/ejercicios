"""
Pedir el ingreso de un username y verificar que la cantidad de caracteres
sea mayor o igual a diez. Mostrar el resultado por pantalla.
"""

username = input("Ingresa tu usuario: ")

if len(username) >= 10:
    print("El usuario está OK")
else:
    print("El usuario no cumple el requisito")