# ============================================================
# Ejercicio 33: Cuadrado N x N
# Categoría: 07_patrones
# ============================================================
#
# ENUNCIADO:
# Imprimí un cuadrado de asteriscos de N filas y N columnas.
#

filas = int(input("ingresa el numero de filas y columnas para construir un cuadrado: "))

i = 1
while i <= filas:
    asteriscos = ""
    j = 1
    while j <= filas:
        asteriscos += "*" 
        j += 1
    print(asteriscos)
    i += 1
    
#--------------------------------------------
print("-" * 50)
#--------------------------------------------
    
# ============================================================
# Ejercicio 33-a: Rectangulo N x N
# Categoría: 07_patrones
# ============================================================
#
# ENUNCIADO:
# Imprimí un rectangulo de asteriscos de 4 filas y 8 columnas.

#El input() puede quedar fijo por ahora (filas = 4, columnas = 8), 
# o podés pedir ambos al usuario con dos input() separados.

filas = 4
columnas = 8   

i = 1
while i <= 4:   
    asteriscos = ""
    j = 1
    while j <= 8:
        asteriscos += "*"
        j += 1
    print(asteriscos)
    i += 1