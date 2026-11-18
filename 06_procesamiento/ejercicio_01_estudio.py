# realizar 🎯 clave entre CONTAR y SUMAR digitos:

n = int(input("ingresa un numero entero: "))
contador_digitos = 0
suma = 0    # Sumamos 1 por cada dígito que encontramos
            # Empezamos la suma en 0 (porque 0 + cualquier cosa = esa cosa)
# n = 456            # Prueba con 456, -85, 0, 12345

# PASO 1: Neutralizar
n = abs(n)

# PASO 2: Excepción del cero
if n == 0:
    suma = 0
else:
    # PASO 3: Cortar y Sumar
    suma = 0
    while n > 0:
        digito = n % 10        # Extraemos el dígito (ej: de 456 saca 6)
        contador_digitos += 1  #💡 CONTADOR: contamos que hay 1 mas y lo sumo, primero 0 y despues ....
        suma += digito        # 💡 ACUMULADOR: Lo sumamos a la suma total
        n = n // 10          # Cortamos ese dígito (456 pasa a 45)

print("La suma de los dígitos es:", suma)
print("El numero de los dígitos es:", contador_digitos)
#📊 Traceo manual
#____________________________________________________________________________________________

# iteracion   Vuelta del while    n actual       digito = n % 10        suma += digito
#____________________________________________________________________________________________
#valor inicial del contador es igual a: 1 con n = 456
#____________________________________________________________________________________________
#     1             1               456               6                     0 + 6 = 6   
#     2             2                45               5                     6 + 5 = 5                   
#     3             3                 4               4                    11 + 4 = 15 imprime
#     4                                                                   sale del bucle
#____________________________________________________________________________________________

""" 📌 Resumen del patrón para tu cuaderno:

Para SUMAR dígitos:

1ro.-   n = abs(n) → neutralizar

2do.-   if n == 0: suma = 0

3ro.-

while n > 0:
digito = n % 10
suma += digito ← ⭐ la clave
n = n // 10

"""