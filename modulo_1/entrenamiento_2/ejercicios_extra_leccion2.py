# -*- coding: utf-8 -*-
"""
Curso de Python - De cero a experto
LECCIÓN 2: VARIABLES Y TIPOS DE DATOS - 40 ejercicios extra

Distribución de dificultad:
  Ejercicios  1 - 15  →  FÁCIL
  Ejercicios 16 - 28  →  MEDIO
  Ejercicios 29 - 40  →  DIFÍCIL

Cómo usar este archivo en VS Code:
  1. Abrí este archivo .py en VS Code.
  2. Leé el enunciado de cada ejercicio (en los comentarios).
  3. Escribí tu solución en el espacio en blanco debajo de "Tu solución:".
  4. Para probar, comentá con # las soluciones anteriores y dejá solo una.

Temas que cubre esta lección:
  - Variables y asignación (=)
  - Tipos básicos: int, float, str, bool
  - print() y input()
  - type() para ver el tipo de una variable
  - Conversión de tipos: int(), float(), str(), bool()

Tips antes de empezar:
  - input() SIEMPRE devuelve str. Si necesitás un número, hay que convertirlo.
  - Las variables se asignan con = (no confundir con == que es comparación).
  - Una variable puede cambiar de tipo si le asignás otro valor distinto.
"""


# ##################################################################
# #                                                                #
# #           NIVEL FÁCIL  (Ejercicios 1 a 15)                     #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 2.1  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "color_favorito" con tu color favorito (str) y
# mostrala con un mensaje claro.
#
# Pista: color_favorito = "azul"
#
# --- Tu solución: -------------------------------------------------
color_favorito = "azul"
print(f"mi color favorito es el: {color_favorito}")

# ------------------------------------------------------------------
# Ej. 2.2  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "edad_perro" con un número entero (la edad de
# tu perro o uno imaginario) y mostrala con un mensaje.
#
# Pista: sin comillas, porque es un número.
#
# --- Tu solución: -------------------------------------------------
edad_perro = 3
print(f" la edad de mi perro es: {edad_perro}")

# ------------------------------------------------------------------
# Ej. 2.3  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario su animal favorito con input() y mostrá:
#   "Tu animal favorito es [animal]"
#
# Pista: input() ya devuelve str, no hace falta convertir.
#
# --- Tu solución: -------------------------------------------------
animal_favorito = input("cual es tu animal favorito?: ")
print(f"el animal favorito del usuario es: {animal_favorito}")


# ------------------------------------------------------------------
# Ej. 2.4  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "precio = 999" (int) y mostrá el valor y su tipo
# usando type().
#
# Pista: print(precio, type(precio))
#
# --- Tu solución: -------------------------------------------------
precio = 999
print(f"el valor del precio es: {precio} y es del tipo:{type(precio).__name__}")

# ------------------------------------------------------------------
# Ej. 2.5  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario un número entero, convertilo a int y mostralo.
# (No hay que hacer ninguna operación, solo mostrarlo ya convertido.)
#
# Pista: numero = int(input("..."))
#
# --- Tu solución: -------------------------------------------------
numero = int(input("decime un numero entero: "))
print(f"este es un numero entero: {numero}")

# ------------------------------------------------------------------
# Ej. 2.6  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "temperatura" como float (por ejemplo 23.5) y
# mostrala con un mensaje: "La temperatura actual es X grados".
#
# Pista: float lleva punto decimal, no coma.
#
# --- Tu solución: -------------------------------------------------
temperatura = float(input("crea una variable temperatura: "))
print(f"La temperatura actual es de:{temperatura} grados")

# ------------------------------------------------------------------
# Ej. 2.7  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "es_finde" como bool (True si es sábado,
# False si es lunes) y mostrala con un mensaje claro.
#
# Pista: los bool solo valen True o False (sin comillas).
#
# --- Tu solución: -------------------------------------------------
dia = input("decime un dia de la semana: ")
es_finde = dia in ("sabado", "domingo") #in sirve para preguntar si algo está dentro de una colección 
#(una tupla, una lista, un string, etc.). Devuelve siempre un bool: True o False.
print(f"dia {dia} es finde: {es_finde}") #dia in ("sabado", "domingo") devuelve True si el día está en la tupla, 
#y False en caso contrario.
# ------------------------------------------------------------------
# Ej. 2.8  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario su nombre con input() y mostrá un saludo:
#   "Hola [nombre], bienvenido al curso"
#
# Pista: podés usar f-string:  f"Hola {nombre}, ..."
#
# --- Tu solución: -------------------------------------------------
nombre = input("decime tu nombre: ")
print(f"Hola {nombre} bienvenido al curso")

