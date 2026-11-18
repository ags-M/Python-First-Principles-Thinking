# =====================================================================
# EJERCICIO #40  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí una contraseña (string). Guardá en 'acceso_ok' True si
# es igual a 'python123'. Usá comparación de string con ==.
#
# QUE SE BUSCA ENTRENAR:
# Practicar == con strings y la idea de 'clave correcta'.
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
contraseña = input("Ingrese su contraseña: ")
acceso_ok = contraseña == "python123"
print(f"ingreso permitido: {acceso_ok}")
print(f"acceso denegado" * (not acceso_ok), end="")

# ---------------- TU SOLUCIÓN ACÁ --------:--------
# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# clave = input('Ingresá la contraseña: ')
# acceso_ok = clave == 'python123'
# print(f'¿Acceso OK?: {acceso_ok}')
#
# =====================================================================
