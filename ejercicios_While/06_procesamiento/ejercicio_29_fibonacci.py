# ============================================================
# Ejercicio 29: Fibonacci
# Categoría: 06_procesamiento
# ============================================================
#
# ENUNCIADO:
# Mostrá los primeros N números de la serie de Fibonacci: 0, 1, 1, 2, 3, 5, 8, ...

"""
🔍 La regla de oro (first principle)

La serie de Fibonacci es que: "Cada número es la suma de los dos anteriores"

### 📊 Serie de Fibonacci: Los primeros 8 números

| Posición | Número | ¿Cómo se obtuvo? |
|:--------:|:------:|:-----------------|
| 1        | 0      | Valor inicial    |
| 2        | 1      | Valor inicial    |
| 3        | 1      | 0 + 1 = 1        |
| 4        | 2      | 1 + 1 = 2        |
| 5        | 3      | 1 + 2 = 3        |
| 6        | 5      | 2 + 3 = 5        |
| 7        | 8      | 3 + 5 = 8        |
| 8        | 13     | 5 + 8 = 13       |
_______________________________________

"""
# vamos resolviendo de acuerdo a los datos el codigo
"""
n_anterior = 0
n_actual = 1
contador = 1

while contador <= 10:
    n_fibonacci = n_anterior + n_actual
    contador += 1

📊 Visualización de la cinta transportadora

### 🔄 Cómo "correr la cinta" en cada vuelta

|### 🔄 Serie de Fibonacci completa: 0, 1, 1, 2, 3, 5, 8, 13...
__________________________________________________________________________________________________
### ✅ Actualización correcta

| Vuelta | n_anterior | n_actual | n_fibonacci | Actualización correcta         |
|:------:|:----------:|:--------:|:-----------:|:------------------------------:|
| 1      | 0          | 1        | 1           |n_ant=n_actual(1), act=fib(1)    |
| 2      | 1          | 1        | 2           |n_ant=n_actual(1), act=fib(2)    |
| 3      | 1          | 2        | 3           |n_ant=n_actual(2), act=fib(3)    |
| 4      | 2          | 3        | 5           |n_ant=n_actual(3), act=fib(5)    |
________________________________________________________________________________

### 📝 Interpretación de la notación

| Notación        | Significado                                                              |
|:----------------|:-------------------------------------------------------------------------|
| `n_ant = n_actual(1)` | "n_anterior toma el valor de n_actual, que en ese momento vale 1"  |
| `act=fib(2)`          | "n_actual toma el valor de n_fibonacci, que vale 2"                |
__________________________________________________________________________________________

# 🎯 La clave: "correr la cinta"
#Después de calcular el siguiente número, necesitás actualizar las variables para la próxima vuelta.

n_fibonacci = n_anterior + n_actual

NECESITAMOS variables!!!
🎯 La clave es que las variables se actualicen dinámicamente, usando lo que ya tenés.

📊 Visualización
### 🔄 Actualización dinámica (usando variables)

n_fibonacci = n_anterior + n_actual
n_anterior = ???   # ← Actualizar esta variable
n_actual = ???     # ← Actualizar esta variable

🎯 Ahora traducido al código

el n_anterior ahora toma el valor de n_fibonacci y el n_actual 
"""
# Valores iniciales

n_anterior = 0
n_actual = 1
contador = 1
n = int(input("ingresa un numero para averiguar la serie de Fibonacci: "))

Serie_Fibonacci = []
Serie_Fibonacci.append(n_anterior)  # Agregar el 0
Serie_Fibonacci.append(n_actual)    # Agregar el 1

while contador <= n:
    n_fibonacci = n_anterior + n_actual
    Serie_Fibonacci.append(n_fibonacci)  # ← AGREGAR a la lista
    n_anterior = n_actual
    n_actual = n_fibonacci
    contador += 1

print(f"La serie de Fibonacci es: {Serie_Fibonacci}")
#_______________________________________________________________________________-

"""
### 🔄 Traceo del bucle Fibonacci

| Vuelta | n_anterior | n_actual | n_fibonacci | Actualización                  |
|:------:|:----------:|:--------:|:-----------:|:------------------------------:|
| 1      | 0          | 1        | 1           | ant=1, act=1                   |
| 2      | 1          | 1        | 2           | ant=1, act=2                   |
| 3      | 1          | 2        | 3           | ant=2, act=3                   |
| 4      | 2          | 3        | 5           | ant=3, act=5                   |
| 5      | 3          | 5        | 8           | ant=5, act=8                   |
| 6      | 5          | 8        | 13          | ant=8, act=13                  |
| 7      | 8          | 13       | 21          | ant=13, act=21                 |
| 8      | 13         | 21       | 34          | ant=21, act=34                 |
_________________________________________________________________________________

"""
