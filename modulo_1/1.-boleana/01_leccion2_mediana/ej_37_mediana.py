# =====================================================================
# EJERCICIO #37  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí si es estudiante (s/n) y si es jubilado (s/n). Guardá en
# 'viaja_barato' True si es estudiante O jubilado.
#
# QUE SE BUSCA ENTRENAR:
# Practicar 'or' con dos inputs s/n.
#
# REGLAS (solo lecciones 2 y 3):
#   - Podés usar: input(), print(), int(), float(), str(), bool()
#   - Operadores aritméticos: +  -  *  /  //  %  **
#   - Operadores de comparación: ==  !=  <  >  <=  >=
#   - Operadores lógicos: and  or  not
#   - f-strings
#   - len() para medir strings
#   - NO uses if/elif/else, ni for, ni while, ni listas, ni funciones
# =====================================================================
estudiante = input("ingrese si es estudiante (s/n): ").lower() == "s"
jubilado = input("ingrese si es jubilado (s/n): ").lower() == "s"
viaje_barato = estudiante or jubilado
print(f"Puede acceder a un viaje mas barato: {viaje_barato}")
print(f"No Puede acceder a un viaje mas barato" * (not viaje_barato), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# estudiante = input('¿Estudiante? (s/n): ').lower() == 's'
# jubilado = input('¿Jubilado? (s/n): ').lower() == 's'
# viaja_barato = estudiante or jubilado
# print(f'¿Viaja barato?: {viaja_barato}')
#
# =====================================================================
