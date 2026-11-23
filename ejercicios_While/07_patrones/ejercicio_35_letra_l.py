# ============================================================
# Ejercicio 35: Letra L
# Categoría: 07_patrones
# ============================================================
#
# ENUNCIADO:
# Imprimí la letra 'L' usando asteriscos con 5 filas y 5 columnas.
"""
LETRA l

*
*
*
*
* * * * *

La letra "L" tiene dos partes:
El palito vertical: las primeras 4 filas tienen 1 solo asterisco
La base horizontal: la última fila tiene 5 asteriscos (todas las columnas)

Entonces, en cada fila te preguntás: "¿soy la última fila?"

Si NO soy la última → imprimí 1 asterisco
Si SOY la última → imprimí 5 asteriscos

"""
# -----------------------------------------------------------

filas = 5
i = 1

while i <= filas:
    # ¿En qué fila estoy?
    if i < filas:
        # No es la última fila → ¿cuántos asteriscos?
        asteriscos = ___    # ← completá
    else:
        # Es la última fila → ¿cuántos asteriscos?
        asteriscos = ___    # ← completá
    
    # Ahora imprimimos los asteriscos de esta fila
    linea = ""
    j = 1
    while j <= asteriscos:
        linea += "*"
        j += 1
    
    print(linea)
    i += 1


