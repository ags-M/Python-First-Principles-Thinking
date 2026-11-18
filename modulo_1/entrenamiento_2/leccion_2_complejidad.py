# -*- coding: utf-8 -*-
"""
Curso de Python - De cero a experto
MÓDULO 1 - LECCIÓN 2: VARIABLES Y TIPOS DE DATOS
Batería de entrenamiento complementaria - 40 ejercicios

Distribución de dificultad:
  Ejercicios  1 - 15  →  FÁCIL
  Ejercicios 16 - 28  →  MEDIO
  Ejercicios 29 - 40  →  DIFÍCIL

Modalidades de ejercicio (novedad de esta batería):
  - PREDICCIÓN: leé el código y decidí qué imprime, SIN ejecutarlo.
  - DEBUGGING:  encontrá el error en el código dado y corregilo.
  - FILL-IN:    completá los huecos (_____) del código.
  - V/F:        afirmación teórica, respondé Verdadero o Falso y justificá.
  - TIPO:       decí qué tipo de dato devuelve la expresión.
  - REFACTOR:   reescribí el código de forma más prolija.
  - CASO LÍMITE: analizá qué pasa con un caso raro o trampa.
  - TEST DE MESA: trazá el código con varios inputs.
  - PROYECTO:   programa integrador usando todo lo de la lección.

Cómo usar este archivo en VS Code:
  1. Abrí este archivo .py en VS Code.
  2. Leé el enunciado de cada ejercicio (en los comentarios).
  3. Escribí tu solución en el espacio debajo de "Tu solución:".
  4. Para PREDICCIÓN, V/F o TIPO: escribí tu respuesta como comentario.
  5. Para DEBUGGING, FILL-IN o REFACTOR: escribí el código corregido.
  6. Para PROYECTO: escribí el programa completo.
  7. Verificá ejecutando cuando corresponda.

Temas que cubre esta batería:
  - Variables y asignación (=)
  - Tipos básicos: int, float, str, bool
  - print() y input()
  - type() para ver el tipo de una variable
  - Conversión de tipos: int(), float(), str(), bool()
  - Errores comunes y casos límite
  - Lectura de código y depuración

Tips antes de empezar:
  - input() SIEMPRE devuelve str. Si necesitás un número, hay que convertirlo.
  - Las variables se asignan con = (no confundir con == que es comparación).
  - Una variable puede cambiar de tipo si le asignás otro valor distinto.
  - bool("") y bool(0) devuelven False. Cualquier otra cosa, True.
  - int("3.5") ROMPE con ValueError. Para eso hay que usar float("3.5") primero.
"""


