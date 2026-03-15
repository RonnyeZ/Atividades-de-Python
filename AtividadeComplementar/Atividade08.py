# Tabuada Personalizada: 
# Peça um número e exiba a tabuada dele de 1 a 10 utilizando a estrutura for e a função range().

valor = int(input("Escolha um numero multiplicador para a Tabuada:\n"))

print(f"---------------\n TABUADA DO {valor}!\n---------------")

for i in range(1, 11):
    print(f"- {valor} x {i} = {valor*i}")