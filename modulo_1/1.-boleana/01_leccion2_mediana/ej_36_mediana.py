# =====================================================================
# EJERCICIO #36  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí saldo (float) y límite (float). Guardá en 'puede_transferir'
# True si saldo > 0 y saldo >= límite.
#
# QUE SE BUSCA ENTRENAR:
# Comparación triple con dos variables.
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

saldo = float(input("ingrese su saldo actual: "))
limite = float(input("ingrese su limite bancario: "))
puede_transferir = (saldo > 0) and (saldo >= limite)
print(f"puede transferir: {puede_transferir}")
print(f"NO puede transferir" * (not puede_transferir), end="")
# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# saldo = float(input('Saldo: '))
# limite = float(input('Límite: '))
# puede_transferir = (saldo > 0) and (saldo >= limite)
# print(f'¿Podés transferir?: {puede_transferir}')
#
# =====================================================================
