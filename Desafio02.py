# O usuario pode executar duas ações, sendo controlar: Luz da Sala e o Ar=Condicionado
# A Casa começa Desligada
# Ligar Luz; Desligar Luz; Abrir a Janela; Fechar a Janela; Ligar Ar; Desligar Ar; Sair
# Se o usuario repetir a ação, o sistema deve responder que "Ação Redundante"

casa = False
Luz = False
Ar = False
Janela = False

while casa == False:
    entrada = input("\nDigite Entrar para ligar a Casa\n").lower()

    if entrada == "entrar":
        casa = True
    else:
        print("\nEntre em casa antes de realizar qualquer comando.")


while casa == True :
    resposta = input("\nOpções: \n-Ligar/Desligar Luz; \n-Abrir/Fechar Janela; \n-Ligar/Desligar Ar; \n-Sair de Casa\n").lower()

    # Ligar as Luzes e Redundância
    if resposta == "ligar luz" and Luz == True:
        print("\nREDUNDÂNCIA: As Luzes já estão Acessas\n")
    elif resposta == "ligar luz" and Luz == False:
        Luz = True
        print("\nAs luzes foram Ligadas\n")
    
    # Desligar as Luzes e Redundância
    elif resposta == "desligar luz" and Luz == False:
        print("\nREDUNDÂNCIA: As Luzes já estão Apagadas\n")
    elif resposta == "desligar luz" and Luz == True:
        Luz = False
        print("\nAs luzes foram Desligadas\n")

    # Abrir/Fechar a Janela & Interação com o Ar-Condicionado
    elif resposta == "fechar janela":
        Janela = False
        print("\nA Janela está Fechada. \nO Ar-Condicionado pode ser reativado\n")
    elif (resposta == "abrir janela" and Ar == False) or (resposta == "ligar ar" and Janela == True):
        Janela = True
        print("\nA Janela está Aberta. \nO Ar-Condicionado não pode ser Ativo enquanto á Janela estiver aberta \n")
    elif resposta == "abrir janela" and Ar == True:
        Janela = True
        Ar = False
        print("\nA Janela foi aberta. O Ar-Condicionado foi Desligado\n")
    
    # Ligar o Ar e Redundância
    elif resposta == "ligar ar" and Ar == True and Janela == False:
        print("\nREDUNDÂNCIA: O Ar-Condicionado já está Ligado\n")
    elif resposta == "ligar ar" and Ar == False:
        Ar = True
        print("\nO Ar-Condicionado foram Ligadas\n")
    
    # Desligar o Ar e Redundância
    elif resposta == "desligar ar" and Ar == False:
        print("\nREDUNDÂNCIA: O Ar-Condicionado já está Desligado\n")
    elif resposta == "desligar ar" and Ar == True:
        Ar = False
        print("\nO Ar-Condicionado foi Desligado\n")
    

    # Desativar a Casa e Redundância
    elif resposta == "entrar":
        print("\nREDUNDÂNCIA: As funções da casa ja estão Ativas.\n")
    elif resposta == "sair" or "sair de casa":
        casa = False
        print("\nAs funções da Casa foram Desativadas.\n")

    # Qualquer outra resposta vai gerar uma Divergencia
    else :

        print("\nUma DIVERGENCIA foi detectada!!! \nEscolha uma das opções já definidas")
