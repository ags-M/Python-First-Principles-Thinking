# =====================================================================
# EJERCICIO #38  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí edad, sin contraindicación (s/n), autorización (s/n),
# embarazo (s/n). 'laser_ok' True si edad>=21 y (no contraindicacion
# o autorizacion) y no embarazo.
#
# QUE SE BUSCA ENTRENAR:
# Cirugía láser con doble negación + paréntesis.
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
# edad = int(input('Edad: '))
# contraindicacion = input('¿Contraindicación? (s/n): ').lower() == 's'
# autorizacion = input('¿Autorización? (s/n): ').lower() == 's'
# embarazo = input('¿Embarazo? (s/n): ').lower() == 's'
# laser_ok = (edad >= 21) and ((not contraindicacion) or autorizacion) and (not embarazo)
# print(f'¿Láser OK?: {laser_ok}')
#
# =====================================================================
