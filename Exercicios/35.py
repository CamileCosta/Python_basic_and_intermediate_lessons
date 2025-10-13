print('-' * 20)
print('Digite o tamanho das retas e direi se pode formar um triãngulo ou não')
print('-' * 20)
r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta: '))
r3 = int(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo com esses valores!')
else:
    print('Não pode formar um triangulo!')