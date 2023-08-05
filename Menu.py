num = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(" \n1 . Média ponderada, com pesos 2 e 3\n")
print(" \n2. Quadrado da soma dos 2 números\n")
print(" \n3. Cubo do menor número\n")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    calculo_media = (2 * num + 3 * num2) / 5
    print(f"\nMédia ponderada, com pesos 2 e 3 é = {calculo_media: .2f} ")
elif opcao == 2:
    calculo_soma = (num + num2) ** 2
    print(f"\nQuadrado da soma dos 2 números é = {calculo_soma: .2f}")
elif opcao == 3:
    if num < num2:
        resultado = num ** 3
        print(f"\nO cubo do menor número é = {resultado: .2f}")
    else:
        resultado = num2 ** 3
    print(f"\nO cubo do menor número é = {resultado: .2f}")
else:
    print("Opção Inválida. Escolha 1, 2 ou 3")