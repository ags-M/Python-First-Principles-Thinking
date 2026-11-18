"""
📘 CATEGORÍA 5 — Adivinanzas y control de intentos

📝 Enunciado del worked example:

Adivinar un número secreto (el 42) con un máximo de 5 intentos. 
El programa debe dar pistas: "Más alto" o "Más bajo".

"""
n_secreto = 42
n_intentos = 0
n_usuario = 0
gano = False # esto es la bandera indica el estado 

# ========================================
# ZONA A: DENTRO DEL BUCLE (indentado)
# ========================================
while (n_intentos < 5) and (n_usuario != n_secreto):
    n_usuario = int(input("Ingresa un número: "))
    
    if n_usuario < n_secreto:
        print("Más Alto")
    elif n_usuario > n_secreto:
        print("Más Bajo")
    else:
        gano = True
    
    n_intentos += 1

# ========================================
# ZONA B: DESPUÉS DEL BUCLE (sin indentar)
# ========================================
if gano:
    print("Ganaste, adivinaste el número secreto")
else:
    print("Se terminaron los intentos: Perdiste")
    