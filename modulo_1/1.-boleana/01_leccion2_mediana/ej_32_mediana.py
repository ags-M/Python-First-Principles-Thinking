# =====================================================================
# EJERCICIO #32  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí temp y humedad. Guardá en 'alarma' True si temp > 50 o
# humedad < 20.
#
# QUE SE BUSCA ENTRENAR:
# Alarmas con 'or' de dos variables.
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

temperatura = float(input("ingresa la temperatura actual: "))
humedad = float(input("ingresa la humedad actual: "))
alarma = temperatura > 50 or (humedad < 20)
print(f"Es una situacion critica:{alarma}")
print(f"No es una situacion critica" * (not alarma), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# temp = float(input('Temperatura: '))
# humedad = int(input('Humedad %: '))
# alarma = (temp > 50) or (humedad < 20)
# print(f'¿Alarma?: {alarma}')
#
# =====================================================================
