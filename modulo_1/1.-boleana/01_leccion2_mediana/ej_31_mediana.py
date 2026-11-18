# =====================================================================
# EJERCICIO #31  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí si la puerta está cerrada (s/n) y peso (int). Guardá en
# 'mueve_ascensor' True si puerta cerrada y peso <= 400.
#
# QUE SE BUSCA ENTRENAR:
# Negación de input s/n + comparación.
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
ascensor_puerta = input("La puerta esta cerrada (s/n): ").lower() == "s"
peso_total_indicador = int(input("ingrese el peso total en el ascensor: "))
mueve_ascensor = ascensor_puerta and (peso_total_indicador <= 400)
print(f"El ascensor se movera: {mueve_ascensor}")
print(f"El ascensor no se movera" * (not mueve_ascensor), end="")
# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# cerrada = input('¿Puerta cerrada? (s/n): ').lower() == 's'
# peso = int(input('Peso (kg): '))
# mueve_ascensor = cerrada and (peso <= 400)
# print(f'¿Se mueve?: {mueve_ascensor}')
#
# =====================================================================
