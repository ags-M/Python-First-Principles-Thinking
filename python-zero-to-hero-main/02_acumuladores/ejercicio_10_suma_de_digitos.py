# ============================================================
# Ejercicio 10: Suma de dígitos
# Categoría: 02_acumuladores
# ============================================================
#
# ENUNCIADO:
# Pedile al usuario un número entero y mostrá la suma de sus dígitos. Ej: 1234 → 1+2+3+4 = 10.
#
"""  Primero separo los digitos utilizando resto y despues division entera
SI EL NUM = 123
#123 % 10 → obtienes el dígito 3. Luego 123 // 10 → el número queda en 12.
#12 % 10 → obtienes el dígito 2. Luego 12 // 10 → el número queda en 1.
#1 % 10 → obtienes el dígito 1. Luego 1 // 10 → el número queda en 0.

"""
# 1. Pedimos el número
num = int(input("Ingresá un número entero: "))

# 2. Preparamos una "cajita" vacía para guardar la suma
suma = 0 # acumulador

# 3. Mientras el número sea mayor a 0, seguimos sacando dígitos
while num > 0: # es el bucle termina cuando el num = 0. El num se va achicando en cada vuelta
    digito = num % 10          # Paso A: Sacamos el último dígito
    suma = suma + digito       # Paso B: Lo agregamos a la suma
    num = num // 10            # Paso C: Achicamos el número (le quitamos ese dígito)

# 4. Mostramos el resultado final
print("La suma de los dígitos es:", suma)

"""
_________________________________________________________________________________________________________
Vuelta del while  ¿num > 0?     digito = num % 10      suma = suma + digito             num = num // 10 
                                ( el resto % Saca)        (Sumar digitos)          (division entera //Achica)
_________________________________________________________________________________________________________
Inicio                                                        suma = 0                      num = 123
_________________________________________________________________________________________________________

Vuelta 1        Sí (123 > 0)       digito = 3           suma = 0 + 3 = 3                     num = 12
_________________________________________________________________________________________________________
Vuelta 2        Sí (12 > 0)        digito = 2           suma = 3 + 2 = 5                     num = 1
_________________________________________________________________________________________________________
Vuelta 3        Sí (1 > 0)         digito = 1           suma = 5 + 1 = 6                     num = 0
________________________________________________________________________________________________________
Vuelta 4        No (0 no es > 0)
_________________________________________________________________________________________________________
¡El while se detiene!

 Esta es una técnica para aprender a programar. Se llama "trazabilidad" (o debugging básico), 
 y consiste en hacer que el programa te "cuente" qué está haciendo en cada paso.

El código con los "rastreadores" (prints) agregué varios print dentro del while para ver cada acción:
"""
#--------------------------------------------
print("*" * 30)
#--------------------------------------------

# Pedimos el número (imaginemos que el usuario escribe 123)
num = int(input("Ingresá un número entero: "))

# Preparamos la suma
suma = 0

print(f"\n--- INICIO: num vale {num} y suma vale {suma} ---")

# El bucle
while num > 0:
    digito = num % 10
    print(f"  1. Saqué el último dígito: {digito}")
    
    suma = suma + digito
    print(f"  2. Lo sumé. Ahora la suma vale: {suma}")
    
    num = num // 10
    print(f"  3. Achiqué el número. Ahora num vale: {num}")
    print("  ---------------------------------------")
print(f"¡TERMINÉ! La suma final de los dígitos es: {suma}")

"""¿Por qué esto te hace hacer "clic"?
Porque dejás de adivinar y ves la realidad:
Entendés el % 10: Ves claramente cómo en el paso 1 siempre "aparece" el número de la derecha (3, luego 2, luego 1).
Entendés el suma = suma + digito: Ves cómo la variable suma no es mágica, va acumulando: empieza en 0, pasa a 3, 
luego a 5, luego a 6.
Entendés el // 10: Ves cómo la variable num se va "comiendo" su propia cola: 123 → 12 → 1 → 0.
Entendés por qué frena el while: En la última vuelta, num queda en 0. El while pregunta: "¿Es 0 mayor que 0?". 
La respuesta es NO, y por eso el bucle se detiene 
y salta al mensaje final de "¡TERMINÉ!".
"""
