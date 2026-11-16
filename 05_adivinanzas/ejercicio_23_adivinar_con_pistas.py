# ============================================================
# Ejercicio 23: Adivinar con pistas
# Categoría: 05_adivinanzas
# ============================================================
#
# ENUNCIADO:
# Número secreto: 27. Después de cada intento, 
# decile si es 'más alto' o 'más bajo'.
#
n_secreto = 27
contador = 0
n_usuario = 0
while n_usuario != n_secreto:
    n_usuario = int(input("Ingresa un numero: "))
    if n_usuario > n_secreto:
        print("mas bajo")
    elif n_usuario < n_secreto:
        print("mas alto")
    else:
        print("adivinaste")
contador += 1
    
