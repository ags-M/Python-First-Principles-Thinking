# ============================================================
# Ejercicio 38: Contar palabras
# Categoría: 08_simulaciones
# ============================================================
#
# ENUNCIADO:
# El usuario ingresa frases. Cuando escriba 'fin', termina. 
# Mostrá el total de palabras ingresadas (contá espacios + 1).
#
"""
La lógica de contar palabras:
contador de palabras es espacio + 1 ... significa que si hay 1 espacio ello implica a dos palabras, por eso 
espacio + 1 es igual a 1 + 1 = 2 entonces hay dos palabras. otro ejemplo una palabra hola, no tiene espacios
entonces espacio + 1 es igual a 0 + 1 es igual a 1 palabra. 

📊 Traceo manual

CASO A: "hola mundo" → "fin"
CASO B: "uno" → "dos tres" → "fin"
CASO C: "GRITO" -> "fin"
CASO D: "fin"
| Paso | dato leído  | dato == "fin"?  | espacios + 1  | total antes | total después  | ¿sigo? |
|------|-------------|--------------- -|---------------|-------------|----------------|--------|
| 1    |hola mundo   |      no         |     2         |     0       |       2        |  si    |
| 2    |uno dos tres |      no         |     3         |     2       |       5        |  si    |
| 3    |   grito     |      no         |     1         |     5       |       6        |  si    |
-----------------------------------------------------------------------------------------------
digo fin TERMINA

"""
