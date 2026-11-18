# =====================================================================
# EJERCICIO #27  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Operadores (Leccion 3)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí un monto y mostrá cuánto sobra después de pagar con billetes
# de 100 (usá %).
#
# QUE SE BUSCA ENTRENAR:
# Módulo aplicado a dinero.
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
monto = int(input("ingrese un monto: "))
resto = monto % 100
print(resto)

# ---------------- TU SOLUCIÓN ACÁ ----------------
# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# monto = int(input('Monto: '))
# sobra = monto % 100
# print(f'Sobran {sobra} pesos')
#
# =====================================================================
