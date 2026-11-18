# =====================================================================
# EJERCICIO #26  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Operadores (Leccion 3)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí un monto en pesos y mostrá cuántos billetes de 100 necesitás
# (usá //).
#
# QUE SE BUSCA ENTRENAR:
# División entera aplicada a dinero.
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
monto = float(input("ingrese el monto del dinero: "))
cant_billetes =monto // 100
print(f"La cantidad de billetes utilizado para pagar el monto adeudado es de: {cant_billetes}")


# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# monto = int(input('Monto en pesos: '))
# billetes = monto // 100
# print(f'Necesitás {billetes} billetes de 100')
#
# =====================================================================
