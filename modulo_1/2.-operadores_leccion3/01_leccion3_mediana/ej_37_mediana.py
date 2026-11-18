# =====================================================================
# EJERCICIO #37  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Operadores (Leccion 3)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí dos números y guardá en 'diferentes' True si son distintos
# (usá !=).
#
# QUE SE BUSCA ENTRENAR:
# Comparación de desigualdad.
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
n1 = int(input("ingrese un numero entero: "))
n2 = int(input("ingrese un numero entero: "))
diferentes = n1 != n2
print(f"los numeros son diferentes {diferentes}")
print(f"los numeros son iguales" * (not diferentes))
# ---------------- TU SOLUCIÓN ACÁ ----------------






# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# a = int(input('Primer número: '))
# b = int(input('Segundo número: '))
# diferentes = a != b
# print(f'¿Son diferentes?: {diferentes}')
#
# =====================================================================
