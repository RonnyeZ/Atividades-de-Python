#Validador de Senha: 
# Crie um loop while que peça uma senha. Se a senha for "python123", mostre "Acesso Permitido" e use break. Caso contrário, peça novamente.

senha = "123"
acesso = False

while acesso == False:
    login = input("\nColoque sua Senha:\n")

    if login != senha:
        print("\nAcesso Negado")

    elif login == senha:
        print("\nAcesso Permitido")
        acesso = True
