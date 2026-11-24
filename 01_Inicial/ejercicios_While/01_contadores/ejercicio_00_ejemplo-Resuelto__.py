# Contar del 1 al 5, mostrando cada número en una línea.

#creo la variable que va a "contar". Empieza en 1 porque es donde quiero arrancar a contar.
contador = 1
#La condición dice "mientras el contador sea menor o igual a 5, segui"
#El <= es clave: si pusiera solo <, se detendria en 4 y no tomaria a 5
while contador <= 5:
    print(contador)
    #actualizo al contador. Si no realizo esto, el bucle nunca termina (bucle al infinito)
    contador = contador + 1 #aca muestra como asciende de a 1 en cada vuelta
print("Terminé de contar.") 
#______________________________________________________________________________________
# iteracion     valor del contador al entrar     se cumple <= 5            que imprime
# el valor del contador es de 1 
#_____________________________________________________________________________________
#     1                      1                       si                         1
#     2                      2                       si                         2
#     3                      3                       si                         3
#     4                      4                       si                         4
#     5                      5                       si                         5
#     6                      6                no -> sale del bucle        no imprime nada
#_______________________________________________________________________________________