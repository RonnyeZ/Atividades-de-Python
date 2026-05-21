"""
Exercício de Regex: Montar um padrão para placa simples do tipo ABC-1234
Critérios:
- três letras maiúsculas
- hífen opcional
- quatro dígitos
Depois, discutir:
- Quais entradas indevidas ainda poderiam passar?
"""

# Desafio da Placa de Carro

import re

placa = input("Escreva uma placa seguindo padrão de AAA-0000, com hifen ou não.")

resultado = re.findall(r'^[A-Z]{3}-?\d{4}$', placa)

if resultado:
    print("Placa válida:", resultado)
else:
    print("Placa inválida")