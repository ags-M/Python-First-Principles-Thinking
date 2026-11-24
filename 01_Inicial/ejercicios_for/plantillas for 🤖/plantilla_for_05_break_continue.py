# ============================================================
#  PLANTILLA FOR #5 - BREAK Y CONTINUE | NOVA 🤖
#  Curso Python - Módulo 1 - Lección 5
# ============================================================
# USO: cuando necesitás CONTROLAR el flujo del bucle:
#   - break:    SALIR del bucle antes de tiempo
#   - continue: SALTAR a la siguiente iteración
# EJEMPLOS: buscar algo y parar, validar contraseñas,
#           filtrar elementos sin romper el bucle.
# ============================================================

# ----------------------------------------------------------------
# CASO A: BREAK - Buscar un elemento y detenerse al encontrarlo
# ----------------------------------------------------------------
numeros = [4, 7, 2, 9, 15, 23, 8, 42, 5]
buscar = 23

for n in numeros:
    if n == buscar:
        print(f"¡Encontré el {buscar}!")
        break                              # ← SALGO del bucle
    print(f"Revisando {n}... no es")


# ----------------------------------------------------------------
# CASO B: BREAK con máximo de intentos (contraseñas)
# ----------------------------------------------------------------
for intento in range(1, 4):                # ← máximo 3 intentos
    clave = input(f"Intento {intento} - Ingresá la contraseña: ")
    if clave == "python123":
        print("✅ ¡Acceso concedido!")
        break                              # ← salgo si acertó
    print("❌ Contraseña incorrecta")
else:
    # Este else se ejecuta si el for termina SIN hacer break
    print("🔒 Cuenta bloqueada")


# ----------------------------------------------------------------
# CASO C: CONTINUE - Saltar iteraciones específicas
# ----------------------------------------------------------------
for i in range(1, 21):
    if i % 3 == 0:
        continue                           # ← salta a la siguiente iteración
    print(i)                               # ← solo se ejecuta si NO es múltiplo de 3


# ----------------------------------------------------------------
# CASO D: BREAK - Detenerse al encontrar una condición
# ----------------------------------------------------------------
for i in range(1, 101):
    if i > 50 and i % 7 == 0:              # ← primer múltiplo de 7 mayor a 50
        print(f"Encontré: {i}")
        break
    print(i)


# ----------------------------------------------------------------
# CASO E: Combinación BREAK + CONTINUE (cajero)
# ----------------------------------------------------------------
saldo = 1000

for _ in range(10):                        # ← máximo 10 operaciones
    monto = int(input("Monto a extraer (0 para salir): "))
    
    if monto == 0:
        print("Saliendo del cajero...")
        break                              # ← salir
    
    if monto > saldo:
        print("Saldo insuficiente")
        continue                           # ← saltar a la siguiente operación
    
    saldo -= monto
    print(f"Retiraste {monto}. Saldo restante: {saldo}")


# ----------------------------------------------------------------
# CASO F: Eliminar duplicados con for + lista nueva
# ----------------------------------------------------------------
numeros = [1, 2, 3, 2, 5, 1, 6, 3, 7, 5]
sin_duplicados = []

for n in numeros:
    if n not in sin_duplicados:            # ← si NO está ya en la lista nueva
        sin_duplicados.append(n)

print("Sin duplicados:", sin_duplicados)


# ============================================================
# TU PRÁCTICA ACÁ 👇
# ============================================================
# Ejercicio: usá esta plantilla para hacer el clásico FizzBuzz
# del 1 al 30 (múltiplos de 3 → "fizz", de 5 → "buzz",
# de ambos → "fizzbuzz")