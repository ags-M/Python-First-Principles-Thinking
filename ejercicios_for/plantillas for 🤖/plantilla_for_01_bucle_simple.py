# ============================================================
#  PLANTILLA FOR #1 - BUCLE SIMPLE | NOVA 🤖
#  Curso Python - Módulo 1 - Lección 5
# ============================================================
# USO: cuando tenés que repetir algo N veces, una sola dimensión.
# EJEMPLOS: contar, sumar una secuencia, imprimir números,
#           tablas de multiplicar, factoriales.
# ============================================================
# VENTAJA vs WHILE: no necesitás inicializar ni incrementar
# el contador manualmente. range() lo hace por vos.
# ============================================================

# ----------------------------------------------------------------
# CASO A: Contar del 1 al N (inclusive)
# ----------------------------------------------------------------
N = int(input("Ingresa un número: "))

for i in range(1, N + 1):      # ← range(inicio, fin+1)
    print(i)                   # ← reemplazá por lo que quieras hacer


# ----------------------------------------------------------------
# CASO B: Contar con pasos (pares, impares, múltiplos)
# ----------------------------------------------------------------
# Pares del 2 al 20:
for i in range(2, 21, 2):      # ← range(inicio, fin+1, paso)
    print(i)

# Impares del 1 al 19:
for i in range(1, 20, 2):
    print(i)

# Múltiplos de 5 del 5 al 50:
for i in range(5, 51, 5):
    print(i)


# ----------------------------------------------------------------
# CASO C: Cuenta regresiva
# ----------------------------------------------------------------
for i in range(10, 0, -1):     # ← range(inicio, fin-1, paso_negativo)
    print(i)


# ----------------------------------------------------------------
# CASO D: Acumulador (sumar o multiplicar una secuencia)
# ----------------------------------------------------------------
suma = 0
for i in range(1, 101):
    suma += i                  # ← acumulador
print("La suma del 1 al 100 es:", suma)

producto = 1
for i in range(1, 6):
    producto *= i              # ← factorial de 5
print("El factorial de 5 es:", producto)


# ============================================================
# TU PRÁCTICA ACÁ 👇
# ============================================================
# Ejercicio: usá esta plantilla para imprimir la tabla del 7
# (7x1, 7x2, ... 7x10)