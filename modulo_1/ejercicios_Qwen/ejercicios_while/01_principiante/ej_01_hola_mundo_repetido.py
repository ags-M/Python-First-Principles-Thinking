# LECCIÓN 5 - BUCLE WHILE | PRINCIPIANTE | Ejercicio 1
# =========================================================
# CONSIGNA: Escribí un programa que imprima "Hola, Python!" exactamente 5 veces
# usando un bucle while.
#
# PISTA: Necesitás una variable "contador" que arranque en 0 y se incremente en 1.
# =========================================================

i = 1 #contador iniciador que empieza el conteo con 1 y lo itera 5 veces segun n
while i <= 5: # la condicion, es decir que la parada del contador se da cuando i es igual a 5
   print("Hola, Python! 🐍") # el cuerpo aca se define con print la salida 
   i += 1 # es la actualizacion permanente del contador i una vuelta mas otra (1) hasta 5

#--------------------------------------
print("-"*12)
#--------------------------------------

i = 1
frase = "Hola mundo con Python!🐍"
while i <= 5:
   print(frase)
   i += 1
