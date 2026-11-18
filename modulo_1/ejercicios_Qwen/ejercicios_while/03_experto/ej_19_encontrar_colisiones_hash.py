# LECCIÓN 5 - BUCLE WHILE | EXPERTO | Ejercicio 19
# =========================================================
# CONSIGNA: Dada una función hash simple: hash(s) = suma de códigos ASCII
# de sus caracteres módulo 100, encontrá las primeras 5 palabras
# (de una lista predefinida) que produzcan la misma hash que "hola".
# =========================================================

def mi_hash(s):
    return sum(ord(c) for c in s) % 100

palabras = ["mundo", "python", "codigo", "bucle", "while", "hola",
            "aloh", "test", "data", "algo", "casa", "ala", "gato",
            "perro", "sol", "luz", "amor", "roma", "amor", "ramo"]

objetivo = mi_hash("hola")
encontradas = []
indice = 0

# TODO: completá el bucle

