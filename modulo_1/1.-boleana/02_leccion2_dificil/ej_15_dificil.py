# =====================================================================
# EJERCICIO #15  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí admin (s/n), audit log (s/n), justificación (s/n),
# datos sensibles (s/n). 'exporta' True si admin y (audit o justificación)
# y no sensibles.
#
# QUE SE BUSCA ENTRENAR:
# Caso de seguridad de datos.
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
# admin = input('¿Admin? (s/n): ').lower() == 's'
# audit = input('¿Audit log? (s/n): ').lower() == 's'
# justificacion = input('¿Justificación? (s/n): ').lower() == 's'
# sensibles = input('¿Datos sensibles? (s/n): ').lower() == 's'
# exporta = admin and (audit or justificacion) and (not sensibles)
# print(f'¿Exporta?: {exporta}')
#
# =====================================================================
