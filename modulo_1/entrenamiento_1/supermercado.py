# Creá un programa que calcule el precio final de un producto.
# Pedí:
#   - precio    (float)
#   - cantidad  (int)
#   - envío premium  (sí/no → bool)
# Mostrá un desglose claro con cada dato, su tipo y un mensaje
# final con el total a pagar.
#
# Pista: total = precio * cantidad. Sumá el envío si corresponde.

precioA = float(input("¿Precio del producto A?: "))
print(f"El precio del producto A es de $: {precioA}")

pedido = int(input("¿Qué cantidad de precioA solicita?: "))
subtotal = precioA * pedido
print(f"El valor del subtotal es de pesos {subtotal}")

respuesta = input("¿Solicita envío premium (s/n)?: ")
envio_premium = (respuesta == "s")              # bool: True/False
costo_envio = 100 if envio_premium else 0       # int: 100 o 0

total_a_pagar = subtotal + costo_envio

print(f"Envío premium: {envio_premium}  (tipo: {type(envio_premium).__name__})")
print(f"Costo de envío: ${costo_envio}")
print(f"El costo total es de pesos {total_a_pagar}")