# =====================================================================
# EJERCICIO #03  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí promedio, ingresos bajos (s/n), situación especial (s/n),
# repetidor (s/n). 'beca' True si promedio>=8 y (ingresos_bajos o especial)
# y no repetidor.
#
# QUE SE BUSCA ENTRENAR:
# Cuatro condiciones con jerarquía de paréntesis.
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
ingresos_bajos = input("Tienes ingresos bajos (s/n): ").lower() == "s"
situacion_special = input("Tienes una situacion especial(s/n): ").lower() == "s"
repetidor = input("Tienes problemas de repetidor(s/n): ").lower() == "s"
beca = promedio >= 8 and (ingresos_bajos or situacion_special) and (not repetidor)
print(f"Beca otorgada: {beca}")
print(f"Beca NO otorgada" * (not beca), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# promedio = float(input('Promedio: '))
# bajos = input('¿Ingresos bajos? (s/n): ').lower() == 's'
# especial = input('¿Situación especial? (s/n): ').lower() == 's'
# repetidor = input('¿Repetidor? (s/n): ').lower() == 's'
# beca = (promedio >= 8) and (bajos or especial) and (not repetidor)
# print(f'¿Beca?: {beca}')
#
# =====================================================================
