# ============================================================
# Ejercicio 18: Factorial
# Categoría: 04_tablas_potencias
# ============================================================
#
# ENUNCIADO:
# Calculá el factorial de un número N (N! = N * (N-1) * ... * 1).

N = int(input("Vamos a calcular un factorial ingresa un numero entero N: "))
#factorial es N ! Si N = 3 entonces 3 x 2 x 1 = factorial 6
# variable para acumular la multiplicacion seria factorial = 1 y el contador seria multiplicador = 1
#while multiplicador <= N 
multiplicador = 1 # contador
factorial = 1 # el que acumula 
while multiplicador <= N:
    factorial = factorial * multiplicador
    print(f"{multiplicador}! = {factorial}")
    multiplicador +=1
print(f"El factorial del numero {N} es: {factorial}")

#📊 Traceo manual
#_________________________________________________________________________________________________________________

# iteracion     valor del contador al entrar  **se multiplicador <= N                   que imprime
                                                  # N = 3                 # factorial = factorial * multiplicador
#_________________________________________________________________________________________________________________
#valor inicial del contador es igual a:
#_________________________________________________________________________________________________________________

#     1                      1                       si  1 <= 3                           1  *  1 = 1 imprime
#     2                      2                       si  2 <= 3                           1  *  2 = 2 imprime
#     3                      3                       si  3 <= 3                           2  *  3 = 6 imprime
#     4                      4                       NO  4 <= 3                   
#                                                no **: sale del bucle        no imprime nada
#_________________________________________________________________________________________________________________

