# =====================================================================
# EJERCICIO #06  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Operadores (Leccion 3)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí dos números enteros y mostrá el resto de la división (%).
#
# QUE SE BUSCA ENTRENAR:
# Practicar el operador % (módulo).
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
n1 = int(input("ingrese un numero entero: ")) #ejemplo 5
n2 = int(input("ingrese un numero entero: ")) #ejemplo 8
resto = n1 % n2
print(f"el resto es de:{resto}") # 5 % 8 → 5 dividido entre 8 da cociente 0 y resto 5 (porque 8 no cabe ni una vez en 5).

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# a = int(input('Primer número: '))
# b = int(input('Segundo número: '))
# resto = a % b
# print(f'El resto es: {resto}')
#
# =====================================================================
