# LECCIÓN 5 - BUCLE WHILE | PRINCIPIANTE | Ejercicio 7
# =========================================================
# CONSIGNA: Pedile al usuario un número y mostrá su tabla de multiplicar
# del 1 al 10 con el formato: "5 x 1 = 5", "5 x 2 = 10", ...
# =========================================================

n = int(input("Ingresá un número para ver su tabla: "))
i = 1
while i <= 10:
    resultado = n * i
    print(f" {n} * {i} = {resultado}")
    i +=1

#--------------------------------------
print("-"*12)
#--------------------------------------

n = int(input("Ingresá un número para ver su tabla: "))
i = 1
while i <= 10:
    print(f" {n} * {i} = {n * i}")   # ← hacé la cuenta acá
    i += 1

