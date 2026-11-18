"""
==========================================================================
Ejercicio 03: Tabla de multiplicar
==========================================================================

ENUNCIADO
---------
Pedile al usuario un entero N. Imprimí su tabla de multiplicar del 1 al 10 usando for.

PISTA (leela solo si te trabás)
-------------------------------
`for i in range(1, 11)`.

"""
n = int(input("Ingresá un número entero: "))

for i in range(1, 11):
    resultado = (n * i) 
    print(f"{n} x {i} = {resultado}")

#----------------------------------------------
print("-"*12)
#_---------------------------------------------


n = int(input("Ingresá un número entero: "))
suma = 0
for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")
    suma += resultado
print(f"La suma de todos los resultados es: {suma}")
