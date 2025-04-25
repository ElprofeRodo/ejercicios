""""
Calcular el promedio de cinco calificaciones, utilizando una variable por
calificación y otra para el resultado del promedio.
Las calificaciones debe ingresarlas el usuario.
"""

# Por defecto las entradas se almacenan como cadenas
# se requiere una conversión de tipo de dato
nota1 = float(input("Ingresa primera nota: "))
nota2 = float(input("Ingresa segunda nota: "))
nota3 = float(input("Ingresa tercera nota: "))
nota4 = float(input("Ingresa cuarta nota: "))
nota5 = float(input("Ingresa quinta nota: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

# Opcionalmente, se puede redondear a un decimal
print(f"El promedio es {promedio:.1f}")