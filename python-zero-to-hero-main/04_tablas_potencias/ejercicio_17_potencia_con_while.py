# ============================================================
# Ejercicio 17: Potencia con while
# Categoría: 04_tablas_potencias
# ============================================================
#
# ENUNCIADO:
# Calculá base^exponente usando solo while (sin usar **). Pedile ambos números al usuario.
base = int(input("ingresa la base con un numero entero:  "))
exponente = int(input("ingresa un exponente con un numero entero:  "))
contador = 1
potencia = 1

# base = 3  y exponente = 2 esto implica potencia = base * base

while exponente >= contador:
    potencia = potencia * base
    contador += 1
print(f" El numero: {base} elevado a la {exponente} es igual a {potencia}")

#___________________________________________________________________________________________

#📊 Traceo manual: base = 2 exponente 3  /// contador = 1 /// potencia = 1
#____________________________________________________________________________________________

# iteracion         valor del contador      **se exponente >= contador       que imprime
                       # al entrar                                        potencia * base
#____________________________________________________________________________________________
#     1                      1                  si  3 >= 1                   1 * 2 = 2
#____________________________________________________________________________________________

#     2                      2                  si  3 >= 2                   2 * 2 = 4
#____________________________________________________________________________________________

#     3                      3                  si  3 >= 3                   4 * 2 = 8
#____________________________________________________________________________________________
#     4                      4                  no 4 >=  3                      
                                             # sale del bucle            # no imprime nada
#____________________________________________________________________________________________

