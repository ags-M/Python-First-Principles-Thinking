# =====================================================================
# EJERCICIO #13  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí un numero y guardá en 'multiplo_3_y_5' True si es múltiplo
# de 3 Y de 5 a la vez.
#
# QUE SE BUSCA ENTRENAR:
# Combinar dos condiciones con 'and'.
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
num = int(input("ingresa un numero: "))
multiplo_3_y_5 = num % 3 == 0 and num % 5 == 0
print(f"Es multiplo de 3 y 5: {multiplo_3_y_5}")
print(f"No es multiplo de 3 y 5" * (not multiplo_3_y_5), end ="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# n = int(input('Ingresá un número: '))
# multiplo_3_y_5 = (n % 3 == 0) and (n % 5 == 0)
# print(f'¿Es múltiplo de 3 y 5?: {multiplo_3_y_5}')
#
# =====================================================================
