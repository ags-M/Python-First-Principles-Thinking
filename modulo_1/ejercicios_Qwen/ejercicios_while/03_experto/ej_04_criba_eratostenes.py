# LECCIÓN 5 - BUCLE WHILE | EXPERTO | Ejercicio 4
# =========================================================
# CONSIGNA: Implementá la Criba de Eratóstenes para encontrar todos los
# primos hasta N. Usá una lista de booleanos (inicializada en True)
# y "tachá" los múltiplos.
# =========================================================

n = int(input("Primos hasta: "))
es_primo = [True] * (n + 1)
es_primo[0] = es_primo[1] = False
actual = 2

# TODO: completá la criba con while

primos = [i for i in range(n + 1) if es_primo[i]]
print(f"Primos encontrados: {len(primos)}")
print(primos)
