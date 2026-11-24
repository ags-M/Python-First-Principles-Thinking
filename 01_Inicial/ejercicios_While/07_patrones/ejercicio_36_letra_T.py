
# 🎯 Ahora: la letra "T"

"""
* * * * *
    *
    *
    *
    *                    

*****    ← fila 1: 5 asteriscos, 0 espacios
  *      ← fila 2: 1 asterisco, 2 espacios a la izquierda
  *      ← fila 3: 1 asterisco, 2 espacios a la izquierda
  *      ← fila 4: 1 asterisco, 2 espacios a la izquierda
  *      ← fila 5: 1 asterisco, 2 espacios a la izquierda

📊 Tabla de análisis

# ====================================================================
# ANÁLISIS: Letra "T" con while (5 filas)
# ====================================================================
#
# | Fila (i) | ¿Es la primera fila? | Espacios | Asteriscos | Línea impresa |
# |----------|----------------------|----------|------------|----------------|
# | 1        | Sí (i == 1)          | 0        | 5          | "*****"        |
# | 2        | No (i != 1)          | 2        | 1          | "  *"          |
# | 3        | No (i != 1)          | 2        | 1          | "  *"          |
# | 4        | No (i != 1)          | 2        | 1          | "  *"          |
# | 5        | No (i != 1)          | 2        | 1          | "  *"          |
#
# FÓRMULAS:
# - Si i == 1 → linea = "*" * filas (barra horizontal)

# - Si i != 1 → linea = " " * espacios + "*" (barra vertical centrada)

# - espacios = (filas - 1) // 2 (calcula el centrado horizontal)
#
# Para filas = 5: espacios = (5 - 1) // 2 = 2
# ====================================================================
"""
filas = 5

i = 1
while i <= filas:
    if i == 1:
        # --- Caso: primera fila (barra horizontal) ---
        linea = "*" * filas   # ← ¿cuántos asteriscos? 5
    else:
        # --- Caso: filas siguientes (barra vertical centrada) ---
        espacios = (filas - 1) // 2   # ← fórmula de espacios para averiguar el CENTRADO de la linea VERTICAL
        linea = " " * espacios + "*"
    
    print(linea)
    i += 1

"""
📊 Tabla de traceo
# ====================================================================
# TRACEO: Letra "T" con while (5 filas) -
# ====================================================================

                                   espacios = (filas - 1) // 2  linea = " " * espacios + "*"
# | Iteración | i  | ¿i == 1? | Rama  | Cálculo de `espacios`      | Cálculo de `linea`        | Salida impresa |
# |-----------|----|----------|-------|----------------------------|---------------------------|----------------|
# | 1         | 1  | Sí       | if    | No se ejecuta              | "*" * 5  → "*****"        | *****          |
# | 2         | 2  | No       | else  | (5 - 1) // 2 = 2           | " " * 2 + "*" → "*"       |   *            |
# | 3         | 3  | No       | else  | (5 - 1) // 2 = 2           | " " * 2 + "*" → "*"       |   *            |
# | 4         | 4  | No       | else  | (5 - 1) // 2 = 2           | " " * 2 + "*" → "*"       |   *            |
# | 5         | 5  | No       | else  | (5 - 1) // 2 = 2           | " " * 2 + "*" → "*"       |   *            |
# | 6         | 6  | Sale     | -     | Condición `i <= 5` es Falsa| Fin del bucle             | ---            |
#
# DETALLE DE LA FÓRMULA DE CENTRADO:
# - (filas - 1) // 2  →  (5 - 1) // 2  →  4 // 2  →  2 espacios.
# - El operador // es la "división entera" (descarta decimales).
# - Esto garantiza que el palo de la "T" quede exactamente en el medio.
"""
# ====================================================================
