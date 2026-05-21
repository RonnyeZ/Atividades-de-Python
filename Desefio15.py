"""
Exercício de Regex: Extrair preços, localizar valores monetários em textos longos.
"""

import re

money = "R$49 R$129,00 $200 100 reais"

dinheiro = re.findall(r'\d+[0-9]', money)

print(dinheiro)