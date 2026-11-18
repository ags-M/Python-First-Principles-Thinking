# ============================================================
# Ejercicio 22: Adivinar con 5 intentos
# Categoría: 05_adivinanzas
# ============================================================
#
# ENUNCIADO:
# Número secreto: 42. El usuario tiene solo 5 intentos. Si los gasta, mostrá 'Perdiste'.

n_secreto = 42 # valor de asignacion siempre es True
n_intentos = 0 # funciona como contador
n_usuario = 0 # valor de asignacion neutro

while (n_intentos < 5) and (n_usuario != n_secreto):
    n_usuario = int(input("ingresa un numero: "))
    # ZONA A: Adentro del bucle
    if n_usuario < n_secreto:
        print("no valido")
    elif n_usuario > n_secreto:
        print("no valido")
    else:  # si no es menor ni mayor, es igual
        print("Adivinaste el numero secreto: Ganaste!!!")
    
    n_intentos += 1  # ← ESTO VA ACÁ, al final del bucle, NO adentro del if

# ZONA B: Después del bucle (sin indentación, al mismo nivel que el while)
if n_usuario != n_secreto:
    print("Se terminaron los intentos: Perdiste")
