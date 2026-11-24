# ============================================================
# Ejercicio 35: Letra L
# Categoría: 07_patrones
# ============================================================
#
# ENUNCIADO:
# Imprimí la letra 'L' usando asteriscos con 5 filas y 5 columnas.
"""
LETRA l

*         ← fila 1: 1 asterisco
*         ← fila 2: 1 asterisco
*         ← fila 3: 1 asterisco
*         ← fila 4: 1 asterisco
*****     ← fila 5: 5 asteriscos (¡la última es diferente!)

La letra "L" tiene dos partes:

En el palito vertical: las primeras 4 filas tienen 1 solo asterisco
La base horizontal: la última fila tiene 5 asteriscos (todas las columnas)

👨‍💻 Explicación "como si fueras ingeniero"

Tenés un bucle externo que itera de 1 a N (filas). 
En cada iteración, necesitás decidir cuántos asteriscos imprimir:

Si i < N → imprimir 1 asterisco por fila

Si i == N → imprimir N asteriscos, si hay 5 filas entonces 5 asteriscos 

Esto se resuelve con una condicional dentro del bucle (branching).
Es un caso simple porque la figura no es simétrica ni centrada.

-------------------------------------------------------------------------------------------
En programación, "branching" (ramificación) dentro de un bucle while se refiere 
a la capacidad de tomar decisiones y ejecutar diferentes caminos de código 
dentro del bucle, dependiendo de ciertas condiciones.

¿Qué significa branching en un while?

Dentro de un bucle while, el branching ocurre cuando usas estructuras de control como:

if / else / elif → para ejecutar bloques según una condición

break → para salir del bucle antes de que la condición sea falsa

continue → para saltar a la siguiente iteración

📊 En resumen
Branching en un while = el flujo de ejecución no es lineal dentro del bucle; 
el programa "ramifica" hacia distintas acciones según las condiciones evaluadas en cada iteración.
------------------------------------------------------------------------------------------

# Análisis de la letra "L" (5 filas)

📊 Tabla de análisis
| Fila (i) | ¿Es la última fila? | Asteriscos a imprimir |
|----------|---------------------|-----------------------|
| 1        | No (i < 5)          | 1                     |
| 2        | No (i < 5)          | 1                     |
| 3        | No (i < 5)          | 1                     |
| 4        | No (i < 5)          | 1                     |
| 5        | Sí (i == 5)         | 5                     |

# Fórmula:
# Si i < filas → 1 asterisco
# Si i == filas → filas asteriscos
# -----------------------------------------------------------
"""
filas = 5

i = 1
while i <= filas:
    if i == filas:
        linea = "*" * filas  # ← Multiplica el string "*" 5 veces
    else:
        linea = "*"          # ← Solo un asterisco
    
    print(linea)
    i += 1
"""
Como la pantalla dibuja de arriba (fila 1) hacia abajo (fila 5), el resultado es este:

*      <- Fila 1 (i=1). El if es Falso. Imprime 1. *
*      <- Fila 2 (i=2). El if es Falso. Imprime 1. *
*      <- Fila 3 (i=3). El if es Falso. Imprime 1. * 
*      <- Fila 4 (i=4). El if es Falso. Imprime 1. *
*****  <- Fila 5 (i=5). El if es VERDADERO. Imprime 5. (¡Aquí está la base!) * * * * *
-------------------------------------------------------------
# 📊 Tabla de traceo

# Traceo de la letra "L" (5 filas)

| Iteración (i) | ¿i == filas? | Rama ejecutada | Asteriscos en `linea` | Salida impresa |
|---------------|--------------|----------------|-----------------------|----------------|
| 1             | No (1 < 5)   | else           | 1                     | `*`            |
| 2             | No (2 < 5)   | else           | 1                     | `*`            |
| 3             | No (3 < 5)   | else           | 1                     | `*`            |
| 4             | No (4 < 5)   | else           | 1                     | `*`            |
| 5             | Sí (5 == 5)  | if             | 5                     | `*****`        |
| 6             | Sale del bucle | No se ejecuta | No imprime           | Fin            |

# Flujo del código:
# 1. Bucle: i va de 1 a 5
# 2. En cada iteración, se evalúa: ¿i == filas?
# 3. Si es verdadero → bucle imprime 5 asteriscos
# 4. Si es falso → imprime 1 asterisco
# 5. Se imprime la línea completa con print(linea)
# 6. Se incrementa i y se repite
___________________________________________________________________________________________

El código original (if i == filas)

En tu código original, le dices a la computadora: "Dibuja un asterisco en cada fila, 
EXCEPTO cuando llegues a la última fila (la 5). Ahí, dibuja 5 asteriscos".

"""
#--------------------------------------------
print("-" * 50)
#--------------------------------------------

# invertir la letra L 

filas = 5

i = 1
while i <= filas:
    if i == 1:  # ACA MODIFICAMOS  SACAMOS FILAS Y PONEMOS EL VALOR 1
        linea = "*" * filas  # ← Multiplica el string "*" 5 veces
    else:
        linea = "*"          # ← Solo un asterisco
    
    print(linea)
    i += 1
    
"""
*****  ← Fila 1 (i=1): if VERDADERO → imprime 5 asteriscos
*      ← Fila 2 (i=2): if FALSO → imprime 1 asterisco
*      ← Fila 3 (i=3): if FALSO → imprime 1 asterisco
*      ← Fila 4 (i=4): if FALSO → imprime 1 asterisco
*      ← Fila 5 (i=5): if FALSO → imprime 1 asterisco

"""