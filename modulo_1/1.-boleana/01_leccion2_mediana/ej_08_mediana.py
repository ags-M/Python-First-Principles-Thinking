# =====================================================================
# EJERCICIO #08  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí un numero y guardá en 'es_impar' True si NO es par.
# Usá el operador 'not'.
#
# QUE SE BUSCA ENTRENAR:
# Practicar 'not' sobre una expresión booleana.
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
es_impar = not (n % 2 == 0)
print(f'¿Es impar?: {es_impar}')

# ---------------- TU SOLUCIÓN ACÁ ----------------

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# n = int(input('Ingresá un número: '))
# es_impar = not (n % 2 == 0)
# print(f'¿Es impar?: {es_impar}')
#
# =====================================================================
