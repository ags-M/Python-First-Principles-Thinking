# =====================================================================
# EJERCICIO #36  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí edad, peso (float), ayuno (s/n), enfermedad (s/n).
# 'donacion_ok' True si 18<=edad<=65 y peso>50 y no ayuno y
# no enfermedad.
#
# QUE SE BUSCA ENTRENAR:
# Cuádruple condición con dos negaciones.
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
# peso = float(input('Peso (kg): '))
# ayuno = input('¿Ayuno? (s/n): ').lower() == 's'
# enfermedad = input('¿Enfermedad? (s/n): ').lower() == 's'
# donacion_ok = (18 <= edad <= 65) and (peso > 50) and (not ayuno) and (not enfermedad)
# print(f'¿Donación OK?: {donacion_ok}')
#
# =====================================================================
