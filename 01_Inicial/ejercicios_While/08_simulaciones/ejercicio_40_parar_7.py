# 📝 consigna conta del 1 al 50 pero debe parar en el numero que es divisible por 7


i = 1
n = 50
while i <= n:
    print(i)
    
    i += 1

#--------------------------------------------
print("-" * 50)
#--------------------------------------------
n = 50
i = 1

while i <= n:
    print(i)
    if i % 7 == 0:      # si es divisible por 7, cortamos
        break
    i += 1 

"""
Explicación

print(i) va primero: así mostrás cada número antes de evaluar si hay que cortar.

if i % 7 == 0: break: cuando encuentra un múltiplo de 7, sale del while inmediatamente.

i += 1 al final: se incrementa siempre (no solo cuando es par)

"""
#--------------------------------------------
print("-" * 50)
#--------------------------------------------

### Variante: si querés que NO imprima el múltiplo de 7 (que pare antes)

n = 50
i = 1

while i <= n:
    if i % 7 == 0:
        break
    print(i)
    i += 1

