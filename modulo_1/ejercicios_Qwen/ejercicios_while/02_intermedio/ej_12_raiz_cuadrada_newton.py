# LECCIÓN 5 - BUCLE WHILE | INTERMEDIO | Ejercicio 12
# =========================================================
# CONSIGNA: Aproximá la raíz cuadrada de un número usando el método
# de Newton. Fórmula: x_nuevo = (x + S/x) / 2
# Iterá hasta que |x_nuevo - x| < 0.0001
# =========================================================

s = float(input("Ingresá un número positivo: "))
x = s / 2

# TODO: completá el bucle

print(f"Raíz aproximada de {s}: {x:.6f}")
