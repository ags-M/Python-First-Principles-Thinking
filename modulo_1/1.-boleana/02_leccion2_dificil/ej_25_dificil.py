# =====================================================================
# EJERCICIO #25  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí terreno propio (s/n), planos aprobados (s/n), excepción (s/n),
# zona protegida (s/n). 'permiso_ok' True si terreno y (planos o
# excepcion) y no protegida.
#
# QUE SE BUSCA ENTRENAR:
# Permiso de obra.
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
# terreno = input('¿Terreno propio? (s/n): ').lower() == 's'
# planos = input('¿Planos aprobados? (s/n): ').lower() == 's'
# excepcion = input('¿Excepción? (s/n): ').lower() == 's'
# protegida = input('¿Zona protegida? (s/n): ').lower() == 's'
# permiso_ok = terreno and (planos or excepcion) and (not protegida)
# print(f'¿Permiso OK?: {permiso_ok}')
#
# =====================================================================
