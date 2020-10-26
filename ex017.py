#Leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
from math import hypot
catop = float(input('Digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
hipot = hypot(catop, catadj)
print(f'O comprimento da hipotenusa é {hipot:.2f}.')
