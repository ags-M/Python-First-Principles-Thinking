# ##################################################################
# #                                                                #
# #           LECCIÓN 3 — OPERADORES                               #
# #                                                                #
# #  Objetivo: Dominar los operadores aritméticos                  #
# #  (+, -, *, /, //, %, **), los de comparación                   #
# #  (==, !=, <, >, <=, >=) y los lógicos (and, or, not).          #
# #                                                                #
# ##################################################################


# ==================================================================
# NIVEL FÁCIL — Aritmética básica
# ==================================================================


# ------------------------------------------------------------------
# Ej. 3.1  [FÁCIL]
# ------------------------------------------------------------------
# Calculá el área de un rectángulo: base = 5 y altura = 3.
# Usá el operador * y mostrá el resultado con un mensaje claro.
#
# Pista: area = base * altura
#
# --- Tu solución: -------------------------------------------------
base = 5
altura = 3
area = base * altura
print(f"El area del rectangulo es {area}")

# ------------------------------------------------------------------
# Ej. 3.2  [FÁCIL]
# ------------------------------------------------------------------
# Tenés 1500 pesos y comprás un producto de 875.
# Calculá cuánto te sobra usando el operador - y mostralo con
# un mensaje.
#
# Pista: vuelto = dinero - precio
#
# --- Tu solución: -------------------------------------------------
dinero = 1500
precio_producto = 875
resto = dinero - precio_producto
print(f"Despues de comprar el producto me sobro:${resto}")


# ------------------------------------------------------------------
# Ej. 3.3  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario dos números (como int) y mostrá su SUMA usando
# + y su RESTA usando -, en dos mensajes distintos.
#
# Pista: dos print() con los dos resultados.
#
# --- Tu solución: -------------------------------------------------
num1 = int(input("escribe un numero: "))
num2 = int(input("escribe un numero: "))
suma = num1 + num2
resta = num1 - num2
print(f"La suma de los numeros da: {suma}")
print(f"La resta de los numeros da: {resta}")

# ------------------------------------------------------------------
# Ej. 3.4  [FÁCIL]
# ------------------------------------------------------------------
# Calculá el promedio de tres notas: 7, 8 y 9.
# Usá + para sumar y / para dividir por 3. Mostrá el resultado.
#
# Pista: promedio = (n1 + n2 + n3) / 3
#
# --- Tu solución: -------------------------------------------------
n1 = 7
n2 = 8
n3 = 9
promedio = (n1 + n2 + n3) / 3
print(f"El promedio de mis notas es de:{promedio}")


# ------------------------------------------------------------------
# Ej. 3.5  [FÁCIL]
# ------------------------------------------------------------------
# Verificá si 15 es mayor que 10 usando el operador >.
# Guardá el resultado en una variable y mostrá:
# debería dar True.
#
# Pista: resultado = 15 > 10
#
# --- Tu solución: -------------------------------------------------
n1 = 15
n2 = 10
resultado = n1 > n2
print(f"El resultado de n1 mayor que n2 es:{resultado}")

# ==================================================================
# NIVEL MEDIO — //, %, ** y comparaciones
# ==================================================================


# ------------------------------------------------------------------
# Ej. 3.6  [MEDIO]
# ------------------------------------------------------------------
# Tenés 100 caramelos para repartir entre 7 chicos.
# Usá // para ver cuántos le tocan a cada uno y % para ver
# cuántos sobran. Mostrá ambos resultados.
#
# Pista: por_chico = 100 // 7  ;  sobran = 100 % 7
#
# --- Tu solución: -------------------------------------------------
caramelos = 100
chicos = 7
por_chico = caramelos // chicos
print(f"Al repartir {caramelos} caramelos en {chicos} chicos le tocan a cada uno {por_chico}")
resto = caramelos % chicos
print(f"Los caramelos que sobran son: {resto}")
print("-"*10)
caramelos, chicos = 100, 7; print(f"A cada uno le tocan {caramelos // chicos}\nSobran {caramelos % chicos}")

# ------------------------------------------------------------------
# Ej. 3.7  [MEDIO]
# ------------------------------------------------------------------
# Calculá el precio con descuento de un producto.
# Precio original: 2000. Descuento: 15%.
# Usá porcentaje (0.15) y multiplicación. Mostrá el precio final.
#
# Pista: final = precio * (1 - 0.15)
#
# --- Tu solución: -------------------------------------------------
precio = 2000
descuento = 0.15
precio_final = round(precio * (1 - descuento))
print(f"El producto tiene un precio final con descuento de: {precio_final}")

