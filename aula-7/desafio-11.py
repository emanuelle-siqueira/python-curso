largura = float(input('Digite o valor da largura: '))
altura = float(input('Digite o avlor da altura: '))

area = altura * largura

litros = area/2

print('A dimensao da parede é de {}x{} e a sua area é de {} m quadrados'.format(largura,altura,area))
print('Sera preciso {} litros para printar a parede.'.format(litros))