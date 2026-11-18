# =====================================================================
# EJERCICIO #10  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí código OK (s/n), en horario (s/n), autorización (s/n),
# bloqueada (s/n). 'abre_caja' True si código y (horario o autorización)
# y no bloqueada.
#
# QUE SE BUSCA ENTRENAR:
# Modelar apertura de caja fuerte.
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
# codigo = input('¿Código OK? (s/n): ').lower() == 's'
# horario = input('¿En horario? (s/n): ').lower() == 's'
# autorizacion = input('¿Autorización? (s/n): ').lower() == 's'
# bloqueada = input('¿Bloqueada? (s/n): ').lower() == 's'
# abre_caja = codigo and (horario or autorizacion) and (not bloqueada)
# print(f'¿Abre?: {abre_caja}')
#
# =====================================================================
