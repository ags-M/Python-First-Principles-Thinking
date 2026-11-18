# LECCIÓN 5 - BUCLE WHILE | PRINCIPIANTE | Ejercicio 13
# =========================================================
# CONSIGNA: El programa tiene un número secreto = 7. Pedile al usuario
# que adivine mientras no acierte. Al final mostrá "¡Ganaste!"
# =========================================================

secreto = 7
n = int(input("Ingresa y adivina un numero secreto: "))

while n != secreto:
    print("No es valido, intenta de nuevo")
    n = int(input("Ingresa y adivina un numero secreto: "))

print("¡Ganaste!")
