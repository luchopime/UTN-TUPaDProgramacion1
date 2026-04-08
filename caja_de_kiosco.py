# 1 Nombre del cliente (solo letras sin vacio)
while True:
    cliente = input("Ingrese el nombre del cliente: ").strip()
    if cliente != "" and cliente.isalpha():
        break
    else:
        print("Error: Ingrese solo letras y no deje el campo vacío.")

# 2 Cantidad de productos (numeros enteros y positivo)
while True:
    cantidad = input("Ingrese la cantidad de productos: ").strip()
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
        break
    else:
        print("Error: Ingrese un numero mayor a 0.")

total_sin_descuento = 0
total_con_descuento = 0

# 3 Ingreso de productos
for i in range(1, cantidad + 1):
    # Precio del producto
    while True:
        precio = input(f"Producto {i} - Ingrese el precio: ").strip()
        if precio.isdigit():
            precio = int(precio)
            break
        else:
            print("Error: Ingrese un número válido.")
    
    total_sin_descuento += precio
    # Descuento S/N
    while True:
        descuento = input("¿Tiene descuento? (S/N): ").strip().lower()
        if descuento == "s" or descuento == "n":
            break
        else:
            print("Error: Ingrese solo S o N.")
    
    # Aplicar descuento si corresponde
    if descuento == "s":
        precio_desc = precio * 0.9
    else:
        precio_desc = precio

    total_con_descuento += precio_desc

# 4 Resultados finales
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print("\n--- RESULTADOS ---")
print(f"Cliente: {cliente}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")