# =====================================================================
# EJERCICIO #13  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí tiene tarjeta (s/n), saldo (float), crédito (s/n),
# lista negra (s/n). 'reserva_ok' True si tarjeta y (saldo>0 o crédito)
# y no lista negra.
#
# QUE SE BUSCA ENTRENAR:
# Caso de hotel con saldo float.
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


# ---------------- TU SOLUCIÓN ACÁ ----------------






# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# tarjeta = input('¿Tarjeta? (s/n): ').lower() == 's'
# saldo = float(input('Saldo: '))
# credito = input('¿Crédito? (s/n): ').lower() == 's'
# negra = input('¿Lista negra? (s/n): ').lower() == 's'
# reserva_ok = tarjeta and ((saldo > 0) or credito) and (not negra)
# print(f'¿Reserva OK?: {reserva_ok}')
#
# =====================================================================
