# =====================================================================
# EJERCICIO #35  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí si está cancelada (s/n) y si está pagada (s/n). Guardá en
# 'suscripcion_activa' True si NO está cancelada Y está pagada.
#
# QUE SE BUSCA ENTRENAR:
# Negación de input s/n con 'and'.
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
suscripcion_cancelada =input("esta cancelada la suscripcion (s/n): ").lower() == "s"
cuota_pagada = input("esta paga la cuota (s/n): ").lower() == "s"
suscripcion_activa = not suscripcion_cancelada and (cuota_pagada)
print(f"la suscripcion esta activa: {suscripcion_activa}")
print(f"la suscripcion no esta activa" * (not suscripcion_activa), end="")
# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# cancelada = input('¿Cancelada? (s/n): ').lower() == 's'
# pagada = input('¿Pagada? (s/n): ').lower() == 's'
# activa = (not cancelada) and pagada
# print(f'¿Activa?: {activa}')
#
# =====================================================================
