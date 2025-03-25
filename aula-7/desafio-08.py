m = float(input('Digite o valor em metros: '))

km = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
cm = m * 100
mm = m * 1000


print('{:.3f} km'. format(km))
print('{:.2f} hm'. format(hm))
print('{:.1f} dam'. format(dam))
print('{:.0f} dm'. format(dm))
print('{:.0f} cm e {:.0f} mm'.format(cm,mm))