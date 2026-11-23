
#Letra H 

"""


*       *
*       *
* * * * *
*       *
*       *
*       *

La letra H esta compuesta por dos verticales y una horizontal.
Hay 6 filas, en la 3 fila hay 5 asteriscos, por lo tanto tiene un ancho de 5 asteriscos


fila 1 hay 1 asterisco + 3 espacios + 1 asterisco
fila 2 hay 1 asterisco + 3 espacios + 1 asterisco
fila 3 hay 5 asteriscos
fila 4 hay 1 asterisco + 3 espacios + 1 asterisco
fila 5 hay 1 asterisco + 3 espacios + 1 asterisco
fila 6 hay 1 asterisco + 3 espacios + 1 asterisco

📊 Tabla de planificación

# ====================================================================
# PLANIFICACIÓN: Letra "H" con while (6 filas, ancho 5)
# ====================================================================
#
# | Fila (i) | ¿Es la fila del medio (i == 3)? | Contenido de `linea`               |
# |----------|---------------------------------|------------------------------------|
# | 1        | No                              | "*" + " " * 3 + "*"  → "*   *"     |
# | 2        | No                              | "*" + " " * 3 + "*"  → "*   *"     |
# | 3        | Sí                              | "*" * 5              → "*****"     |
# | 4        | No                              | "*" + " " * 3 + "*"  → "*   *"     |
# | 5        | No                              | "*" + " " * 3 + "*"  → "*   *"     |
# | 6        | No                              | "*" + " " * 3 + "*"  → "*   *"     |
#
# HERRAMIENTAS A USAR:
# - Bucle while: i = 1; while i <= 6: ... i += 1
# - Condición: if i == 3: ... else: ...
# - Multiplicación de strings: "*" * 5  y  " " * 3
# - Concatenación: "*" + " " * 3 + "*"

🧮 La fórmula real para calcular los espacios:

Para cualquier letra con dos palos verticales (como la H, la U, o la N), el cálculo siempre es así:
Definí el ancho_total: Es la cantidad de asteriscos de la barra horizontal (en tu caso, 5).
Restá los asteriscos fijos: Siempre hay 1 a la izquierda y 1 a la derecha (Total = 2).

El resto son los espacios: espacios = ancho_total - 2.

por ello es igual a  espacios = 5 - 2  = 3

# ====================================================================

"""
filas = 6
i = 1
ancho = 5
espacio = ancho - 2

while i <= filas:
    if i == 3:
        linea = "*" * ancho
    else:
        linea = "*" + " " * espacio + "*"
    print(linea)
    i += 1

#---------------------------------------------------------------------