# =====================================================================
# EJERCICIO #11  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Operadores (Leccion 3)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí el monto de la cuenta y un nivel de servicio (1-5). Calculá
# la propina así: 1=5%, 2=10%, 3=15%, 4=18%, 5=20%.
# Truco: propina_pct = (nivel == 1)*5 + (nivel == 2)*10 + ...
#
# QUE SE BUSCA ENTRENAR:
# Propina escalonada con truco de booleans sumados.
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


# ---------------- TU SOLUCIÓN ACÁ ----------------






# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# cuenta = float(input('Cuenta: '))
# nivel = int(input('Nivel (1-5): '))
# pct = (nivel == 1) * 5 + (nivel == 2) * 10 + (nivel == 3) * 15 + (nivel == 4) * 18 + (nivel == 5) * 20
# propina = cuenta * pct / 100
# print(f'Propina: {propina}')
#
# =====================================================================
