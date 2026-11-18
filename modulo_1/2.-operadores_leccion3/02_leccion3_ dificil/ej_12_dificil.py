# =====================================================================
# EJERCICIO #12  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Operadores (Leccion 3)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí horas trabajadas y pago por hora. Si trabajó más de 40 horas,
# las horas extra valen 1.5x. Calculá el salario total.
# Truco: extra = max(0, horas - 40); total = 40*pago + extra*pago*1.5
# (no podés usar max, usá: extra = (horas > 40) * (horas - 40)).
#
# QUE SE BUSCA ENTRENAR:
# Salario con horas extras, truco booleano.
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
# horas = float(input('Horas trabajadas: '))
# pago = float(input('Pago por hora: '))
# extra = (horas > 40) * (horas - 40)
# normales = horas - extra
# total = normales * pago + extra * pago * 1.5
# print(f'Salario: {total}')
#
# =====================================================================
