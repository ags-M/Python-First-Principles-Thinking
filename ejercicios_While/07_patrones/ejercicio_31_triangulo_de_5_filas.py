# ============================================================
# Ejercicio 31: Triángulo de 5 filas
# Categoría: 07_patrones
# ============================================================
#
# ENUNCIADO:
# Imprimí un triángulo rectángulo de 5 filas con asteriscos:
#____________________________________________________________
# --- Triángulo rectángulo de 5 filas con while ---
"""
🧒 Explicación:

Hay que construir una escalera de ladrillos (los ladrillos son *)

La fila 1 tiene 1 ladrillo.
La fila 2 tiene 2 ladrillos.
La fila 3 tiene 3 ladrillos… y así hasta la 5.

Necesitás dos cabezas pensando al mismo tiempo:

Una cabeza dice: "¿en qué fila voy?" (el while de afuera).

La otra cabeza dice: "¿cuántos ladrillos pongo en esta fila?" (el while de adentro).

Cada vez que terminás una fila, bajás al siguiente escalón y repetís.

"""
# --- Triángulo rectángulo de 5 filas con while ---

filas = 5          # total de filas que queremos dibujar
i = 1              # 'i' es el número de fila actual (arranca en 1)
 
while i <= filas:              # MIENTRAS no hayamos pasado la fila 5... SON LAS FILAS
    asteriscos = ""            # ...empezamos cada fila con una cadena vacía
    j = 1                      # 'j' cuenta los asteriscos de ESTA fila, arranca con 1 asterisco SON LAS COLUMNAS
    while j <= i:              # en la fila 'i' queremos exactamente 'i' asteriscos
        asteriscos += "*"      # agregamos un asterisco a la cadena
        j += 1                 # avanzamos el contador interno
    print(asteriscos)          # terminamos la fila → la imprimimos completa
    i += 1                     # y pasamos a la siguiente fila
#____________________________________________________________________________________________

#📊 Traceo manual
#____________________________________________________________________________________________

# iteracion     valor del contador al entrar   **se cumple i <= filas    j <= i bucle interno
#                                                   bucle externo        se imprimen asteriscos
#                                                                           j += 1
#____________________________________________________________________________________________
#valor inicial del contador filas i: 1
#____________________________________________________________________________________________
#     1                      1                       si                         *
#     2                      2                       si                         **
#     3                      3                       si                         ***
#     4                      4                       si                         ****
#     5                      5                       si                         *****
#     6                                       no **: sale del bucle        no imprime nada
#____________________________________________________________________________________________ 

#--------------------------------------------
print("-" * 50)
#--------------------------------------------

# hacer un triangulo rectangulo de 5 filas de mayor a menor

filas = 5
i = 1

while i <= filas :
    asteriscos = ""
    j = 5
    while j >= i:
        asteriscos +="*"
        j -= 1
    print(asteriscos)
    i += 1
    
    
