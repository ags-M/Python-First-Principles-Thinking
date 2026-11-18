# =====================================================================
# EJERCICIO #12  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí batería OK (s/n), combustible (float), eléctrico OK (s/n),
# falla motor (s/n). 'arranca' True si batería y (combustible>0 o
# electrico) y no falla.
#
# QUE SE BUSCA ENTRENAR:
# Combina booleanos con un float.
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
# bateria = input('¿Batería OK? (s/n): ').lower() == 's'
# combustible = float(input('Combustible (L): '))
# electrico = input('¿Eléctrico OK? (s/n): ').lower() == 's'
# falla = input('¿Falla motor? (s/n): ').lower() == 's'
# arranca = bateria and ((combustible > 0) or electrico) and (not falla)
# print(f'¿Arranca?: {arranca}')
#
# =====================================================================
