# LECCIÓN 5 - BUCLE WHILE | EXPERTO | Ejercicio 20
# =========================================================
# CONSIGNA: Implementá el método babilónico para calcular la raíz cuadrada.
# Es un caso particular de Newton: x_nuevo = (x + S/x) / 2
# Pero esta vez mostrá la evolución de la aproximación en cada iteración
# y compará con el resultado de math.sqrt().
# =========================================================

import math
s = float(input("Ingresá un número positivo: "))
x = s / 2
iteracion = 1

# TODO: completá el bucle mostrando cada iteración

print(f"math.sqrt: {math.sqrt(s):.10f}")
