# Par ou Ímpar: 
# Crie um programa que peça um número inteiro e diga se ele é par ou ímpar usando o operador de resto % (Dica: use if/else).

while True:
    try:
        numero = int(input("\nDigite um número inteiro a sua escolha:\n"))

        if (numero % 2) == 1:
            print("\nO valor inserido é um número Impar!\n")

        elif (numero % 2) == 0:
            print("\nO Valor Inserido é um número Par!\n")

    except ValueError:
        print("\nO Valor inserido não é um Número Inteiro\n")