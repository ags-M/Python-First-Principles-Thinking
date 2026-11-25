# ============================================================
# Ejercicio 38: Contar palabras
# Categoría: 08_simulaciones
# ============================================================
#
TABLA_PILARES = """ logica de programacion:
_____________________________________________________________________________________________________________
| # | PILAR       | PREGUNTA           | EN PYTHON                | ANALOGIA: el mate                        |
|---|-------------|--------------------|--------------------------|------------------------------------------|
| 1 | Secuencia   |  En que orden?     | Sentencias una tras otra | Hervir, poner la bolsita de TE, servir   |
| 2 | Seleccion   |  Que camino tomo?  | if / elif / else         | Ya hirvio? Si si, sirvo; si no, espero.  |
| 3 | Repeticion  |  Hasta cuando?     | while (despues, for)     | Mientras no hierva, sigo calentando.     |

Regla de oro: la tabla de estado va ANTES del codigo. El codigo solo la traduce.
"""
"""
| CAPA       | PREGUNTA           | QUÉ ES                          | en algun ejercicio        |
|------------|--------------------|---------------------------------|---------------------------|
| Datos      | ¿Qué tengo ?       | Variables y tipos               | contador, acumulador      |
| Condición  | ¿Qué comparo?      | Expresión que da True o False   | saldo < 100               |
| Secuencia  | ¿En qué orden?     | Pasos uno tras otro             | leer, sumar, imprimir     |
| Selección  | ¿Qué camino tomo?  | if / elif / else                | if saldo >= 100           |
| Repetición | ¿Hasta cuándo?     | while                           | while frase != "fin"      |
| Traceo     | ¿Cómo lo verifico? | Tabla de estado en papel        | una fila por iteración    |

"""
# __________________________________________________________________________________________________________
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
