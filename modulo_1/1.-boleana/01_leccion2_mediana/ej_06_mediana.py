# =====================================================================
# EJERCICIO #06  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí una temperatura (entera) y guardá en 'agradable' True si está
# entre 15 y 25 grados (incluidos).
#
# QUE SE BUSCA ENTRENAR:
# Aplicar comparación encadenada a un caso real.
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
temperatura =int(input("Que temperatura hace hoy: "))
agradable = 15 <= temperatura <= 25
print(f"la temperatura actual de hoy es agradable: {agradable} ")

# ---------------- TU SOLUCIÓN ACÁ ----------------
# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# temp = int(input('Ingresá la temperatura: '))
# agradable = 15 <= temp <= 25
# print(f'¿Es agradable?: {agradable}')
#
# =====================================================================
