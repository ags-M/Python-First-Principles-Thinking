# -*- coding: utf-8 -*-
"""
SOLUCIONES - LECCIÓN 1: PRIMEROS PASOS
Curso de Python - De cero a experto

Este archivo tiene las 15 soluciones de la Lección 1 (5 fáciles + 5 medios
+ 5 difíciles), con una explicación corta antes de cada una.

Para probarlas:
  - Abrí este archivo en VS Code.
  - Ejecutá el archivo entero con: python solucion_leccion1.py
  - O comentá con # las soluciones que no quieras ver ahora y dejá solo una.

Recordá: hay muchas formas correctas de resolver cada ejercicio. Estas son
UNA solución posible, no LA única.
"""


# ##################################################################
# #                                                                #
# #           NIVEL FÁCIL                                          #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 1.1  [FÁCIL]
# ------------------------------------------------------------------
# Enunciado: imprimir tu nombre completo en una sola línea.
#
# Solución: una sola llamada a print() con el texto del nombre.
# print() muestra en pantalla lo que le pases entre paréntesis.
# Las comillas "..." indican que es texto (str).
#
print("Alejandro Pérez")


# ------------------------------------------------------------------
# Ej. 1.2  [FÁCIL]
# ------------------------------------------------------------------
# Enunciado: imprimir "Hola, mundo" y debajo tu ciudad.
#
# Solución: dos print() seguidos. Cada uno imprime su línea.
# Cuando print() termina, automáticamente salta a la línea siguiente.
#
print("Hola, mundo")
print("Buenos Aires")


# ------------------------------------------------------------------
# Ej. 1.3  [FÁCIL]
# ------------------------------------------------------------------
# Enunciado: mostrar tres líneas (nombre, edad, hobby).
#
# Solución: tres print(), uno por dato. La edad va SIN comillas porque
# es un número (int). Si la pusieras con comillas, también funcionaría,
# pero sería texto y no número.
#
print("Alejandro")
print(66)
print("estudiar Python")


# ------------------------------------------------------------------
# Ej. 1.4  [FÁCIL]
# ------------------------------------------------------------------
# Enunciado: en el REPL, mostrar "Estoy aprendiendo Python".
#
# Solución: abrís la terminal, escribís "python" para entrar al REPL,
# y luego escribís:
#
#   >>> print("Estoy aprendiendo Python")
#   Estoy aprendiendo Python
#
# También podrías escribir solo el string (sin print):
#
#   >>> "Estoy aprendiendo Python"
#   'Estoy aprendiendo Python'
#
# Pero en ese caso el REPL repite el texto CON comillas simples.
# Para mostrarlo limpio, usá print().
#
# Lo que vos pegaste mostraba un error porque faltó el print() o porque
# quedó algo sin cerrar. En el REPL, un string solo NO da error.
print("Estoy aprendiendo Python")


# ------------------------------------------------------------------
# Ej. 1.5  [FÁCIL]
# ------------------------------------------------------------------
# Enunciado: cartel de bienvenida a tu cumpleaños con separadores.
#
# Solución: varios print() con asteriscos arriba y abajo para enmarcar
# el cartel. Cada print() es una línea. Podés combinar * y texto.
#
print("******************************")
print("*                            *")
print("*  ¡Feliz cumple, Alejandro! *")
print("*    31 de octubre de 2026   *")
print("*                            *")
print("******************************")


# ##################################################################
# #                                                                #
# #           NIVEL MEDIO                                          #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 1.6  [MEDIO]
# ------------------------------------------------------------------
# Enunciado: menú de un café con 4 productos y precios alineados.
#
# Solución: un print() por producto, rellenando con puntos ("......")
# hasta que el precio quede parejo. Va un encabezado y un pie.
#
print("===== MENÚ DEL CAFÉ =====")
print("Café ........... $1500")
print("Latte .......... $2000")
print("Capuchino ...... $2200")
print("Té ............. $1000")
print("=========================")


# ------------------------------------------------------------------
# Ej. 1.7  [MEDIO]
# ------------------------------------------------------------------
# Enunciado: tarjeta de presentación con separadores de asteriscos.
#
# Solución: una fila de "*" arriba, los datos en el medio,
# y otra fila de "*" abajo. Cada print() es una línea.
#
print("****************************")
print("Alejandro Pérez")
print("Programador")
print("Tel: 11-5555-5555")
print("Email: ale@example.com")
print("****************************")


# ------------------------------------------------------------------
# Ej. 1.8  [MEDIO]
# ------------------------------------------------------------------
# Enunciado: factura simple con cliente, 3 productos y total.
#
# Solución: encabezado con el cliente, separador, los productos
# alineados con puntos, separador, y el total.
# El total lo dejamos como texto por ahora (más adelante lo vamos
# a calcular de verdad con variables).
#
print("Cliente: María Gómez")
print("------------------------")
print("Pan .......... $500")
print("Leche ........ $800")
print("Huevos ....... $1200")
print("------------------------")
print("Total ........ $2500")


# ------------------------------------------------------------------
# Ej. 1.9  [MEDIO]
# ------------------------------------------------------------------
# Enunciado: poema o canción de 4 estrofas de 2 líneas.
#
# Solución: un print() por línea. Las estrofas se separan con un
# print() vacío, que imprime una línea en blanco.
# (Podés inventar tu propio poema.)
#
print("Canta el zorzal")
print("en la montaña")
print()
print("Baja la luna")
print("por el río")
print()
print("Brilla la espuma")
print("de la memoria")
print()
print("Y un sueño corre")
print("por la mentira")


