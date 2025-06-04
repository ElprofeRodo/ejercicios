numeros_pares = 0
multiplos_cinco = 0
multiplos_5_pares = 0
otros_valores = 0
valores_invalidos = 0
negativos_ceros = 0
total = 0

while True:
    print("A: Ingresar un número y clasificarlo")
    print("B: Mostrar cuántos valores pares (pero no múltiplos de 5) han sido ingresados")
    print("C: Mostrar cuántos valores múltiplos de 5 impares han sido ingresados")
    print("D: Mostrar cuántos valores inválidos se intentaron ingresar")
    print("S: Salir del programa")
    opcion = input("Ingresa opción: ")
    if opcion == "A":
        try:
            numero = int(input("Ingresa numero: "))
            total += 1
            if numero > 0:
                # Si numero es par Y no es multiplo de 5
                if numero % 2 == 0 and numero % 5 != 0:
                    numeros_pares += 1
                # Si numero es multiplo de 5 Y es impar
                elif numero % 5 == 0 and numero % 2 != 0:
                    multiplos_cinco += 1
                # Si numero es multiplo de 5 Y es par
                elif numero % 5 == 0 and numero % 2 == 0:
                    multiplos_5_pares += 1
                else:
                    otros_valores += 1
            else:
                negativos_ceros += 1
        except:
            valores_invalidos += 1
            print("El valor no es válido")
    elif opcion == "B":
        print(f"Cantidad de pares y no multiplos de 5: {numeros_pares}")
    elif opcion == "C":
        print(f"Cantidad de multiplos de 5 impares: {multiplos_cinco}")
    elif opcion == "D":
        print(f"Cantidad de valores invalidos: {valores_invalidos}")
    elif opcion == "S":
        print(f"Total valores ingresados: {total}")
        print(f"Total pares {numeros_pares + multiplos_5_pares}")
        print(f"Porcentaje pares {(total / (numeros_pares + multiplos_5_pares)) * 100}")
        break
    else:
        print(f"La opción {opcion} es incorrecta!")