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

"""

📋 Tabla: 
# ╔══════════════════════════════════════════════════════════════════╗
# ║  📝 MÉTODOS DE STRINGS ÚTILES PARA CONTAR PALABRAS              ║
# ╚══════════════════════════════════════════════════════════════════╝
#
# ┌──────────────────────────────────────────────────────────────────┐
# │  MÉTODO          │ ¿Qué hace?              │ Ejemplo             │
# ├──────────────────────────────────────────────────────────────────┤
# │  .split()        │ Divide por espacios y   │ "hola mundo".split()│
# │                  │ devuelve lista de       │ → ["hola", "mundo"] │
# │                  │ palabras. Ignora        │                     │
# │                  │ espacios múltiples.     │                     │
# ├──────────────────────────────────────────────────────────────────┤
# │  len(lista)      │ Cuenta elementos de     │ len(["a","b","c"])  │
# │  (SIN LÍMITE)    │ cualquier secuencia.    │ → 3                 │
# │                  │ NO tiene límite de 10.  │                     │
# ├──────────────────────────────────────────────────────────────────┤
# │  .lower()        │ Convierte a minúsculas. │ "HOLA".lower()      │
# │                  │ Útil para comparar.     │ → "hola"            │
# ├──────────────────────────────────────────────────────────────────┤
# │  .strip()        │ Elimina espacios al     │ "  hola  ".strip()  │
# │                  │ inicio y final.         │ → "hola"            │
# └──────────────────────────────────────────────────────────────────┘
#
# 💡 COMBINACIÓN MÁGICA para contar palabras:
# ──────────────────────────────────────────────────────────────────
# frase = "  Hola   mundo  desde  Python  "
# palabras = frase.split()        # → ["Hola", "mundo", "desde", "Python"]
# cantidad = len(palabras)        # → 4
#
# O espacios en una sola línea: cantidad = len(frase.split())   # → 4
# ════════════════════════════════════════════════════════════════════
"""
"""
# ╔══════════════════════════════════════════════════════════════════╗
# ║  📝 MÉTODOS PARA CONTAR PALABRAS EN UN STRING                   ║
# ╚══════════════════════════════════════════════════════════════════╝
#
# ┌──────────────────────────────────────────────────────────────────┐
# │  MÉTODO                  │ ¿Cómo funciona?        │ ¿Confiabilidad?│
# ├─────────────────────────────────────────────────────────────────┤
# │  len(frase.split())      │ Divide por espacios,   │ ✅ ALTA       │
# │  (RECOMENDADO)           │ ignora espacios        │ Funciona con  │
# │                          │ múltiples, y cuenta    │ cualquier     │
# │                          │ los elementos reales.  │ caso.         │
# ├──────────────────────────────────────────────────────────────────┤
# │  frase.count(" ") + 1    │ Cuenta espacios y      │ ⚠️ BAJA       │
# │  (NO RECOMENDADO)        │ suma 1. Falla con      │ Falla con     │
# │                          │ espacios múltiples o   │ espacios      │
# │                          │ frases vacías.         │ extra.        │
# └──────────────────────────────────────────────────────────────────┘
#
 🧪 PRUEBA DE COMPARACIÓN:
# ──────────────────────────────────────────────────────────────────
# frase = "  hola   mundo  "
#
# print(len(frase.split()))        # → 2 ✅ (correcto)
# print(frase.count(" ") + 1)      # → 7 ❌ (cuenta todos los espacios) + 1 = 8 error!!!

frase = "  hola   mundo  "
Frase: "· · h o l a · · · m u n d o · ·"
        ↑ ↑         ↑ ↑ ↑           ↑ ↑
        1 2         3 4 5           6 7 ACA SE COMETE EL ERROR !!!
#
# frase_vacia = ""
# print(len(frase_vacia.split()))  # → 0 ✅ (correcto)
# print(frase_vacia.count(" ") + 1)# → 1 ❌ (dice que hay 1 palabra)
#
# 💡 CONCLUSIÓN: Usá SIEMPRE len(frase.split())
#    Es más robusto y maneja todos los casos correctamente.
# ════════════════════════════════════════════════════════════════════
"""
"""
#______________________________________________________________________________________

#📋 Tabla para VS Code: Encadenar métodos

# ╔══════════════════════════════════════════════════════════════════╗
# ║  🔗 ENCADENAR MÉTODOS DE STRINGS                                ║
# ╚══════════════════════════════════════════════════════════════════╝
#
# 💡 IDEA: Podés aplicar varios métodos uno detrás del otro,
#    siempre que el resultado sea del tipo correcto.
#
# 📌 EJEMPLOS COMUNES:
# ──────────────────────────────────────────────────────────────────
# ✅ Leer y convertir a minúsculas en una sola línea:
# nombre = input("Tu nombre: ").lower()
#
# ✅ Leer, quitar espacios y pasar a minúsculas:
# nombre = input("Tu nombre: ").strip().lower()
#
# ✅ Leer y dividir en palabras directamente:
# palabras = input("Frase: ").split()
#
# ✅ Leer, limpiar, normalizar y contar palabras:
# cantidad = len(input("Frase: ").strip().lower().split())
#
# 📌 ORDEN IMPORTANTE:
# ──────────────────────────────────────────────────────────────────
# ❌ MAL:  input("...").split().lower()
#    → split() devuelve una LISTA, y las listas NO tienen .lower()
#    → ERROR: AttributeError
#
# ✅ BIEN: input("...").lower().split()
#    → lower() devuelve string → split() funciona sobre string DANDO UNA LISTA
# #
# 🎯 REGLA DE ORO:
# ──────────────────────────────────────────────────────────────────
#    Los métodos de STRING deben aplicarse ANTES de split()
#    (porque split() convierte el string en lista).
# ════════════════════════════════════════════════════════════════════
"""


