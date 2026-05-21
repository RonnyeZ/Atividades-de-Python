"""
Exercício de Regex: Remover espaços duplicados, e substituir por apenas um.
"""

import re

texto = "texto  texto bla  bla"

regex = re.sub(r'\s+'," ", texto)

print(regex)



