# Exercício de Regex: Dando um texto, encontre todos os númeors presentes. Ex: "Ana tem 2 gatos e 15 livros", Retorno = [2, 15]

import re

texto = input("Escreva um texto abaixo:\n")

numeros = re.findall(r'\d+', texto)

if numeros:
    print(f"\nO texto possui o(s) número(s) {numeros}\n")
else:
    print("\nNenhum número encontrado\n")