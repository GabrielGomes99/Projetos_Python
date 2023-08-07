import math

nota1 = float(input("Digite a nota do primeiro bimestre: ")) 
nota2 = float(input("Digite a nota do segundo bimestre: ")) 
nota3 = float(input("Digite a nota do terceiro bimestre: ")) 
nota4 = float(input("Digite a nota do quarto bimestre: ")) 

media_nota = (nota1 + nota2 + nota3 + nota4) / 4

if media_nota < 4.9:
    print("\nAluno Reprovado!\n")
elif 5.0 <= media_nota <= 6.9:
    print("\nAluno em Recuperação!\n")
if media_nota >= 7.0:
    print("\nAluno Aprovado!\n")
