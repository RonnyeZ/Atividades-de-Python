# Exercício de Regex: capture hashtags de um texto de rede social. Ex: "Estudei #python e #regex no laboratório", retorno [Python, SQL]

import re

texto = input("Escreva um texto abaixo:\n")

hashtags = re.findall(r'#\w+', texto)

if hashtags:
    print(f"Palavras com hastaghs {hashtags}")
else:
    print("Nenhuma hashtag encontrada")