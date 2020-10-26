#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Qual o seu salário?\nSalário: R$ '))
acr = 15 / 100 * sal
salf = sal + acr
print(f'Seu salário com 15% de aumento é R$ {salf:.2f}.')
