# =====================================================================
# EJERCICIO #24  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
# CONSIGNA UN USUARIO ESTA ACTIVO O PASIVO, DEBE SER VERIFICADO, SI CUMPLE 
# CON ACTIVO Y VERIFICADO ES TRUE CONFIABLE

estado_usuario = input("ingrese su estado (activo/pasivo): ").lower() == "activo"
verificado = input("se ha verificado (s/n): ").lower() == "s"
confiable = estado_usuario and verificado
print(f"el usuario es confiable: {confiable}")
print(f"el usuario no es confiable" * (not confiable))

# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# estado = input('Estado (activo/inactivo): ').lower()
# verificado = input('¿Verificado? (s/n): ').lower() == 's'
# confiable = (estado == 'activo') and verificado
# print(f'¿Es confiable?: {confiable}')
#
# =====================================================================


