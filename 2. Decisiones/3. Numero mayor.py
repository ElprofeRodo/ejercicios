"""
Ingresar dos numeros por el teclado y determinar cual es el mayor de ellos.
Mostrar el resultado por pantalla.
"""

numero1 = int(input("Ingresa primer numero: "))
numero2 = int(input("Ingresa segundo numero: "))

if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
else:
    if numero2 > numero1:
        print(f"{numero2} es mayor que {numero1}")
    else:
        print(f"{numero1} es igual a {numero2}")