# LECCIÓN 5 - BUCLE WHILE | EXPERTO | Ejercicio 16
# =========================================================
# CONSIGNA: Aproximá la raíz cúbica de un número S usando Newton.
# Fórmula: x_nuevo = (2*x + S/(x*x)) / 3
# Iterá hasta que |x_nuevo - x| < 0.00001
# =========================================================

s = float(input("Ingresá un número: "))
x = s / 3 if s != 0 else 0

# TODO: completá el bucle

print(f"Raíz cúbica aproximada: {x:.6f}")
