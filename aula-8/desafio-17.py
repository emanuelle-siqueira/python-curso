import math
coposto = float(input('quanto o cateto oposto? '))
cadjacente = float(input('quanto falta o cateto adjacente? '))

#hipotenusa = (coposto**2 + cadjacente**2)**(1/2)
hipotenusa = math.hypot(coposto, cadjacente)
print('{:.2f}'.format(hipotenusa))