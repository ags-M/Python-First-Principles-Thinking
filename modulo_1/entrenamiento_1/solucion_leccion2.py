
# ##################################################################
# #                                                                #
# #           LECCIÓN 2 — VARIABLES Y TIPOS DE DATOS              #
# #                                                                #
# #  Objetivo: Aprender a guardar información en variables,        #
# #  conocer los tipos int / float / str / bool, y usar            #
# #  print() e input() para mostrar y pedir datos.                 #
# #                                                                #
# ##################################################################


# ==================================================================
# NIVEL FÁCIL — Variables básicas
# ==================================================================


# ------------------------------------------------------------------
# Ej. 2.1  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "nombre" con tu nombre y otra "edad" con tu
# edad (como número entero).
# Imprimí ambas con un mensaje, por ejemplo:
#   Mi nombre es ... y tengo ... años
#
# Pista: asigná con = y mostrá con print().
#
# --- Tu solución: -------------------------------------------------
nombre = "Alejandro"
edad = 66
print(f"Mi nombre es {nombre} y tengo {edad} años")

# ------------------------------------------------------------------
# Ej. 2.2  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario su ciudad usando input() y guardala en una
# variable. Mostrá un saludo personalizado:
#   Vivís en ...
#
# Pista: input() devuelve texto, no hace falta convertir.
#
# --- Tu solución: -------------------------------------------------
ciudad = input("¿Cual es tu ciudad?: ")
print(f"Hola vivis en la ciudad {ciudad}")

# ------------------------------------------------------------------
# Ej. 2.3  [FÁCIL]
# ------------------------------------------------------------------
# Creá tres variables:
#   precio_producto = 1500      (int)
#   descuento       = 0.10      (float)
#   nombre_producto = "Remera"  (str)
# Imprimí cada una junto con su tipo usando type().
#
# Pista: print(type(precio_producto))
#
# --- Tu solución: -------------------------------------------------
precio_producto = 1500
print(type(precio_producto))
descuento= 0.10
print(type(descuento))
nombre_producto = "Remera"
print(type(nombre_producto))
# ------------------------------------------------------------------
# Ej. 2.4  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario su nombre y su año de nacimiento con dos
# input(). Guardá ambos en variables.
# Mostrá un mensaje:
#   Hola [nombre], naciste en [año]
#
# Pista: el año lo podés dejar como texto por ahora.
#
# --- Tu solución: -------------------------------------------------
nombre=input("decime tu nombre?: ")
año_nacido=input("decime en que año naciste?: ")
print(f"Hola {nombre} ud nació en el año: {año_nacido}")

# ------------------------------------------------------------------
# Ej. 2.5  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable booleana "mayor_edad" con el valor True o
# False según tu edad real.
# Imprimí un mensaje que diga si sos o no mayor de edad,
# usando esa variable.
#
# Pista: las variables bool solo valen True o False.
#
# --- Tu solución: -------------------------------------------------
edad = int(input("¿cuantos años tiene?: "))
mayor_edad = edad >= 18
print(f" ¿sos mayor de edad?: {mayor_edad}")

# ==================================================================
# NIVEL MEDIO — Conversión y tipos mixtos
# ==================================================================


# ------------------------------------------------------------------
# Ej. 2.6  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario dos números como texto con input().
# Convertí ambos a int y mostrá su suma.
# Acordate: input() siempre devuelve str, hay que convertir.
#
# Pista: int(input("..."))
#
# --- Tu solución: -------------------------------------------------
num1=(input("¿decime un numero?: "))
num1 = int(num1)
num2=(input("¿decime otro numero?: "))
num2 = int(num2)
suma = num1 + num2
print(suma)

# ------------------------------------------------------------------
# Ej. 2.7  [MEDIO]
# ------------------------------------------------------------------
# Creá variables para el precio de 3 productos en una compra
# (por ejemplo: pan, leche, huevos).
# Mostrá el total sumando los tres.
# Luego cambiá los precios y volvé a probar.
#
# Pista: sumá con + y guardá en una variable total.
#
# --- Tu solución: -------------------------------------------------
p_pan = 10
p_leche = 3
p_huevos = 6
total_gasto = p_pan + p_leche + p_huevos
print(total_gasto)
print("-" * 10)
p_pan = 10
p_leche = 2
p_huevos = 5
total_gasto = p_pan + p_leche + p_huevos
print(total_gasto)
# ------------------------------------------------------------------
# Ej. 2.8  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario su nombre y su altura en metros.
# Guardá ambos en variables con tipos correctos (str y float).
# Mostrá una frase que combine ambos:
#   [nombre] mide [altura] metros
#
# Pista: para altura → float(input(...))
#
# --- Tu solución: -------------------------------------------------
nombre = input("¿cual es tu nombre?: ")
altura = float(input("¿cual es tu altura?: "))
print(f"{nombre}, ud tiene una altura de {altura} metros")

# ------------------------------------------------------------------
# Ej. 2.9  [MEDIO]
# ------------------------------------------------------------------
# Hacé un programa que pida la temperatura en grados Celsius al
# usuario. Guardala como float en una variable y mostrala con un1.1
# mensaje que aclare su tipo:
#   La temperatura es X y su tipo es ...
#
# Pista: usá type() dentro del print().
#
# --- Tu solución: -------------------------------------------------
temperatura_Celsius = 23.5
print(f"La temperatura es de: {temperatura_Celsius} y su tipo es: {type(temperatura_Celsius)}")

