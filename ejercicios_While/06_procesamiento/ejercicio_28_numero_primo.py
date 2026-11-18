# ============================================================
# Ejercicio 28: Número primo
# Categoría: 06_procesamiento
# ============================================================
# ENUNCIADO:
# Pedir al usuario un número y decí si es primo usando while. 
"""
🧠 Primero: ¿Qué es un número primo?
Un número primo es aquel que solo se puede dividir exactamente por 2 números: el 1 y él mismo.

🔍 ¿Cómo sabemos si un número divide a otro?
En Python, usamos el operador % (módulo), que nos da el resto de la división.

Pregunta clave: si n % divisor == 0, ¿qué significa?
🎯 Volvamos a lo básico
Para saber si un número es primo, tenemos que probar dividirlo por otros números, uno por uno.
Pregunta simple: si quiero saber si 7 es primo, ¿por cuál número empiezo a probar dividir?
Respuesta: por el 2 (porque el 1 siempre divide a todos, no cuenta).
🧩 Las DOS variables que necesitás
Pensá en esto como una persona probando divisores:
n = el número que queremos verificar (ej: 7)
divisor = el número por el cual estamos probando dividir (arranca en 2)
Pregunta: si arrancamos probando con divisor = 2, ¿cómo escribirías la inicialización de estas dos variables?

divisor = 2
n_es_primo = 

🎯 un número primo es aquel que NO es divisible por NINGÚN número entre 2 y n-1. No alcanza con probar solo el 2.
supongamos n = 7
Para saber si 7 es primo, tenemos que probar:

¿El 7 es divisible por 1? → Si, PERO OJO!!! El 1 siempre da resto 0, así que si lo incluyeras en el bucle, 
el programa diría que ningún número es primo. Por eso el divisor arranca en 2!!!.🎯

¿El 7 es divisible por 2? → No da resto 1
¿El 7 es divisible por 3? → No da resto 1
¿El 7 es divisible por 4? → No da reste 3
¿El 7 es divisible por 5? → No da resto 2
¿El 7 es divisible por 6? → No da resto 1
¿El 7 es divisible por 7? → SI da resto 0

Conclusión: ninguno de los divisores útiles (2 a 6) dio resto 0 → 7 es primo ✅
"""
n = int(input("ingresa un numero: "))
divisor = 2
flag = True  # Asumimos que es primo hasta que encontremos un divisor

while divisor < n:
    if n % divisor == 0:
        flag = False  # Encontramos un divisor, NO es primo
        # (no hace falta hacer nada más, podemos seguir o romper)
    
    divisor += 1  # ← está alineado con el if (no dentro), y el mensaje final está después del bucle.

# DESPUÉS DEL BUCLE, mostramos el resultado
if flag:
    print("El numero es primo")
else:
    print("El numero no es primo")
        
