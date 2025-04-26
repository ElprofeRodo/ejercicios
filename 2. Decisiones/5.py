"""
Pedir el ingreso de un teléfono y verificar que la cantidad de números
sea igual que nueve. Mostrar el resultado por pantalla.
"""

telefono = input("Ingresa un teléfono: ")

if len(telefono) == 9:
    print("El teléfono está OK")
else:
    print("El teléfono debe tener 9 digitos")