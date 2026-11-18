# =====================================================================
# EJERCICIO #04  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí la edad y guardá en 'es_mayor' True si tiene 18 o más.
#
# QUE SE BUSCA ENTRENAR:
# Practicar >= y el concepto de mayoría de edad.
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
edad = int(input("Ingresa tu edad: "))
edad_mayor = edad >= 18
print(f"Tu edad es de una persona mayor: {edad_mayor}")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# edad = int(input('Ingresá tu edad: '))
# es_mayor = edad >= 18
# print(f'¿Es mayor de edad?: {es_mayor}')
#
# =====================================================================
