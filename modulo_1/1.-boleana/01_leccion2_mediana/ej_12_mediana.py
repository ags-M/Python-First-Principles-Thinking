# =====================================================================
# EJERCICIO #12  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí un numero y guardá en 'es_multiplo_5' True si n%5 == 0.
#
# QUE SE BUSCA ENTRENAR:
# Módulo aplicado a múltiplos.
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
es_multiplo_5 = num % 5 == 0
print(f"¿El número ingresado es múltiplo de 5?: es {es_multiplo_5}")
print(f"Es falso por que No es multiplo de 5" * (not es_multiplo_5), end = "")


# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# n = int(input('Ingresá un número: '))
# es_multiplo_5 = n % 5 == 0
# print(f'¿Es múltiplo de 5?: {es_multiplo_5}')
#
# =====================================================================