# ------------------------------------------------------------------
# Ej. 2.10  [MEDIO]
# ------------------------------------------------------------------
# Creá tres variables:
#   es_estudiante = True
#   edad          = 20
#   altura        = 1.75
# Imprimí el tipo de cada una con type() y, debajo de cada una,
# escribí con un comentario (#) por qué crees que tiene ese tipo.
#
# Pista: los comentarios van con #.
#
# --- Tu solución: -------------------------------------------------
es_estudiante = True
print("Esta variable es de tipo: type(es_estudiante)")
#es una variable que asigna a un boleano True
edad = 20
print("Esta variable es de tipo: type(edad)")
#es una variable que asigna un numero entero
altura = 1.75
print("Esta variable es de tipo: type(altura))")
#es una variable que asigna un numero decimal o float

# ==================================================================
# NIVEL DIFÍCIL — Tipos combinados y fichas
# ==================================================================


# ------------------------------------------------------------------
# Ej. 2.11  [DIFÍCIL]
# ------------------------------------------------------------------
# Hacé un programa que pida al usuario su nombre, su edad y si
# está trabajando (respondiendo "sí" o "no").
# Convertí la respuesta sí/no a un valor booleano (True si
# escribió "sí", False si escribió "no") y mostrá un resumen:
#   Juan, 25 años, trabajando: True
#
# Pista: trabajando = (respuesta == "sí")
#
# --- Tu solución: -------------------------------------------------
nombre = input("decime tu nombre: ")
edad = int(input("decime tu edad: "))
respuesta = input("¿estas trabajando? (s/n)")
trabajando = (respuesta =="s")
print(f"{nombre}, {edad}, esta trabajando es {trabajando}")

# ------------------------------------------------------------------
# Ej. 2.12  [DIFÍCIL]
# ------------------------------------------------------------------
# Creá un programa que calcule el precio final de un producto.
# Pedí:
#   - precio    (float)
#   - cantidad  (int)
#   - envío premium  (sí/no → bool)
# Mostrá un desglose claro con cada dato, su tipo y un mensaje
# final con el total a pagar.
#
# Pista: total = precio * cantidad. Sumá el envío si corresponde.
#
# --- Tu solución: -------------------------------------------------
precioA = float(input("¿Precio del producto A?: "))
print(f"El precio del producto A es de $: {precioA}")

pedido = int(input("¿Qué cantidad de precioA solicita?: "))
subtotal = precioA * pedido
print(f"El valor del subtotal es de pesos {subtotal}")

respuesta = input("¿Solicita envío premium (s/n)?: ")
envio_premium = (respuesta == "s")              # bool: True/False
costo_envio = 100 if envio_premium else 0       # int: 100 o 0

total_a_pagar = subtotal + costo_envio

print(f"Envío premium: {envio_premium}  (tipo: {type(envio_premium).__name__})")
print(f"Costo de envío: ${costo_envio}")
print(f"El costo total es de pesos {total_a_pagar}")


# ------------------------------------------------------------------
# Ej. 2.13  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario la cantidad de horas que durmió anoche (como
# int) y la cantidad recomendada (8).
# Mostrá un mensaje que diga si durmió MENOS, IGUAL o MÁS que
# la recomendación.
# Usá variables y comparaciones simples con ==.
#
# Pista: podés usar tres if (lo veremos en la Lección 4) o tres
# print() condicionales a mano.
#
# --- Tu solución: -------------------------------------------------
horas_recomendadas = 8
horas_dormidas = int(input("¿Cuántas horas dormiste anoche?: "))

print("Durmió MENOS:", horas_dormidas < horas_recomendadas)
print("Durmió IGUAL:", horas_dormidas == horas_recomendadas)
print("Durmió MÁS:  ", horas_dormidas > horas_recomendadas)

# ------------------------------------------------------------------
# Ej. 2.14  [DIFÍCIL]
# ------------------------------------------------------------------
# Hacé un programa que simule el registro de un cliente.
# Pedí: nombre, email, teléfono y edad.
# Guardá todo en variables con tipos correctos (str, str, str, int)
# y mostrá una "ficha" del cliente con cada dato y su tipo,
# separada con una línea de guiones arriba y abajo.
#
# Pista: tres input() str + un input() convertido a int.
#
# --- Tu solución: -------------------------------------------------

nombre = input("Nombre: ")
email = input("Email: ")
telefono = input("Teléfono: ")
edad = int(input("Edad: "))

print("----------------------------------")
print(f"Nombre:   {nombre}   (tipo: {type(nombre).__name__})")
print(f"Email:    {email}    (tipo: {type(email).__name__})")
print(f"Teléfono: {telefono} (tipo: {type(telefono).__name__})")
print(f"Edad:     {edad}     (tipo: {type(edad).__name__})")
print("----------------------------------")


# ------------------------------------------------------------------
# Ej. 2.15  [DIFÍCIL]
# ------------------------------------------------------------------
# Creá un programa para preparar el cálculo del IMC (Índice de
# Masa Corporal).
# Pedí al usuario su peso en kg y su altura en metros (ambos
# como float). Guardalos en variables.
# Mostrá las dos variables, sus tipos, y dejá un comentario en
# el código con la fórmula del IMC (peso / altura²).
# NO calcules todavía el resultado.
#
# Pista: el comentario va con #. La fórmula es peso / (altura ** 2).
#
# --- Tu solución: -------------------------------------------------
peso = float(input("cual es tu peso actual?: "))
altura = float(input("cual es tu altura: "))
print(f"el peso tiene un tipo: {type(peso).__name__}")
print(f"la altura tiene un tipo: {type(altura).__name__}")
#El indice de masa corporal tiene la siguiente formula: peso / (altura ** 2) 

