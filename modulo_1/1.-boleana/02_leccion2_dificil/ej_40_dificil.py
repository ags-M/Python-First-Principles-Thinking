# =====================================================================
# EJERCICIO #40  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí glucosa (float), ayuno (s/n), síntomas (s/n), embarazo (s/n).
# 'diabetes' True si glucosa>126 y (ayuno o sintomas) y no embarazo.
#
# QUE SE BUSCA ENTRENAR:
# Diagnóstico médico con float + 3 booleans.
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
glucemia = float(input("ingrese el valor de la glucemia: ")) 
ayuno = input("hizo el ayuno de 8 horas(s/n): ").lower() == "s"
sintomas = input("presento algun sintoma(s/n): ").lower() == "s"
embarazo = input("esta embarazada(s/n): ").lower() == "s"
diabetes = (glucemia > 126) and (ayuno or sintomas) and (not embarazo)
print(f"Ud tiene un diagnostico de diabetes: {diabetes}")
print(f"No presenta signos de diabetes" or (not diabetes), end="")






# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# glucosa = float(input('Glucosa: '))
# ayuno = input('¿Ayuno? (s/n): ').lower() == 's'
# sintomas = input('¿Síntomas? (s/n): ').lower() == 's'
# embarazo = input('¿Embarazo? (s/n): ').lower() == 's'
# diabetes = (glucosa > 126) and (ayuno or sintomas) and (not embarazo)
# print(f'¿Diabetes?: {diabetes}')
#
# =====================================================================
