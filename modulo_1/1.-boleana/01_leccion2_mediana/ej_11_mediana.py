# =====================================================================
# EJERCICIO #11  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí una edad y guardá en 'es_valida' True si está entre 0 y 120.
#
# QUE SE BUSCA ENTRENAR:
# Rango válido de un dato de entrada.
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
edad = int(input("Decime tu edad: "))
es_valida = 0 <= edad <= 120
print(f"La edad que ingresaste: {edad} es valida? {es_valida}")
print(f"No es válida" * (not es_valida), end ="")

# ---------------- TU SOLUCIÓN ACÁ ----------------

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# edad = int(input('Ingresá una edad: '))
# es_valida = 0 <= edad <= 120
# print(f'¿Es válida?: {es_valida}')
#
# =====================================================================
