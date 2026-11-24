# ============================================================
#  PLANTILLA FOR #4 - RECORRER UNA COLECCIÓN | NOVA 🤖
#  Curso Python - Módulo 1 - Lección 5
# ============================================================
# USO: cuando tenés una lista, tupla o string y querés
# procesar cada elemento uno por uno.
# EJEMPLOS: mostrar frutas, buscar un nombre, calcular
#           promedios, transformar textos.
# ============================================================
# VENTAJA: no necesitás índices. Python te da el elemento directo.
# ============================================================

# ----------------------------------------------------------------
# CASO A: Recorrer una lista simple
# ----------------------------------------------------------------
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:                       # ← "fruta" es cada elemento
    print(fruta)


# ----------------------------------------------------------------
# CASO B: Recorrer un string (cada letra)
# ----------------------------------------------------------------
palabra = "python"

for letra in palabra:
    print(letra.upper())                   # ← cada letra en mayúscula


# ----------------------------------------------------------------
# CASO C: Recorrer una tupla
# ----------------------------------------------------------------
meses_31 = ("Enero", "Marzo", "Mayo", "Julio", "Agosto", "Octubre", "Diciembre")

for mes in meses_31:
    print(f"El mes de {mes} tiene 31 días")


# ----------------------------------------------------------------
# CASO D: Necesitás el índice Y el elemento → enumerate()
# ----------------------------------------------------------------
nombres = ["Ana", "Bruno", "Alejandro", "Carla"]

for i, nombre in enumerate(nombres):       # ← i = índice, nombre = elemento
    print(f"Posición {i}: {nombre}")


# ----------------------------------------------------------------
# CASO E: Calcular promedio de una lista
# ----------------------------------------------------------------
numeros = [10, 20, 30, 40, 50]
suma = 0

for n in numeros:
    suma += n

promedio = suma / len(numeros)
print("El promedio es:", promedio)


# ----------------------------------------------------------------
# CASO F: Encontrar el mayor SIN usar max()
# ----------------------------------------------------------------
numeros = [23, 45, 12, 67, 34, 89, 5]
mayor = numeros[0]                         # ← asumimos que el primero es el mayor

for n in numeros:
    if n > mayor:                          # ← si encuentro uno más grande
        mayor = n                          # ← lo guardo

print("El mayor es:", mayor)


# ============================================================
# TU PRÁCTICA ACÁ 👇
# ============================================================
# Ejercicio: usá esta plantilla para imprimir solo los nombres
# de una lista que empiezan con la letra "A"