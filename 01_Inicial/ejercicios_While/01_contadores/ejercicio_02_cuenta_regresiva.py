# ============================================================
# Ejercicio 2: Cuenta regresiva
# Categoría: 01_contadores
# ============================================================
#
# ENUNCIADO:
# Mostrá los números del 10 al 1 usando while. Al final imprimí '¡Despegue!'
#
contador = 10 # inicio
while contador >= 1: #condicion
    print(contador) # cuerpo: que es lo que hará imprimiendo la salida del traceo
    contador -= 1 # actualizo ACA se ve que le resta a 10 el valor de 1 en cada vuelta
print("Despegue!") # imprimo el final

#__________________________________________________________________________________________

# iteracion     valor del contador al entrar     ** se cumple >= 1            que imprime
                                                    #contador >= 1
#_________________________________________________________________________________________

#el valor del contador es de 10
#__________________________________________________________________________________________
#      1                    10                       si                        10
#      2                     9                       si                         9
#      3                     8                       si                         8
#      4                     7                       si                         7
#      5                     6                       si                         6
#      6                     5                       si                         5
#      7                     4                       si                         4
#      8                     3                       si                         3 
#      9                     2                       si                         2
#      10                    1                       si                         1
#      11                    0                no **: sale del bucle        no imprime nada
#                                               no cumple 0 >= 1
#___________________________________________________________________________________________

