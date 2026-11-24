
# Invertir un número entero usando solo while. Ejemplo: 1234 → 4321.

# 1.- PRIMERO VALIDAR ENTRADA:

while True:
    n = input("Ingrese un número entero: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("❌ Error: debe ingresar un número entero válido.")
# 2.- ver si EL NUMERO es NEGATIVO? tomar en cuenta esto....

es_n_negativo = n < 0 # hay que tener en cuenta el ingreso de un numero negativo
n = abs(n) # se puede escribir = -n es lo mismo que el absoluto, lo convertimos para poder manejar los digitos

n_invertido = 0

while n > 0:
    digito = n % 10
    n_invertido = n_invertido * 10 + digito
    n = n // 10

# Restauramos el signo si el numero ingresado por el usuario era negativo
if es_n_negativo:
    n_invertido = - n_invertido   

print(f"El numero invertido es: {n_invertido}") 
# AHORA VOY A VER COMO SE ARREGLAN LAS COSAS SIGUEN HACIENDO LEVEMENTE LOS COMBIOS PERO NO 