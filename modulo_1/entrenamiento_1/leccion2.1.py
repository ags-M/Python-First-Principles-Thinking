#calcular si un numero es par o impar

numero = int(input("Decime un número: "))
es_par = numero % 2 == 0
print(f"¿Es par? {es_par}")
print(f"¿Es impar? {not es_par}")