#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int((input('Digite um número: ')))
dobro = n * 2
triplo = n * 3
rquad = n ** (1/2)
print(f'O dobro de {n} vale {dobro}.\nO triplo de {n} vale {triplo}.\nE a raiz quadrada de {n} é igual a {rquad:.2f}.')
