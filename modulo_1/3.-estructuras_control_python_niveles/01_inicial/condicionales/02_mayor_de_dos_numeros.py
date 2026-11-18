"""
==========================================================================
Ejercicio 02: Mayor de dos números
==========================================================================

ENUNCIADO
---------
Pedile al usuario dos números y mostrá cuál es el mayor.

PISTA (leela solo si te trabás)
-------------------------------
Compará los dos con un if simple.

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
n1 = float(input("escribe un numero: "))
n2 = float(input("escribe un numero: "))
if n1 > n2:
   print(f"n1 {n1} es mayor que n2 [n2]")
elif n2 > n1:
   print(f"n2 {n2} es mayor que n1 {n1}")
else:
   print("los numeros son iguales")
# ============================================================
#  Escribí tu código desde acá
#  (borrá este comentario cuando empieces)
# ============================================================




# ============================================================
#  Casos de prueba sugeridos
#  Antes de ejecutar: anotá qué salida esperás de cada uno.
#  Después probá tu código y compará. Si coinciden en todos → OK.
# ============================================================
#   - 3 y 5
#   - 10 y 2
#   - 7 y 7
