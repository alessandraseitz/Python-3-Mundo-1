#Programa que leia algo pelo teclado e mostre o seu tipo primitivo e todas as informações possíveis sobre ele.

info = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(info)}.')
print(f'É alfanumérico? {(info.isalnum())}')
print(f'É alfabético? {(info.isalpha())}')
print(f'É um número? {(info.isnumeric())}')
print(f'Só tem espaços? {(info.isspace())}')
print(f'Está apenas em maiúsculas? {(info.isupper())}')
print(f'Está apenas em minúsculas? {(info.islower())}')
print(f'Está capitalizada? {(info.istitle())}')



