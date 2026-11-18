# LECCIÓN 5 - BUCLE WHILE | EXPERTO | Ejercicio 14
# =========================================================
# CONSIGNA: Simulá una cola de atención al cliente durante 60 minutos.
# Cada minuto:
#   - con 40% de probabilidad llega un cliente (random)
#   - si hay alguien en la cola, se atiende (tarda 2 min)
# Llevá registro de: clientes atendidos, clientes que se fueron sin ser
# atendidos (si la cola supera 5), tiempo promedio de espera.
# =========================================================

import random
minuto = 0
cola = 0
atendidos = 0
perdidos = 0
tiempo_espera_total = 0
minutos_atencion_restantes = 0

# TODO: completá el bucle

