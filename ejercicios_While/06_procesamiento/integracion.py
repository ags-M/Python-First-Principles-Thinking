
# CONSIGNA: saber si un numero es primo, saber cuantos numeros dentro de el son primos y decir cuales son

while True:
    # ═══════════════════════════════════════════════════════════
    # 🛡️ 1. Validar que el usuario ingrese un número
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
    if n_limite_original < 0:
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
        # PARTE 1: ¿El número ingresado ES PRIMO?
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
            print(f"Los numeros a investigar dentro del {n_limite} son el {n_dentro_de_n_limite}") 
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

        print(f"Hay {contador_primos} números primos entre el 2 y el {n_limite}")
        print(f"Los números primos son: {lista_n_primos}")
    
    # ═══════════════════════════════════════════════════════════
    #  📊 3. Mostrar estadísticas de los primos encontrados
    # ═══════════════════════════════════════════════════════════
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

    # ═══════════════════════════════════════════════════════════
    # ¿Continuar?
    # ═══════════════════════════════════════════════════════════
    seguir = input("\n¿Querés ingresar otro número? (s/n): ").lower()

    if seguir != 's':
        print("¡Gracias por usar el programa!")
        break 