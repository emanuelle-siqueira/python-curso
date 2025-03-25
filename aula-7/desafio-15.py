dias = int(input('Quantos dias o carro alugado? '))
km = float(input('Quantos km foram pecorridos? '))

total = dias*60 + km*0.15

print('O total a pagar é R${:.2f}'.format(total))