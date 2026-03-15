#Dicionário de Preços: 
# Crie um dicionário onde a chave é o nome de um produto e o valor é o preço. Peça ao usuário para buscar um produto e exiba o preço ou uma mensagem de "Não encontrado".

produtos = {
    "tv": 1199.99,
    "celular": 2499.99,
    "computador": 4799.49
}

while True:
    busca = input("\nDigite o nome do produto:\n").lower()

    if busca in produtos:
        print(f"\nO preço de {busca} é R${produtos[busca]:.2f}\n")

    else:
        print("\nProduto não encontrado.\n")