# Exercício de Regex: Extraia tags <p>...</p> de uma string simples. Ex: "<p>Oi</p><p>Tchau</p>". O Objetivo é comparar o comportamento greedy e lazy. Monte duas versões e compare

import re

texto = "<p>Oi</p><p>Tchau</p>"

greedy = re.findall(r'<p>(.*)</p>', texto)

lazy = re.findall(r'<p>(.*?)</p>', texto)

print(f"\n- Greedy: {greedy}")
print(f"\n- Lazy: {lazy}")

if not greedy and not lazy:
    print("Nenhuma tag encontrada")