# ------------------------------------------------------------------
# Ej. 3.8  [MEDIO]
# ------------------------------------------------------------------
# Verificá si un usuario puede entrar a un boliche.
# Pedí su edad y comprobá con >= si tiene 18 o más.
# Mostrá True o False.
#
# Pista: puede = edad >= 18
#
# --- Tu solución: -------------------------------------------------
edad = int(input("decime tu edad: "))
ingresa = edad >= 18
print(f"el usuario puede ingresar {ingresa}")

print("-" * 12)

edad = int(input("decime tu edad: "))
if edad >= 18:
    print("puede ingresar al boliche")
else:
    print("No puede ingresar al boliche")


# ------------------------------------------------------------------
# Ej. 3.9  [MEDIO]
# ------------------------------------------------------------------
# Combiná condiciones con and.
# Una persona puede votar si tiene 18 años o más Y tiene DNI.
# Usá variables:
#   edad = 20
#   tiene_dni = True
# Mostrá el resultado de la condición combinada.
#
# Pista: puede_votar = (edad >= 18) and tiene_dni
#
# --- Tu solución: -------------------------------------------------
edad = 20
tiene_dni = True
puede_votar= edad >= 18 and tiene_dni
print(puede_votar)

# ------------------------------------------------------------------
# Ej. 3.10  [MEDIO]
# ------------------------------------------------------------------
# Calculá el CUADRADO y el CUBO de un número usando el operador
# ** (potencia).
# Pedí el número al usuario y mostrá ambos resultados.
#
# Pista: cuadrado = n ** 2  ;  cubo = n ** 3
#
# --- Tu solución: -------------------------------------------------
numero = int(input("decime un numero entero: "))
cuadrado = numero ** 2
cubo = numero ** 3
print(f"El cuadrado del numero: {numero} es = {cuadrado} y el cubo de ese numero es igual a: {cubo}")

# ==================================================================
# NIVEL DIFÍCIL — Operadores combinados
# ==================================================================


# ------------------------------------------------------------------
# Ej. 3.11  [DIFÍCIL]
# ------------------------------------------------------------------
# Hacé un programa que calcule el sueldo neto de un trabajador.
# Datos:
#   sueldo_bruto = 500000
# Descuentos:
#   - jubilación: 11%
#   - obra social: 3%
# También calculá el aguinaldo (sueldo_bruto / 12).
# Mostrá el desglose de cada descuento y el sueldo neto final.
#
# Pista: jubilacion = sueldo_bruto * 0.11
#        neto = bruto - jubilacion - obra_social
#
# --- Tu solución: -------------------------------------------------
sueldo = 500000
jubilacion = sueldo * 0.11
print(jubilacion)
obra_social = sueldo * 0.03
print(obra_social)
aguinaldo = sueldo / 12
sueldo_total = round((sueldo - (jubilacion + obra_social) + aguinaldo), 2)
print(f"El salario neto es de: ${sueldo_total}")



# ------------------------------------------------------------------
# Ej. 3.12  [DIFÍCIL]
# ------------------------------------------------------------------
# Creá un programa que determine si un año es bisiesto.
# Regla: es bisiesto si es divisible por 4 Y
#        (NO divisible por 100  O  divisible por 400)
# Combiná %, and, or y not.
# Probá con los años 2024, 1900 y 2000 y mostrá el resultado de
# cada uno.
#
# Pista:
#   bisiesto = (anio % 4 == 0) and ((not anio % 100 == 0) or (anio % 400 == 0))
#
# --- Tu solución: -------------------------------------------------
año1 = 2024
año2 = 1900
año3 = 2000
bisiesto1 = (año1 % 4 == 0) and ((not año1 % 100 == 0) or (año1 % 400 == 0))
bisiesto2= (año2 % 4 == 0) and ((not año2 % 100 == 0) or (año2 % 400 == 0))
bisiesto3 = (año3 % 4 == 0) and ((not año3 % 100 == 0) or (año3 % 400 == 0))
print(f"El año 2024 es bisiesto: {bisiesto1}")
print(f"El año 1900 es bisiesto: {bisiesto2}")
print(f"El año 2000 es bisiesto: {bisiesto3}")
# ------------------------------------------------------------------
# Ej. 3.13  [DIFÍCIL]
# ------------------------------------------------------------------
# Hacé un programa que reciba el monto de una compra y decida
# qué descuento aplicar:
#   - si la compra es >= 10000  →  descuento del 20%
#   - si es >= 5000             →  descuento del 10%
#   - sino                      →  descuento del 0%
# Usá comparaciones y operadores lógicos.
# Mostrá el descuento aplicado y el precio final.
#
# Pista: podés armar tres condiciones por separado o una
# combinada con and.
#
# --- Tu solución: -------------------------------------------------
compra = float(input("ingresa el importe de tu compra: $ "))
descuento = (compra >= 10000) * 20 + (5000 <= compra < 10000) * 10 + (compra < 5000) * 0
monto_descuento = compra * descuento / 100
precio_final = compra - monto_descuento
print(f"El descuento aplicado: {descuento}%")
print(f"El precio final: ${precio_final}")

