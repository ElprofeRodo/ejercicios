def sumar_quince_numeros():
    suma = 0
    contador = 1
    while contador <= 15:
        numero = input("Ingrese un número: ")
        suma = suma + int(numero)
        contador = contador + 1
    print("La suma de los 15 números es:", suma)
sumar_quince_numeros()
