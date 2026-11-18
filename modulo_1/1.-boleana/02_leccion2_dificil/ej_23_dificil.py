# =====================================================================
# EJERCICIO #23  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí residente (s/n), placa OK (s/n), autorización (s/n),
# lista negra (s/n). 'ingresa_cond' True si residente y (placa o
# autorizacion) y no negra.
#
# QUE SE BUSCA ENTRENAR:
# Acceso a barrio privado.
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
# residente = input('¿Residente? (s/n): ').lower() == 's'
# placa = input('¿Placa OK? (s/n): ').lower() == 's'
# autorizacion = input('¿Autorización? (s/n): ').lower() == 's'
# negra = input('¿Lista negra? (s/n): ').lower() == 's'
# ingresa_cond = residente and (placa or autorizacion) and (not negra)
# print(f'¿Ingresa?: {ingresa_cond}')
#
# =====================================================================
