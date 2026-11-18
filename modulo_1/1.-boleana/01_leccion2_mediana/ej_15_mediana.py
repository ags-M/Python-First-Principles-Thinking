# =====================================================================
# EJERCICIO #15  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí el promedio (float) y si reprobo alguna materia (s/n).
# Guardá en 'pasa_de_anio' True si promedio >= 7 Y no reprobo.
#
# QUE SE BUSCA ENTRENAR:
# Combinar un float con un booleano del input con == 's'.
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
promedio = float(input("ingresa tu promedio: "))
reprobo_materias = input("reprobaste alguna materia (s/n): ").lower() == "s"
pasa_de_año = promedio >= 7 and not reprobo_materias
print(f"Por tus calificaciones, pasas de año: {pasa_de_año}")
print(f"No pasas de año" * (not pasa_de_año), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# promedio = float(input('Promedio: '))
# reprobo = input('¿Reprobaste alguna materia? (s/n): ').lower() == 's'
# pasa_de_anio = (promedio >= 7) and (not reprobo)
# print(f'¿Pasás de año?: {pasa_de_anio}')
#
# =====================================================================
