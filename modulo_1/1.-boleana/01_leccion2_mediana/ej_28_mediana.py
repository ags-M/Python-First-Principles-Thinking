# =====================================================================
# EJERCICIO #28  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí edad y si es jubilado (s/n). Guardá en 'adulto_activo' True
# si edad >= 18 y NO es jubilado.
#
# QUE SE BUSCA ENTRENAR:
# Practicar 'and' + 'not' con input s/n.
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
jubilado = input("Esta ud jubilado (s/n): ").lower() == "s"
adulto_activo = (edad >= 18) and (not jubilado)
print(f"Ud forma parte de la P.E.A.: {adulto_activo}")
print(f"No esta en la P.E.A." * (jubilado))

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# edad = int(input('Edad: '))
# es_jubilado = input('¿Sos jubilado? (s/n): ').lower() == 's'
# adulto_activo = (edad >= 18) and (not es_jubilado)
# print(f'¿Sos adulto activo?: {adulto_activo}')
#
# =====================================================================
