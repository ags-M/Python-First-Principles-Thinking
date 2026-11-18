# =====================================================================
# EJERCICIO #01  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedile al usuario un numero entero y guardá en una variable
# 'es_positivo' True si es mayor que 0. Mostralo con print.
#
# QUE SE BUSCA ENTRENAR:
# Fijar la idea de comparación simple (>) y su resultado booleano.
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
es_positivo = num > 0
print(f"El numero que ingresastee es positivo: {es_positivo}")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# n = int(input('Ingresá un número: '))
# es_positivo = n > 0
# print(f'¿Es positivo?: {es_positivo}')
#
# =====================================================================
