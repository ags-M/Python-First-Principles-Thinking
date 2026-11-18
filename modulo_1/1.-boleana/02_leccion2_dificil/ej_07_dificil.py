# =====================================================================
# EJERCICIO #07  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí dosis (int), contraindicación (s/n), edad, autorización (s/n).
# 'vacunacion_ok' True si dosis>=2 y no contraindicación y
# (edad>=12 o autorizacion).
#
# QUE SE BUSCA ENTRENAR:
# Combina números con varios booleans.
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
# dosis = int(input('Dosis: '))
# contraindicacion = input('¿Contraindicación? (s/n): ').lower() == 's'
# edad = int(input('Edad: '))
# autorizacion = input('¿Autorización? (s/n): ').lower() == 's'
# vacunacion_ok = (dosis >= 2) and (not contraindicacion) and ((edad >= 12) or autorizacion)
# print(f'¿Vacunación OK?: {vacunacion_ok}')
#
# =====================================================================
