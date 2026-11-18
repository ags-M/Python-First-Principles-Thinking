# =====================================================================
# EJERCICIO #22  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí un numero y guardá en 'positivo_o_par' True si es > 0 O par.
#
# QUE SE BUSCA ENTRENAR:
# Practicar 'or' vs 'and' (comparar con el anterior).
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
positivo_o_par= (num > 0 ) or (num % 2 == 0)
print(f"El numero es positivo o par: {positivo_o_par}")
print(f"El numero no es positivo ni es par" * (not positivo_o_par))
print("-" * 12)
#con este ejercicio se discrimina la respuesta
num = int(input("ingresa un numero: "))
es_positivo = num > 0
es_par = num % 2 == 0
print("Positivo y par" * (es_positivo and es_par), end="")
print("Positivo e impar" * (es_positivo and not es_par), end="")
print("Negativo y par" * (not es_positivo and es_par), end="")
print("Negativo e impar" * (not es_positivo and not es_par), end="" )

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# n = int(input('Ingresá un número: '))
# positivo_o_par = (n > 0) or (n % 2 == 0)
# print(f'¿Es positivo o par?: {positivo_o_par}')
#
# =====================================================================
