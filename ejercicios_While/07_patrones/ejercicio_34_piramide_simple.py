# ============================================================
# Ejercicio 34: Pirámide simple
# Categoría: 07_patrones
# ============================================================
#
# ENUNCIADO:
# Imprimí una pirámide centrada de N filas. Ej para N = 5:
"""

    *         ← fila 1   
   ***        ← fila 2
  *****       ← fila 3
 *******      ← fila 4
*********     ← fila 5

🔍 Ahora busquemos el patrón de los ESPACIOS

Ahora, en cada fila hay dos cosas: espacios a la izquierda y asteriscos. 
Vamos a contarlas a mano, fila por fila:

epacios        asteriscos            i
   4               1          fila 1 = valor de i   
   3               3          fila 2 = valor de i 
   2               5          fila 3 = valor de i 
   1               7          fila 4 = valor de i 
   0               9          fila 5 = valor de i 

espacios numero decreciente
asteriscos numero que se le suma 2

Si i es el contador de filas se puede hacer una relacion tal que:

cantidad de filas  resta cantidad de espacios , nos de la cantidad de asteriscos

cantidad de filas - valor de i = cantidad de espacios
5 - 1 = 4
5 - 2 = 3
5 - 3 = 2
5 - 4 = 1
5 - 5 = 0

entonces ESPACIOS = FILAS - i (Los espacios estan en una relación inversa del numero de la fila)

🔍 Ahora busquemos el patrón de los ASTERISCOS

Si contamos los asteriscos de la piramide son todos numeros impares.
partiendo de 1 asterisco primera fila si se suma 2 en la segunda fila hay 3 asteriscos
partiendo de 3 asteriscos en la 3 fila abrá 5 asterisco y asi sucesivamente...hasta 9 ultima fila 5.

el patron es:

(i X 2) - 1 = numero impar que sera el numero de los asteriscos
veamos 

fila 1 = i = 1 ---> (i x 2) - 1 = 1 asterisco
fila 2 = i = 2 ---> (i x 2) - 2 = 3 asteriscos
fila 3 = i = 3 ---> (i x 2) - 3 = 5 asteriscos
fila 4 = i = 4 ---> (i x 2) - 4 = 7 asteriscos
fila 5 = i = 5 ---> (i x 2) - 5 = 9 asteriscos

entonces ASTERISCOS = (2 X i) - 1

¿Por qué? Porque cada fila suma 2 asteriscos más que la anterior (uno por cada lado de la pirámide). 
Empezás con 1 y vas sumando 2.


"""
filas = 5
i = 1
while i <= filas: # ✅ BUCLE EXTERNO
    linea = ""
    # --- Espacios a la izquierda ---
    espacios = 1
    while espacios <= filas - i:      # ← fórmula de espacios # ✅ BUCLE INTERNO
        linea += " "
        espacios += 1
    
    # --- Asteriscos ---
    asteriscos = 1
    while asteriscos <= (2 * i) - 1:    # ← fórmula de asteriscos # ✅ BUCLE INTERNO
        linea += "*"
        asteriscos += 1
    
    print(linea)
    i += 1  # ✅ CONTADOR DEL BUCLE EXTERNO
    
"""
🎯 hacer el codigo para una pirámide invertida:

*********    ← fila 1: 0 espacios, 9 asteriscos
 *******     ← fila 2: 1 espacio, 7 asteriscos
  *****      ← fila 3: 2 espacios, 5 asteriscos
   ***       ← fila 4: 3 espacios, 3 asteriscos
    *        ← fila 5: 4 espacios, 1 asterisco


primero vemos los espacios:

i - 1 = valor de espacio  en 5 filas
 
fila 1 --> 1 - 1 = 0   
fila 2 --> 2 - 1 = 1 
fila 3 --> 3 - 1 = 2    
fila 4 --> 4 - 1 = 3     
fila 5 --> 5 - 1 = 4    

es decir los espacios crecen linealmente
---------------------------------------------
segundo veamos los asteriscos:

Asteriscos: 2 * (filas - i) + 1 → decrece linealmente (9, 7, 5, 3, 1)
i=1: 2*(5-1)+1 = 2*4+1 = 9 ✅
i=2: 2*(5-2)+1 = 2*3+1 = 7 ✅
etc
"""

#--------------------------------------------
print("-" * 50)
#--------------------------------------------

filas = 5
i = 1
while i <= filas:  # ✅ BUCLE EXTERNO
    linea = ""
    
    # --- Espacios a la izquierda ---
    espacios = 1
    while espacios <= i - 1:      # ← fórmula de espacios (i - 1) ✅ BUCLE INTERNO
        linea += " "
        espacios += 1
    
    # --- Asteriscos ---
    asteriscos = 1
    while asteriscos <=  2 * (filas - i) + 1:    # ← fórmula de asteriscos ✅ BUCLE INTERNO
        linea += "*"
        asteriscos += 1
    
    print(linea)
    i += 1   # ✅ CONTADOR DEL BUCLE EXTERNO
    