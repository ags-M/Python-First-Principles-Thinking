"""
🟡 ANALISIS PARA COMPRENDER COMO UN N es primo:

🐍 primero deberia saber si el n que introdujo el usuario es primo = ej 10 ?, 

🐍 segundo saber si los numeros del 2 al 10 algunos son o no primos 

🐍y tercero decir cuales son? si?
"""
n_limite = int(input("ingresa un numero: "))

divisor = 2
while divisor < n_limite:
    if n_limite % divisor == 0: # Si el número es divisible por otro (el residuo es 0), significa que NO es primo.
       print(f"el numero {n_limite} NO es un numero primo")
       break
    divisor += 1
else:
    print(f"el numero {n_limite} ES un numero primo")

"""
¿Por qué funciona?
Si encuentra divisor → imprime "no es primo" → hace break → el else NO se ejecuta
Si NO encuentra divisor → el bucle termina normalmente → el else SÍ se ejecuta → imprime "es primo"

"""
n_limite = int(input("ingresa un numero: "))
divisor = 2
flag = True # flag = True → "asumo que es primo"
while divisor < n_limite:
    if n_limite % divisor == 0: # Si el número es divisible por otro (el residuo es 0 !!!), significa que NO es primo.
       flag = False # flag = False → "significa que encontre un numero que no es primo"
    divisor += 1 #el divisor += 1 esta fuera del if por eso no esta identado

if flag:# el if flag esta fuera del while por eso NO esta identado, es decir adento de él, solo alineado 
        # ( me hace recordar al salmo 91, el que habita a la sombra del omnipotente ESTA IDENTADO!!! y aca no!! JAJAJA)
    print(f"el numero {n_limite} ES un numero primo")
else: 
    print(f"el numero {n_limite} NO es un numero primo")
     # ¿Por qué? Si el bucle termina y flag sigue siendo True → significa que no se encontró ningún divisor → es primo
               # Si flag es False → en else se imprime "NO es un numero primo"

#____________________________________________________________________________________________
#📊 Traceo manual
#____________________________________________________________________________________________

# iteracion     valor del contador al entrar  **se cumple divisor < n_limite      que imprime
#                                                     n_limite = 7
#____________________________________________________________________________________________
#valor inicial del contador divisor es igual = 2
#____________________________________________________________________________________________

#     1                      2                    si  2 < 7                     
#     2                      3                    si  3 < 7                           -
#     3                      4                    si  4 < 7                           -
#     4                      5                    si  5 < 7                           - 
#     5                      6                    si  6 < 7                           -
#     6                      7                    NO  7 < 7# 
#                                           no **: sale del bucle        imprime ES un numero primo
#____________________________________________________________________________________________