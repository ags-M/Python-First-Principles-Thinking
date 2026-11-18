# =====================================================================
# EJERCICIO #20  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí edad y si es ciudadano (s/n). Guardá en 'puede_votar' True
# si edad >= 16 y es ciudadano.
#
# QUE SE BUSCA ENTRENAR:
# Combinar edad con input s/n usando 'and'.
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
ciudadano = input("es ciudadano (s/n): ").lower() == "s"
puede_votar = (edad >= 16) and ciudadano
print(f"¿Puede votar?: {puede_votar}")
print(f"No puede votar" * (not puede_votar), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# edad = int(input('Edad: '))
# es_ciudadano = input('¿Sos ciudadano? (s/n): ').lower() == 's'
# puede_votar = (edad >= 16) and es_ciudadano
# print(f'¿Podés votar?: {puede_votar}')
#
# =====================================================================
