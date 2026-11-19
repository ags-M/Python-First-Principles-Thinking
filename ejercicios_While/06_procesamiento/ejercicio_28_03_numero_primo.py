"""
⭐ ANALISIS DE BUCLES ANIDADOS ⭐
"""

n_limite = int(input("ingresa un numero: "))
n_dentro_n_limite = 2 # Contador persistente que avanza entre vueltas, cuenta que numero esta verificando en n_limite
contador_primos = 0 # Contador persistente que avanza entre vueltas, cuenta cuantos numeros primos encontro
n_primos = []  # ← ACÁ, antes del bucle externo (como contador_primos), lista que guarda los numeros primos

while n_dentro_n_limite <= n_limite: # mientras se cumpla la condicion del contador de numeros que sean menores
                                     # dentro del numero que indico el usuario         
                                     # comienza el Bucle EXTERNO: recorre 2, 3, 4... 10 ENTONCES HACE EL RECORRIDO
    
    # Para CADA número, verificamos si es primo
    divisor = 2   # ← Contador temporal se reinicia en cada vuelta del bucle externo, cuenta que divisor esta probando
                  # para cada numero del numero que ingreso el usuario
    flag = True   # ← Asumir que es primo
    

    while n_dentro_n_limite > divisor:    # Bucle INTERNO: prueba divisores. Mientras se cumpla la condicion de que
                                          # el numero que divide a los numeros que integran el numero que ingreso el
                                          # usuario sea MENOR el bucle sigue haciendo ....              
        if n_dentro_n_limite % divisor == 0:  # ← ¿El número actual es divisible por divisor? si el resto es CERO 
                                              # no es un numero primo Flag False y contador divisor busca otro numero..
            flag = False
        divisor += 1 # contador que sigue dividiendo a los numeros que siguen en n_dentro_n_limite

    if flag:
       contador_primos += 1 # ACA se suman la cantidad de primos que se averiguan dentro del n_limite
       n_primos.append(n_dentro_n_limite)  # ← ACÁ, se agregan a la lista los numeros que son primos de cada una de las
                                           # cuentas que se realizan con resto pero dice quienes son     
    n_dentro_n_limite += 1                # ← Avanzar al siguiente número

# Despues del bucle externo, mostrar el resultado:
print(f"Hay {contador_primos} numeros primos entre el 2 y el {n_limite}")
print(f"Los primos son: {n_primos}")
