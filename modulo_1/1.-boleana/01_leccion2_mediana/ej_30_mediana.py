# =====================================================================
# EJERCICIO #30  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí edad, lista (s/n) y si pagás entrada (s/n). Guardá en
# 'entra' True si edad >= 18 y (en_lista o paga).
#
# QUE SE BUSCA ENTRENAR:
# Versión completa del boliche. Combina 'and' + 'or' con paréntesis.
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

edad = int(input("Ingresa tu edad: "))
lista = input("consulta estas en la lista (s/n): ").lower() == "s"
paga = input("Paga la entrada (s/n): ").lower() == "s"
entra= (edad >= 18) and (lista or paga)
print(f"Podes entrar al boliche: {entra}")
print(f"No podes entrar al boliche" * (not entra), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# edad = int(input('Edad: '))
# en_lista = input('¿En lista? (s/n): ').lower() == 's'
# paga = input('¿Pagás entrada? (s/n): ').lower() == 's'
# entra = (edad >= 18) and (en_lista or paga)
# print(f'¿Entrás?: {entra}')
#
# =====================================================================
