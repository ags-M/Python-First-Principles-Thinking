# =====================================================================
# EJERCICIO #37  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí wallet válida (s/n), saldo (float), crédito (s/n),
# lista negra (s/n). 'crypto_ok' True si wallet y (saldo>0 o crédito)
# y no negra.
#
# QUE SE BUSCA ENTRENAR:
# Transacción cripto.
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
# wallet = input('¿Wallet válida? (s/n): ').lower() == 's'
# saldo = float(input('Saldo: '))
# credito = input('¿Crédito? (s/n): ').lower() == 's'
# negra = input('¿Lista negra? (s/n): ').lower() == 's'
# crypto_ok = wallet and ((saldo > 0) or credito) and (not negra)
# print(f'¿Crypto OK?: {crypto_ok}')
#
# =====================================================================
