# Objetivo é fazer uma catraca a qual pode estar LIBERADA/TRAVADA, e atribuir duas Ações ao usuario, sendo elas: Moeda, para adicionar um Passe na Catraca; Empurrar, para atravessar a catraca caso esteja com um Passe; Empurrar(Redundância) para travar a Catraca quando nao tiver moead

catraca = 0

print("\nDefina uma das ações a seguir:")

while True :
    acao = input("-EMPURRAR à Catraca \n-Inserir uma MOEDA \n").lower()

    if acao == "moeda" :
        catraca += 1
        print(f"\nA Catraca está LIBERADA. Você possui {catraca} Passe(s).\n")

    elif acao == "empurrar" and catraca <= 0 :
        print("\nCatraca está TRAVADA, adicione uma Moeda\n")

    elif acao == "empurrar" and catraca >= 1 :
        catraca -= 1
        print(f"\nVocê atravessa a Catraca. \nUm Passe foi consumido, restam agora {catraca}.\n") 

    else :
        print("\nUma DIVERGENCIA foi detectada!!! \nEscolha uma das opções já definidas\n")
    