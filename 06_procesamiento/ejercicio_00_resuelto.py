"""
📘 CATEGORÍA 6 — Procesamiento de números
📝 Enunciado del worked example (Ejercicio 27)
Invertir un número entero usando solo while. Ejemplo: 1234 → 4321.

"""
#.- 💻 Código resuelto:

# 1. Pedimos el número al usuario
n = int(input("Ingresá un número entero: "))

# 2. Trabajamos con el valor absoluto para que funcione también con negativos
#    (ej: -123 → invertimos 123 → 321, y al final le ponemos el signo)
n_es_negativo = n < 0
n = abs(n)

# 3. Inicializamos el acumulador que va CONSTRUYENDO el número invertido
#    ¿Por qué 0? Porque vamos a ir "pegando" dígitos a la derecha.
n_invertido = 0
# 4. Mientras queden dígitos por procesar...
while n > 0:
    digito = n % 10                         # Paso A: Sacamos el último dígito
    n_invertido = n_invertido * 10 + digito #(la formula es el Constructor del numero invertido) 
                                            #Paso B: ¿Por qué multiplicar por 10?
                                            # Porque en matemática, multiplicar por 10 "corre" todos los dígitos 
                                            # un lugar a la izquierda y deja un cero a la derecha, listo 
                                            # para ser reemplazado.Lo "pegamos" a la derecha del invertido
  
    n = n // 10                             # Paso C: (La Guillotina) Achicamos el número original. 
                                            # Esto elimina el último dígito del número original.

# 🛑 Fin del bucle
#Ahora n = 0. La condición n > 0 es Falsa en el while. El bucle se detiene. ¡Y n_invertido quedó realizado!

# 5. Si el número original era negativo, le devolvemos el signo
if n_es_negativo:
    n_invertido = -n_invertido

# 6. Mostramos el resultado
print(f"El número invertido es: {n_invertido}")

# 📊 Traceo manual (hacelo en papel para numero = 1234)

"""
__________________________________________________________________________________________________________________________

Iteración     n (entrada)    ¿n > 0?    digito = n % 10    n_invertido = n_invertido * 10 + digito    n = n // 10
__________________________________________________________________________________________________________________________

  Inicio         1234            —              —                     n_invertido = 0                      —
__________________________________________________________________________________________________________________________

  1              1234           Sí                4                   0 * 10 + 4 = 4                      123
__________________________________________________________________________________________________________________________

  2               123           Sí                3                   4 * 10 + 3 = 43                     12
__________________________________________________________________________________________________________________________

  3                12           Sí                2                   43 * 10 + 2 = 432                   1
__________________________________________________________________________________________________________________________

  4                 1           Sí                1                   432 * 10 + 1 = 4321                 0
__________________________________________________________________________________________________________________________

  5                 0          No → sale          —                          —                             —
__________________________________________________________________________________________________________________________

Resultado final: 4321 ✅

"""

