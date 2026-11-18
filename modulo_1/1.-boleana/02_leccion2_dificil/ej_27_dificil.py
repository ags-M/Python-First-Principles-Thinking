# =====================================================================
# EJERCICIO #27  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí socio activo (s/n), sin multas (s/n), pagó multa (s/n),
# libro reservado (s/n). 'presta_libro' True si socio y (sin_multas o
# pago) y no reservado.
#
# QUE SE BUSCA ENTRENAR:
# Biblioteca.
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
# socio = input('¿Socio activo? (s/n): ').lower() == 's'
# sin_multas = input('¿Sin multas? (s/n): ').lower() == 's'
# pago = input('¿Pagó multa? (s/n): ').lower() == 's'
# reservado = input('¿Reservado? (s/n): ').lower() == 's'
# presta_libro = socio and (sin_multas or pago) and (not reservado)
# print(f'¿Presta?: {presta_libro}')
#
# =====================================================================
