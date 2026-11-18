# =====================================================================
# EJERCICIO #25  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí stock (int) y precio (float). Guardá en 'disponible' True si
# stock > 0 y precio <= 1000.
#
# QUE SE BUSCA ENTRENAR:
# Combinar int y float con 'and'.
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
stock_p = int(input("ingrese la cantidad que hay en stock: "))
precio_p = float(input("ingrese el precio del producto: "))
disponible = (stock_p > 0) and (precio_p <= 1000)
print(f"El producto esta disponible: {disponible}")
print("El NO producto esta disponible" * ( not disponible), end="")

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# stock = int(input('Stock: '))
# precio = float(input('Precio: '))
# disponible = (stock > 0) and (precio <= 1000)
# print(f'¿Está disponible?: {disponible}')
#
# =====================================================================
