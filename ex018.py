#Leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(ângulo)
cosseno = cos(ângulo)
tangente = tan(ângulo)
print(f'O ângulo de {ângulo} tem o SENO de {seno:.3f}')
print(f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.3f}.')
print(f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.3f}.')
