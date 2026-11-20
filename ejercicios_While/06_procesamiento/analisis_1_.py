"""
🟡 ANALISIS PARA COMPRENDER COMO UN N es primo:

🐍 primero deberia saber si el n que introdujo el usuario es primo = ej 10 ?, 

🐍 segundo saber si los numeros del 2 al 10 algunos son o no primos 

🐍y tercero decir cuales son? si?
"""
# primera etapa
n_limite = int(input("ingresa un numero ENTERO positivo mayor que 1: "))
n_limite = abs(n_limite)   # ⚡ Si ingresás -7, se convierte en 7
divisor = 2
while divisor < n_limite:
    if n_limite % divisor == 0: # Si el número es divisible por otro (el residuo es 0), significa que NO es primo.
       print(f"el numero {n_limite} NO es un numero primo")
       break
    divisor += 1
else:
    print(f"el numero {n_limite} ES un numero primo")

"""
¿Por qué funciona?
Si encuentra divisor → imprime "no es primo" → hace break → el else NO se ejecuta
Si NO encuentra divisor → el bucle termina normalmente → el else SÍ se ejecuta → imprime "es primo"

"""
#--------------------------------------------
print("-" * 50)
#--------------------------------------------
# segunda etapa, usando flag

n_limite = int(input("ingresa un numero Entero Positivo y mayor que 1: "))
n_limite = abs(n_limite)   # ⚡ Si ingresás -7, se convierte en 7
divisor = 2
flag = True # flag = True → "asumo que es primo"
while divisor < n_limite:
    if n_limite % divisor == 0: # Si el número es divisible por otro (el residuo es 0 !!!), significa que NO es primo.
       flag = False # flag = False → "significa que encontre un numero que no es primo"
    divisor += 1 #el divisor += 1 esta fuera del if por eso no esta identado

if flag:# el if flag esta fuera del while por eso NO esta identado, es decir adento de él, solo alineado 
        # ( me hace recordar al salmo 91, el que habita a la sombra del omnipotente ESTA IDENTADO!!! y aca no!! JAJAJA)
    print(f"el numero {n_limite} ES un numero primo")
else: 
    print(f"el numero {n_limite} NO es un numero primo")
     # ¿Por qué? Si el bucle termina y flag sigue siendo True → significa que no se encontró ningún divisor → es primo
               # Si flag es False → en else se imprime "NO es un numero primo"

#____________________________________________________________________________________________
#📊 Traceo manual
#____________________________________________________________________________________________

# iteracion     valor del contador al entrar  **se cumple divisor < n_limite      que imprime
#                                                     n_limite = 7
#____________________________________________________________________________________________
#valor inicial del contador divisor es igual = 2
#____________________________________________________________________________________________

#     1                      2                    si  2 < 7                     
#     2                      3                    si  3 < 7                           -
#     3                      4                    si  4 < 7                           -
#     4                      5                    si  5 < 7                           - 
#     5                      6                    si  6 < 7                           -
#     6                      7                    NO  7 < 7# 
#                                           no **: sale del bucle        imprime ES un numero primo
#____________________________________________________________________________________________

#--------------------------------------------
print("-" * 50)
#--------------------------------------------
# tercera etapa 

# CONSIGNA: saber si un numero es primo, saber cuantos numeros dentro de el son primos y decir cuales son

n_limite_original = int(input("Ingresá un número entero: "))

# ═══════════════════════════════════════════════════════════
# VALIDACIÓN: Convertir a valor absoluto si es negativo
# ═══════════════════════════════════════════════════════════
es_negativo = n_limite_original < 0   # ⚡ Guardo si fue negativo

if es_negativo:
    print(f"Tomaré el valor absoluto: {abs(n_limite_original)}")

n_limite = abs(n_limite_original)

# ═══════════════════════════════════════════════════════════
# VALIDACIÓN: 0 y 1 NO son primos
# ═══════════════════════════════════════════════════════════
if n_limite <= 1:
    print(f"El número {n_limite_original} NO es un número primo")
    print(f"No hay números primos menores o iguales a {n_limite_original}")
    
else:
    # ═══════════════════════════════════════════════════════
    # PARTE 1: ¿El número ingresado por el usuario ES PRIMO?
    # ═══════════════════════════════════════════════════════
    divisor = 2
    flag_n_limite = True

    while n_limite > divisor:
        if n_limite % divisor == 0:
            flag_n_limite = False
            break
        divisor += 1

    if flag_n_limite:
        print(f"El número {n_limite_original} ES un número primo")
    else:
        print(f"El número {n_limite_original} NO es un número primo")

    # ═══════════════════════════════════════════════════════
    # PARTE 2 y 3: ¿Cuántos primos hay? ¿Cuáles son?
    # ═══════════════════════════════════════════════════════
    n_dentro_de_n_limite = 2
    lista_n_primos = []
    contador_primos = 0

    while n_dentro_de_n_limite <= n_limite:
        divisor = 2
        flag = True
        
        while n_dentro_de_n_limite > divisor:
            if n_dentro_de_n_limite % divisor == 0:
                flag = False
                break
            divisor += 1
        
        if flag:
            contador_primos += 1
            lista_n_primos.append(n_dentro_de_n_limite)
        
        n_dentro_de_n_limite += 1

    # ═══════════════════════════════════════════════════════
    # PARTE 4: Si el input fue negativo, muestro la lista en negativo
    # ═══════════════════════════════════════════════════════
    if es_negativo:
        lista_n_primos = [-n for n in lista_n_primos]   # ⚡ Convierto a negativos

    print(f"Hay {contador_primos} números primos entre el 2 y el {n_limite_original}")
    print(f"Los números primos son: {lista_n_primos}")
    
