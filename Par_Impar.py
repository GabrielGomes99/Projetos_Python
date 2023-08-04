valor = int(input("Digite um número: "))

if valor % 2 == 0:
    resultado = valor **2
    print("O número é par! Seu valor ao quadrado é: ", resultado)
else:
    resultado = valor **3
    print("O número é impar! Seu valor ao cubo é: ", resultado)