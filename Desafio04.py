# Receba uma palavra, e então devolva ela revertida, puxando letra por letra

palavra = input("Escreva uma palavra:\n")
reverso = ""

for letra in palavra:
    reverso = letra + reverso

print(f"palavra Original:", palavra)
print(f"palavra Reversa:", reverso)



