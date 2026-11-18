# =====================================================================
# EJERCICIO #32  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí cámara ON (s/n), movimiento (s/n), sensor (s/n),
# mantenimiento (s/n). 'seguridad_on' True si camara y (movimiento o
# sensor) y no mantenimiento.
#
# QUE SE BUSCA ENTRENAR:
# Sistema de seguridad.
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
# camara = input('¿Cámara ON? (s/n): ').lower() == 's'
# movimiento = input('¿Movimiento? (s/n): ').lower() == 's'
# sensor = input('¿Sensor? (s/n): ').lower() == 's'
# mantenimiento = input('¿Mantenimiento? (s/n): ').lower() == 's'
# seguridad_on = camara and (movimiento or sensor) and (not mantenimiento)
# print(f'¿Seguridad ON?: {seguridad_on}')
#
# =====================================================================
