# LECCIÓN 5 - BUCLE WHILE | PRINCIPIANTE | Ejercicio 12
# =========================================================
# CONSIGNA: Pedile al usuario un número y sumá todos sus dígitos.
# Ejemplo: 1234 → 1+2+3+4 = 10
# PISTA: usá el operador % (módulo) para obtener el último dígito.
# =========================================================

n = int(input("Ingresá un número: "))
suma = 0

while n > 0:
    digito = n % 10        # saco el último dígito
    suma = suma + digito   # lo sumo
    n = n // 10            # le quito el último dígito

print(f"La suma de los dígitos es: {suma}")