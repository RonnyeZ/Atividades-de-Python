# Exercício de Regex: Localize palavras que começam com a letra maiúscula. Ex: "Python Java ruby SQL", retorno [Python, SQL]

import re

texto = input("Escreva um texto abaixo:\n")

palavras = re.findall(r'\b[A-Z][a-z]*\b', texto)

if palavras:
    print(f"Palavras em Maiúsculos {palavras}")
else:
    print("Nenhuma palavra encontrada")