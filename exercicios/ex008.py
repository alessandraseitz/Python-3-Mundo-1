#Escreva um programa que leia um valor em metros e o exibe convertido em centímetros e milímetros.
m = float(input('Digite uma distância em metros: '))
cm = m * 100
mm = m * 1000
print(f'{m:.0f} metros corresponde a {cm:.0f} centímetros e {mm:.0f} milímetros.')
