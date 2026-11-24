# ============================================================
#  PLANTILLA FOR #2 - BUCLE ANIDADO (filas × columnas) | NOVA 🤖
#  Curso Python - Módulo 1 - Lección 5
# ============================================================
# USO: cuando tenés que dibujar una grilla, tabla o patrón 2D.
# EJEMPLOS: cuadrado, rectángulo, triángulo, pirámide, rombo,
#           tablas de multiplicar completas, combinaciones.
# ============================================================
# REGLA DE ORO: el bucle EXTERNO controla las FILAS,
#               el bucle INTERNO controla las COLUMNAS.
# ============================================================

# ----------------------------------------------------------------
# CASO A: Cuadrado NxN de asteriscos
# ----------------------------------------------------------------
N = int(input("Ingresa el tamaño del cuadrado: "))

for i in range(1, N + 1):                  # BUCLE EXTERNO: filas
    linea = ""
    for j in range(1, N + 1):              # BUCLE INTERNO: columnas
        linea += "*"                       # ← reemplazá por lo que quieras
    print(linea)


# ----------------------------------------------------------------
# CASO B: Triángulo rectángulo (columnas dependen de la fila)
# ----------------------------------------------------------------
filas = 5

for i in range(1, filas + 1):              # BUCLE EXTERNO: filas
    linea = ""
    for j in range(1, i + 1):              # ← ¡ojo! columnas = i
        linea += "*"
    print(linea)
# Salida:
# *
# **
# ***
# ****
# *****


# ----------------------------------------------------------------
# CASO C: Triángulo invertido
# ----------------------------------------------------------------
filas = 5

for i in range(filas, 0, -1):              # ← filas decrece
    linea = ""
    for j in range(1, i + 1):
        linea += "*"
    print(linea)


# ----------------------------------------------------------------
# CASO D: Pirámide centrada (espacios + asteriscos)
# ----------------------------------------------------------------
filas = 5

for i in range(1, filas + 1):
    espacios = " " * (filas - i)           # ← espacios a la izquierda
    asteriscos = "*" * (2 * i - 1)         # ← asteriscos impares
    print(espacios + asteriscos)


# ----------------------------------------------------------------
# CASO E: Tablas de multiplicar completas (del 1 al 5)
# ----------------------------------------------------------------
for tabla in range(1, 6):                  # ← bucle externo: qué tabla
    print(f"\n--- Tabla del {tabla} ---")
    for i in range(1, 11):                 # ← bucle interno: multiplicador
        print(f"{tabla} x {i} = {tabla * i}")


# ============================================================
# TU PRÁCTICA ACÁ 👇
# ============================================================
# Ejercicio: usá esta plantilla para dibujar un rombo de 9 filas