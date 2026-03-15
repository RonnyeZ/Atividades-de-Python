# Analisador de Texto: 
# Peça para o usuário digitar uma frase e mostre quantos caracteres ela possui (usando len()) e qual o tipo do dado (usando type()).

frase = input("\nEscreva uma frase:\n")

quantia = len(frase)
tipo = type(frase)

print(f"\n- Sua frase possui {quantia} Caracteres, e ela pertence ao Tipo {tipo}")