# LECCIÓN 5 - BUCLE WHILE | INTERMEDIO | Ejercicio 4
# =========================================================
# CONSIGNA: El programa elige un número secreto entre 1 y 100
# (usá import random; random.randint(1,100)). El usuario adivina y
# el programa responde "más alto" o "más bajo" hasta que acierte.
# Al final mostrá los intentos.
# =========================================================

import random
secreto = random.randint(1, 100)
intentos = 0

# TODO: completá el bucle con pistas

print(f"¡Ganaste en {intentos} intentos! El número era {secreto}.")
