# LECCIÓN 5 - BUCLE WHILE | PRINCIPIANTE | Ejercicio 19
# =========================================================
# CONSIGNA: Pedile al usuario un número N y calculá su factorial (N!).
# Ejemplo: 5! = 5*4*3*2*1 = 120
# =========================================================

# PASO 1: Pedir el número con validación
n = int(input("Ingresá un número entero positivo: "))

while n < 0: # MIENTRAS sea negativo
    print("Error: el número debe ser positivo o cero.")
    n = int(input("Ingresá un número entero positivo: "))

# PASO 2: Calcular el factorial
resultado = 1
contador = n

while contador > 1:
    resultado = resultado * contador
    contador = contador - 1

# PASO 3: Mostrar resultado
print(f"El factorial de {n} es: {resultado}")
