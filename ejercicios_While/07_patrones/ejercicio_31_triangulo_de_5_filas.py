# ============================================================
# Ejercicio 31: Triángulo de 5 filas
# Categoría: 07_patrones
# ============================================================
#
# ENUNCIADO:
# Imprimí un triángulo rectángulo de 5 filas con asteriscos:


# --- Triángulo rectángulo de 5 filas con while ---

filas = 5          # total de filas que queremos dibujar
n_filas = 1              # 'i' es el número de fila actual (arranca en 1)

while n_filas <= filas:              # MIENTRAS no hayamos pasado la fila 5...
    asteriscos = " "            # ...empezamos cada fila con una cadena vacía
    contador = 1                      # 'contador' cuenta los asteriscos de ESTA fila
    while contador <= n_filas:              # en la fila '1' queremos exactamente '1' asteriscos
        asteriscos += "*"      # agregamos un asterisco a la cadena
        contador += 1                 # avanzamos el contador interno
    print(asteriscos)          # terminamos la fila → la imprimimos completa
    n_filas += 1                     # y pasamos a la siguiente fila