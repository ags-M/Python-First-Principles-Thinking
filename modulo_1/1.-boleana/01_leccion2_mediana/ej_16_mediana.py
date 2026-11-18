# =====================================================================
# EJERCICIO #16  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí edad y si tenés deudas (s/n). Guardá en 'puede_conducir' True
# si edad entre 17 y 65 Y NO tiene deudas.
#
# QUE SE BUSCA ENTRENAR:
# Combinar rango, input s/n, and y not. Como tu código original.
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
edad = int(input('Edad: '))
tiene_deudas = input('¿Tenés deudas? (s/n): ').lower() == 's'
edad_ok = 17 <= edad <= 65
puede_conducir = edad_ok and (not tiene_deudas)
print(f'¿Podés conducir?: {puede_conducir}')
print(f"No podes sacar el registro" * (not puede_conducir), end="")



# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# edad = int(input('Edad: '))
# tiene_deudas = input('¿Tenés deudas? (s/n): ').lower() == 's'
# edad_ok = 17 <= edad <= 65
# puede_conducir = edad_ok and (not tiene_deudas)
# print(f'¿Podés conducir?: {puede_conducir}')
#
# =====================================================================
