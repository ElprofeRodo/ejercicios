"""
Solicitar la cantidad de números que el usuario 
desea introducir, luego solicitar esos números 
y devolver por pantalla el menor y el mayor de ellos
"""

cantidad = int(input("Ingresa cantidad: "))
contador = 0

while contador < cantidad:
    contador += 1
    numero = int(input("Ingresa numero: "))
    if contador == 1:
        num_mayor = numero
        num_menor = numero
    else:
        if numero > num_mayor:
            num_mayor = numero
        if numero < num_menor:
            num_menor = numero

print(f"El menor es {num_menor}")
print(f"El mayor es {num_mayor}")