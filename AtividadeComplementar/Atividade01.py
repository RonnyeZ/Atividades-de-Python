# Conversor de Medidas: 
# Peça ao usuário uma distância em metros e exiba o valor convertido em centímetros e milímetros.

metros = abs(int(input("Adicione uma distância em metros:\n")))

cm = metros * 100
mm = metros * 1000

print(f"\n- Valor em Centimetros: {cm}cm \n- Valor em Milimetros: {mm}mm")