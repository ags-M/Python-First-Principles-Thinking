# =====================================================================
# EJERCICIO #02  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí un numero entero y guardá en 'es_par' True si es par (n%2 == 0).
# Mostralo.
#
# QUE SE BUSCA ENTRENAR:
# Practicar el operador módulo (%) combinado con ==.
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


# ---------------- TU SOLUCIÓN ACÁ ----------------
n = int(input("ingresa un numero: "))
es_par = n % 2 == 0
print(f"el numero ingresado {n}, es un numero par?: {es_par}")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# n = int(input('Ingresá un número: '))
# es_par = n % 2 == 0
# print(f'¿Es par?: {es_par}')
#
# =====================================================================
