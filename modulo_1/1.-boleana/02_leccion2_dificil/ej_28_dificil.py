# =====================================================================
# EJERCICIO #28  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí credencial (s/n), capacitación (s/n), acompañado (s/n),
# sancionado (s/n). 'entra_lab' True si credencial y (capacitacion o
# acompanado) y no sancionado.
#
# QUE SE BUSCA ENTRENAR:
# Acceso a laboratorio.
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
# credencial = input('¿Credencial? (s/n): ').lower() == 's'
# capacitacion = input('¿Capacitación? (s/n): ').lower() == 's'
# acompanado = input('¿Acompañado? (s/n): ').lower() == 's'
# sancionado = input('¿Sancionado? (s/n): ').lower() == 's'
# entra_lab = credencial and (capacitacion or acompanado) and (not sancionado)
# print(f'¿Entra?: {entra_lab}')
#
# =====================================================================
