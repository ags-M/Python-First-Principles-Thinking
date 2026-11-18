"""
==========================================================================
Ejercicio 17: Día laborable o fin de semana
==========================================================================

ENUNCIADO
---------
Pedile al usuario un número de día (1-7, Lunes a Domingo). Decí 'Laborable' (1-5) o 'Finde' (6-7). Otro: 'Inválido'.

PISTA (leela solo si te trabás)
-------------------------------
Podés usar `in [1,2,3,4,5]` para los laborables.

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
dia = int(input("escribe un dia de lunes a domingo, con un numero (1/7): "))
if dia in [1,2,3,4,5]:
   print("es un dia laborable")
elif dia in [6, 7]:
   print("es un dia de fin de semana")
else:
   print("es invalido")


# ============================================================
#  Casos de prueba sugeridos
#  Antes de ejecutar: anotá qué salida esperás de cada uno.
#  Después probá tu código y compará. Si coinciden en todos → OK.
# ============================================================
#   - 1
#   - 6
#   - 7
#   - 0
