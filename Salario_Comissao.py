import math

nome = str(input("Digite o nome do corretor: "))
vendas = int(input("Quantidade de imóveis vendidos: "))
valor = float(input("Digite o valor total das vendas: "))

porcentagem_vendas = valor * 0.05
comissao = vendas * 200
salario = 1500

soma = salario + comissao + porcentagem_vendas

print("O nome do corretor é:", nome)
print(f"Seu salário final é = R$ {soma: .2f}")