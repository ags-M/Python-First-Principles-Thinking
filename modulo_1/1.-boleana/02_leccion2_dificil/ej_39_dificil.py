# =====================================================================
# EJERCICIO #39  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí inscripto (s/n), pago (s/n), beca (s/n), suspendido (s/n).
# 'examen_ok' True si inscripto y (pago o beca) y no suspendido.
#
# QUE SE BUSCA ENTRENAR:
# Examen internacional.
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
# inscripto = input('¿Inscripto? (s/n): ').lower() == 's'
# pago = input('¿Pago? (s/n): ').lower() == 's'
# beca = input('¿Beca? (s/n): ').lower() == 's'
# suspendido = input('¿Suspendido? (s/n): ').lower() == 's'
# examen_ok = inscripto and (pago or beca) and (not suspendido)
# print(f'¿Examen OK?: {examen_ok}')
#
# =====================================================================
