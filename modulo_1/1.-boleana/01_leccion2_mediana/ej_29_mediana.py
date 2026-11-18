# =====================================================================
# EJERCICIO #29  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí edad y si estás en lista (s/n). Guardá en 'entra_boliche'
# True si edad >= 18 y estás en lista.
#
# QUE SE BUSCA ENTRENAR:
# Versión simple del boliche.
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
entra_boliche = (edad >= 18) and (lista)
print(f"Podes entrar al boliche: {entra_boliche}")
print(f"No podes entrar al boliche" * (not entra_boliche), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# edad = int(input('Edad: '))
# en_lista = input('¿Estás en lista? (s/n): ').lower() == 's'
# entra_boliche = (edad >= 18) and en_lista
# print(f'¿Entrás al boliche?: {entra_boliche}')
#
# =====================================================================
