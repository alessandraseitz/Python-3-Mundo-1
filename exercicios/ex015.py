dias = float(input('Por quantos dias o carro foi alugado?\nDias: '))
km = float(input('O carro percorreu quantos kms?\nKm: '))
valorf = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${valorf:.2f}')
