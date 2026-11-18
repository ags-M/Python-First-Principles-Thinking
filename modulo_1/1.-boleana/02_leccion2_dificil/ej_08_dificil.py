# =====================================================================
# EJERCICIO #08  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí declaración OK (s/n), impuesto pagado (s/n), exención (s/n),
# mercancía prohibida (s/n). 'pasa_aduana' True si declaración y
# (pagado o exención) y no prohibida.
#
# QUE SE BUSCA ENTRENAR:
# Cuatro booleans con paréntesis interno.
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
# declaracion = input('¿Declaración OK? (s/n): ').lower() == 's'
# pagado = input('¿Impuesto pagado? (s/n): ').lower() == 's'
# exencion = input('¿Exención? (s/n): ').lower() == 's'
# prohibida = input('¿Prohibida? (s/n): ').lower() == 's'
# pasa_aduana = declaracion and (pagado or exencion) and (not prohibida)
# print(f'¿Pasa aduana?: {pasa_aduana}')
#
# =====================================================================
