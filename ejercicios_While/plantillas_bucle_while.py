# ====================================================================
# PLANTILLAS DE BUCLES WHILE - VERSIÓN FUNCIONAL
# ====================================================================
# IMPORTANTE: Estas son PLANTILLAS (esqueletos).
# Para usarlas en un ejercicio, copiás la que más se parezca
# y reemplazás los valores por los del problema concreto.
# ====================================================================


# ====================================================================
# PLANTILLA 1: Bucle simple (contar del 1 al N)
# ====================================================================
# Uso: cuando tenés que repetir algo N veces, una sola dimensión.
# Ejemplos: contar, sumar una secuencia, imprimir números.
# ====================================================================

N = int(input("Ingresa un número: "))
i = 1
while i <= N:
    print(i)          # ← reemplazá por lo que quieras hacer
    i += 1


# ====================================================================
# PLANTILLA 2: Bucle con bucle interno (filas × columnas)
# ====================================================================
# Uso: cuando tenés que dibujar una grilla, tabla o patrón 2D.
# Ejemplos: cuadrado, rectángulo, triángulo, pirámide.
# ====================================================================

filas = int(input("Ingresa cantidad de filas: "))
columnas = int(input("Ingresa cantidad de columnas: "))

i = 1
while i <= filas:                  # BUCLE EXTERNO: controla las filas
    linea = ""
    j = 1
    while j <= columnas:           # BUCLE INTERNO: controla las columnas
        linea += "*"               # ← reemplazá por lo que quieras poner
        j += 1
    print(linea)
    i += 1


# ====================================================================
# PLANTILLA 3: Bucle con condición (if/else adentro)
# ====================================================================
# Uso: cuando en algunas iteraciones querés hacer una cosa,
# y en otras querés hacer otra cosa distinta.
# Ejemplos: letra L, letra T, letra H, patrones mixtos.
# ====================================================================

N = int(input("Ingresa un número: "))
i = 1
while i <= N:
    if i == 3:                     # ← reemplazá por tu condición real
        print("Caso A: fila especial")
    else:
        print("Caso B: fila normal")
    i += 1
    
"""
# ====================================================================
# RESUMEN: ¿CUÁNDO USAR CADA PLANTILLA?
# ====================================================================
#
# | Plantilla | Estructura                      | Cuándo usarla                              | Ejemplo típico          |
# |-----------|---------------------------------|--------------------------------------------|-------------------------|
# | 1         | 1 bucle (while simple)          | Repetir algo N veces, una sola dimensión   | Contar del 1 al 10      |
# | 2         | 2 bucles anidados               | Dibujar grillas, patrones 2D               | Cuadrado, triángulo     |
# | 3         | 1 bucle + if/else adentro       | Filas con comportamientos distintos        | Letra L, T, H           |
#
# REGLAS DE ORO:
# - Una plantilla NUNCA se ejecuta tal cual. Siempre hay que completarla.
# - Los contadores (i, j) SIEMPRE se reinician donde corresponde:
#   - i se inicializa ANTES del bucle externo
#   - j se inicializa DENTRO del bucle externo, ANTES del bucle interno
# - Las variables de control (filas, columnas, N) se definen ANTES del bucle.
# - Los comentarios (# hacer algo) NO son código. Reemplazalos por código real.
# ====================================================================


"""
