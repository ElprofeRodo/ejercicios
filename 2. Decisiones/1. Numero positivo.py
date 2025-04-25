"""
Solicitar un número por el teclado y verificar si es positivo (mayor que cero)
Mostrar el resultado de la comprobación por pantalla.
"""

numero = int(input("Ingresa un numero: "))

if numero > 0:
    print("El numero es positivo")
else:
    if numero < 0:
        print("El numero es negativo")
    else:
        print("El numero es cero")