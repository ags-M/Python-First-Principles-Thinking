# =====================================================================
# EJERCICIO #33  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí tiempo (int minutos) y temp (int). Guardá en 'cookie_lista'
# True si tiempo >= 10 y temp == 180.
#
# QUE SE BUSCA ENTRENAR:
# Dos condiciones simultáneas con 'and'.
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

tiempo_coccion = int(input("ingresa los minutos: "))
temperatura = int(input("ingresa la temperatura: "))
cookie_lista = (tiempo_coccion >= 10) and (temperatura == 180)
print(f"Las cookies estan listas: {cookie_lista}")
print(f"las cookies no estaran listas" * (not cookie_lista), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# tiempo = int(input('Tiempo (min): '))
# temp = int(input('Temperatura: '))
# cookie_lista = (tiempo >= 10) and (temp == 180)
# print(f'¿Lista?: {cookie_lista}')
#
# =====================================================================
