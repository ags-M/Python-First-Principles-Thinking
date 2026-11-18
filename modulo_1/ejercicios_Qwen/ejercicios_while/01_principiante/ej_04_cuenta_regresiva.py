# LECCIÓN 5 - BUCLE WHILE | PRINCIPIANTE | Ejercicio 4
# =========================================================
# CONSIGNA: Imprimí una cuenta regresiva del 10 al 1 y al final mostrá "¡Despegue!"
# =========================================================

n = 5
i = 5              # ARRANCA en 10 (el techo) → esto lo tenías bien
while i >= 1:       # SEGUÍ mientras i no haya bajado del piso que es 1
    print(i)        # muestra el número actual
    i -= 1          # baja de a 1 → acerca i al piso, así el bucle termina
print("¡Despegue!") # esto está FUERA del while (sin sangría): se ejecuta 1 vez al final

#--------------------------------------
print("-"*12)
#--------------------------------------

# Consigna: Cuenta regresiva del 20 al 10 (inclusive los dos extremos), de a 1. Al final imprimí "¡Listo!".
n = 20
i = 20
while i >= 10:
    print(i)
    i -= 1
print("¡listo!")
