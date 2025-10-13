km = float(input('Quantos km foram percorridos com o carro? '))
dias = float(input('Quantos dias ele foi alugado? '))
preco = (dias * 60) + (km * 0.15)
print('O preçoa a pagar o carro de acordo com as informações dadas é de R${}'.format(preco))