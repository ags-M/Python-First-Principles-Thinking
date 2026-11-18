# LECCIÓN 5 - BUCLE WHILE | EXPERTO | Ejercicio 18
# =========================================================
# CONSIGNA: Simulá 10000 partidas de "ruleta rusa" estadística (sin daño real).
# Un revólver de 6 cámaras con 1 bala. Se gira el tambor cada vez.
# Contá cuántas partidas terminan en "susto" (bala) vs "alivio".
# Debería dar ~16.67% de sustos.
# =========================================================

import random
partidas = 10000
sustos = 0
i = 0

# TODO: completá el bucle

print(f"Sustos: {sustos}/{partidas} = {sustos/partidas*100:.2f}%")
