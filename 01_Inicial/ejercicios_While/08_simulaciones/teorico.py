"""
LOGICA DE LA PROGRAMACION:

Existe un principio matemático llamado el Teorema de la Programación Estructurada (Böhm-Jacopini), 
que demuestra que cualquier programa o algoritmo, por complejo que sea, puede construirse usando 
únicamente esos 3 pilares: Secuencia, Selección y Repetición.

El matiz importante (Nivel Experto):
Aunque con solo esos 3 pilares podés resolver cualquier problema, en la vida real los programas se vuelven gigantes. 
Si usáramos solo esos 3 pilares sin organización, el código sería un caos ilegible.
Por eso, a esos 3 pilares base les agregamos capas de organización para manejar la complejidad:

# ==============================================================================
# NIVELES DE LA PROGRAMACIÓN (Ancho optimizado para VSCode ~80 caracteres)
# ==============================================================================
# | Nivel    | Concepto    | Para qué sirve            | Analogía del Mate 🧉        |
# |----------|-------------|---------------------------|-----------------------------|
# | Básico   | 3 Pilares   | Lógica paso a paso        | Calentar, evaluar, servir   |
# | Medio    | Funciones   | Agrupar bloques de código | Receta escrita, no repetir  |
# | Medio    | Estructuras | Organizar muchos datos    | Bandeja para 5 mates juntos |
# | Avanzado | Errores     | Prever fallos sin colapsar| Trapo a mano si se derrama  |
# ==============================================================================

💡 Analogía clara:
Los 3 pilares son como el alfabeto (vocales y consonantes). 
Con solo el alfabeto podés escribir cualquier libro del mundo. 
Pero para escribir una enciclopedia, necesitás organizar esas 
letras en palabras, párrafos y capítulos (Funciones y Estructuras de Datos).
"""
"""
TABLA_PILARES =  logica de programacion:
_____________________________________________________________________________________________________________
| # | PILAR       | PREGUNTA           | EN PYTHON                | ANALOGIA: el mate                        |
|---|-------------|--------------------|--------------------------|------------------------------------------|
| 1 | Secuencia   |  En que orden?     | Sentencias una tras otra | Hervir, poner la bolsita de TE, servir   |
| 2 | Seleccion   |  Que camino tomo?  | if / elif / else         | Ya hirvio? Si si, sirvo; si no, espero.  |
| 3 | Repeticion  |  Hasta cuando?     | while (despues, for)     | Mientras no hierva, sigo calentando.     |
_____________________________________________________________________________________________________________

Regla de oro: la tabla de estado va ANTES del codigo. El codigo solo la traduce.

"""
"""
_________________________________________________________________________________________________
| CAPA       | PREGUNTA           | QUÉ ES                          | en algun ejercicio        |
|------------|--------------------|---------------------------------|---------------------------|
| Datos      | #¿Qué tengo ?      | Variables y tipos               | contador, acumulador      |
| Condición  | #¿Qué comparo?     | Expresión que da True o False   | saldo < 100               |
| Secuencia  | #¿En qué orden?    | Pasos uno tras otro             | leer, sumar, imprimir     |
| Selección  | #¿Qué camino tomo? | if / elif / else                | if saldo >= 100           |
| Repetición | #¿Hasta cuándo?    | while                           | while frase != "fin"      |
| Traceo     | #¿Cómo lo verifico?| Tabla de estado en papel        | una fila por iteración    |
"""