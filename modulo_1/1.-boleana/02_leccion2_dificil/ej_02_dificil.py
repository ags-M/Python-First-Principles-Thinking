# =====================================================================
# EJERCICIO #02  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí edad, ingresos, deudas (s/n), aval (s/n). Guardá 'prestamo_ok'
# True si 18<=edad<=65 y ingresos>1000 y (no deudas o tiene aval).
#
# QUE SE BUSCA ENTRENAR:
# Cuádruple condición combinada.
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

edad = int(input("ingresa tu edad: "))
ingresos = int(input("ingresa cuanto ganas: "))
deudas = input("Tiene deudas (s/n): ").lower() == "s"
aval = input("Tiene aval (s/n): ").lower() == "s"
prestamo_ok = (18 <= edad <= 65) and (ingresos > 1000) and ((not deudas) or aval)
print(f"Prestamo otorgado: {prestamo_ok}")
print(f"Prestamo denegado" * (not prestamo_ok), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# edad = int(input('Edad: '))
# ingresos = float(input('Ingresos: '))
# deudas = input('¿Deudas? (s/n): ').lower() == 's'
# aval = input('¿Aval? (s/n): ').lower() == 's'
# prestamo_ok = (18 <= edad <= 65) and (ingresos > 1000) and ((not deudas) or aval)
# print(f'¿Préstamo OK?: {prestamo_ok}')
#
# =====================================================================
