# =====================================================================
# EJERCICIO #33  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí clima OK (s/n), combustible OK (s/n), sistema OK (s/n),
# fallo previo (s/n). 'despega' True si clima y (combustible o
# sistema) y no fallo_previo.
#
# QUE SE BUSCA ENTRENAR:
# Lanzamiento de cohete.
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
# clima = input('¿Clima OK? (s/n): ').lower() == 's'
# combustible = input('¿Combustible OK? (s/n): ').lower() == 's'
# sistema = input('¿Sistema OK? (s/n): ').lower() == 's'
# fallo_previo = input('¿Fallo previo? (s/n): ').lower() == 's'
# despega = clima and (combustible or sistema) and (not fallo_previo)
# print(f'¿Despega?: {despega}')
#
# =====================================================================
