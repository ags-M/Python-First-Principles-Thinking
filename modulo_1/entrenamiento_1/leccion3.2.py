#conversor de segundos a horas y minutos
total_segundos=int(input("decime una cantidad de segundos: "))
horas=total_segundos // 3600
resto=total_segundos % 3600
minutos=resto// 60
segundos=resto % 60
print(f"Los {total_segundos} segundos equivalen a:{horas} horas: {minutos} minutos y {segundos} segundos")

