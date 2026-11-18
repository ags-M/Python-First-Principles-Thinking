sueño_recomendado = 8
sueño_paciente = int(input("cuantas horas durmio anoche?: "))
if sueño_paciente == sueño_recomendado:
    print("El paciente tuvo sueño normal")
elif sueño_paciente >= sueño_recomendado:
    print("El paciente durmio mas horas")
else:
    print("El paciente durmio menos horas")

print("-"*15)

horas_recomendadas = 8
horas_dormidas = int(input("¿Cuántas horas dormiste anoche?: "))

print("Durmió MENOS:", horas_dormidas < horas_recomendadas)
print("Durmió IGUAL:", horas_dormidas == horas_recomendadas)
print("Durmió MÁS:  ", horas_dormidas > horas_recomendadas)