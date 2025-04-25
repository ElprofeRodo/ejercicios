"""
Convertir temperatura de grados Fahrenheit a grados Celsius, considerando
la siguiente fórmula: temperatura en grados Fahrenheit menos treinta y dos,
luego dividir el resultado anterior por uno punto ocho.
La temperatura en grados Fahrenheit debe ser ingresada por el usuario y
el resultado debe ser mostrado por pantalla:
[TEMP_FAH]°F equivale a [TEMP_CEL]°C
"""

# La temperatura podria contener decimales, por es se convierte a FLOAT
temp_f = float(input("Ingresa temperatura en Fahrenheit: "))
temp_c = (temp_f - 32) / 1.8

# Opcionalmente, se puede redondear con 1 decimal
print(f"{temp_f}°F equivale a {temp_c:.1f}°C")