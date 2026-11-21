
# CONSIGNA: saber si un numero es primo, saber cuantos numeros dentro de el son primos y decir cuales son

while True:
        
        # ═══════════════════════════════════════════════════════════
        # 🛡️ Validar que el usuario ingrese un número
        # ═══════════════════════════════════════════════════════════
        while True:
         try:
          n_limite_original = int(input("Ingresá un número entero: "))
        
          break
         except ValueError:
            print("⚠️ Error: debés ingresar un número entero válido.")

        # ═══════════════════════════════════════════════════════════
        # VALIDACIÓN: Convertir a valor absoluto si es negativo
        # ═══════════════════════════════════════════════════════════
        es_negativo = n_limite_original < 0   # ⚡ Guardo si fue negativo

        if es_negativo:
            
          print(f"Ingresaste un numero negativo. Tomaré de {n_limite_original} el valor absoluto: {abs(n_limite_original)}")

        n_limite = abs(n_limite_original)

        # ═══════════════════════════════════════════════════════════
        # VALIDACIÓN: 0 y 1 NO son primos
        # ═══════════════════════════════════════════════════════════
        if n_limite <= 1:
            print(f"El número {n_limite} NO es un número primo")
            print(f"No hay números primos menores o iguales a {n_limite}")
            
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
                print(f"El número {n_limite} ES un número primo")
            else:
                print(f"El número {n_limite} NO es un número primo")

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

            print(f"Hay {contador_primos} números primos entre el 2 y el {n_limite}")
            print(f"De acuerdo al numero ingresado: {n_limite_original} los números primos son: {lista_n_primos}")

            # ═══════════════════════════════════════════════════════
            # 📊 PARTE 4: Mostrar estadísticas de los primos encontrados
            # ═══════════════════════════════════════════════════════
            if lista_n_primos:
             suma_primos = sum(lista_n_primos)
             promedio = suma_primos / len(lista_n_primos)
             mayor = max(lista_n_primos)
             menor = min(lista_n_primos)
            
             print(f"\n📊 ESTADÍSTICAS:")
             print(f"   Suma de los primos: {suma_primos}")
             print(f"   Promedio: {promedio:.2f}")
             print(f"   Primo mayor: {mayor}")
             print(f"   Primo menor: {menor}")

            # ═══════════════════════════════════════════════════════
            # 🔁 PARTE 6: Permitir ejecutar varias veces sin cerrar el programa
            # ═══════════════════════════════════════════════════════
            
            seguir = input("\n¿Querés ingresar otro número? (s/n): ").lower()
            if seguir != 's':
                print("¡Gracias por usar el programa!")
                
                break
#_________________________________________________________________________________________________
"""
         ESTO LO REALIZARE EN EL MOMENTO APROPIADO PERO ES PARA TENER EN CUENTA

✅ Optimización con raíz cuadrada
Muestra que entendés algoritmos (muy útil para números grandes)
En vez de probar divisores hasta n-1, probá solo hasta la raíz cuadrada de n. Es mucho más rápido:

import math

# Reemplazá el while interno por:
while divisor <= math.isqrt(n_dentro_de_n_limite):
    if n_dentro_de_n_limite % divisor == 0:
        flag = False
        break
    divisor += 1

Ejemplo: para verificar si 1000003 es primo, el código original hace ~1.000.000 divisiones. 
Con la raíz cuadrada, solo hace ~1000. ¡1000 veces más rápido!
__________________________________________________________________________________________

👯 5. Mostrar los primos gemelos (bonus matemático):
Los primos gemelos son pares de primos que difieren en 2 (ej: 3 y 5, 11 y 13):

gemelos = [(lista_n_primos[i], lista_n_primos[i+1]) 
           for i in range(len(lista_n_primos)-1) 
           if lista_n_primos[i+1] - lista_n_primos[i] == 2]

if gemelos:
    print(f"\n👯 Primos gemelos encontrados: {gemelos}")
__________________________________________________________________________________________

🔢 6. Mostrar la factorización prima del número ingresado
def factorizar(n):
    factores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1
    return factores

print(f"\n🔢 Factorización de {n_limite_original}: {factorizar(n_limite)}")
# Ejemplo: 60 → [2, 2, 3, 5]
__________________________________________________________________________________________

📁 7. Guardar los resultados en un archivo:

with open("primos_resultados.txt", "a") as archivo:
    archivo.write(f"Límite: {n_limite_original} | Primos: {lista_n_primos}\n")
print("✅ Resultados guardados en 'primos_resultados.txt'")

🎯 Se ve que el ejercicio se completa con:

✅ Validación con try/except  ------> Evita errores del usuario
✅ Bucle para repetir         ------> Más práctico
✅ Estadísticas (suma, promedio, mayor, menor) --------> Agrega valor
✅ Optimización con raíz cuadrada ---------> Muestra que entendés algoritmos con el 4.-Optimización con raíz cuadrada
                                                                       
""" 
#     