"""
🎯 La estructura completa:
┌─────────────────────────────────────────────┐
│ VALIDACIÓN: n_limite <= 1                   │
│ → Si es True: mostrar mensaje y terminar    │
│ → Si es False: continuar                    │
└─────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────┐
│ PARTE 1: ¿n_limite es primo?                │
└─────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────┐
│ PARTE 2 y 3: Recorrer 2 a n_limite          │
│ - Bucle externo + bucle interno             │
│ - Contar y guardar primos                   │
└─────────────────────────────────────────────┘

🎯 La lógica del bucle interno:

Para cada número (n_dentro_de_n_limite):
  
  1. divisor = 2 (empiezo probando el 2)
  2. flag = True (asumo que es primo)
  
  3. Bucle interno:
     while n_dentro_de_n_limite > divisor:
       Si n_dentro_de_n_limite % divisor == 0:
         flag = False ← encontré un divisor, NO es primo
       divisor += 1 ← pruebo el siguiente divisor ( arranco con 2 despues en la otra vuelta sumo 1 y seguimos)
  
  4. Cuando sale del bucle interno:
     Si flag == True → es primo → guardar
     Si flag == False → no es primo → ignorar

🎯 No hay salto, hay secuencia
Python ejecuta las líneas una después de otra, de arriba hacia abajo. 

Cuando el bucle interno termina (porque n_dentro_de_n_limite > divisor es False, Y todos en el bucle interno 
van haciendo divisor 2 con numero de adentro del n_limite (MAS bucle divisor += 1), hay un punto en que 
el n_dentro_de_n_limite hace que por ejemplo que 5 > 5 entonces eso el FALSE ),   
Python simplemente baja a la siguiente línea entra en el flag.
if flag y realiza lo que debe. Para luego entrar en por n_dentro_de_n_limite += 1 reinicia el bucle externo

┌─────────────────────────────────────────────┐
│ BUCLE EXTERNO (para cada número)            │
│                                             │
│  divisor = 2                                │
│  flag = True                                │
│                                             │
│  ┌──────────────────────────────────────┐   │
│  │ BUCLE INTERNO                        │   │
│  │                                      │   │
│  │  Prueba divisores uno por uno        │   │
│  │  Si encuentra uno → flag = False     │   │
│  │                                      │   │
│  │  Cuando termina → SALE               │   │
│  └──────────────────────────────────────┘   │
│                    ↓                        │
│                    ↓ (baja a la siguiente   │
│                    ↓  línea, no salta nada) │
│                    ↓                        │
│  if flag:                                   │
│      contador_primos += 1                   │
│      lista_n_primos.append(...)             │
│                                             │
│  n_dentro_de_n_limite += 1                  │
│                                             │
│   LUEGO HACE LOS PRINT CORRESPONDIENTE      │
└─────────────────────────────────────────────┘

### 📊 Tabla resumen: ¿Es primo o no?

| Número | Divisores probados    | ¿Encontró divisor? | flag final | ¿Se guarda? |
|:------:|:------------------:   |:------------------:|:----------:|:-----------:|
|   2    |     (ninguno)         |         No         |    True    | ✅ Sí       |
|   3    |         2             |         No         |    True    | ✅ Sí       |
|   4    |        2, 3           |       Sí (2)       |   False    | ❌ No       |
|   5    |       2, 3, 4         |         No         |    True    | ✅ Sí       |
|   6    |     2, 3, 4, 5        |       Sí (2)       |   False    | ❌ No       |
|   7    |    2, 3, 4, 5, 6      |         No         |    True    | ✅ Sí       |
|   8    |   2, 3, 4, 5, 6, 7    |       Sí (2)       |   False    | ❌ No       |
|   9    |  2, 3, 4, 5, 6, 7, 8  |      Sí (3)        |   False    | ❌ No       |
|  10    | 2, 3, 4, 5, 6, 7, 8, 9|    Sí (2)          |   False    | ❌ No       |

**Resultado final:** `lista_n_primos = [2, 3, 5, 7]`

💡 La clave
El bucle interno prueba todos los divisores posibles (desde 2 hasta n-1). 
Si encuentra al menos uno que divida exactamente (resto 0), marca flag = False. 
Si después de probar todos no encuentra ninguno, flag queda en True y el número es primo.

"""
"""
Vuelta 3: n_dentro_de_n_limite = 4                   ejemplo

divisor = 2
flag = True

Bucle interno:
  while 4 > 2 → TRUE (entra)
    4 % 2 = 0 → flag = False ← ¡ENCONTRÓ DIVISOR! es false por que encontro un divisor no es true eso significa
    divisor += 1 → divisor ahora vale 3
  
  while 4 > 3 → TRUE (entra)
    4 % 3 = 1 (no es 0) → flag sigue False
    divisor += 1 → divisor ahora vale 4
  
  while 4 > 4 → FALSO (sale)
  → flag queda en False

if flag: → NO ENTRA (flag es False)
  → No suma al contador
  → No agrega a la lista

n_dentro_de_n_limite += 1 → ahora vale 5

"""