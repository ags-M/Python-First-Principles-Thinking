# 🛠️ CONSIGNA DECIR CUANTOS NUMEROS PRIMOS HAY EN UN NUMERO EJ: 100

"""
🧠 La idea general:
1ro.- un numero primo solo es divisible por 1 y por si mismo

2.- En lugar de verificar UN número (si es primo o no lo es), ahora vas a verificar TODOS 
los números desde 2 hasta el límite que te den (ej: 100), y contar cuántos son primos.
Recordar que 1 no es primo al igual que 0. Por esa razon el diviso empieza con 2

Pregunta para pensar: si querés verificar todos los números desde 2 hasta 100, ¿qué necesitás?

Respuesta: un bucle externo que recorra ese rango.

3.- los numeros del 2 al 100 seran recorridos por medio de un bucle interno
"""
n_limite = int(input("ingresa un numero: "))
n_dentro_n_limite = 2
contador_primos = 0
n_primos = []  # ← ACÁ, antes del bucle externo (como contador_primos)

while n_dentro_n_limite <= n_limite:          # Bucle EXTERNO: recorre 2, 3, 4... 10
    
    # Para CADA número, verificamos si es primo
    divisor = 2                           # ← Inicializar divisor para ESTE número
    flag = True                           # ← Asumir que es primo
    

    while divisor < n_dentro_n_limite:    # Bucle INTERNO: prueba divisores
        if n_dentro_n_limite % divisor == 0:  # ← ¿El número actual es divisible por divisor?
            flag = False
        divisor += 1

    if flag:
       contador_primos += 1 # ACA se suman la cantidad de primos en n_limite
       n_primos.append(n_dentro_n_limite)  # ← ACÁ, dentro del if flag
    
    n_dentro_n_limite += 1                # ← Avanzar al siguiente número

# Despues del bucle externo, mostrar el resultado:
print(f"Hay {contador_primos} numeros primos entre el 2 y el {n_limite}")
print(f"Los primos son: {n_primos}")



