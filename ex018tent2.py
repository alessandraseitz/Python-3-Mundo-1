from math import tan, cos, sin, radians
an = float(input('Digite o ângulo que você deseja: '))
rad = radians(an)
print(f'O ângulo de {an} tem o SENO de {sin(rad):.2f}.')
print(f'O ângulo de {an} tem o COSSENO de {cos(rad):.2f}.')
print(f'O ângulo de {an} tem a TANGENTE de {tan(rad):.2f}.')
