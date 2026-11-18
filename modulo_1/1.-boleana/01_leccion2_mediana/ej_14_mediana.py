# =====================================================================
# EJERCICIO #14  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí un numero y guardá en 'en_rangos' True si está en [1,10] O en
# [90,100].
#
# QUE SE BUSCA ENTRENAR:
# Practicar 'or' con dos rangos.
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
n = int(input("ingresa un numero entero: "))
en_rangos = (1 <= n <= 10) or (90 <= n <= 100)
print(f"esta en los rangos deseados {en_rangos}")
print(f"No esta en los rangos deseados" * (not en_rangos), end="" )

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# n = int(input('Ingresá un número: '))
# en_rangos = (1 <= n <= 10) or (90 <= n <= 100)
# print(f'¿Está en los rangos?: {en_rangos}')
#
# =====================================================================
