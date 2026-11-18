# =====================================================================
# EJERCICIO #09  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí paciente estable (s/n), consentimiento (s/n), tutor (s/n),
# riesgo alto (s/n). 'cirugia_ok' True si estable y (consentimiento o
# tutor) y no riesgo.
#
# QUE SE BUSCA ENTRENAR:
# Caso médico con varios booleans.
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
# estable = input('¿Paciente estable? (s/n): ').lower() == 's'
# consentimiento = input('¿Consentimiento? (s/n): ').lower() == 's'
# tutor = input('¿Tutor? (s/n): ').lower() == 's'
# riesgo = input('¿Riesgo alto? (s/n): ').lower() == 's'
# cirugia_ok = estable and (consentimiento or tutor) and (not riesgo)
# print(f'¿Cirugía OK?: {cirugia_ok}')
#
# =====================================================================
