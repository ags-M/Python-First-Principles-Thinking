# ============================================================
#  PLANTILLA FOR #3 - CON CONDICIÓN (if/else adentro) | NOVA 🤖
#  Curso Python - Módulo 1 - Lección 5
# ============================================================
# USO: cuando en algunas iteraciones querés hacer una cosa,
# y en otras querés hacer otra cosa distinta.
# EJEMPLOS: filtrar números, clasificar pares/impares,
#           reemplazar valores, patrones mixtos.
# ============================================================

# ----------------------------------------------------------------
# CASO A: Filtrar números (mostrar solo los que cumplen condición)
# ----------------------------------------------------------------
for i in range(1, 21):
    if i % 2 == 0:                         # ← tu condición
        print(i, "es par")


# ----------------------------------------------------------------
# CASO B: Dos comportamientos distintos (if/else)
# ----------------------------------------------------------------
numeros = [5, 12, 8, 20, 3, 15, 7, 25]

for n in numeros:
    if n > 10:                             # ← tu condición
        print(n, "es mayor a 10")
    else:
        print(n, "es menor o igual a 10")


# ----------------------------------------------------------------
# CASO C: Clasificar en categorías (if/elif/else)
# ----------------------------------------------------------------
for n in range(1, 31):
    if n % 3 == 0 and n % 5 == 0:          # ← condición más específica PRIMERO
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)


# ----------------------------------------------------------------
# CASO D: Contar cuántos cumplen una condición
# ----------------------------------------------------------------
frase = "Hola Alejandro, ¿cómo estás?"
contador_vocales = 0

for letra in frase:
    if letra.lower() in "aeiou":           # ← condición
        contador_vocales += 1

print("Cantidad de vocales:", contador_vocales)


# ----------------------------------------------------------------
# CASO E: Construir una nueva lista filtrada
# ----------------------------------------------------------------
numeros = [-5, 3, -1, 0, 8, -10, 15, 4]
positivos = []

for n in numeros:
    if n > 0:                              # ← condición de filtro
        positivos.append(n)

print("Solo positivos:", positivos)


# ============================================================
# TU PRÁCTICA ACÁ 👇
# ============================================================
# Ejercicio: usá esta plantilla para separar una lista en
# dos listas: una con pares y otra con impares