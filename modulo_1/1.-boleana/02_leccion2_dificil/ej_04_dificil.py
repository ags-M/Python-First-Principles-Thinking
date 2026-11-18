# =====================================================================
# EJERCICIO #04  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí firewall (s/n), VPN (s/n), red local confiable (s/n),
# IP sospechosa (s/n). 'red_segura' True si firewall y (VPN o red_local)
# y no IP sospechosa.
#
# QUE SE BUSCA ENTRENAR:
# Cuatro booleans combinados con jerarquía.
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

firewall = input("Tienes firewall (s/n): ").lower() == "s"
VPN = input("Tienes una VPN (s/n): ").lower() == "s"
red = input("Tienes red local confiable (s/n): ").lower() == "s"
IP_sospechosa = input("Tienes una IP sospechosa (s/n): ").lower() == "s"
red_segura = firewall and (VPN or red) and (not IP_sospechosa)
print(f"Tiene una red segura: {red_segura}")
print(f"No tiene una red segura" * (not red_segura), end="")


# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# firewall = input('¿Firewall ON? (s/n): ').lower() == 's'
# vpn = input('¿VPN? (s/n): ').lower() == 's'
# local = input('¿Red local confiable? (s/n): ').lower() == 's'
# sospechosa = input('¿IP sospechosa? (s/n): ').lower() == 's'
# red_segura = firewall and (vpn or local) and (not sospechosa)
# print(f'¿Red segura?: {red_segura}')
#
# =====================================================================
