# =====================================================================
# EJERCICIO #22  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí materias OK (s/n), tesis (s/n), equivalente (s/n),
# deudas (s/n). 'diploma_ok' True si materias y (tesis o equivalente)
# y no deudas.
#
# QUE SE BUSCA ENTRENAR:
# Caso académico.
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
# materias = input('¿Todas las materias? (s/n): ').lower() == 's'
# tesis = input('¿Tesis? (s/n): ').lower() == 's'
# equivalente = input('¿Equivalente? (s/n): ').lower() == 's'
# deudas = input('¿Deudas? (s/n): ').lower() == 's'
# diploma_ok = materias and (tesis or equivalente) and (not deudas)
# print(f'¿Diploma?: {diploma_ok}')
#
# =====================================================================
