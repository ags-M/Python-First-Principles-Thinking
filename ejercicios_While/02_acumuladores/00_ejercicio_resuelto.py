#CONSIGNA : Sumar los números del 1 al N, donde N lo ingresa el usuario.

# Pido el número al usuario. int() convierte el texto a número entero.
n = int(input("Ingresá un número: "))

# La suma empieza en 0. Esto se llama ACUMULADOR: va juntando valores.
# ¿Por qué 0? Porque 0 es el "neutro" de la suma: no altera el resultado.
suma = 0

# El contador empieza en 1 porque queremos sumar desde 1 hasta n.
contador = 1

while contador <= n:
    suma = suma + contador   # Acumulo el valor actual en la suma
    contador = contador + 1  # Avanzo al siguiente número

print(f"La suma de 1 a {n} es: {suma}")

#____________________________________________________________________________________________

# iteracion     valor del contador al entrar     ** se cumple <= n            que imprime
#                                                    #contador <= n ejemplo n=5
#__________________________________________________________________________________________________
#valor inicial del contador es igual a: 1
#____________________________________________________________________________________________
#     1                      1                       si                         1
#     2                      2                       si                         2
#     3                      3                       si                         3
#     4                      4                       si                         4
#     5                      5                       si                        15
#     6                      6                no **: sale del bucle        no imprime nada
#                                             no cumple 6 <=5
#____________________________________________________________________________________________