"""
Calcular índice de masa corporal (IMC) según la fórmula:
peso en kilogramos dividido por estatura en metros elevada a dos.
El peso y la estatura deben ser ingresados por el usuario.
Mostrar por pantalla el resultado.
"""

# Peso se convierte a un dato entero
peso = int(input("Ingresa tu peso: "))

# Estatura se converte a un tipo de dato real (con decimales)
estatura = float(input("Ingresa tu estatura: "))

# Estatura elevada a 2
imc = peso / (estatura**2)

# Opcionalmente, se puede redondear a 2 decimales
print(f"Tu IMC es {imc:.2f}")