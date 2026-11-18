"""
==========================================================================
Ejercicio 05: Aprobado o desaprobado
==========================================================================

ENUNCIADO
---------
Pedile al usuario una nota (0 a 10) e indicá 'Aprobado' si es 6 o más, 'Desaprobado' si no.

PISTA (leela solo si te trabás)
-------------------------------
Comparación simple con >=.

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
n = int(input("escribe tu calificacion: "))
if n >= 6:
    print("aprobado")
else:
    print("desaprobado")
# ============================================================
#  Escribí tu código desde acá
#  (borrá este comentario cuando empieces)
# ============================================================




# ============================================================
#  Casos de prueba sugeridos
#  Antes de ejecutar: anotá qué salida esperás de cada uno.
#  Después probá tu código y compará. Si coinciden en todos → OK.
# ============================================================
#   - 8
#   - 4
#   - 6
