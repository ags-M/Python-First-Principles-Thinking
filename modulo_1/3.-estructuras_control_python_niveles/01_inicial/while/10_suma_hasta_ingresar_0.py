"""
==========================================================================
Ejercicio 10: Suma hasta ingresar 0
==========================================================================

ENUNCIADO
---------
Pedile al usuario números uno por uno hasta que ingrese 0. Mostrá la suma acumulada (sin incluir el 0).

PISTA (leela solo si te trabás)
-------------------------------
Mientras el número no sea 0, sumá y volvé a pedir.

"""
suma = 0  # Acumulador: arranca en 0 porque vamos sumando

numero = int(input("Ingresá un número (0 para terminar): "))

while numero != 0:
    suma = suma + numero   # Acumulamos el número ingresado
    numero = int(input("Ingresá otro número (0 para terminar): "))

print(f"La suma acumulada es: {suma}")