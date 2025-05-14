"""
Solicitar un número desde el teclado y validar 
que sea positivo. En caso de no serlo, 
volver a pedir el número hasta que supere la validación.
"""

numero = int(input("Ingresa un numero: "))

while numero < 0:
    print("Debe ser positivo!")
    numero = int(input("Ingresa un numero: "))