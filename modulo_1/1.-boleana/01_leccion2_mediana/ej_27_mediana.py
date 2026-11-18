# =====================================================================
# EJERCICIO #27  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí asistencia de clases (0-100) y recuperó algun parcial (s/n). Guardá en 'puede_final'
# True si asistencia >= 75 o recuperó.
#
# QUE SE BUSCA ENTRENAR:
# Umbral + 'or' con booleano.
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
asistencia_clase = int(input("Ingrese la cantidad de asistencia a clase (0-100): "))
parcial_recuperatorio = input("Ingrese: ¿recupero los parciales desaprobados?(s/n): ").lower() == "s"
puede_final = (asistencia_clase >= 75) or parcial_recuperatorio
print(f"Puede dar finales: {puede_final}")
print(f"No cumple con los criterios" * (not puede_final), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# asistencia = int(input('Asistencia (0-100): '))
# recupero = input('¿Recuperaste? (s/n): ').lower() == 's'
# puede_final = (asistencia >= 75) or recupero
# print(f'¿Podés dar final?: {puede_final}')
#
# =====================================================================
