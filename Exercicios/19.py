import random
first = input('Insira o nome do primeiro aluno: ')
second = input('Insira o nome do segundo aluno: ')
third = input('Insira o nome do terceiro aluno: ')
fourth = input('Insira o nome do quarto aluno: ')
print('O aluno escolhido foi: {}' .format(random.choice([first,second,third,fourth])))