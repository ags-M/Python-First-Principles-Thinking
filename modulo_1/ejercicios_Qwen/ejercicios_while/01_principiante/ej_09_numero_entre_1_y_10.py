# LECCIÓN 5 - BUCLE WHILE | PRINCIPIANTE | Ejercicio 9
# =========================================================
# CONSIGNA: Pedile al usuario un número hasta que esté entre 1 y 10 (inclusive).
# Si se equivoca, mostrá "Número inválido, intentá de nuevo".
# =========================================================

# TODO: usá while con una condición compuesta (and / or)
  
"""

Condición: 🐍 Python!

"Es válido si está entre 1 y 10"
n >= 1 and n <= 10

"Es inválido si está fuera de 1-10"
n < 1 or n > 10
    
"""

n = int(input("Ingresá un número: "))
while not (n >= 1 and n <=10):
   print("numero invalido, intenta de nuevo")
   n = int(input("Ingresá un número: "))
print("numero valido")
    
