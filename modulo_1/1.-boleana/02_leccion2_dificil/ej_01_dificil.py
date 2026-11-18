# =====================================================================
# EJERCICIO #01  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí rol, contraseña (s/n OK), 2FA (s/n). Guardá 'es_admin' True
# si rol=='admin' y (contraseña_ok o tiene_2fa).
#
# QUE SE BUSCA ENTRENAR:
# Combina texto, dos inputs s/n y paréntesis con 'or' interno.
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

rol = input('Rol: ').lower()
pass_ok = input('¿Contraseña OK? (s/n): ').lower() == 's'
tiene_2fa = input('¿2FA? (s/n): ').lower() == 's'
es_admin = (rol == 'admin') and (pass_ok or tiene_2fa)
print(f"es el administrador?: {es_admin}")
print(f"no es el administrador" * (not es_admin), end="")


# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# rol = input('Rol: ').lower()
# pass_ok = input('¿Contraseña OK? (s/n): ').lower() == 's'
# tiene_2fa = input('¿2FA? (s/n): ').lower() == 's'
# es_admin = (rol == 'admin') and (pass_ok or tiene_2fa)
# print(f'¿Es admin?: {es_admin}')
#
# =====================================================================
