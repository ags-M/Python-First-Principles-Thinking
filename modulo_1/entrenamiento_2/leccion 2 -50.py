# -*- coding: utf-8 -*-
"""
Curso de Python - De cero a experto
LECCIÓN 2: VARIABLES Y TIPOS DE DATOS - 50 ejercicios extra

Distribución de dificultad:
  Ejercicios  1 - 20  →  FÁCIL
  Ejercicios 21 - 35  →  MEDIO
  Ejercicios 36 - 50  →  DIFÍCIL

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
# #           NIVEL FÁCIL  (Ejercicios 1 a 20)                     #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 2.1  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "ciudad_favorita" con el nombre de tu ciudad
# favorita (str) y mostrala con un mensaje claro.
#
# Pista: ciudad_favorita = "Rosario"
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.2  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "libros_leidos" con un número entero que
# represente cuántos libros leíste este año. Mostrala con un mensaje.
#
# Pista: sin comillas, porque es un número.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.3  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario su deporte favorito con input() y mostrá:
#   "Tu deporte favorito es [deporte]"
#
# Pista: input() ya devuelve str, no hace falta convertir.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.4  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "codigo_producto = 1024" (int) y mostrá el
# valor y su tipo usando type().
#
# Pista: print(codigo_producto, type(codigo_producto).__name__)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.5  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario cuántas horas durmió anoche (como texto) y
# convertilo a int. Mostrá el resultado ya convertido.
#
# Pista: horas = int(input("..."))
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.6  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "distancia_km" como float (por ejemplo 12.5)
# y mostrala con un mensaje: "La distancia es X km".
#
# Pista: float lleva punto decimal, no coma.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.7  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "esta_soleado" como bool (True si hace sol,
# False si está nublado) y mostrala con un mensaje claro.
#
# Pista: los bool solo valen True o False (sin comillas).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.8  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario su serie favorita con input() y mostrá:
#   "Genial, [serie] es una gran serie"
#
# Pista: una sola llamada a input().
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.9  [FÁCIL]
# ------------------------------------------------------------------
# Creá tres variables con el día, mes y año de hoy (todas como str).
# Mostrá la fecha completa en una sola línea:
#   "Hoy es 8 de noviembre de 2026"
#
# Pista: las tres variables son str, las unís con f-string.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.10  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario su estación favorita del año y mostrá:
#   "Tu estación favorita es [estacion]"
#
# Pista: una sola input() + un print() con f-string.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.11  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "cantidad_vehiculos" como int (por ejemplo 2)
# que represente cuántos autos tiene tu familia. Mostrala con un
# mensaje claro.
#
# Pista: sin comillas, es número.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.12  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario su talla de zapato (como float) y mostrala.
#
# Pista: float(input("..."))
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.13  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "peso" como float (por ejemplo 70.5) y mostrá:
#   "Peso: [peso] kg"
#
# Pista: usá f-string.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.14  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "tiene_licencia" como bool y mostrala con un
# mensaje que aclare el significado:
#   "¿Tiene licencia de conducir? True"
#
# Pista: el bool va sin comillas dentro del f-string.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.15  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario el nombre de su banda favorita y mostrá:
#   "Sonando ahora: [banda]"
#
# Pista: una sola input() + un print() con f-string.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.16  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "marca_computadora" como str (por ejemplo "Dell")
# y mostrala con un mensaje claro.
#
# Pista: str va con comillas.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.17  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "cantidad_alumnos" como int (por ejemplo 30)
# y mostrala junto con su tipo usando type().
#
# Pista: print(cantidad_alumnos, type(cantidad_alumnos).__name__)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.18  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "descuento" como float (por ejemplo 0.25, que
# representaría 25%). Mostrala con un mensaje: "Descuento: X".
#
# Pista: float lleva punto decimal.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.19  [FÁCIL]
# ------------------------------------------------------------------
# Creá una variable "esta_abierto" como bool (True si el local
# está abierto, False si está cerrado) y mostrala con un mensaje.
#
# Pista: bool sin comillas.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.20  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario un color y mostrá:
#   "Elegiste el color [color]"
#
# Pista: una sola input() + print() con f-string.
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #           NIVEL MEDIO  (Ejercicios 21 a 35)                    #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 2.21  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario dos números como texto (str) con dos input().
# Convertí AMBOS a int y mostrá la MULTIPLICACIÓN.
# Acordate: input() SIEMPRE devuelve str.
#
# Pista: n1 = int(input("..."))  ;  print(n1 * n2)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.22  [MEDIO]
# ------------------------------------------------------------------
# Creá tres variables:
#   libro   = "El Principito"   (str)
#   precio  = 2500.99           (float)
#   stock   = 15                (int)
# Mostrá cada una junto con su tipo usando type().
#
# Pista: print(libro, type(libro).__name__)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.23  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario su edad como texto (str) con input().
# Convertila a int y mostrá el TRIPLE de esa edad.
#
# Pista: edad = int(input("..."))  ;  print(edad * 3)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.24  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario un número decimal como texto (str).
# Convertilo a float y mostralo restándole 5.
#
# Pista: num = float(input("..."))  ;  print(num - 5)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.25  [MEDIO]
# ------------------------------------------------------------------
# Creá variables:  nombre = "Carlos"   edad = 28
# Mostralas en un solo mensaje usando f-string:
#   "Carlos tiene 28 años"
#
# Pista: print(f"{nombre} tiene {edad} años")
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.26  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario una frase (str) y un número (int, después de
# convertir). Mostrá ambos y el tipo de cada uno.
#
# Pista: dos input(), el segundo convertido con int().
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.27  [MEDIO]
# ------------------------------------------------------------------
# Creá una variable "saldo = 2300.75" (float) y mostrala con
# exactamente 2 decimales usando f-string:
#   "Tu saldo es: $2300.75"
#
# Pista: f"{saldo:.2f}"  formatea a 2 decimales.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.28  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario un número entero y mostrá True o False indicando
# si es igual a 0. NO uses if, solo la comparación con ==.
#
# Pista: print(numero == 0)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.29  [MEDIO]
# ------------------------------------------------------------------
# Creá una variable "numero_str = '500'" (str).
# Convertila a int y guardala en otra variable "numero_int".
# Mostrá ambas variables y sus tipos para ver la diferencia.
#
# Pista: numero_int = int(numero_str)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.30  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario: nombre, años de experiencia y sueldo esperado.
# Guardá cada uno con el tipo correcto (str, int, float).
# Mostrá los tres con type().
#
# Pista: tres input() con sus conversiones correspondientes.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.31  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario una respuesta "sí" o "no" a la pregunta
# "¿Te gusta la pizza?".
# Convertila a bool: True si escribió "sí", False en caso contrario.
# Mostrá el resultado.
#
# Pista: resultado = (respuesta == "sí")
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.32  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario dos nombres de ciudades (str) y mostrá la
# concatenación usando el operador +, separadas por " y ":
#   "Rosario y Córdoba"
#
# Pista: ciudad1 + " y " + ciudad2
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.33  [MEDIO]
# ------------------------------------------------------------------
# Creá estas tres variables:
#   es_cliente = True       (bool)
#   saldo      = 5000.50    (float)
#   nombre     = "Ana"      (str)
# Mostrá un mini reporte con cada una y su tipo, en líneas separadas.
#
# Pista: tres print() con f-string + type().__name__.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.34  [MEDIO]
# ------------------------------------------------------------------
# Creá una variable "nota_str = '9.5'" (str).
# Convertila a float y guardala en otra variable "nota_float".
# Mostrá ambas variables y mostrá también un mensaje:
#   "Nota: 9.5"
#
# Pista: nota_float = float(nota_str)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.35  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario el nombre de una ciudad (str).
# Mostrá el nombre repetido 3 veces seguidas usando el operador *.
# Ejemplo: "RosarioRosarioRosario"
#
# Pista: ciudad * 3  →  repite el str 3 veces.
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #           NIVEL DIFÍCIL  (Ejercicios 36 a 50)                  #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 2.36  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario los datos para inscribirse a un evento:
#   - nombre completo (str)
#   - tipo de entrada (str, por ejemplo "general" o "VIP")
#   - cantidad de entradas (int, convertir con int())
#   - precio unitario (float, convertir con float())
# Mostrá una ficha con cada dato, su tipo y una línea de guiones
# arriba y abajo.
#
# Pista: cuatro input() con conversiones + type().__name__.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.37  [DIFÍCIL]
# ------------------------------------------------------------------
# Creá variables para un curso online:
#   nombre   = "Python"       (str)
#   precio   = 15000.99       (float)
#   clases   = 40             (int)
#   online   = True           (bool)
# Mostrá una ficha del curso con cada dato, su tipo y un mensaje
# final "Curso cargado correctamente".
#
# Pista: cuatro variables + cinco print().
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.38  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario un número como texto (str).
# Antes de convertir, mostrá el valor y su tipo (debería decir str).
# Después convertilo a int y volvé a mostrar valor y tipo.
#
# Pista: dos prints antes de la conversión, dos prints después.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.39  [DIFÍCIL]
# ------------------------------------------------------------------
# Simulá un carrito de compras con 2 productos:
#   - Pedí el nombre de 2 productos (str) con 2 input().
#   - Pedí el precio de cada uno (str) con 2 input().
#   - Convertí los precios a float.
#   - Mostrá el total de la compra.
#
# Pista: cuatro input() en total, dos str (nombres) y dos float (precios).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.40  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario un número como texto (str).
# Convertilo a int y mostrá True o False indicando si es MÚLTIPLO
# DE 3. NO uses if: usá la comparación (numero % 3 == 0).
#
# Pista: numero % 3 da 0 si es múltiplo de 3.
#        Entonces: print((numero % 3) == 0)  → True si lo es.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.41  [DIFÍCIL]
# ------------------------------------------------------------------
# Simulá el registro de un jugador de fútbol:
#   - nombre (str)
#   - posición (str)
#   - dorsal (int, convertir con int())
#   - goles (int, convertir con int())
# Mostrá una ficha con cada dato y su tipo, separada con bordes de "=".
#
# Pista: cuatro input() (dos con int()), seis print().
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.42  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario su nombre y TRES notas (como texto).
# Convertí las notas a float y mostrá el promedio:
#   "[nombre], tu promedio es [promedio]"
#
# Pista: tres float(input()) + suma y división por 3.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.43  [DIFÍCIL]
# ------------------------------------------------------------------
# Creá variables para una membresía de gimnasio:
#   costo_mensual = 8000       (int)
#   meses         = 3          (int)
#   tiene_promo   = True       (bool)
# Calculá el subtotal (costo_mensual * meses) y mostrá:
#   - cada variable con su tipo
#   - el subtotal con su tipo
#   - un mensaje: "Promo aplicable: True/False"
#
# Pista: seis prints en total con type().__name__.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.44  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario: nombre, profesión y teléfono.
# Mostrá una "tarjeta de presentación" formateada con bordes de
# asteriscos (*) arriba y abajo. Cada dato en su línea, alineado.
# Ejemplo:
#   ******************************
#   Nombre:     Juan
#   Profesión:  Programador
#   Teléfono:   1112345678
#   ******************************
#
# Pista: encabezado y pie con filas de "*", medio con f-strings.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.45  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario dos preguntas:
#   "¿Querés sopa? (sí/no)"
#   "¿Querés postre? (sí/no)"
# Convertí ambas respuestas a bool (True si "sí", False si no).
# Mostrá un mensaje combinado con los dos bools:
#   "Sopa: True, Postre: False"
#
# Pista: dos input() + dos comparaciones == "sí".
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.46  [DIFÍCIL]
# ------------------------------------------------------------------
# Registro de biblioteca. Creá variables:
#   titulo       = "Cien Años de Soledad"   (str)
#   autor        = "García Márquez"         (str)
#   año          = 1967                     (int)
#   paginas      = 471                      (int)
#   disponible   = True                     (bool)
# Mostrá una ficha con cada dato y su tipo, separada con bordes de "=".
#
# Pista: cinco variables + seis print().
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.47  [DIFÍCIL]
# ------------------------------------------------------------------
# Pedí al usuario: nombre (str) y dominio (str, por ejemplo "gmail.com").
# Construí un email concatenando con "@":
#   "Tu email es: [nombre]@[dominio]"
# Por ejemplo:  nombre="juan", dominio="gmail.com"  →  juan@gmail.com
#
# Pista: email = nombre + "@" + dominio
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.48  [DIFÍCIL]
# ------------------------------------------------------------------
# Reporte de clima. Pedí al usuario:
#   - ciudad (str)
#   - temperatura como texto (str) → convertir a float
#   - humedad como texto (str) → convertir a int
# Mostrá una ficha con cada dato, su tipo y un mensaje al final:
#   "Reporte generado correctamente".
#
# Pista: tres input() (dos con conversión) + type().__name__.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.49  [DIFÍCIL]
# ------------------------------------------------------------------
# Ficha de paciente en un hospital. Pedí al usuario:
#   - nombre del paciente (str)
#   - edad (int, convertir con int())
#   - grupo sanguíneo (str)
#   - peso en kg (float, convertir con float())
#   - altura en metros (float, convertir con float())
# Mostrá una ficha con cada dato y su tipo, separada con bordes de "=".
#
# Pista: cinco input() con conversiones + type().__name__.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 2.50  [DIFÍCIL]
# ------------------------------------------------------------------
# Registro de mascota en una veterinaria. Pedí al usuario:
#   - nombre (str)
#   - especie (str)
#   - edad en años (int, convertir con int())
#   - peso en kg (float, convertir con float())
#   - vacunado (str: "sí" o "no") → convertir a bool
# Mostrá una ficha con cada dato, su tipo y un mensaje al final:
#   "Mascota registrada correctamente".
#
# Pista: cinco input() con conversiones + type().__name__.
#        Para vacunado:  vacunado_bool = (vacunado_str == "sí")
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #  ¡Fin de los 50 ejercicios extra de la Lección 2!              #
# #                                                                #
# #  Cuando termines, mandame este archivo .py con tus soluciones  #
# #  y te lo devuelvo corregido ejercicio por ejercicio.           #
# #                                                                #
# ##################################################################
