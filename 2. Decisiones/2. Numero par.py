"""
Solicitar un número por el teclado y comprobar si es par o no.
Mostrar el resultado de la verificación por pantalla.
"""

numero = int(input("Ingresa un numero: "))

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero no es par")