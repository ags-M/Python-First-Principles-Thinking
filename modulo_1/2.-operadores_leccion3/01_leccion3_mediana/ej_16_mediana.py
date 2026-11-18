# =====================================================================
# EJERCICIO #16  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Operadores (Leccion 3)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí una temperatura en Celsius y convertila a Fahrenheit.
# Fórmula: F = C * 9/5 + 32.
#
# QUE SE BUSCA ENTRENAR:
# Fórmula combinada con *, /, +.
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
t_celsius = float(input("ingrese la temperatura en grados celsius: ")) 
conversion = t_celsius * 9/5 + 32
print(f"la temperatura {t_celsius}°C en grados Fahrenheit es de: {conversion}°F")
# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# c = float(input('Temperatura en Celsius: '))
# f = c * 9 / 5 + 32
# print(f'{c}°C = {f}°F')
#
# =====================================================================