# ------------------------------------------------------------------
# Ej. 3.14  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá el costo total de un viaje:
#   - 5 días de hotel a 8000 por noche
#   - 3 excursiones de 4500 cada una
#   - comida a 3000 por día
# Usá distintos operadores (*, +).
# Mostrá cada subtotal (hotel, excursiones, comida) y el total
# del viaje.
#
# Pista:
#   hotel = 5 * 8000
#   excursiones = 3 * 4500
#   comida = 5 * 3000
#
# --- Tu solución: -------------------------------------------------
hospedaje_noche = 8000
excursion = 4500
comida = 3000
hotel = hospedaje_noche * 5
print(f"costo de hotel por 5 dias es: {hotel}")
diversion = excursion * 3
print(f"costo de diversion por 3 dias {diversion}")
alimentos = comida * 5
print(f"costo de alimentos por 5 dias es: {alimentos}")
viaje_costo_total = hotel + diversion + alimentos
print(f"El costo final del viaje es de: $ {viaje_costo_total}")

# ------------------------------------------------------------------
# Ej. 3.15  [DIFÍCIL]
# ------------------------------------------------------------------
# Hacé un programa que verifique si una persona puede sacar
# licencia de conducir.
# Debe tener entre 17 y 65 años, Y no tener deudas pendientes,
# O tener un aval.
# Combiná varias comparaciones con and, or y not.
# Probá con dos casos distintos (uno que sí pueda, otro que no)
# y mostrá el resultado de cada uno.
#
# Pista:
#   edad_ok = 17 <= edad <= 65
#   Caso A: 30 años, sin deudas.
#   Caso B: 70 años, con aval.
#
# --- Tu solución: -------------------------------------------------
#CASO DE 30 AÑOS:
edad = int(input("Ingresá tu edad: "))
tiene_deudas = input("¿Tenés deudas? (s/n): ").lower() == "s"
tiene_aval = input("¿Tenés aval? (s/n): ").lower() == "s" #aval es un garante de pago de deuda!!!
edad_ok = 17 <= edad <= 65
puede_sacar_licencia = edad_ok and (not tiene_deudas or tiene_aval)
print(f"¿Podés sacar la licencia?: {puede_sacar_licencia}")

print("-" * 12)

#CASO DE 70 AÑOS
edad = 70
tiene_deudas = input("¿Tenés deudas? (s/n): ").lower() == "s"
tiene_aval = input("¿Tenés aval? (s/n): ").lower() == "s"  # aval es un garante de pago de deuda
edad_ok = 17 <= edad <= 65  # 17 <= 70 <= 65 → False
puede_sacar_licencia = edad_ok and (not tiene_deudas or tiene_aval)  # False and ... → False
print(f"¿Podés sacar la licencia?: {puede_sacar_licencia}")

# ##################################################################
# #                                                                #
# #  ¡Llegaste al final!                                           #
# #                                                                #
# #  Antes de avanzar a la Lección 4 (if / elif / else),           #
# #  asegurate de haber resuelto los tres niveles de cada          #
# #  lección. Mandame este archivo .py con tus soluciones          #
# #  y te lo devuelvo corregido ejercicio por ejercicio.           #
# #                                                                #
# ##################################################################
