# =====================================================================
# EJERCICIO #38  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# ==================================================
#
# CONSIGNA:
# Pedí nota (0-10) y si dejó en blanco (s/n). Guardá en 'es_valida'
# True si nota >= 0 y nota <= 10 y NO está en blanco.
#
# QUE SE BUSCA ENTRENAR:
# Tres condiciones combinadas con 'and' + 'not'.
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
nota = int(input("Ingrese su nota de calificacion (0-10): "))
en_blanco = input("Quedo en blanco (s/n): ").lower() == "s"
es_valida = (0 <= nota <= 10) and (not en_blanco)
print(f"Tu calificacion es valida: {es_valida}")
print(f"Tu calificacion No es valida" * (not es_valida), end="")
# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# nota = float(input('Nota (0-10): '))
# en_blanco = input('¿En blanco? (s/n): ').lower() == 's'
# es_valida = (0 <= nota <= 10) and (not en_blanco)
# print(f'¿Válida?: {es_valida}')
#
# =====================================================================
