"""
Calcular la edad de un usuario. El usuario debe ingresar su nombre y año de
nacimiento. Por pantalla se debe mostrar: 
Hola [USUARIO], tienes [EDAD] años.
"""

# Nombre es una cadena, no requiere una conversión de tipo de dato
nombre = input("Ingresa tu nombre: ")

# Año de nacimiento es un número, se debe convertir a entero
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))

edad = 2025 - anio_nacimiento

print(f"Hola {nombre}, tienes {edad} años.")