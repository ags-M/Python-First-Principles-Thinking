# =====================================================================
# EJERCICIO #18  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí temperatura (float) y guardá en 'tiene_fiebre' True si > 37.5.
#
# QUE SE BUSCA ENTRENAR:
# Comparación con float y umbral médico.
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
temperatura_niño = float(input("decime la temperatura del niño: "))
tiene_fiebre = temperatura_niño > 37.5
print(f"la temperatura del niño indica que tiene fiebre es: {tiene_fiebre}")
print(f"No tiene fiebre" * (not tiene_fiebre), end="")

# ---------------- TU SOLUCIÓN ACÁ ----------------
# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# temp = float(input('Temperatura: '))
# tiene_fiebre = temp > 37.5
# print(f'¿Tenés fiebre?: {tiene_fiebre}')
#
# =====================================================================
