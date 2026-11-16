"""
📘 CATEGORÍA 5 — Adivinanzas y control de intentos

📝 Enunciado del worked example:

Adivinar un número secreto (el 42) con un máximo de 5 intentos. 
El programa debe dar pistas: "Más alto" o "Más bajo".

"""
n_secreto = 42 # valor de asignacion siempre es True
n_intentos = 0 # funciona como contador
n_usuario = 0 # valor de asignacion neutro

while (n_intentos < 5) and (n_usuario != n_secreto):
    n_usuario = int(input("ingresa un numero: "))
    # ZONA A: Adentro del bucle
    if n_usuario < n_secreto:
        print("Más Alto")
    elif n_usuario > n_secreto:
        print("Más Bajo")
    else:  # si no es menor ni mayor, es igual
        print("Adivinaste el numero secreto: Ganaste!!!")
    
    n_intentos += 1  # ← ESTO VA ACÁ, al final del bucle, NO adentro del if

# ZONA B: Después del bucle (sin indentación, al mismo nivel que el while)
if n_usuario != n_secreto:
    print("Se terminaron los intentos: Perdiste")