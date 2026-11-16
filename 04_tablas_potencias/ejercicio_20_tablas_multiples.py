# ============================================================
# Ejercicio 20: Tablas múltiples
# Categoría: 04_tablas_potencias
# ============================================================
#
# ENUNCIADO:
# Mostrá las tablas de multiplicar del 1 al 5, cada una del 1 al 10.

#tabla de multiplicar /// 1 n = 1 /// contador = 10
#tabla de multiplicar /// 2 n = 2 /// contador = 10
#tabla de multiplicar /// 3 n = 3 /// contador = 10
#tabla de multiplicar /// 4 n = 4 /// contador = 10
#tabla de multiplicar /// 5 n = 5 /// contador = 10

#primero contar las tablas del 1 al 5 -cinco es el límite
#segundo realizar las tablas de cada una multiplicadas del 1 al 10
"""
tabla_actual = 1 # seria el contador
while tabla_actual <= 5:
      print(tabla_actual) # la salida es 1 al 5
      tabla_actual += 1

#despues veo cada una las tablas del 1 al 5 multiplicadas del 1 al 10, van a se while anidadas

multiplicador = 1 # seria el contador
while multiplicador <= 10:
      print(tabla_actual * multiplicador)
      multiplicador += 1

Tengo los dos bucles:

Externo: while tabla_actual <= 5: (recorre las tablas del 1 al 5)
Interno: while multiplicador <= 10: (recorre los multiplicadores del 1 al 10)

"""
tabla_actual = 1
while tabla_actual <= 5:
    print(f"\nTabla del {tabla_actual}")  # ← Primero anunciás
    multiplicador = 1                     # ← Después preparás
    while multiplicador <= 10:            # ← Finalmente ejecutás
        print(f"{tabla_actual} x {multiplicador} = {tabla_actual * multiplicador}")
        multiplicador += 1
    tabla_actual += 1