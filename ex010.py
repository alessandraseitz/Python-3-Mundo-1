#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real/3.27
print(f'Você tem U${dolar:.2f} dólares.')

