#calculadora de imc
peso = float(input("¿Cuánto pesás (kg)? "))
altura = float(input("¿Cuánto medís (m)? "))
imc = peso / (altura ** 2)

peso_normal = 18.5 <= imc < 25
sobrepeso = 25 <= imc < 30
preobesidad = 30 <= imc < 35
obesidad = imc >= 35

print(f"IMC: {round(imc, 1)}")
print(f"¿Peso normal? {peso_normal}")
print(f"¿Sobrepeso? {sobrepeso}")
print(f"¿Preobesidad? {preobesidad}")
print(f"¿Obesidad? {obesidad}")