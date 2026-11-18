#ejercicio es par o impar?
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(f"el numero: {numero} que ingresaste es par")
else:
    print(f"el numero: {numero} que ingresaste es impar")

print("-"*10)

#el validador de acceso, uso de and
edad = int(input("¿por favor digame su edad?: "))
invitacion = input ("¿ud tiene invitacion (s o n)? ")
if edad >= 18 and invitacion == "s":
    print("ud cumple con la condición")
else:
    print("ud No cumple con la condición")

print("-"*10)

#el validador de acceso, uso de or
edad = int(input("¿por favor digame su edad?: "))
invitacion = input ("¿ud tiene invitacion (s o n)?: ")
pase_especial = input("¿ud tiene pase especial (s o n)?; ")
if edad >= 18 or invitacion == "s":
    print("ud cumple con la condición")
elif edad <18 and pase_especial == "s":
     print("ud puede entrar")
else:
    print("ud No cumple con la condición")

print("-"*10)

#Validador de acceso con booleanos

edad = 66
tiene_entrada = True

# ¿Puede entrar al cine? (mayor de edad Y con entrada)
puede_entrar = edad >= 18 and tiene_entrada
print(puede_entrar)   # True

# ¿Es jubilado? (65 o más)
es_jubilado = edad >= 65
print(es_jubilado)    # True

# ¿Es menor O jubilado? (descuento especial)
tiene_descuento = edad < 18 or edad >= 65
print(tiene_descuento)  # True (porque es jubilado)
    



