"""
Exercício de Regex: Validar o IPv4, testar IPs válidos e inválidos usando regex apresentada
Casos para Avaliar:
- 192.168.0.1
- 255.255.255.255
- 256.10.1.1
- 10.0.0
"""

import re

ip = "192.168.0.1"

regex = regex = r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'

print(bool(re.match(regex, ip)))
