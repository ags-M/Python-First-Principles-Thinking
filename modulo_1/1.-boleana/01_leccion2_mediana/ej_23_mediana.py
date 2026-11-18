# =====================================================================
# EJERCICIO #23  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí una palabra y guardá en 'tiene_5' True si tiene exactamente 5
# letras (usá len).
#
# QUE SE BUSCA ENTRENAR:
# Practicar len() con string y comparación.
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
palabra = input("decime una palabra: ")
tiene_5 = len(palabra) == 5
print(f"La palabra tiene 5 letras?: {tiene_5}")
print(f"La palabra no tiene 5 letras" * (not tiene_5))

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# palabra = input('Ingresá una palabra: ')
# tiene_5 = len(palabra) == 5
# print(f'¿Tiene 5 letras?: {tiene_5}')
#
# =====================================================================
