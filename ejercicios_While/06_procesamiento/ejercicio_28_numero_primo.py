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
if n <= 1:
    print("El numero no es primo")
else:
    divisor = 2
    flag = True  # Asumimos que es primo hasta que encontremos un divisor
    
    while divisor < n: # ESTA ES LA ZONA A
        if n % divisor == 0:
            flag = False  # Encontramos un divisor, NO es primo
        divisor += 1  # ← ESTO VA DENTRO DEL WHILE (alineado con el if) 
    
    # DESPUÉS DEL BUCLE, mostramos el resultado ZONA B
    if flag:
        print("El numero es primo")
    else:
        print("El numero no es primo")
        

#--------------------------------------------
print("-" * 30)
#--------------------------------------------

# En este ejercicio impedimos que el BUCLE siga y se detiene cuando encuentra un resto de CERO, dentro del n -1 

n = int(input("ingresa un numero: "))
divisor = 2
flag = True  # Asumimos que es primo hasta que encontremos un divisor
#ZONA A
while divisor < n:
    if n % divisor == 0:
        flag = False
        print(f"No es primo porque lo divide {divisor}")
        break
        
    divisor += 1  # ← está alineado con el if (no dentro), y el mensaje final está después del bucle
#ZONA B
if flag:
    print("El numero es primo")
"""
____________________________________________________________________________________________________
TEORICO:

N = 7
divisor=2: 7%2=1 → no divide → divisor=3
divisor=3: 7%3=1 → no divide → divisor=4
divisor=4: 7%4=3 → no divide → divisor=5
divisor=5: 7%5=2 → no divide → divisor=6
divisor=6: 7%6=1 → no divide → divisor=7
divisor=7: 7<7 es False → sale del bucle
flag=True → "El numero es primo" ✅

N = 9
divisor=2: 9%2=1 → no divide → divisor=3
divisor=3: 9%3=0 → flag=False → "No es primo porque lo divide 3" → break
flag=False → no muestra nada más ✅

🎯 Lo que dominaste con este ejercicio

Concepto                             ¿Cómo lo aplicaste?
Flag / Bandera                flag = True inicial, cambia a False si encontrás divisor
Bucle while                   Probás divisores uno por uno hasta n-1
Operador %                    Detectás si un número divide exactamente
break                         Cortás el bucle apenas encontrás el primer divisor
ZONA A / ZONA B               Lógica dentro del bucle vs. resultado final después

"""
"""
🧠 Bonus matemático (curiosidad)

Pregunta: ¿Qué pasa si el usuario ingresa n = 1?

Mirá el código: divisor = 2, y la condición while divisor < n → 2 < 1 es False desde el principio. 
El bucle no arranca, flag queda en True, y el programa dice "El numero es primo".
Pero matemáticamente, el 1 NO se considera primo. 
¿Por qué? Porque los números primos tienen exactamente 2 divisores (1 y él mismo), y el 1 solo tiene 1 divisor.

Por esto se agrega una validación al inicio para manejar este caso especial? Sería algo como:
if n <= 1:
    print("El numero no es primo")
else:
    # ... todo el código que ya tenés VER EL PRIMER EJERCICIO
"""