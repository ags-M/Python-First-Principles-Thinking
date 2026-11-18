# =====================================================================
# EJERCICIO #31  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí presupuesto OK (s/n), plazo factible (s/n), agile (s/n),
# conflictos (s/n). 'proyecto_ok' True si presupuesto y (plazo o agile)
# y no conflictos.
#
# QUE SE BUSCA ENTRENAR:
# Aprobación de proyecto.
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
# presupuesto = input('¿Presupuesto OK? (s/n): ').lower() == 's'
# plazo = input('¿Plazo factible? (s/n): ').lower() == 's'
# agile = input('¿Agile? (s/n): ').lower() == 's'
# conflictos = input('¿Conflictos? (s/n): ').lower() == 's'
# proyecto_ok = presupuesto and (plazo or agile) and (not conflictos)
# print(f'¿Proyecto OK?: {proyecto_ok}')
#
# =====================================================================
