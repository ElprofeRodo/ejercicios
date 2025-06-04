while True:
    print("1. Agregar producto")
    print("2. Mostrar carrito")
    print("3. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        while True:
            print("1. Manzana")
            print("2. Pera")
            print("3. Platano")
            print("4. Volver")
            opcion2 = input("Opción: ")

            if opcion2 == "1":
                while True:
                    try:
                        cantidad = int(input("Cantidad: "))
                    except:
                        print("La cantidad debe ser numerica")
            elif opcion2 == "2":
                print("una pera")
            elif opcion2 == "3":
                print("un platano")
            elif opcion2 == "4":
                break
            else:
                print("La opción es incorrecta")
    elif opcion == "2":
        print()
    elif opcion == "3":
        break
    else:
        print("La opción no es correcta")