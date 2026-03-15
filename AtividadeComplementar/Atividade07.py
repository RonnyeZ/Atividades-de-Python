# Maior de Três: 
# Peça três números ao usuário e utilize as funções max() e min() para mostrar qual é o maior e qual é o menor deles.

lista = []

print("Defina três números a seguir:\n")

for i in range(3):
    valor = float(input())

    lista.append(valor)

print(f"\nDos valores citados '{max(lista)}' é o Maior, e o '{min(lista)}' é o Menor.\n")