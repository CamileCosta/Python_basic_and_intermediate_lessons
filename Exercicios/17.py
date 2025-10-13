import math
cateto_oposto = float(input('Digite um cateto oposto: '))
cateto_adjacente = float(input('Digite um cateto adjacente: '))
hip = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
print('A sua hipotenusa vale: {:.2f}'.format(hip))
