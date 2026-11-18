# =====================================================================
# EJERCICIO #39  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Entender
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí un numero y guardá en 'es_negativo_o_cero' True si NO es
# positivo (n <= 0). Hacelo dos veces: una con <= y otra con not (n>0).
#
# QUE SE BUSCA ENTRENAR:
# Ver que hay dos formas equivalentes de expresar lo mismo.
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
n = int(input('Ingresá un número: '))
forma1 = n <= 0
forma2 = not (n > 0)
print(f'Forma 1: {forma1}  |  Forma 2: {forma2}  |  Iguales: {forma1 == forma2}')

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# n = int(input('Ingresá un número: '))
# forma1 = n <= 0
# forma2 = not (n > 0)
# print(f'Forma 1: {forma1}  |  Forma 2: {forma2}  |  Iguales: {forma1 == forma2}')
#
# =====================================================================
