#Leia a largura e altura em m, calcule sua área e a quantidade de tinta necessárias para pintá-la. Cada l pinta 2m².
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print(f'A sua parede tem a dimensão de {alt}x{larg} e {area:.3f}m² de área.\nPara pintar essa parede, você precisará de {tinta:.4f}l de tinta.')
