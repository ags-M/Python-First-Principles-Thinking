# LECCIÓN 5 - BUCLE WHILE | EXPERTO | Ejercicio 10
# =========================================================
# CONSIGNA: Simulá el problema de Monty Hall 10000 veces.
# - 3 puertas, 1 con premio.
# - El jugador elige una.
# - El presentador abre una sin premio.
# - El jugador CAMBIA de puerta.
# Contá cuántas veces gana. Debería dar ~66%.
# =========================================================

import random
simulaciones = 10000
victorias = 0
i = 0

# TODO: completá el bucle

print(f"Victorias cambiando: {victorias}/{simulaciones} = {victorias/simulaciones*100:.2f}%")
