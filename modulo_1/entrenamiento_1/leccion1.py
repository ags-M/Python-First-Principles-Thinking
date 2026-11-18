#presentacion interactiva
nombre = input ("Cual es tu nombre?")
ciudad = input ("Cual es tu ciudad?")
print(f"Hola estimado{nombre} que bueno que nos escribas desde {ciudad}!")

print("-" * 10)

#calculadora de propinas
cuenta_de_restaurante = float(input("Cual es el total de la cuenta del restaurante?"))
propina = float(input(f"¿Cual es el porcentaje de propina que deseas dejar?"))
propina = float(cuenta_de_restaurante * (propina / 100))
print(f"El total de la propina es: $ {round(float(propina), 2)}")
total_a_pagar = float(cuenta_de_restaurante + propina)
print(f"El total a pagar es: $ {round(total_a_pagar, 2)}")

print("-" * 10)





