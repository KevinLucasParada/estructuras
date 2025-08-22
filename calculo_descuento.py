def calcular_descuento(cant_productos, compras_previas, monto_total, promo_especial):
    descuento = 0

    # Condiciones
    if cant_productos > 10:
        descuento += 10

    if compras_previas > 5:
        descuento += 5

    if monto_total > 500:
        descuento += 7

    if promo_especial.lower() == "sí" or promo_especial.lower() == "si":
        descuento += 15

    # Límite máximo de descuento
    if descuento > 30:
        descuento = 30

    return descuento


# Solicitar datos al usuario
print("Bienvenido al sistema de cálculo de descuentos")

cant_productos = int(input("Ingrese la cantidad de productos comprados: "))
compras_previas = int(input("Ingrese la cantidad de compras previas del cliente: "))
monto_total = float(input("Ingrese el monto total de la compra ($): "))
promo_especial = input("¿Es un día de promoción especial? (sí/no): ")

# Calcular descuento
descuento_final = calcular_descuento(cant_productos, compras_previas, monto_total, promo_especial)

# Mostrar resultado
print(f"El descuento aplicado es del {descuento_final}%.")
