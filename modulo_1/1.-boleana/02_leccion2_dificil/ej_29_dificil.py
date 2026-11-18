# =====================================================================
# EJERCICIO #29  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí postor registrado (s/n), garantía (s/n), depósito (s/n),
# embargado (s/n). 'subasta_ok' True si postor y (garantia o
# deposito) y no embargado.
#
# QUE SE BUSCA ENTRENAR:
# Subasta judicial.
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
# postor = input('¿Postor registrado? (s/n): ').lower() == 's'
# garantia = input('¿Garantía? (s/n): ').lower() == 's'
# deposito = input('¿Depósito? (s/n): ').lower() == 's'
# embargado = input('¿Embargado? (s/n): ').lower() == 's'
# subasta_ok = postor and (garantia or deposito) and (not embargado)
# print(f'¿Subasta OK?: {subasta_ok}')
#
# =====================================================================
