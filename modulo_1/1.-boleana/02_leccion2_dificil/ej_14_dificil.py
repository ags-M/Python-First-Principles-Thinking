# =====================================================================
# EJERCICIO #14  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí orden de compra (s/n), fondos (s/n), crédito (s/n),
# bloqueado (s/n). 'paga_proveedor' True si orden y (fondos o crédito)
# y no bloqueado.
#
# QUE SE BUSCA ENTRENAR:
# Caso contable con tres booleans + negación.
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
# orden = input('¿Orden de compra? (s/n): ').lower() == 's'
# fondos = input('¿Fondos? (s/n): ').lower() == 's'
# credito = input('¿Crédito? (s/n): ').lower() == 's'
# bloqueado = input('¿Bloqueado? (s/n): ').lower() == 's'
# paga_proveedor = orden and (fondos or credito) and (not bloqueado)
# print(f'¿Paga?: {paga_proveedor}')
#
# =====================================================================