# ##################################################################
# #                                                                #
# #           NIVEL FÁCIL  (Ejercicios 1 a 15)                     #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 2.1  [FÁCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime este código? NO lo ejecutes, pensá primero.
#
#   x = "Hola"
#   print(x)
#
# Pista: una variable str se imprime sin las comillas.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.2  [FÁCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   n = 42
#   print(type(n).__name__)
#
# Pista: type() devuelve el tipo de la variable y __name__ te da
#        el nombre legible ("int", "float", "str", "bool").
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.3  [FÁCIL]  (FILL-IN)
# ------------------------------------------------------------------
# Completá el hueco para que "edad" sea un int:
#
#   edad = _____(input("Edad: "))
#
# Pista: input() devuelve str. Para tener int, hay que convertir.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.4  [FÁCIL]  (V/F)
# ------------------------------------------------------------------
# Afirmación: "input() SIEMPRE devuelve un str, aunque el usuario
# escriba un número."
#
# Respondé V o F y justificá con un ejemplo.
#
# Pista: pensá qué pasa si el usuario escribe "25".
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.5  [FÁCIL]  (TIPO)
# ------------------------------------------------------------------
# ¿Qué tipo devuelve esta expresión?
#
#   int("5")
#
# Pista: int() convierte a entero.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.6  [FÁCIL]  (DEBUGGING)
# ------------------------------------------------------------------
# Este código rompe. Encontrá el error y escribi el código corregido.
#
#   nombre = Juan
#   print(nombre)
#
# Pista: Juan no es una variable definida. Los strings van entre comillas.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.7  [FÁCIL]  (FILL-IN)
# ------------------------------------------------------------------
# Completá el hueco para que "saludo" sea un str con valor "Hola":
#
#   saludo = _____
#
# Pista: los str van con comillas (simples o dobles).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.8  [FÁCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   a = "Py"
#   b = "thon"
#   print(a + b)
#
# Pista: + con strings los concatena (une).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.9  [FÁCIL]  (V/F)
# ------------------------------------------------------------------
# Afirmación: "bool('False') devuelve False."
#
# Respondé V o F y justificá.
#
# Pista: bool() de un str no vacío siempre es True, sin importar
#        qué texto diga (incluso si dice "False").
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.10  [FÁCIL]  (TIPO)
# ------------------------------------------------------------------
# ¿Qué tipo devuelve?
#
#   type(3.14).__name__
#
# Pista: 3.14 lleva punto decimal, eso lo hace float.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.11  [FÁCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   nombre = "Ana"
#   edad = 25
#   print(f"{nombre} tiene {edad} años")
#
# Pista: las f-strings reemplazan {variable} por su valor.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.12  [FÁCIL]  (DEBUGGING)
# ------------------------------------------------------------------
# Este código rompe. Encontrá el error y escribi el código corregido.
#
#   edad = input("Edad: ")
#   print(edad + 1)
#
# Pista: input() devuelve str. No podés sumarle un int directamente.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.13  [FÁCIL]  (CASO LÍMITE)
# ------------------------------------------------------------------
# ¿Qué devuelve cada una? Justificá por qué.
#
#   bool("")
#   bool(0)
#   bool("0")
#   bool(0.0)
#
# Pista: bool() de "vacío" o "cero numérico" da False.
#        bool("0") es distinto: es un str no vacío.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.14  [FÁCIL]  (FILL-IN)
# ------------------------------------------------------------------
# Completá el hueco para convertir "precio_str" a float:
#
#   precio_str = "1500.50"
#   precio_float = _____(precio_str)
#
# Pista: float() convierte str numéricos a float.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.15  [FÁCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   x = True
#   print(type(x).__name__)
#
# Pista: True y False son valores de tipo bool (sin comillas).
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #           NIVEL MEDIO  (Ejercicios 16 a 28)                    #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 2.16  [MEDIO]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   x = 5
#   x = "cinco"
#   print(type(x).__name__)
#
# Pista: las variables pueden cambiar de tipo al reasignarse.
#        Cuenta el ÚLTIMO valor asignado.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.17  [MEDIO]  (DEBUGGING)
# ------------------------------------------------------------------
# Este código NO rompe, pero no hace lo que se espera.
# Si el usuario escribe "25", el doble sale "2525" en vez de 50.
# Corregilo.
#
#   edad = input("Edad: ")
#   doble = edad * 2
#   print(doble)
#
# Pista: str * int REPITE el string. Para sumar como número,
#        primero hay que convertir.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.18  [MEDIO]  (FILL-IN)
# ------------------------------------------------------------------
# Completá los 3 huecos para que las variables tengan los tipos
# correctos (str, int, float):
#
#   nombre  = _____(input("Nombre: "))    # str
#   edad    = _____(input("Edad: "))      # int
#   altura  = _____(input("Altura: "))    # float
#
# Pista: el primero NO necesita conversión (input ya devuelve str).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.19  [MEDIO]  (V/F)
# ------------------------------------------------------------------
# Afirmación: "Una variable declarada como int puede convertirse
# en str más adelante, sin errores."
#
# Respondé V o F y justificá con un ejemplo en código.
#
# Pista: probá  x = 5  ;  x = str(x)  ;  type(x).__name__
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.20  [MEDIO]  (TIPO)
# ------------------------------------------------------------------
# ¿Qué tipo (y qué valor) devuelve esta expresión?
#
#   int("5") + float("3.5")
#
# Pista: int + float en Python siempre da float.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.21  [MEDIO]  (REFACTOR)
# ------------------------------------------------------------------
# Reescribí este código de forma más prolija, usando un SOLO print()
# con f-string:
#
#   nombre = "María"
#   edad = 30
#   print("Nombre: ", nombre)
#   print("Edad: ", edad)
#
# Pista: f"{nombre} tiene {edad} años" o similar.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.22  [MEDIO]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   print(f"{2 + 3}")
#
# Pista: dentro de {} podés poner expresiones, no solo variables.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.23  [MEDIO]  (DEBUGGING)
# ------------------------------------------------------------------
# Este código rompe. Encontrá el error y corregilo.
#
#   print(mensaje)
#   mensaje = "Hola"
#
# Pista: hay que ASIGNAR una variable ANTES de usarla.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.24  [MEDIO]  (CASO LÍMITE)
# ------------------------------------------------------------------
# ¿Qué pasa al ejecutar esto? ¿Por qué?
#
#   n = int("3.5")
#
# Pista: int() espera un str que represente un número ENTERO.
#        "3.5" tiene un punto, no es un entero válido.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.25  [MEDIO]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   palabra = "ja"
#   print(palabra * 3)
#
# Pista: * con un str y un int REPITE el str.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.26  [MEDIO]  (FILL-IN)
# ------------------------------------------------------------------
# Completá el hueco para que "es_si" sea True si respuesta es "sí",
# False en caso contrario:
#
#   respuesta = input("¿Querés continuar? (sí/no): ")
#   es_si = (respuesta _____ "sí")
#
# Pista: el operador de IGUALDAD es == (no confundir con =).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.27  [MEDIO]  (V/F)
# ------------------------------------------------------------------
# Afirmación: "int('abc') funciona y devuelve 0 porque 'abc'
# no es un número."
#
# Respondé V o F y justificá.
#
# Pista: int() NO puede convertir texto no numérico. Lanza ValueError.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.28  [MEDIO]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   nombre = "Juan"
#   edad = 25
#   altura = 1.75
#   print(f"{nombre} | {edad} | {altura}")
#
# Pista: las barras | se imprimen literal, no son operadores.
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #           NIVEL DIFÍCIL  (Ejercicios 29 a 40)                  #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 2.29  [DIFÍCIL]  (REFACTOR)
# ------------------------------------------------------------------
# Este código funciona pero es feo y repetitivo (los datos están
# "quemados" adentro de los print). Refactorizalo usando variables
# arriba y f-strings en los print:
#
#   print("##############################")
#   print("Nombre: Juan")
#   print("Edad: 25")
#   print("Email: juan@mail.com")
#   print("##############################")
#
# Pista: declará nombre, edad, email antes, después usá f-strings.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.30  [DIFÍCIL]  (DEBUGGING)
# ------------------------------------------------------------------
# Este mini-programa tiene 2 bugs. Encontrálos y corregilos.
#
#   nombre = input("Nombre: ")
#   edad = int(input("Edad: ")
#   print(f"{nombre} tiene {edad años}")
#
# Pista 1: revisá los paréntesis balanceados en la línea de edad.
# Pista 2: dentro de {} en una f-string va solo el nombre de la
#          variable, el texto va AFUERA de las llaves.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.31  [DIFÍCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprimen estas líneas, en orden?
#
#   a = "10"
#   b = "20"
#   c = int(a) + int(b)
#   print(c)
#   print(type(c).__name__)
#   print(type(a).__name__)
#
# Pista: a y b SIGUEN siendo str (no se convirtieron en int).
#        c sí es int, porque se convirtió ANTES de sumar.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.32  [DIFÍCIL]  (CASO LÍMITE)
# ------------------------------------------------------------------
# ¿Qué imprimen estas líneas? ¿Por qué?
#
#   print(float("inf"))
#   print(float("-inf"))
#   print(float("nan"))
#   print(type(float("inf")).__name__)
#
# Pista: Python reconoce "inf", "-inf" y "nan" como valores
#        especiales de tipo float.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.33  [DIFÍCIL]  (FILL-IN)
# ------------------------------------------------------------------
# Completá los 4 huecos para que el carrito calcule el total:
#
#   p1 = float(input("Precio 1: "))
#   p2 = _____(input("Precio 2: "))
#   p3 = float(_____("Precio 3: "))
#   total = p1 _____ p2 _____ p3
#   print(f"Total: ${total}")
#
# Pista: las tres conversiones son float. La suma usa +.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.34  [DIFÍCIL]  (V/F)
# ------------------------------------------------------------------
# Respondé V o F a cada una y justificá con un ejemplo:
#
#   1) type(5) == type(5.0)        ¿son del mismo tipo?
#   2) str(5) + str(3) == '53'     ¿se concatena como str?
#   3) bool('False') == False      ¿bool de 'False' da False?
#   4) int(3.99) == 3              ¿int trunca decimales hacia abajo?
#
# Pista: una de estas cuatro afirmaciones es FALSA. ¿Cuál?
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.35  [DIFÍCIL]  (TIPO)
# ------------------------------------------------------------------
# ¿Qué tipo (y qué valor) devuelve esta expresión?
#
#   str(int(3.99)) + "5"
#
# Pista: int(3.99) da 3 (trunca). str(3) da "3".
#        "3" + "5" da... pensá qué hace + con dos str.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.36  [DIFÍCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprimen estas 4 líneas, en orden?
#
#   x = 5
#   print(type(x).__name__)
#   x = 5.0
#   print(type(x).__name__)
#   x = "5"
#   print(type(x).__name__)
#   x = True
#   print(type(x).__name__)
#
# Pista: la misma variable x va cambiando de tipo en cada reasignación.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.37  [DIFÍCIL]  (DEBUGGING)
# ------------------------------------------------------------------
# Este programa pide 2 precios y muestra el total, pero NO funciona
# como esperado. Si el usuario ingresa 100 y 200, el total sale
# "100200" en vez de 300. ¿Cuál es el bug? Corregilo.
#
#   p1 = input("Precio 1: ")
#   p2 = input("Precio 2: ")
#   total = p1 + p2
#   print(f"Total: ${total}")
#
# Pista: + con dos str CONCATENA (une), no suma números.
#        Hay que convertir cada input a float (o int) antes de sumar.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.38  [DIFÍCIL]  (REFACTOR)
# ------------------------------------------------------------------
# Esta ficha funciona pero es muy repetitiva. Refactorizala usando
# variables arriba y f-strings en los print:
#
#   print("****************************")
#   print("Nombre: Ana")
#   print("Edad: 30")
#   print("Altura: 1.65")
#   print("Peso: 60.5")
#   print("****************************")
#
# Pista: variables arriba (str, int, float, float) + 6 print con f-strings.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.39  [DIFÍCIL]  (TEST DE MESA)
# ------------------------------------------------------------------
# Para cada caso, ¿qué imprime este programa?
#
#   s = input("Saldo inicial: ")
#   g = input("Gasto: ")
#   saldo = int(s) - int(g)
#   print(f"Saldo final: {saldo}")
#
# Casos:
#   a) s="100", g="30"
#   b) s="500", g="500"
#   c) s="50",  g="100"
#
# Pista: trazá línea por línea. Anotá el valor de cada variable.
#        Para el caso (c), el saldo puede ser NEGATIVO.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.40  [DIFÍCIL]  (PROYECTO INTEGRADOR)
# ------------------------------------------------------------------
# Escribí un programa completo que:
#   1) Pida al usuario: nombre, edad, altura (m) y peso (kg).
#   2) Convierta cada uno al tipo correcto (str, int, float, float).
#   3) Calcule el IMC = peso / (altura ** 2) y guardalo en una variable.
#   4) Muestre una ficha con bordes de "=" arriba y abajo, cada dato
#      en su línea (incluyendo el IMC con 2 decimales).
#   5) Al final, muestre el tipo de cada variable usando type().__name__.
#
# Requisitos: usar TODO lo de la lección (input, conversiones,
# f-strings, type, f-string con formato .2f).
#
# Pista: 4 input() con conversiones + varios print + type().
#        Para 2 decimales: f"{imc:.2f}".
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #  ¡Fin de los 40 ejercicios de complejidad - Lección 2!         #
# #                                                                #
# #  Cuando termines, mandame este archivo .py con tus soluciones  #
# #  y te lo devuelvo corregido ejercicio por ejercicio.           #
# #                                                                #
# ##################################################################
