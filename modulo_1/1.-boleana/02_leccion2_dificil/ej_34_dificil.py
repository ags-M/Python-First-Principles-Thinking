# =====================================================================
# EJERCICIO #34  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí hijo menor (s/n), padre con ingresos (s/n), trabaja (s/n),
# otra pensión (s/n). 'pension_ok' True si menor y (ingresos o
# trabaja) y no otra_pension.
#
# QUE SE BUSCA ENTRENAR:
# Pensión alimentaria.
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
# menor = input('¿Hijo menor? (s/n): ').lower() == 's'
# ingresos = input('¿Padre con ingresos? (s/n): ').lower() == 's'
# trabaja = input('¿Trabaja? (s/n): ').lower() == 's'
# otra_pension = input('¿Otra pensión? (s/n): ').lower() == 's'
# pension_ok = menor and (ingresos or trabaja) and (not otra_pension)
# print(f'¿Pensión?: {pension_ok}')
#
# =====================================================================
