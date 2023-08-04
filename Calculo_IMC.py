import math

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))


calculo =  peso / (altura * altura)

print(f"Seu IMC é = {calculo: .2f}")