"""
==========================================================================
Ejercicio 12: Rango de temperatura
==========================================================================

ENUNCIADO
---------
Pedile al usuario una temperatura en °C y decí 'Frío' (<10), 'Templado' (10-25) o 'Calor' (>25).
"""

temperatura = int(input("ingresa temperatura actual: "))
if temperatura < 10:
    print("hace Frio")
elif 10 <= temperatura <= 25:
    print("temperatura agradable")
else:
    print("hace Calor")



# ============================================================




# ============================================================
#  Casos de prueba sugeridos
#  Antes de ejecutar: anotá qué salida esperás de cada uno.
#  Después probá tu código y compará. Si coinciden en todos → OK.
# ============================================================
#   - 5
#   - 18
#   - 30
