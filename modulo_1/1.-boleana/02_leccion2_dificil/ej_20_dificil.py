# =====================================================================
# EJERCICIO #20  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí cuenta destino OK (s/n), swift (s/n), IBAN (s/n),
# país riesgo (s/n). 'transf_ok' True si cuenta y (swift o IBAN) y
# no riesgo.
#
# QUE SE BUSCA ENTRENAR:
# Caso bancario internacional.
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
# cuenta = input('¿Cuenta OK? (s/n): ').lower() == 's'
# swift = input('¿SWIFT? (s/n): ').lower() == 's'
# iban = input('¿IBAN? (s/n): ').lower() == 's'
# riesgo = input('¿País riesgo? (s/n): ').lower() == 's'
# transf_ok = cuenta and (swift or iban) and (not riesgo)
# print(f'¿Transferencia OK?: {transf_ok}')
#
# =====================================================================
