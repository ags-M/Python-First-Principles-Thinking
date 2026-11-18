# =====================================================================
# EJERCICIO #35  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí sospechoso (s/n), mandato judicial (s/n), auditor (s/n),
# apelación (s/n). 'congela' True si sospechoso y (mandato o auditor)
# y no apelacion.
#
# QUE SE BUSCA ENTRENAR:
# Congelamiento de cuenta.
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
# sospechoso = input('¿Sospechoso? (s/n): ').lower() == 's'
# mandato = input('¿Mandato judicial? (s/n): ').lower() == 's'
# auditor = input('¿Auditor? (s/n): ').lower() == 's'
# apelacion = input('¿Apelación? (s/n): ').lower() == 's'
# congela = sospechoso and (mandato or auditor) and (not apelacion)
# print(f'¿Congela?: {congela}')
#
# =====================================================================
