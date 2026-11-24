# ============================================================
# Ejercicio 37: Alcancía
# Categoría: 08_simulaciones
# ============================================================
#
# ENUNCIADO:
# Meta: 500 pesos. El usuario ingresa montos hasta alcanzar o superar la meta. Mostrá cuántos aportes hizo.
#

# ============================================================
# Ejercicio 37: La Alcancía (Simulación de acumulación)
# Categoría: 08_simulaciones | Modalidad: Bucles while y acumuladores
# ============================================================

# 📝 ENUNCIADO:
# Meta: Ahorrar 500 pesos. El usuario ingresa montos uno por uno 
# hasta alcanzar o superar la meta. 
# Objetivo: Mostrar cuántos aportes se realizaron y el monto final.

# 🧠 TRAZADO MANUAL EN PAPEL (First Principles Thinking):
# Variables de estado:
#   - META = 500 (constante, no cambia)
#   - total_ahorrado = 0 (acumulador, empieza en 0)
#   - cantidad_aportes = 0 (contador, empieza en 0)
#   - monto (variable de entrada del usuario)
#
# Iteración 1 (Ejemplo):
#   - Input: monto = 200
#   - total_ahorrado = 0 + 200 = 200
#   - cantidad_aportes = 0 + 1 = 1
#   - Condición while: 200 < 500 -> True (el bucle continúa)
#
# Iteración 2 (Ejemplo):
#   - Input: monto = 350
#   - total_ahorrado = 200 + 350 = 550
#   - cantidad_aportes = 1 + 1 = 2
#   - Condición while: 550 < 500 -> False (el bucle termina)

# 🛠️ CONFIGURACIÓN INICIAL DEL ESTADO
META = 500
total_ahorrado = 0.0
cantidad_aportes = 0

print(f"🎯 Meta de ahorro: ${META}")
print("Ingresa montos para aportar. (Ingresa 0 o negativo para cancelar)")

# 🔄 BUCLE PRINCIPAL: Se ejecuta MIENTRAS no lleguemos a la meta
while total_ahorrado < META:
    
    # 1. Entrada de datos
    entrada = input("💰 Ingresa el monto a aportar: ")
    
    # 2. Depuración activa: Validación de tipo de dato
    # ¿Por qué? Para evitar que el programa colapse si el usuario escribe "hola"
    try:
        monto = float(entrada)
    except ValueError:
        print("⚠️ Error: Debes ingresar un número válido. Intenta de nuevo.")
        continue  # Vuelve al inicio del while sin contar este intento fallido

    # 3. Lógica de negocio: Manejo de caso borde (cancelación)
    if monto <= 0:
        print("🛑 Aporte cancelado. El ahorro se detiene.")
        break  # Rompe el bucle inmediatamente, ignorando la condición del while

    # 4. Actualización del estado (El "corazón" del algoritmo)
    total_ahorrado += monto       # Acumulador: suma el nuevo valor al total existente
    cantidad_aportes += 1         # Contador: registra que ocurrió un evento válido
    
    # 5. Feedback al usuario en cada iteración (Transparencia del estado)
    print(f"   ➡️ Aporte registrado. Total acumulado: ${total_ahorrado:.2f} / ${META}")

# 🏁 RESULTADO FINAL (Fuera del bucle)
print("\n" + "="*45)
if total_ahorrado >= META:
    print(f"🎉 ¡Felicidades! Meta alcanzada o superada.")
    print(f"   Monto final ahorrado: ${total_ahorrado:.2f}")
    print(f"   Cantidad de aportes realizados: {cantidad_aportes}")
else:
    print(f"📊 Ahorro detenido prematuramente por el usuario.")
    print(f"   Monto final ahorrado: ${total_ahorrado:.2f}")
    print(f"   Faltaron: ${META - total_ahorrado:.2f} para la meta.")
print("="*45)