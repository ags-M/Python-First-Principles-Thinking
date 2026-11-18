# =====================================================================
# EJERCICIO #34  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí si hay movimiento (s/n) y si es el dueño (s/n). Guardá en
# 'suena_alarma' True si hay movimiento Y NO es el dueño.
#
# QUE SE BUSCA ENTRENAR:
# Combinar dos inputs s/n con 'and' + 'not'.
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
movimiento = input("existe movimiento visible (s/n): ").lower() == "s"
dueño_movimiento = input("es el dueño que esta moviendose (s/n): ").lower() =="s"
suena_alarma = movimiento and (not dueño_movimiento)
print(f"Peligro suena la alarma:{suena_alarma}")
print(f"No suena la alarma" * (not suena_alarma), end="")
# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# movimiento = input('¿Hay movimiento? (s/n): ').lower() == 's'
# es_dueno = input('¿Es el dueño? (s/n): ').lower() == 's'
# suena_alarma = movimiento and (not es_dueno)
# print(f'¿Suena?: {suena_alarma}')
#
# =====================================================================
