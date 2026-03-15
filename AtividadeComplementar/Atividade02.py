# Calculadora de Desconto: 
# Crie um programa que receba o preço de um produto e um percentual de desconto. Exiba o novo valor.

while True:
    produto = input("\n> Defina um Preço para um Produto:\n")
    desconto = input("\n> Adicione um Desconto (%) no Produto anterior:\n")

    try:
        produto = abs(float(produto))
        desconto = abs(float(desconto))

        preco = produto * (1 - (desconto/100))

        print(
            f"\n - Valor do Produto: R${produto}\n", 
            f"\n - Desconto (%): {desconto}\n", 
            f"\n - Preço Final: R${preco:.2f}")

    except ValueError:    
        print("\nError: Adicione somente valores numerico!!!")