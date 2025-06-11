# 1. Sumar 15 números ingresados
def sumar_quince_numeros():
    suma= 0
    contador= 1
    while contador<= 15:
        numero= input("Ingrese un número: ")
        suma= suma+ int(numero)
        contador+= 1
    return suma

print("La suma de 15 números:", sumar_quince_numeros())

# 2. Verificar mayoría de edad
def verificar_mayoria_edad():
    edad= input("Ingrese su edad: ")
    edad= int(edad)
    if edad>= 18:
        return "Es mayor de edad."
    else:
        return "Es menor de edad."

print("Verificación de edad:", verificar_mayoria_edad())
