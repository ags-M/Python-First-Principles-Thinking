"""
📘 CATEGORÍA 5 — Adivinanzas y control de intentos

                📝 Enunciado del worked example:

Adivinar un número secreto (el 42) con un máximo de 5 intentos. 
El programa debe dar pistas: "Más alto" o "Más bajo".

"""
# 💻 Código resuelto:

# 1. Configuración inicial del juego
secreto = 42
max_intentos = 5
intentos = 0
adivino = False   # Variable "bandera" (flag). Empieza en False.

# 2. El bucle se mantiene mientras queden intentos Y no haya adivinado
while intentos < max_intentos and not adivino:
    numero = int(input("Intentá adivinar el número (1-100): "))
    intentos = intentos + 1  # Contamos este intento
    
    # 3. Lógica de evaluación
    if numero == secreto:
        print("¡Ganaste! 🎉")
        adivino = True       # Cambiamos la bandera a True para salir del while
    elif numero < secreto:
        print("🔼 Más alto...")
    else:
        print("🔽 Más bajo...")

# 4. Verificación final fuera del bucle
if not adivino:
    print(f"❌ Perdiste. Te quedaste sin intentos. El número era {secreto}.")
else:
    print(f"Lo lograste en {intentos} intento(s).")

"""
________________________________________________________________________________________________________________________

Iteración   intentos   ¿intentos < 5 AND    numero     ¿numero == 42?   Acción / Pista             adivino    intentos
            (entrada)  not adivino?         ingresado                               (después del if)  después
________________________________________________________________________________________________________________________

  Inicio        0            True               —             —                —                      False        0
________________________________________________________________________________________________________________________

  1             0            True               30            No (30 < 42)     "🔼 Más alto..."       False        1
________________________________________________________________________________________________________________________

  2             1            True               50            No (50 > 42)     "🔽 Más bajo..."       False        2
________________________________________________________________________________________________________________________

  3             2            True               42            Sí               "¡Ganaste! 🎉"         True         3
________________________________________________________________________________________________________________________

  4             3      False (adivino=True)      —             —          Sale del bucle              —          —
________________________________________________________________________________________________________________________

Resultado final: El usuario ganó en 3 intentos. ✅









"""