# ------------------------------------------------------------------
# Ej. 2.9  [FÁCIL]
# ------------------------------------------------------------------
# Creá tres variables con tu día, mes y año de nacimiento (todas
# como str). Mostrá la fecha completa en una sola línea:
#   "Nací el 15 de marzo de 1990"
#
# Pista: las tres variables son str, las unís con f-string.
#
# --- Tu solución: -------------------------------------------------
dia = "15"
mes = "marzo"
año ="1990"
print(f"Naci el {dia} de {mes} de {año}")

# ------------------------------------------------------------------
# Ej. 2.10  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario su comida favorita y mostrá:
#   "Te gusta comer [comida]"
#
# Pista: una sola llamada a input().
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.11  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "cantidad_hermanos" como int (por ejemplo 2)
# y mostrala con un mensaje claro.
#
# Pista: sin comillas, es número.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.12  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario su peso en kg (como float) y mostralo.
#
# Pista: float(input("..."))
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.13  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "altura" como float (por ejemplo 1.70) y mostrá:
#   "Mido [altura] metros"
#
# Pista: usá f-string.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.14  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "es_mayor_edad" como bool y mostrala con un
# mensaje que aclare el significado:
#   "¿Sos mayor de edad? True"
#
# Pista: el bool va sin comillas dentro del f-string.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.15  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario el nombre de una canción y mostrá:
#   "Ahora escuchando: [cancion]"
#
# Pista: una sola input() + un print() con f-string.
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #           NIVEL MEDIO  (Ejercicios 16 a 28)                    #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 2.16  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario dos números como texto (str) con dos input().
# Convertí AMBOS a int y mostrá la SUMA.
# Acordate: input() SIEMPRE devuelve str.
#
# Pista: n1 = int(input("..."))
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.17  [MEDIO]
# ------------------------------------------------------------------
# Creá tres variables:
#   numero   = 42        (int)
#   altura   = 1.75      (float)
#   saludo   = "hola"    (str)
# Mostrá cada una junto con su tipo usando type().
#
# Pista: print(numero, type(numero).__name__)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.18  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario su edad como texto (str) con input().
# Convertila a int y mostrá el doble de esa edad.
#
# Pista: edad = int(input("..."))  ;  print(edad * 2)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.19  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario un número decimal como texto (str).
# Convertilo a float y mostralo sumándole 10.
#
# Pista: num = float(input("..."))  ;  print(num + 10)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.20  [MEDIO]
# ------------------------------------------------------------------
# Creá variables:  nombre = "María"   edad = 30
# Mostralas en un solo mensaje usando f-string:
#   "María tiene 30 años"
#
# Pista: print(f"{nombre} tiene {edad} años")
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.21  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario una frase (str) y un número (int, después de
# convertir). Mostrá ambos y el tipo de cada uno.
#
# Pista: dos input(), el segundo convertido con int().
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.22  [MEDIO]
# ------------------------------------------------------------------
# Creá una variable "saldo = 1500.5" (float) y mostrala con
# exactamente 2 decimales usando f-string:
#   "Tu saldo es: $1500.50"
#
# Pista: f"{saldo:.2f}"  formatea a 2 decimales.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.23  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario un número entero y mostrá True o False indicando
# si es igual a 10. NO uses if, solo la comparación con ==.
#
# Pista: print(numero == 10)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.24  [MEDIO]
# ------------------------------------------------------------------
# Creá una variable "precio_str = '1500'" (str).
# Convertila a int y guardala en otra variable "precio_int".
# Mostrá ambas variables y sus tipos para ver la diferencia.
#
# Pista: precio_int = int(precio_str)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.25  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario: nombre, edad y altura.
# Guardá cada uno con el tipo correcto (str, int, float).
# Mostrá los tres con type().
#
# Pista: tres input() con sus conversiones correspondientes.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.26  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario una respuesta "sí" o "no".
# Convertila a bool: True si escribió "sí", False en caso contrario.
# Mostrá el resultado.
#
# Pista: resultado = (respuesta == "sí")
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.27  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario dos palabras (str) y mostrá la concatenación
# (unidas) usando el operador +.
#
# Pista: print(palabra1 + palabra2)  →  sale "pegado".
#        Para separarlas: palabra1 + " " + palabra2
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.28  [MEDIO]
# ------------------------------------------------------------------
# Creá estas tres variables:
#   es_alumno = True        (bool)
#   nota      = 8.5         (float)
#   nombre    = "Juan"      (str)
# Mostrá un mini reporte con cada una y su tipo, en líneas separadas.
#
# Pista: tres print() con f-string + type().__name__.
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #           NIVEL DIFÍCIL  (Ejercicios 29 a 40)                  #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 2.29  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario: nombre completo, edad, altura y peso.
# Guardá cada uno con el tipo correcto (str, int, float, float).
# Mostrá una ficha con cada dato, su tipo y una línea de guiones
# arriba y abajo.
#
# Pista: cuatro input() con conversiones + type().__name__.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.30  [DIFÍCIL]
# ------------------------------------------------------------------
# Creá variables para un producto:
#   nombre       = "Teclado"      (str)
#   precio       = 8500.50        (float)
#   stock        = 25             (int)
#   disponible   = True           (bool)
# Mostrá una ficha del producto con cada dato, su tipo y un mensaje
# final "Producto cargado correctamente".
#
# Pista: cuatro variables + cinco print().
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.31  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario una temperatura como texto (str).
# Antes de convertir, mostrá el valor y su tipo (debería decir str).
# Después convertila a float y volvé a mostrar valor y tipo.
#
# Pista: dos prints antes de la conversión, dos prints después.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.32  [DIFÍCIL]
# ------------------------------------------------------------------
# Simulá un carrito de compras:
#   - Pedí el nombre de 3 productos (str) con 3 input().
#   - Pedí el precio de cada uno (str) con 3 input().
#   - Convertí los precios a float.
#   - Mostrá el total de la compra.
#
# Pista: seis input() en total, tres str (nombres) y tres float (precios).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.33  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario un número como texto (str).
# Convertilo a int y mostrá True o False indicando si es PAR o IMPAR.
# NO uses if: usá la comparación (numero % 2 == 0).
#
# Pista: numero % 2 da 0 si es par, 1 si es impar.
#        Entonces: print((numero % 2) == 0)  → True si es par.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.34  [DIFÍCIL]
# ------------------------------------------------------------------
# Simulá el registro de un vehículo:
#   - marca (str)
#   - modelo (str)
#   - año (int, convertir con int())
#   - color (str)
# Mostrá una ficha con cada dato y su tipo, separada con bordes de "=".
#
# Pista: cuatro input() (uno con int()), seis print().
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.35  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario su nombre y dos notas (como texto).
# Convertí las notas a float y mostrá el promedio:
#   "[nombre], tu promedio es [promedio]"
#
# Pista: dos float(input()) + suma y división por 2.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.36  [DIFÍCIL]
# ------------------------------------------------------------------
# Creá variables:
#   precio        = 1500       (int)
#   cantidad      = 3          (int)
#   hay_descuento = True       (bool)
# Calculá el subtotal (precio * cantidad) y mostrá:
#   - cada variable con su tipo
#   - el subtotal con su tipo
#   - un mensaje: "Descuento aplicable: True/False"
#
# Pista: seis prints en total con type().__name__.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.37  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario: nombre, edad y email.
# Mostrá una "tarjeta de presentación" formateada con bordes de
# asteriscos (*) arriba y abajo. Cada dato en su línea, alineado.
# Ejemplo:
#   ******************************
#   Nombre:  Juan
#   Edad:    25
#   Email:   juan@mail.com
#   ******************************
#
# Pista: encabezado y pie con filas de "*", medio con f-strings.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.38  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario dos preguntas:
#   "¿Está lloviendo? (sí/no)"
#   "¿Tenés paraguas? (sí/no)"
# Convertí ambas respuestas a bool (True si "sí", False si no).
# Mostrá un mensaje combinado con los dos bools:
#   "Lluvia: True, Paraguas: False"
#
# Pista: dos input() + dos comparaciones == "sí".
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.39  [DIFÍCIL]
# ------------------------------------------------------------------
# Programa para un gimnasio. Pedí al usuario:
#   - nombre (str)
#   - edad (int)
#   - peso en kg (float)
#   - altura en metros (float)
# Mostrá una ficha con cada dato y su tipo, y agregá al final
# una línea con la fórmula del IMC COMO COMENTARIO:
#   # IMC = peso / (altura ** 2)
# (NO calcules el IMC todavía, solo dejá el comentario.)
#
# Pista: cuatro input() con conversiones + comentario con #.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.40  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario un número telefónico de 10 dígitos como str
# (ejemplo: "1112345678").
# Mostrá el número formateado como: "Tel: (11) 1234-5678"
# Usá slicing básico de strings: numero[0:2], numero[2:6], numero[6:10]
#
# Pista:
#   codigo_area = telefono[0:2]
#   primera     = telefono[2:6]
#   segunda     = telefono[6:10]
#   print(f"Tel: ({codigo_area}) {primera}-{segunda}")
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #  ¡Fin de los 40 ejercicios extra de la Lección 2!              #
# #                                                                #
# #  Cuando termines, mandame este archivo .py con tus soluciones  #
# #  y te lo devuelvo corregido ejercicio por ejercicio.           #
# #                                                                #
# ##################################################################
