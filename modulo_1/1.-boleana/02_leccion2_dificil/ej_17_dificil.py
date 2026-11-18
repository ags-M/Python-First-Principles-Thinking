# =====================================================================
# EJERCICIO #17  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí factura comercial (s/n), arancel pagado (s/n), tratado (s/n),
# sancionado (s/n). 'envio_ok' True si factura y (pagado o tratado)
# y no sancionado.
#
# QUE SE BUSCA ENTRENAR:
# Comercio internacional.
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
# factura = input('¿Factura comercial? (s/n): ').lower() == 's'
# pagado = input('¿Arancel pagado? (s/n): ').lower() == 's'
# tratado = input('¿Tratado? (s/n): ').lower() == 's'
# sancionado = input('¿Sancionado? (s/n): ').lower() == 's'
# envio_ok = factura and (pagado or tratado) and (not sancionado)
# print(f'¿Envío OK?: {envio_ok}')
#
# =====================================================================
