# ============================================================
# Ejercicio 19: Primeras N potencias de 2
# Categoría: 04_tablas_potencias
# ============================================================
#
# ENUNCIADO:
# Mostrá las primeras N potencias de 2: 1, 2, 4, 8, 16, ...
"""
mostrar las primeras N potencias si elijo N= 4 es igual a 1, 2, 4, 8 seria mostrar 
2 a la 0 = 1
2 a la 1 = 2
2 a la 2 = 4
2 a la 3 = 8
contador = 0
base = 2
---------------------------------------------
entonces el contador va a ser igual al exponente 0, 1, 2, 3 todo en base 2
contador = 0
---------------------------------------------
while necesita la condicion y aca N = 4 si el contador empieza con 0, entonces la condicion
es while contador < 4 para no pasarse en el bucle , ya que dara 4 vueltas
---------------------------------------------
"""
N = int(input("Ingresa la cantidad de potencias N de base 2: "))
base = 2
contador = 0 #el contador es igual al exponente
print(f"Estas fueron las primeras {N} potencias de 2.")

while contador < 4:
    resultado = base ** contador
    print(resultado)
    contador += 1

#--------------------------------------------
print("-" * 30)
#--------------------------------------------

N = int(input("Ingresa la cantidad de potencias N de base 2: "))
base = 2
contador = 0
potencia = 1 

while contador < N:
    print(potencia)
    potencia = potencia * 2 
    contador += 1

print(f"Esas fueron las primeras {N} potencias de 2.")


#____________________________________________________________________________________________

#📊 Traceo manual
#____________________________________________________________________________________________

# iteracion     valor del contador al entrar   **se contador < 4           que imprime
#____________________________________________________________________________________________
#valor inicial del contador es igual a: 0 //                       resultado = base ** contador (exponente)
#____________________________________________________________________________________________

#     1                      0                       si                         2 ** 0 = 1
#     2                      1                       si                         2 ** 1 = 2
#     3                      2                       si                         2 ** 2 = 4
#     4                      3                       si                         2 ** 3 = 8
#     5                      4                      4 < 4 **
                                             # no **: sale del bucle        no imprime nada
#____________________________________________________________________________________________

