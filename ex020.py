#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
#dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
aluno1 = input('Nome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print(f'A ordem de apresentação dos alunos será: {alunos}.')
