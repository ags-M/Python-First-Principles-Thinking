# ============================================================
# Ejercicio 25: Adivinar palabra
# Categoría: 05_adivinanzas
# ============================================================
#
# ENUNCIADO:
# Palabra secreta: 'python'. El usuario tiene 3 intentos. Usá while.
#
# ========================================
# ZONA A: DENTRO DEL BUCLE (indentado)
# Se repite en cada intento
# ========================================
intentos = 0
secreta = "python"
usuario = ""
while intentos < 3 and secreta != usuario:
    usuario = input("ingresa una palabra: ").lower()  # ← Pedir palabra
    if usuario == secreta:                             # ← ¿Adivinó?
        print("adivinaste")                            # ← Sí: mostrar mensaje
        break                                          # ← Salir del bucle YA
    intentos += 1                                      # ← Contar el intento

# ========================================
# ZONA B: DESPUÉS DEL BUCLE (sin indentar)
# Se ejecuta UNA SOLA VEZ cuando el bucle termina
# ========================================
if usuario != secreta:                                 # ← ¿No adivinó?
    print("perdiste")                                  # ← Mostrar mensaje


#--------------------------------------------
print("-" * 30)
#--------------------------------------------


# 🚀 EJERCICIO CON FLAG

secreta = "python"
intentos = 0
usuario = ""
gano = False
while intentos < 3 and secreta != usuario:
    usuario = input("ingresa una palabra, tenes 3 intentos: ").lower()
    if usuario == secreta:
        gano = True
    intentos += 1
#ZONA B
if gano:
    print("Ganaste, adivinaste la palabra secreta")
else:
    print("Se terminaron los intentos: Perdiste")


