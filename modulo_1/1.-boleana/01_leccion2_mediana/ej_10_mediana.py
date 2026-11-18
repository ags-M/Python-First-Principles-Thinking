# =====================================================================
# EJERCICIO #10  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí una contraseña y guardá en 'es_segura' si tiene 8 o más caracteres.
#
# QUE SE BUSCA ENTRENAR:
# Comparación >= con un caso de seguridad.
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

contraseña= input("ingresa una contraseña con 8 o mas caracteres alfa numericos: ")
long= len(contraseña)
es_segura = long >= 8
print(f"La contraseña que elegiste es segura?: {es_segura}")
print(f"No es segura" * (not es_segura), end ="") #este end hace que no haya una linea vacia al terminar el codigo






# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
#
#
# =====================================================================
