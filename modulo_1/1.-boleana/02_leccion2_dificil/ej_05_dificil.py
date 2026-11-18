# =====================================================================
# EJERCICIO #05  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA: lanzamiento de un cohete espacial

# Pedí combustible %, oxígeno %, sistema vital (s/n), alerta (s/n).
# 'puede_lanzar' True si combustible>80 y (oxígeno>70 y vital) y no alerta.
#
# QUE SE BUSCA ENTRENAR:
# Paréntesis anidados: 'and' dentro de 'and'.
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
combustible = int(input(" ingrese la cantidad de combustible: "))
oxigeno = int(input(" ingrese la cantidad de oxigeno: "))
sistema_vital = (input("El sistema vital esta operativo (s/n): ")).lower() == "s"
alerta = (input("El sistema señala alguna alerta (s/n): ")).lower() == "s"
lanzamiento = (combustible > 80) and (oxigeno > 70 and sistema_vital) and (not alerta)
print(f"Proceda con el lanzamiento: {lanzamiento}")
print(f" NO Proceda con el lanzamiento" * (not lanzamiento), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# combustible = float(input('Combustible %: '))
# oxigeno = float(input('Oxígeno %: '))
# vital = input('¿Sistema vital OK? (s/n): ').lower() == 's'
# alerta = input('¿Alerta? (s/n): ').lower() == 's'
# puede_lanzar = (combustible > 80) and ((oxigeno > 70) and vital) and (not alerta)
# print(f'¿Puede lanzar?: {puede_lanzar}')
#
# =====================================================================
