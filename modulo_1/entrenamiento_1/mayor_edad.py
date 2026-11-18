edad = int(input("¿cuantos años tiene?: "))
mayor_edad = edad >= 18
print(f"¿sos mayor de edad?: {mayor_edad}")

print("-"*10)

edad = int(input("¿cuantos años tiene?: "))
mayor_edad = edad >= 18
print("sos mayor de edad" if mayor_edad else "no sos mayor de edad")
