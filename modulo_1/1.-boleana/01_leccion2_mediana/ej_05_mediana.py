# =====================================================================
# EJERCICIO #05  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí un numero y guardá en 'en_rango' True si está entre 1 y 100
# (incluidos). Usá la forma encadenada 1 <= n <= 100.
#
# QUE SE BUSCA ENTRENAR:
# Comparación encadenada, característica de Python.
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
en_rango = 1 <= num <= 100
print(f"El numero esta en el rango de 1 y 100: {en_rango}")

# ---------------- TU SOLUCIÓN ACÁ ----------------

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# n = int(input('Ingresá un número: '))
# en_rango = 1 <= n <= 100
# print(f'¿Está entre 1 y 100?: {en_rango}')
#
# =====================================================================
