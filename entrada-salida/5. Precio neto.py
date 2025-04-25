"""
Calcular el precio neto de un producto. El nombre del producto y su precio
con IVA (19%) deben ser ingresados por el usuario. El resultado debe ser
mostrado por pantalla: El precio neto de [PRODUCTO] es $[PRECIO_NETO]
"""

# El producto es una cadena, no necesita una conversión de tipo
producto = input("Ingresa producto: ")

# El precio es numero entero, se realiza la conversión de tipo
precio = int(input("Ingresa precio: "))

precio_neto = precio - (precio*0.19) # (precio*19/100)

# Opcionalmente, se puede recondear con 0 decimales
print(f"El precio neto de {producto} es ${precio_neto:.0f}")