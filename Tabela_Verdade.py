def tabela_and(bit1, bit2):
    print("\nTabela verdade de 'AND': ")
    print(f"\n{bit1} and {bit2} =", bit1 and bit2)
def tabela_or(bit1, bit2):
    print("\nTabela verdade de 'OR': ")
    print(f"\n{bit1} or {bit2} =", bit1 or bit2)
def tabela_not(bit1):
    print("\nTabela verdade de 'NOT': ")
    print(f"\n{bit1} not =", not bit1)

print("\n******* Tabela Verdade *******\n")
print("       1. Operador AND          ")
print("       2. Operador OR           ")
print("       3. Operador Not        \n")
print("******************************\n")

opcao = int(input("Digite a opção desejada: "))


if opcao ==1:
    bit1 = bool(int(input("\nDigite o primeiro bit (0 ou 1): ")))
    bit2 = bool(int(input("\nDigite o segundo bit (0 ou 1): ")))
    tabela_and(bit1, bit2)

elif opcao ==2:
    bit1 = bool(int(input("\nDigite o primeiro bit (0 ou 1): ")))
    bit2 = bool(int(input("\nDigite o segundo bit (0 ou 1): ")))
    tabela_or(bit1, bit2)

elif opcao ==3:
    bit1 = bool(int(input("\nDigite o bit (0 ou 1) para aplicar o 'NOT': ")))
    tabela_not(bit1)

else:
    print("\nOpção Inválida! Digite de 1 a 3\n")
