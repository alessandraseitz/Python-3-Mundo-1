#Crie um programa que leia um número Real qualquer pelo teclado e mostre na ela a sua porção inteira.
from math import trunc
num = float(input('Digite um número: '))
inteira = trunc(num)
print(f'O número {num} tem a parte inteira {inteira}.')
