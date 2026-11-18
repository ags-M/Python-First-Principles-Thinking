# =====================================================================
# EJERCICIO #16  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí balances completos (s/n), sin errores (s/n), supervisado (s/n),
# pendiente (s/n). 'cierre_ok' True si balances y (sin_errores o
# supervisado) y no pendiente.
#
# QUE SE BUSCA ENTRENAR:
# Cierre contable con paréntesis.
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
# balances = input('¿Balances completos? (s/n): ').lower() == 's'
# sin_errores = input('¿Sin errores? (s/n): ').lower() == 's'
# supervisado = input('¿Supervisado? (s/n): ').lower() == 's'
# pendiente = input('¿Pendiente? (s/n): ').lower() == 's'
# cierre_ok = balances and (sin_errores or supervisado) and (not pendiente)
# print(f'¿Cierre OK?: {cierre_ok}')
#
# =====================================================================
