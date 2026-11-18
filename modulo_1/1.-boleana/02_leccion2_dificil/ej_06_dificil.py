# =====================================================================
# EJERCICIO #06  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí edad, ingresos, aval (s/n), codeudor (s/n), mora (s/n).
# 'hipotecario' True si 25<=edad<=55 y ingresos>2000 y (aval o codeudor)
# y no mora.
#
# QUE SE BUSCA ENTRENAR:
# Cinco condiciones combinadas.
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
# edad = int(input('Edad: '))
# ingresos = float(input('Ingresos: '))
# aval = input('¿Aval? (s/n): ').lower() == 's'
# codeudor = input('¿Codeudor? (s/n): ').lower() == 's'
# mora = input('¿En mora? (s/n): ').lower() == 's'
# hipotecario = (25 <= edad <= 55) and (ingresos > 2000) and (aval or codeudor) and (not mora)
# print(f'¿Hipotecario?: {hipotecario}')
#
# =====================================================================
