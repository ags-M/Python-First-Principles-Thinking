# =====================================================================
# EJERCICIO #09  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí edad y género ('m' o 'f'). Un hombre se jubila a los 65,
# una mujer a los 60. Guardá en 'puede_jubilarse' True si le toca.
#
# QUE SE BUSCA ENTRENAR:
# Combinar comparación con 'and' y dos caminos.
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
edad = int(input("ingrese su edad: "))
genero = input("ingrese su genero (masculino/femenino): ")
puede_jubilarse= edad >= 65 and genero == "m" or (edad >= 60 and genero == "f")
print(f"Con {edad} años y genero {genero} PUEDE jubilarse: {puede_jubilarse}")
print("NO puede jubilarse" * (not puede_jubilarse))
"""
Los booleanos se pueden tomar un valor como 1 (True) o 0 (False). Y un string multiplicado por un número se repite:

| `puede_jubilarse`                      | `False` = `0` (no cumple) |

| `not puede_jubilarse`                  | `True` = `1` |

"NO puede jubilarse" * (not puede_jubilarse)` | `"NO puede jubilarse" * 1` |

| Resultado | `"NO puede jubilarse"` (el texto, una sola vez) | ya que el string multiplicado por 1 se repite
no pasa lo mismo si se multiplica por cero, ahi puede jubilarse
"""

# ---------------- TU SOLUCIÓN ACÁ ----------------

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# edad = int(input('Edad: '))
# genero = input('Género (m/f): ').lower()
# puede_jubilarse = (edad >= 65 and genero == 'm') or (edad >= 60 and genero == 'f')
# print(f'¿Puede jubilarse?: {puede_jubilarse}')
#
# =====================================================================
