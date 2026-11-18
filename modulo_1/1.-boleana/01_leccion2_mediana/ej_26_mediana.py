# =====================================================================
# EJERCICIO #26  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí saldo (float) y si tiene descubierto autorizado (s/n).
# Guardá en 'puede_pagar' True si saldo > 0 o tiene descubierto.
#
# QUE SE BUSCA ENTRENAR:
# Practicar 'or' con input s/n.
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
saldo_cuenta = float(input("ingrese su saldo: "))
descubierto_autorizado = input("Posee descubierto autorizado (s/n): ").lower() == "s"
puede_pagar = (saldo_cuenta > 0) or (descubierto_autorizado)
print(f"El cliente puede pagar es: {puede_pagar}")
print(f"No puede pagar" * (not puede_pagar))
# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# saldo = float(input('Saldo: '))
# descubierto = input('¿Tenés descubierto? (s/n): ').lower() == 's'
# puede_pagar = (saldo > 0) or descubierto
# print(f'¿Podés pagar?: {puede_pagar}')
#
# =====================================================================
