def validar_acesso1(login, password1):
    return login == "procopio" and password1 == 12345

def validar_acesso2(login2, password2):
    return login2 == "paiva" and password2 == 54321

print("\n------ Painel de rede (Login) ------")
valor= (input("\nLogin: "))
senha = int(input("Senha: "))
print("\n------------------------------------\n")

if validar_acesso1(valor, senha) or validar_acesso2(valor, senha):
    print("\nSeja Bem Vindo!\n")
else:
    print("\nUsuário/Senha não conferem! Digite Novamente")