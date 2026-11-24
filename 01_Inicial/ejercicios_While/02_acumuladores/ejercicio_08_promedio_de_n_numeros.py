# ============================================================
# Ejercicio 8: Promedio de N números
# Categoría: 02_acumuladores
# ============================================================
#
# ENUNCIADO:
# Pedile al usuario cuántos números va a ingresar. Luego leés esa cantidad de números y calculás el promedio.

cantidad = int(input("ingrese un numero como cantidad para realizar un promedio: "))
suma = 0
contador = 0 # El 🔄 contador es una variable que usamos para llevar la cuenta 
             # de cuántos números ha ingresado el usuario hasta el momento. Lo inicializamos en 0 porque, 
             # antes de que empiece el bucle while, el usuario todavía no ha ingresado ningún número. 
             # El conteo empieza desde cero.
while contador < cantidad:
    numero = int(input("ingresa un numero: "))
    suma = suma + numero # aca esta la alcancia
    contador += 1 # aca esta el 🔄
promedio = suma / cantidad
print(f"El promedio de los numeros ingresados es: {round(promedio, 2)}")


"""
#____________________________________________________________________________________________
# iteracion     valor del contador al entrar   **contador < cantidad            que imprime
#                                          cumple cantidad < 5 ejemplo n= 5
#____________________________________________________________________________________________
#valor inicial del contador es igual a: 0          
#____________________________________________________________________________________________
#     1                      0              contador 0 < cantidad 5                1
#     2                      1              contador 1 < cantidad 5                2
#     3                      2              contador 2 < cantidad 5                3
#     4                      3              contador 3 < cantidad 5                4
#     5                      4              contador 4 < cantidad 5                5
#     6                      5               no **: sale del bucle             no imprime nada 
#                                            no cumple 5 < 5
#____________________________________________________________________________________________

Este ejercicio tiene niveles de interaccion por un lado la cantidad como numero para realizar
el promedio de la suma de los numeros ingresados, y ademas los numeros ingresados son igual a la 
misma cantidad de veces que señala la cantidad. Por eso el contador es menor que la cantidad de
dado que empieza por el cero y como se ve en el traceo, por que el contador se le dio el valor de cero
(no habia un numero de contador antes de la pregunta).
Como el bucle incluye el ingreso de los numeros y ademas la suma de los numeros que se iteran igual 
a lo que el contador tiene, es decir contador < cantidad , se realizan los ingresos y resulta al final
de las vueltas suma y division = a promedio. 

"""
#--------------------------------------------
print("-" * 30)
#--------------------------------------------

# VALIDACION DEL BUCLE, ES EL MISMO EJERCICIO PERO ACA SI EL USUARIO NO AGREGA EL NUMERO 
#EN EL BUCLE SE LO HACE CONOCER Y VUELVE A PEDIR EL NUMERO:

cantidad = int(input("ingrese un numero como cantidad para realizar un promedio: "))
suma = 0
contador = 0

while contador < cantidad:
    entrada = input("ingresa un numero: ")
    if entrada == "":  # Si presionó Enter sin escribir nada
        print("no agregaste todos los numeros")
        continue  # Vuelve al inicio del while sin sumar ni incrementar
    
    numero = int(entrada)  # Recién acá convertimos a número
    suma = suma + numero
    contador += 1

promedio = suma / cantidad
print(f"El promedio es {round(promedio, 2)}")