# ------------------------------------------------------------------
# Ej. 1.10  [MEDIO]
# ------------------------------------------------------------------
# Enunciado: cronograma de un día, una actividad por línea con hora.
#
# Solución: un print() por actividad, con la hora al inicio.
# El guion medio (-) separa la hora de la actividad.
#
print("08:00 - Desayuno")
print("09:00 - Trabajo")
print("13:00 - Almuerzo")
print("14:00 - Reunión")
print("17:00 - Café con amigos")
print("20:00 - Cena")
print("22:00 - Estudiar Python")


# ##################################################################
# #                                                                #
# #           NIVEL DIFÍCIL                                        #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 1.11  [DIFÍCIL]
# ------------------------------------------------------------------
# Enunciado: tabla con notas de 5 materias (Materia | Nota | Estado).
#
# Solución: un print() para el encabezado, otro para la línea
# separadora (con guiones y pipes "|"), y un print() por materia.
# Para alinear, dejamos los mismos espacios en cada fila.
# El pipe "|" hace de separador vertical entre columnas.
#
print("Materia        | Nota | Estado")
print("---------------|------|---------------")
print("Matemática     |  8   | Aprobado")
print("Historia       |  6   | Aprobado")
print("Lengua         |  4   | Desaprobado")
print("Biología       |  9   | Aprobado")
print("Geografía      |  7   | Aprobado")


# ------------------------------------------------------------------
# Ej. 1.12  [DIFÍCIL]
# ------------------------------------------------------------------
# Enunciado: bandera de tres franjas horizontales con caracteres.
#
# Solución: la bandera de Argentina tiene tres franjas horizontales
# (celeste, blanca, celeste). Usamos # para las franjas celestes
# y espacios en blanco para la franja del medio.
# Cada print() es una fila de la bandera.
# (Si querés otra bandera, cambiá los caracteres o el orden.)
#
print("####################")
print("####################")
print("                    ")
print("                    ")
print("####################")
print("####################")


# ------------------------------------------------------------------
# Ej. 1.13  [DIFÍCIL]
# ------------------------------------------------------------------
# Enunciado: dibujo de una casa con techo, paredes, puerta y ventanas.
#
# Solución: cada print() es una fila de la casa.
#   - El techo se hace con barras: /\ arriba, /____\ abajo.
#   - Las paredes con el carácter | a los costados.
#   - Las ventanas con corchetes [].
#   - La puerta con guiones y una "manija" representada por un carácter.
# IMPORTANTE: en Python, la barra invertida \ es un carácter especial.
# Para imprimir UNA barra invertida literal, hay que escribirla doble: \\.
#
print("      /\\      ")
print("     /  \\     ")
print("    /____\\    ")
print("   |      |   ")
print("   |[]  []|   ")
print("   |      |   ")
print("   | __   |   ")
print("   |  |   |   ")
print("   |__|___|   ")


# ------------------------------------------------------------------
# Ej. 1.14  [DIFÍCIL]
# ------------------------------------------------------------------
# Enunciado: recibo de supermercado con encabezado, 4 productos,
# separadores con guiones, subtotal y agradecimiento final.
#
# Solución: combinamos varias técnicas de los ejercicios anteriores.
# Encabezado con = arriba y abajo, productos alineados con puntos,
# subtotal separado con guiones, y un mensaje de cierre.
#
print("================================")
print("     SUPERMERCADO EL ÁNGEL      ")
print("================================")
print("Producto          Cant.   Precio")
print("--------------------------------")
print("Leche               2     $1600")
print("Pan                 3     $1200")
print("Huevos              1     $1800")
print("Yogur               4     $2400")
print("--------------------------------")
print("Subtotal                  $7000")
print("================================")
print("¡Gracias por su compra!")
print("Vuelva pronto.")


# ------------------------------------------------------------------
# Ej. 1.15  [DIFÍCIL]
# ------------------------------------------------------------------
# Enunciado: imprimir la letra "A" gigante con asteriscos (*).
#
# Solución: cada print() es una fila de la letra.
# Vamos de arriba hacia abajo:
#   - Fila 1: un solo asterisco arriba (la punta).
#   - Filas 2 y 3: dos asteriscos separados (los lados que se abren).
#   - Fila 4: una línea completa de asteriscos (la barra del medio).
#   - Filas 5, 6 y 7: los lados que se abren más, hasta la base.
#
print("       *       ")
print("      * *      ")
print("     *   *     ")
print("    *******    ")
print("   *       *   ")
print("  *         *  ")
print(" *           * ")


# ##################################################################
# #                                                                #
# #  Fin de las soluciones de la Lección 1                          #
# #                                                                #
# #  Tips finales:                                                 #
# #  - print() SIEMPRE salta a la línea siguiente al terminar.      #
# #  - Las comillas "..." indican texto (str).                      #
# #  - Los números van SIN comillas (int o float).                  #
# #  - El carácter \\ dentro de un string es UNA barra invertida.   #
# #  - Para alinear texto, usá puntos (......) o espacios.          #
# #                                                                #
# ##################################################################
