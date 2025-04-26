"""
Crear un programa que permita imprimir una boleta con el detalle de una compra.
El programa debe solicitar tres productos, sus precios y cantidades.
El programa debe aplicar un descuento del 10% si la compra es igual o superior
a $20.000, el detalle de la boleta se muestra por pantalla
"""

prod1 = input("Ingresa primer producto: ")
prec1 = int(input(f"Ingresa precio de {prod1}: "))
cant1 = int(input(f"Ingresa cantidad de {prod1}: "))

prod2 = input("Ingresa segundo producto: ")
prec2 = int(input(f"Ingresa precio de {prod2}: "))
cant2 = int(input(f"Ingresa cantidad de {prod2}: "))

prod3 = input("Ingresa tercer producto: ")
prec3 = int(input(f"Ingresa precio de {prod3}: "))
cant3 = int(input(f"Ingresa cantidad de {prod3}: "))

subtotal = prec1*cant1 + prec2*cant2 + prec3*cant3

if subtotal >= 20000:
    descuento = subtotal * 0.19
else:
    descuento = 0

print(f"{cant1} x {prod1} \t ${cant1*prec1:7,}")
print(f"{cant2} x {prod2} \t ${cant2*prec2:7,}")
print(f"{cant3} x {prod3} \t ${cant3*prec3:7,}")
print(f"Subtotal \t ${subtotal:7,}")
print(f"Descuento \t ${descuento:7,.0f}")
print(f"Total pagar \t ${subtotal-descuento:7,.0f}")