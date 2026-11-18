"""
==========================================================================
Ejercicio 31: Número en rango [1, 100]
==========================================================================

ENUNCIADO
---------
Pedile al usuario un número y decí True si está entre 1 y 100 (inclusive), False si no.

PISTA (leela solo si te trabás)
-------------------------------
Comparación encadenada: `1 <= n <= 100`.

CÓMO TRABAJAR
-------------
1. Leé el enunciado con atención y pensá qué te pide.
2. Identificá qué datos de entrada necesitás y qué salida esperada debe dar.
3. Escribí tu código abajo desde cero. No hay plantilla: vos decidís
   si usás función, input(), print(), o lo que haga falta.
4. Antes de ejecutar, anotá en papel o en un comentario qué salida
   esperás para cada caso de prueba sugerido.
5. Corré el archivo con `python <nombre>.py` y compará.
6. Intentá al menos 15 minutos por tu cuenta antes de pedir ayuda.
==========================================================================
"""
n = int(input("escribe un numero: "))

if n >= 1 and n <= 100:
    print(True)
else:
    print(False)


# ============================================================
#  Casos de prueba sugeridos
#  Antes de ejecutar: anotá qué salida esperás de cada uno.
#  Después probá tu código y compará. Si coinciden en todos → OK.
# ============================================================
#   - 50
#   - 1
#   - 100
#   - 0
#   - 101
