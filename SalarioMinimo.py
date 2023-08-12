import math

salario_minimo_atual = float(input("Digite o valor atual do salário mínimo atual: "))
salario_usuario = float(input("Digite seu salário: "))

calculo = salario_usuario / salario_minimo_atual

print(f"A quantidade de salários mínimos recebidos é = {calculo: .2f}")