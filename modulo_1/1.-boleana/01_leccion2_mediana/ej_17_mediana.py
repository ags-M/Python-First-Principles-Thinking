# =====================================================================
# EJERCICIO #17  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí monto de compra y si es cliente VIP (s/n). Guardá en
# 'tiene_descuento' True si monto > 1000 o es VIP.
#
# QUE SE BUSCA ENTRENAR:
# Practicar 'or' entre número y booleano.
#
# REGLAS (solo lecciones 2 y 3):
#   - Podés usar: input(), print(), int(), float(), str(), bool()
#   - Operadores aritméticos: +  -  *  /  //  %  **
#   - Operadores de comparación: ==  !=  <  >  <=  >=
#   - Operadores lógicos: and  or  not
#   - f-strings
#   - len() para medir strings
#   - NO uses if/elif/else, ni for, ni while, ni listas, ni funciones
#
# =====================================================================

total_compra = int(input("ingresa el monto total de tu compra: "))
cliente_vip = input("sos cliente vip (s/n): ").lower() == "s"
descuento = total_compra >= 1000 or cliente_vip
print(f"tiene descuento: {descuento}")
print(f"No tiene descuento" * (not descuento), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# monto = float(input('Monto de compra: '))
# es_vip = input('¿Sos VIP? (s/n): ').lower() == 's'
# tiene_descuento = (monto > 1000) or es_vip
# print(f'¿Tenés descuento?: {tiene_descuento}')
#
# =====================================================================
