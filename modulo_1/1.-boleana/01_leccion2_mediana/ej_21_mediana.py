# =====================================================================
# EJERCICIO #21  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí un numero y guardá en 'positivo_y_par' True si es > 0 Y par.
#
# QUE SE BUSCA ENTRENAR:
# Combinar > y % con 'and'.
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
positivo_par = (num > 0 ) and (num % 2 == 0)
print(f"El numero es positivo y par: {positivo_par}")
print(f"El numero no completa la consigna" * (not positivo_par), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# n = int(input('Ingresá un número: '))
# positivo_y_par = (n > 0) and (n % 2 == 0)
# print(f'¿Es positivo y par?: {positivo_y_par}')
#
# =====================================================================
