"""
Solicitar el ingreso de tres calificaciones a través del teclado, calcular
el promedio de ellas y determinar si el estudiante aprueba o no una asignatura,
considerando que la nota de aprobación debe ser mayor o igual a 5.
Mostrar el resultado por pantalla.
"""

nota1 = float(input("Ingresa primera nota: "))
nota2 = float(input("Ingresa segunda nota: "))
nota3 = float(input("Ingresa tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 5:
    print(f"Tu promedio es {promedio:.1f}, has aprobado")
else:
    print(f"Tu promedio es {promedio:.1f}, has reprobado")