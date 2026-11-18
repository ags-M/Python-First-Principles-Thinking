# ============================================================
# Ejercicio 7: Suma de pares hasta N
# Categoría: 02_acumuladores
# ============================================================
#
# ENUNCIADO:
# Pedile al usuario un número N y sumá solo los números pares entre 1 y N.

n = int(input("ingrese un numero: "))
suma = 0
contador = 2
while contador <= n:
    suma = suma + contador
    contador += 2
print(f"La suma de los numeros pares del 1 al {n} es: {suma}")

#____________________________________________________________________________________________

# iteracion     valor del contador al entrar   **contador <= 5             que imprime
#                                               cumple <= 5 ejemplo n= 5
#____________________________________________________________________________________________

#valor inicial del contador es igual a: 2                                  suma + contador = 6
#____________________________________________________________________________________________
#     1                      2                       si                         2
#     2                      4                       si                         6
#     3                      6                no **: sale del bucle        no imprime nada
#                                             no cumple 6 <= 5
#____________________________________________________________________________________________